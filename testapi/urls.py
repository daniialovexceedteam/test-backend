from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AccountViewSet, CardViewSet, TransactionViewSet, CustomTokenObtainPairView

router = DefaultRouter()
router.register('accounts', AccountViewSet)
router.register('cards', CardViewSet)
router.register('transactions', TransactionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("api/login/",  CustomTokenObtainPairView.as_view(), name="jwt-login"),
]