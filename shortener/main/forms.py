from django import forms 
from main import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .validators import validate_url

def validate_url(value):
    url_validator=URLValidator()
    try:
        url_validator(value)
    except:
        try:
            url_validator('http://'+value)
        except:
            raise ValidationError("Invalid URL")
    return value


class URLinputform(forms.Form):
    url=forms.CharField(max_length=500,label='url',validators=[validate_url]) 


