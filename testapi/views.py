from decimal import Decimal, InvalidOperation

from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Account, Card, Transaction
from .permissions import CardPermission
from .serializers import AccountSerializer, TransactionSerializer, CardSerializer

from rest_framework_simplejwt.views import TokenObtainPairView


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
        with transaction.atomic():
            try:
                from_card = request.data["from_card"]
                from_card = Card.objects.get(id=from_card)
                from_card.amount -= Decimal(request.data["amount"])
                to_card = request.data["to_card"]
                to_card = Card.objects.get(number=to_card)
                to_card.amount += Decimal(request.data["amount"])
                from_card.save()
                to_card.save()
            except (ObjectDoesNotExist, InvalidOperation, KeyError):
                return Response({"message": "Invalid number, from or to card"}, status=400)
        request.data["to_card"] = to_card.id
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Transaction.objects.all()
        return Transaction.objects.filter(from_card__account__owner=self.request.user)


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.set_cookie('access_token', response.data["access"])
        response.set_cookie('refresh_token', response.data["refresh"])
        return response

