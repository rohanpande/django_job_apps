from django import forms
from django.utils.translation import gettext_lazy as _
from subscribe.models import Subscribe

def validate_comma(value):
    if ',' in value:
        raise forms.ValidationError("Invalid Last Name")
    return value


class SubscribeForm(forms.ModelForm):
    class Meta:
        
        model = Subscribe

        # exclude = ('first_name', )
        # fields = __all__

        labels = {
            'first_name': _('Enter First Name'),
            'last_name': _('Enter Last Name'),
            'email': _('Enter Email'),
            'option': _("Select Options")
        }

        help_texts = {'first_name': _('Enter characters only')}

        error_messages = {
            'first_name':{
                "required": _('You can"t move forward without first name')
            }
        }

        fields = ['first_name', 'last_name', 'email', 'option']

# class SubscribeForm(forms.Form):

#     first_name = forms.CharField(required= True,max_length=100, label="Enter First name", help_text="Enter Characters only", validators=[validate_comma])
#     last_name = forms.CharField(required= True,max_length=100, label="Enter Last name", disabled = False, validators=[validate_comma])
#     email = forms.EmailField(required= True, max_length=100, label="Enter Email", validators=[validate_comma])

#     # def clean_first_name(self):
#     #     data = self.cleaned_data['first_name']
#     #     if "," in data:
#     #         raise forms.ValidationError("Invalid First Name")
#     #     return data