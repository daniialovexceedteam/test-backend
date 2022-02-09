from rest_framework import serializers

from .models import Transaction, Card, Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['amount', 'id']
        model = Account
    
    def create(self, validated_data):
        return Account.objects.create(owner=self.context["request"].user)


class CardSerializer(serializers.ModelSerializer):
    cvv = serializers.CharField(required=False)
    date_expire = serializers.CharField(required=False)
    number = serializers.CharField(required=False)
    owner = serializers.SerializerMethodField()

    def get_owner(self, instance):
        return instance.account.owner.id

    class Meta:
        fields = ['name', 'account', 'amount', 'id', 'cvv', 'number', 'date_expire', 'owner']
        model = Card


class TransactionSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    def get_owner(self, instance):
        return instance.from_card.account.owner.id

    class Meta:
        fields = ['from_card', 'to_card', 'amount', 'type', 'owner']
        model = Transaction