import uuid

from django.test import TestCase

from uuidfield.uuidfield_tests import models


class UUIDFieldTestCase(TestCase):

    def test_auto(self):
        obj = models.Auto.objects.create()
        self.assertTrue(isinstance(obj.uuid, uuid.UUID))

        obj2 = models.Auto.objects.create()
        self.assertNotEqual(obj.uuid, obj2.uuid)

    def test_auto_manual_assign(self):
        test_uuid = uuid.UUID('12345678123456781234567812345678')
        manually_assigned = models.Auto.objects.create(uuid=test_uuid)
        self.assertEqual(manually_assigned.uuid, test_uuid)

    def test_custom_auto(self):
        obj = models.CustomAuto.objects.create(name='test')
        self.assertTrue(isinstance(obj.uuid, uuid.UUID))

        self.assertEqual(obj.uuid, models.custom_uuid(obj))

        obj3 = models.CustomAuto.objects.create(name='different')
        self.assertNotEqual(obj.uuid, obj3.uuid)

    def test_custom_auto_manual_assign(self):
        test_uuid = uuid.UUID('12345678123456781234567812345678')
        manually_assigned = models.CustomAuto.objects.create(uuid=test_uuid)
        self.assertEqual(manually_assigned.uuid, test_uuid)

    def test_custom_null(self):
        obj = models.Nullable.objects.create()
        self.assertTrue(obj.uuid is None)

        test_uuid = uuid.UUID('12345678123456781234567812345678')
        obj = models.Nullable.objects.create(uuid=test_uuid)
        self.assertEqual(obj.uuid, test_uuid)

    def test_lookup(self):
        obj = models.Auto.objects.create()
        self.assertEqual(models.Auto.objects.get(uuid=obj.uuid), obj)
        self.assertEqual(models.Auto.objects.get(uuid=obj.uuid.hex), obj)
        self.assertEqual(models.Auto.objects.get(uuid=unicode(obj.uuid.hex)),
            obj)
