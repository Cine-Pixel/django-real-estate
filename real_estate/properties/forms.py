from django import forms

from .models import Image, Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = "__all__"
        exclude = ('owner', )


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image 
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }
