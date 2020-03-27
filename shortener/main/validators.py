from django.core.exceptions import ValidationError 
from django.core.validators import URLValidator

def validate_url(value):
    url_validator=URLValidator()
    v1=True
    v2=True 
    try:
        url_validator(value)
    except:
        v1=False
    value1="http://"+value 
    try:
        url_validator(value1)
    except:
        v2=False
    if not v1 and not v2:
        raise ValidationError("Invalid URL")
    return value

