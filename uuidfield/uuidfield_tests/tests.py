import uuid

from django.test import TestCase

from uuidfield.uuidfield_tests import models


class UUIDFieldTestCase(TestCase):
    database = 'default'

    def test_auto(self):
        obj = models.Auto.objects.using(self.database).create()
        self.assertTrue(isinstance(obj.uuid, uuid.UUID))

        obj2 = models.Auto.objects.using(self.database).create()
        self.assertNotEqual(obj.uuid, obj2.uuid)

    def test_auto_manual_assign(self):
        test_uuid = uuid.UUID('12345678123456781234567812345678')
        manually_assigned = models.Auto.objects.using(self.database)\
            .create(uuid=test_uuid)
        self.assertEqual(manually_assigned.uuid, test_uuid)

    def test_custom_auto(self):
        obj = models.CustomAuto.objects.using(self.database)\
            .create(name='test')
        self.assertTrue(isinstance(obj.uuid, uuid.UUID))

        self.assertEqual(obj.uuid, models.custom_uuid(obj))

        obj2 = models.CustomAuto.objects.using(self.database)\
            .create(name='different')
        self.assertNotEqual(obj.uuid, obj2.uuid)

    def test_custom_auto_manual_assign(self):
        test_uuid = uuid.UUID('12345678123456781234567812345678')
        manually_assigned = models.CustomAuto.objects.using(self.database)\
            .create(uuid=test_uuid)
        self.assertEqual(manually_assigned.uuid, test_uuid)

    def test_custom_null(self):
        obj = models.Nullable.objects.using(self.database).create()
        self.assertTrue(obj.uuid is None)

        test_uuid = uuid.UUID('12345678123456781234567812345678')
        obj = models.Nullable.objects.using(self.database)\
            .create(uuid=test_uuid)
        self.assertEqual(obj.uuid, test_uuid)

    def test_lookup(self):
        obj = models.Auto.objects.using(self.database).create()
        get = models.Auto.objects.using(self.database).get
        self.assertEqual(get(uuid=obj.uuid), obj)
        self.assertEqual(get(uuid=obj.uuid.hex), obj)
        self.assertEqual(get(uuid=unicode(obj.uuid.hex)), obj)


class FallbackUUIDFieldTestCase(UUIDFieldTestCase):
    database = 'sqlite'
    multi_db = True
