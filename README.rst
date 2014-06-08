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

3. You should set null=True and blank=True in the fields that you want to make nullable, like this::

      from django.db import models
      from nullablecharfield.db.models.fields import CharNullField 
      
      class Person(models.Model): 
          first_name = CharNullField(max_length=30, null=True, blank=True) 
          last_name = CharNullField(max_length=30, null=True, blank=True)
