from django.db import models

from uuidfield.fields import UUIDField


class UUIDFieldTestModel(models.Model):
    uuid = UUIDField(auto=True)
