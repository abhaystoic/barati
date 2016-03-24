from django import forms
from .models import *

class ContactUsForm(forms.Form):
    name = forms.CharField(label='',
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder':'Name'}
        )
    )
    email = forms.EmailField(label='',
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder':'Email'}
        )
    )
    text = forms.CharField(label='',
        required=True,
        widget=forms.Textarea(
            attrs={'rows' : '6',
                'placeholder':'Some Text Here',
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        uname,provider = email.split('@')
        service,extension = provider.split('.')
        if uname != '' and service != '' and extension != '':
            return email
        raise forms.ValidationError('Email is Not in Correct Format')

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ('first_name','middle_name','last_name','religion','email','contact1','contact2','contact3','address')
        widgets = {
            


            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your first_name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your middle_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your last_name'}),
            'religion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your religion'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter your email'}),
            #'phone_regex': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your phone-no'}),
            'contact1': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your contact'}),
            'contact2': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your contact'}),
            'contact3': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your contact'}),
            'address': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter your message here'}),
            }
