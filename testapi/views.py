from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Account, Card, Transaction
from .permissions import CardPermission
from .serializers import AccountSerializer, TransactionSerializer, CardSerializer


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AccountSerializer
    lookup_field = 'id'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Account.objects.all()
        return Account.objects.filter(owner=self.request.user)

class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    permission_classes = [IsAuthenticated, CardPermission]
    serializer_class = CardSerializer
    lookup_field = 'id'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Card.objects.all()
        return Card.objects.filter(account__owner=self.request.user)

class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        from_card = request.data["from_card"]
        from_card = Card.objects.get(id=from_card)
        from_card.amount -= request.data["amount"]
        from_card.save()

        to_card = request.data["to_card"]
        to_card = Card.objects.get(id=to_card)
        to_card.amount += request.data["amount"]
        to_card.save()

        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Transaction.objects.all()
        return Transaction.objects.filter(from_card__account__owner=self.request.user)