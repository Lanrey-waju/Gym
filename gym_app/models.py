from django.db import models
from users.models import CustomUser

# Create your models here.


class Gymmer(models.Model):
    DAY = "DY"
    THREE_DAYS = "TD"
    EVERYDAY = "ED"
    SUBSCRIPTION_PLANS = {
        EVERYDAY: "Everyday",
        THREE_DAYS: "Three days in a week",
        DAY: "One day",
    }
    gymmer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subscription_plan = models.CharField(
        max_length=2, choices=SUBSCRIPTION_PLANS, default=DAY
    )
