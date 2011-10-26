import uuid

from django.db import models

from uuidfield.fields import UUIDField


class Auto(models.Model):
    uuid = UUIDField(auto=True)


def custom_uuid(obj):
    namespace = uuid.UUID('12345678123456781234567812345678')
    return uuid.uuid5(namespace, obj.name)


class CustomAuto(models.Model):
    name = models.CharField(max_length=10)
    uuid = UUIDField(auto=custom_uuid)


class Nullable(models.Model):
    uuid = UUIDField(null=True)


class PrimaryKey(models.Model):
    id = UUIDField(primary_key=True, auto=True)
