from django import forms


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        print("clean email")

    def clean_password(self):
        print("clean password")
