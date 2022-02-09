import uuid
from datetime import timedelta
from random import randint

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class BaseClass(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Account(BaseClass):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def amount(self):
        return self.cards.all().aggregate(models.Sum('amount'))['amount__sum']

class Card(BaseClass):
    name = models.CharField(max_length=64, blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='cards')
    number = models.CharField(max_length=16, unique=True)
    cvv = models.CharField(max_length=3)
    amount = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10, default=0)
    date_expire = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.date_expire = timezone.now() + timedelta(days=1460)
            self.number = str(randint(10 ** 15, 10 ** 16 - 1))
            self.cvv = str(randint(100, 999))
        super().save(*args, **kwargs)


class Transaction(BaseClass):
    TYPE_CHOICES = (
        ("invoice", "Invoice"),
        ("transfer", "Transfer"),
        ("letter_of_credit", "Letter of Credit")
    )

    from_card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="transactions_from")
    to_card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="transactions_to")
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    type = models.CharField(max_length=16, choices=TYPE_CHOICES)


