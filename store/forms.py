
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from store.models import Customer, Comments, Offer, Support
from django.core.validators import EmailValidator


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter a password with 8 or more characters and at least 1 digit'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UpdateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name','last_name', 'country', 'zipcode','email', 'mobile', 'referrer_code', 'wallet', 'image']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'image': ('Profile Picture'),
        }
        help_texts = {
            'image': ('Please upload a profile picture.'),
        }
        error_messages = {
            'image': {
                'max_length': ("This file is too large."),
                'invalid': ("This file format is not supported."),
            },
        }
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['image']

class WalletForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['wallet']

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['subject', 'comment', 'rate']
       
class CustomerOfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['subject', 'email', 'comment']


class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = [ 'subject', 'email', 'comment']

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    email = forms.EmailField(validators=[EmailValidator], widget=forms.TextInput(attrs={'placeholder': 'Введите email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Введите количество токенов которые хотели бы приобрести, и как мы сможем с вами связаться помимо почты'}), ) 


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'email', 'image', 'mobile', 'referral_code']

