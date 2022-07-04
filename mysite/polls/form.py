from django import forms

class NameForm(forms.Form):
    code = forms.CharField(label='code', max_length=100)
    problemID = forms.IntegerField()