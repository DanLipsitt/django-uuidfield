import uuid

from django.test import TestCase

from uuidfield.uuidfield_tests.models import UUIDFieldTestModel


class UUIDFieldTestCase(TestCase):

    def test_auto_uuid4(self):
        inst = UUIDFieldTestModel.objects.create()
        self.assertTrue(inst.uuid)
        self.assertTrue(isinstance(inst.uuid, uuid.UUID))
