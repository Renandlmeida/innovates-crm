from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'name',
            'phone',
            'email',
            'company',
            'status',
            'lead_source',
            'potential_value',
            'notes',
            'last_contact_at',
            'next_contact_at',
        ]
        widgets = {
            'last_contact_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'next_contact_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                continue
            css = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = (css + ' form-control').strip()

        if 'status' in self.fields:
            css = self.fields['status'].widget.attrs.get('class', '')
            self.fields['status'].widget.attrs['class'] = (css + ' form-select').strip()

        if 'notes' in self.fields:
            self.fields['notes'].widget.attrs.setdefault('rows', 4)
