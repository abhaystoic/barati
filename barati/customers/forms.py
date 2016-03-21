from django import forms

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