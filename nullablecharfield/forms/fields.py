from django.forms.fields import CharField
from django.utils.encoding import smart_str
from nullablecharfield.widgets import NullableTextWidget

class CharNullField(CharField):
    widget = NullableTextWidget
    description = "CharField that stores NULL"

    def __init__(self, *args, **kwargs):
        if 'null' in kwargs:
            self.null = kwargs['null']
            del kwargs['null']
        super(CharNullField, self).__init__(*args, **kwargs)
        self.widget.isnull = self.null

    def to_python(self, value):
        if value is None:
            return None
        return smart_str(value)

    def get_db_prep_value(self, value):
        return value
