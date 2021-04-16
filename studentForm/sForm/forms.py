from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from views import *


class StudentForm(forms.Form):
    name = forms.CharField(label='Enter Name', max_length=25, required=False)

    def clean_name(self):
        input_name = self.cleaned_data['name']
        if len(input_name.strip()) == 0:
            raise ValidationError("Please enter a name")
        return input_name

    gender_choices = (('male', 'Male'), ('female', 'FeMale'), ('others', 'Others'))
    gender = forms.ChoiceField(label='Select Gender', choices=gender_choices,
                               widget=forms.RadioSelect(), required=False)

    def clean_gender(self):
        input_gender = self.cleaned_data['gender']
        if len(input_gender.strip()) == "":
            raise ValidationError("Please select gender")
        return input_gender

    email = forms.EmailField(label='Enter Email Id')

    def clean_email(self):
        input_email = self.cleaned_data['email']
        validator = EmailValidator("Please enter a valid email address")
        validator(input_email)
        return input_email

    def clean_photo(self):
        input_photo = self.cleaned_data['photo']
        validator = EmailValidator("Please select a .jpeg/.jpg files only")
        validator(input_photo)
        return input_photo
