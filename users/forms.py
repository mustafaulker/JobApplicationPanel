from django import forms

from .models import CustomUser


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(label='First name', max_length=30)
    last_name = forms.CharField(label='Last name', max_length=30)
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=True, attrs={'class': 'form-control', 'placeholder': 'Your password'}))

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your username'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your first name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your last name'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your password'})

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'password',)


class HRSignUpForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=True, attrs={'class': 'form-control', 'placeholder': 'Your password'}))

    def __init__(self, *args, **kwargs):
        super(HRSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your password'})

    class Meta:
        model = CustomUser
        fields = ('username', 'password',)
