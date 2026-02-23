from django.conf import settings
from django.db import models


class Client(models.Model):
    class Status(models.TextChoices):
        NEW = 'NEW', 'Novo'
        IN_PROGRESS = 'IN_PROGRESS', 'Em atendimento'
        WON = 'WON', 'Fechado'
        LOST = 'LOST', 'Perdido'

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='clients',
    )
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    company = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=Status.choices)
    lead_source = models.CharField(max_length=255)
    potential_value = models.DecimalField(max_digits=12, decimal_places=2)
    notes = models.TextField()
    last_contact_at = models.DateTimeField()
    next_contact_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self) -> str:
        return self.name

    @property
    def status_badge_class(self) -> str:
        if self.status == self.Status.NEW:
            return 'text-bg-primary'
        if self.status == self.Status.IN_PROGRESS:
            return 'text-bg-warning'
        if self.status == self.Status.WON:
            return 'text-bg-success'
        if self.status == self.Status.LOST:
            return 'text-bg-danger'
        return 'text-bg-secondary'
