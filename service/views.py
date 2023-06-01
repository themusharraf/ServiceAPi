from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from service.models import Subscription
from service.serializers import SubscriptionSerializer


class SubscriptionModelViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
