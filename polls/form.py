from django import forms

languages= [
    ('c++', 'cpp'),
    ('python', 'python'),
    ('java', 'java'),
    ]

class NameForm(forms.Form):
    code = forms.FileField()
    language = forms.CharField(label='choose language', widget=forms.Select(choices=languages))
    # code = forms.CharField()
    # problemID = forms.IntegerField()