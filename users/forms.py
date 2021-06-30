from django import forms


class SignupForm(forms.Form):
    username = forms.CharField(label="Your name", required=True)
    email = forms.EmailField(required=True, label_suffix=":*")
    password = forms.CharField(required=True, label_suffix=":*" )

class LoginForm(forms.Form):
    username = forms.CharField(required=True, label_suffix=":*")
    password = forms.CharField(required=True, label_suffix=":*" , error_messages={'invalid': "Invalid Password"})
