from django.db import models
from django.core.validators import MaxValueValidator
from apps.models import Client


class Service(models.Model):
    name = models.CharField(max_length=100)
    full_price = models.PositiveIntegerField


class Plan(models.Model):
    PLAN_TYPE = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount'),
    )
    plan_type = models.CharField(choices=PLAN_TYPE, max_length=10)
    discount = models.PositiveIntegerField(default=0, validators=[
        MaxValueValidator(100),
    ])


class Subscription(models.Model):
    client = models.ForeignKey(Client, related_name='subscriptions',on_delete=models.PROTECT)
    service = models.ForeignKey(Service , related_name='subscriptions',on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan , related_name='subscriptions',on_delete=models.PROTECT)
