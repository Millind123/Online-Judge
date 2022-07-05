from django import forms

class NameForm(forms.Form):
    code = forms.FileField()
    # code = forms.CharField()
    # problemID = forms.IntegerField()