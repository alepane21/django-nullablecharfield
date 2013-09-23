from django.forms.widgets import TextInput
from django.utils.html import format_html
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
        if self.isnull:
            checkbox = format_html(' <input type="checkbox" onchange="NullableText.null_event(this)" name="{0}" id="{0}" value="1"{1}><label class="vCheckboxLabel" for="{0}">{2}</label>', 'id_' + name + '_isnull', checked, _('Not specified'))
        return super(TextInput, self).render(name, value, attrs) + checkbox

    def value_from_datadict(self, data, files, name):
        null = data.get(name + '_isnull')
        value = data.get(name)
        if null == '1':
            return None
        return value
