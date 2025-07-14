# detection_app/forms.py
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django import forms
from .models import PatientProfile

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['age', 'gender', 'contact_number']


class CustomAuthenticationForm(AuthenticationForm):
    """
    Custom form for user login to apply specific styling.
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your username',
            'class': 'form-input-field' # This class will be applied
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
            'class': 'form-input-field' # This class will be applied
        })
    )

class CustomUserCreationForm(UserCreationForm):
    """
    Custom form for user registration to apply specific styling.
    """
    # UserCreationForm already has username, password, password2.
    # You might want to add email here if you need it for registration.
    # For now, just ensuring existing fields get the class.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['username', 'password', 'password2']: # password2 is 'Password confirmation'
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({
                    'class': 'form-input-field',
                    'placeholder': self.fields[field_name].label # Use label as placeholder
                })
        # If you add an email field:
        # self.fields['email'].widget.attrs.update({
        #     'class': 'form-input-field',
        #     'placeholder': 'Enter your email'
        # })

    class Meta(UserCreationForm.Meta):
        model = UserCreationForm.Meta.model
        fields = ('username',) + UserCreationForm.Meta.fields[1:] # Keep existing fields, adjust as needed if adding email
        # If adding email:
        # fields = ('username', 'email') + UserCreationForm.Meta.fields[1:]
        
       