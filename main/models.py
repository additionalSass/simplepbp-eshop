import uuid
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30, unique=True)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(default='Default')
    stocks = models.IntegerField(validators=[MinValueValidator(0)])
    recom_status_last_update = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name