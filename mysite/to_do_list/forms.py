from .models import ToDo
from django import forms
import datetime

class ToDoForm(forms.ModelForm):
    refresh_time = forms.TimeField(
            widget=forms.TimeInput(format='%H:%M')
        )

    def __init__(self, *args, **kwargs):
        super(ToDoForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = ToDo
        fields = ['task', 'refresh_days_field', 'refresh_time']
