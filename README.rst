Django NullableCharField
==========================

This app is a collection of a widget, form field and db field that allows to have
a nullable charfield inside django.

Quick start
----------------

1. Add "nullablecharfield" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'nullablecharfield',
      )

2. Use in your model CharNullField from nullablecharfield.db.models.fields
