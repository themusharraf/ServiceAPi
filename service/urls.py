from rest_framework.routers import DefaultRouter
from service.views import SubscriptionModelViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'subscriptions', SubscriptionModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]

