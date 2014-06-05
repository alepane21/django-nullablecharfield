from django.forms.widgets import TextInput
from django.utils.html import format_html, mark_safe
from django.utils.translation import string_concat
from django.utils.translation import gettext_lazy as _

class NullableTextWidget(TextInput):
    """
    A Widget for displaying ManyToMany ids in the "raw_id" interface rather than
    in a <select multiple> box.
    """

    isnull = False

    class Media:
        js = ('js/nullabletext.js',)

    def __init__(self, attrs=None):
        if attrs is not None:
            self.isnull = attrs.pop('isnull', self.isnull)
        super(TextInput, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        if attrs is None:
            attrs = {}
        attrs['class'] = 'vTextField nullable_text'
        attrs['onchange'] = 'NullableText.input_event(this)'
        checked = ''
        if value is None:
            checked = ' checked="checked"'
        checkbox = format_html('')
        widget_name = 'id_' + name + '_isnull'
        if self.isnull:
            checkbox = string_concat(' <input type="checkbox" onchange="NullableText.null_event(this)" name="', widget_name,'" id="', widget_name, '" value="1"', checked,'><label class="vCheckboxLabel" for="', widget_name, '">', _('Not specified'),'</label>')
        return mark_safe(string_concat(super(TextInput, self).render(name, value, attrs), checkbox))

    def value_from_datadict(self, data, files, name):
        null = data.get(name + '_isnull')
        value = data.get(name)
        if null == '1':
            return None
        return value
