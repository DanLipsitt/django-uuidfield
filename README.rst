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

Utilities
=========

.. module:: uuidfield.utils

	The ``uuidfield.utils`` module contains utilities to convert a UUID to and
	from a short URL safe string.

``to_short_string``
-------------------

.. method:: to_short_string(value)

	Converts a UUID instance to a short, URL safe string (via Python's
	``base64.urlsafe_b64encode`` method, stripping trailing ``'='`` padding
	characters).

You can use a string value as part of a UUID field lookup, for example::

	>>> my_uuid = uuid.UUID('54755d26-a264-479d-bc23-3292a4e8edac')
	>>> MyModel.objects.create(uuid=my_uuid)
	>>> MyModel.objects.get(uuid=to_short_string(my_uuid)).uuid
	UUID('54755d26-a264-479d-bc23-3292a4e8edac')

``from_short_string``
---------------------

.. method:: from_short_string(value, ignore_errors=False)

	Attempts to convert a string to a UUID instance.

	:param value: The string to be converted.
	:param ignore_errors: If set to ``True`` (default is ``False``) then
		``None`` will be returned if any error is encountered trying to convert
		the string.
