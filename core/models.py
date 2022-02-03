from django.db import models


class BaseModel(models.Model):
    create_timestamp = models.DateTimeFieldField(auto_now_add=True)
    update_timestamp = models.DateTimeFieldField(auto_now=True)

    class Meta:
        abstract = True
