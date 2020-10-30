"""
 In Django it's possible to create forms directly from the model itself.
And allow Django to handle all the form validation.
"""

# import forms to use built-in form funtionalities
from django import forms

# we import our Item model
from .models import Item


# the form will be a class that inherits builin django class
class ItemForm(forms.ModelForm):
    # tell the form which model is going to be associated with
    class Meta:
        model = Item
        fields = ['name', 'done']
