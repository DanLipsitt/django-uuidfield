import uuid

from django.test import TestCase

from uuidfield.uuidfield_tests import models
from uuidfield import utils


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

    def test_is_uuid(self):
        models.Auto.objects.using(self.database).create()
        # Retrieve the data from the database to ensure the field gets coerced
        # back to UUID.
        obj = models.Auto.objects.using(self.database).get()
        self.assertTrue(isinstance(obj.uuid, uuid.UUID))

    def test_shortstring_filter(self):
        models.Nullable.objects.using(self.database).create(
            uuid=uuid.UUID('54755d26-a264-479d-bc23-3292a4e8edac')
        )
        obj = models.Nullable.objects.using(self.database).get(
            uuid='VHVdJqJkR528IzKSpOjtrA'
        )
        self.assertEqual(
            obj.uuid,
            uuid.UUID('54755d26-a264-479d-bc23-3292a4e8edac')
        )


class FallbackUUIDFieldTestCase(UUIDFieldTestCase):
    database = 'sqlite'
    multi_db = True


class UtilsTest(TestCase):
    example_uuid = uuid.UUID('54755d26-a264-479d-bc23-3292a4e8edac')
    example_uuid_string = 'VHVdJqJkR528IzKSpOjtrA'

    def test_to_string(self):
        self.assertEqual(
            utils.to_short_string(self.example_uuid),
            self.example_uuid_string
        )

    def test_from_string(self):
        self.assertEqual(
            utils.from_short_string(self.example_uuid_string),
            self.example_uuid
        )

    def test_from_bad_string(self):
        self.assertRaises(TypeError, utils.from_short_string, 'a')
        self.assertRaises(ValueError, utils.from_short_string, 'aaaaAA==')
        self.assertEqual(
            utils.from_short_string('a', ignore_errors=True),
            None
        )
        self.assertEqual(
            utils.from_short_string('aaaaAA==', ignore_errors=True),
            None
        )
