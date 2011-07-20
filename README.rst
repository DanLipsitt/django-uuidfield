django-uuidfield
---------------

Provides a UUIDField for use in your Django models.

Installation
============

Install it with pip (or easy_install)::

	pip install django-uuidfield

Usage
=====

Simply add the UUIDField to your model. For example::

    from uuidfield import UUIDField

    class MyModel(models.Model):
        uuid = UUIDField(auto=True)


.. class:: uuidfeild.UUIDField

    This field allows you to store and reference UUID objects in your model.

    In PostgreSQL, the field is represented in the database by a true UUID
    column type. In all other databases, it will be represented by a character
    field of length 32.

    This field is compatible with South.

	.. method:: __init__(auto=False, **standard_field_kwargs)

        :param auto:
            Used to generate a UUID for models on save when the field attribute
            is not provided. If set, ``editable=False`` and ``unique=True`` are
            implied for this field.

            To generate a standard UUID4, set to ``True``. For custom UUID
            generation, set to a callable that accepts the model instance as
            its only argument.
