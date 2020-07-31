from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Customer, Labourer, User, Interface
from django import forms

class CustomerSignUpForm(UserCreationForm):
    
    first_name = forms.CharField(required= True)
    last_name = forms.CharField(required= True)
    phone_number = forms.CharField(required= True)
    locality = forms.CharField(required= True)
    photo = forms.ImageField(required= True)
    email = forms.EmailField(required= True)

    class Meta(UserCreationForm.Meta):
        model= User

    @transaction.atomic    
    def save(self):
        user=super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.locality = self.cleaned_data.get('locality')
        user.photo = self.cleaned_data.get('photo')
        user.save()
        customer= Customer.objects.create(user=user)
        customer.email = self.cleaned_data.get('email')
        customer.save()
        return user



class LabourerSignUpForm(UserCreationForm):
    
    first_name = forms.CharField(required= True)
    last_name = forms.CharField(required= True)
    phone_number = forms.CharField(required= True)
    locality = forms.CharField(required= True)
    photo = forms.ImageField(required= False)
    skill_set= forms.CharField(required= True)

    class Meta(UserCreationForm.Meta):
        model= User

    @transaction.atomic    
    def save(self):
        
        user=super().save(commit=False)
        user.is_labourer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.locality = self.cleaned_data.get('locality')
        user.photo = self.cleaned_data.get('photo')
        user.save()
        labourer= Customer.objects.create(user=user)
        labourer.skill_set = self.cleaned_data.get('skill_set')
        labourer.save()
        
        return user    