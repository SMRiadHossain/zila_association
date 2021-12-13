from django.contrib.auth.forms import UserCreationForm ,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class PasswordChange(PasswordChangeForm):

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
    def __init__(self, *args, **kwargs):
        super(PasswordChange, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].help_text = "<small><ul><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul></small>"
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'



class EditProfileForm(UserChangeForm):
    password=forms.CharField(label="", widget= forms.TextInput(attrs ={'type':'hidden',}))
    email = forms.EmailField(widget= forms.TextInput(attrs ={'class':'form-control'} ))
    first_name = forms.CharField(max_length =100, widget= forms.TextInput(attrs ={'class':'form-control'} ) )
    last_name = forms.CharField(max_length =100, widget= forms.TextInput(attrs ={'class':'form-control'} ))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].help_text = "<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>"


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",widget= forms.TextInput(attrs ={'class':'form-control','placeholder':'Email address'} ))
    first_name = forms.CharField(label="",max_length =100, widget= forms.TextInput(attrs ={'class':'form-control','placeholder':'First name'} ) )
    last_name = forms.CharField(label="",max_length =100, widget= forms.TextInput(attrs ={'class':'form-control','placeholder':'Last name'} ))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = ""
        self.fields['username'].help_text = "<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>"
        self.fields['username'].widget.attrs['placeholder'] = 'Username'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label = ""
        self.fields['password1'].help_text = "<small><ul><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul></small>"
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label = ""
        self.fields['password2'].help_text = "<small>Enter the same password as before, for verification.</small>"
        self.fields['password2'].widget.attrs['placeholder'] = 'Retype Password'

