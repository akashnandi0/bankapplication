from django.forms import ModelForm
from django import forms
from profiles.models import createProfileModel


class createProfileForm(ModelForm):
    # user = forms.IntegerField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model = createProfileModel
        fields = "__all__"
        widgets = {'user': forms.HiddenInput(),
                   'date_of_birth': forms.DateInput(attrs={'class':'datepicker'})
                   }
