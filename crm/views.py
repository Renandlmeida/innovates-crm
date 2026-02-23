from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q, Sum
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

import json

from .forms import ClientForm
from .models import Client


@login_required
def client_list(request: HttpRequest) -> HttpResponse:
    status = (request.GET.get('status') or '').strip()
    q = (request.GET.get('q') or '').strip()
    sort = (request.GET.get('sort') or '').strip()
    direction = (request.GET.get('dir') or '').strip().lower()

    clients = Client.objects.filter(owner=request.user)

    if status in Client.Status.values:
        clients = clients.filter(status=status)

    if q:
        clients = clients.filter(
            Q(name__icontains=q)
            | Q(phone__icontains=q)
            | Q(email__icontains=q)
        )

    allowed_sorts = {
        'name': 'name',
        'potential': 'potential_value',
    }
    sort_field = allowed_sorts.get(sort)
    if sort_field:
        if direction == 'desc':
            clients = clients.order_by(f'-{sort_field}', '-updated_at')
        else:
            clients = clients.order_by(sort_field, '-updated_at')

    total_potential = clients.aggregate(total=Sum('potential_value'))['total'] or 0

    return render(
        request,
        'crm/client_list.html',
        {
            'clients': clients,
            'status': status,
            'q': q,
            'status_choices': Client.Status.choices,
            'total_potential': total_potential,
            'sort': sort,
            'dir': direction,
        },
    )


@login_required
def dashboard(request: HttpRequest) -> HttpResponse:
    qs = Client.objects.filter(owner=request.user)

    totals_by_status_qs = (
        qs.values('status')
        .annotate(count=Count('id'))
        .order_by('status')
    )
    totals_by_status = {row['status']: row['count'] for row in totals_by_status_qs}

    total_potential = qs.aggregate(total=Sum('potential_value'))['total'] or 0

    status_cards = []
    chart_labels = []
    chart_counts = []
    for value, label in Client.Status.choices:
        chart_labels.append(label)
        chart_counts.append(totals_by_status.get(value, 0))
        status_cards.append(
            {
                'value': value,
                'label': label,
                'count': totals_by_status.get(value, 0),
            }
        )

    return render(
        request,
        'crm/dashboard.html',
        {
            'status_cards': status_cards,
            'total_potential': total_potential,
            'chart_labels_json': json.dumps(chart_labels),
            'chart_counts_json': json.dumps(chart_counts),
        },
    )


@login_required
def client_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.owner = request.user
            client.save()
            return redirect('crm:client_list')
    else:
        form = ClientForm()

    return render(request, 'crm/client_form.html', {'form': form, 'mode': 'create'})


@login_required
def client_update(request: HttpRequest, pk: int) -> HttpResponse:
    client = get_object_or_404(Client, pk=pk, owner=request.user)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('crm:client_list')
    else:
        form = ClientForm(instance=client)

    return render(request, 'crm/client_form.html', {'form': form, 'mode': 'update'})


@login_required
def client_delete(request: HttpRequest, pk: int) -> HttpResponse:
    client = get_object_or_404(Client, pk=pk, owner=request.user)

    if request.method == 'POST':
        client.delete()
        return redirect('crm:client_list')

    return render(request, 'crm/client_confirm_delete.html', {'client': client})
