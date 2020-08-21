from django import forms
from django.forms import ModelForm
from . import models

class lkEmptyForm(ModelForm):
    class Meta:
        model = models.lk
        fields = ['url']

class lkForm(ModelForm):
    class Meta:
        model = models.lk
        fields = ['content']