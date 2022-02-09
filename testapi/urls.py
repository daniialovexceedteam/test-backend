from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AccountViewSet, CardViewSet, TransactionViewSet


router = DefaultRouter()
router.register('accounts', AccountViewSet)
router.register('cards', CardViewSet)
router.register('transactions', TransactionViewSet)

urlpatterns = router.urls