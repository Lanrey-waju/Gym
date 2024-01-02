from django.db import models
from django.utils import timezone

from users.models import CustomUser

# Create your models here.


class Gymmer(models.Model):
    # Choice of different subscription categories
    DAY = "DY"
    THREE_DAYS = "TD"
    EVERYDAY = "ED"
    SUBSCRIPTION_PLANS = {
        EVERYDAY: "Everyday",
        THREE_DAYS: "Three days in a week",
        DAY: "One day",
    }
    subscription_plan = models.CharField(
        max_length=2, choices=SUBSCRIPTION_PLANS, default=DAY
    )
    gymmer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subscription_is_active = models.BooleanField(default=False, null=False)
    started = models.DateTimeField(auto_now_add=True, default=timezone.now)
