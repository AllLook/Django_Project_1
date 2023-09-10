from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    telephone = forms.IntegerField()
    address = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=0, max_value=120)
    about_me = forms.CharField(widget=forms.Textarea)
    password = forms.CharField()
    user_photo = forms.ImageField(required=False)
