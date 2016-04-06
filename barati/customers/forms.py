from django import forms
from .models import *
from django.forms.models import inlineformset_factory


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
        WHAT_ARE_YOU_CHOICES = (
      ('bride', 'bride'),
      ('groom', 'groom'),
      ('family', 'family'),
      ('friend', 'friend'),
   )
        fields = ('what_are_you','first_name','middle_name','last_name','religion','email','contact1','contact2','contact3')

        # widgets = {
            
        #     #'what_are_you': forms.CharField(label='what are you', choice=WHAT_ARE_YOU_CHOICES, widget=forms.Select(attrs={'class':'regDropDown'})),
        #     #'what_are_you':forms.TextInput(attrs={'class': 'form-control,dropdown','placeholder':'Enter your first_name'}),
        #     'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your first_name'}),
        #     'middle_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your middle_name'}),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your last_name'}),
        #     #'religion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your religion'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter your email'}),
        #     #'phone_regex': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your phone-no'}),
        #     'contact1': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your contact, format :+999999999'}),
        #     'contact2': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your contact, format :+999999999'}),
        #     'contact3': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your contact, format :+999999999'}),
        #     }

class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('building_number','street','locality','landmark','city','state','country','zipcode')

        widgets = {
            

            #'what_are_you':forms.TextInput(attrs={'class': 'form-control,dropdown','placeholder':'Enter your first_name'}),
            'building_number': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter building number'}),
            'street': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter street'}),
            'locality': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your locality'}),
            'landmark': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter landmark'}),
            'city': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter city'}),
            'state': forms.Select(attrs={'class': 'form-control ','placeholder':'Enter state'}),
            'country': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter country'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter zipcode'}),
            }
            
            
            
            
            
            

