from django.forms import Form, widgets
from django import forms


class FormRegister(Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        username = forms.CharField(max_length=200, min_length=4)

        self.fields[('username', username)]


    # username = forms.CharField(max_length=200, min_length=4)
    # email = forms.CharField(max_length=200, min_length=4)
    # password_1 = forms.CharField(max_length=200, min_length=4,
    #                              widget=widgets.PasswordInput(attrs={'placeholder':'Password'}))
    # password_2 = forms.CharField(max_length=200, min_length=4,
    #                              widget=widgets.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    #
    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if not username.isalnum():
    #         self.add_error('username', 'Only Alphanum chars Allowed!')
    #         return None
    #     return username
    #
    # def clean(self):
    #     password_1 = self.cleaned_data['password_1']
    #     password_2 = self.cleaned_data['password_2']
    #     if password_2 != password_1:
    #         self.add_error('password_1', 'Password does not Match !')
    #
    #     return super(FormRegister, self).clean()