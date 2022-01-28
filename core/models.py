from django.db import models


class BaseModel(models.Model):
    create_timestamp = models.DateField(auto_now_add=True)
    update_timestamp = models.DateField(auto_now=True)

    class Meta:
        abstract = True
