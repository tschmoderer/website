# -*- coding: utf-8 -*-
from django import forms
from .models import Homepage, Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ('first_name', 'last_name', 'email', )

class HomepageForm(forms.ModelForm):
    class Meta:
        model   = Homepage
        exclude = ('user', )

class ProfileForm(forms.ModelForm):
    clear_picture = forms.BooleanField(initial=False, required=False)
    class Meta:
        model   = Profile
        widgets = {
            'picture': forms.FileInput(attrs=None)
        }
        exclude = ('user', )