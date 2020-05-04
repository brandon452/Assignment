from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

free_email_provider_domains=['googlemail.com', 'icloud.com', 'gmail.com', 'yahoo.com', 'hotmail.com', 'hotmail.co.uk', 'me.com']
def validate_domain_name(value):
    if not 'gmail.com' in value:#and not 'icloud.com' and not 'yahoo.com' and not 'hotmail.com' and not 'hotmail.co.uk' and not 'me.com' and not 'googlemail.com' in value doesnt work:
        raise ValidationError(_("Check your domain name"))
    return value

phone_regex = RegexValidator(regex=r'^\+(254)\d{9}$', message='Phone number must be entered in the format: "+254..." Minimum 12 digits.')