from django import forms
from .models import Image
from django.utils.text import slugify
from urllib import request
from django.core.files.base import ContentFile
# Create your Forms here.

class ImageCreateForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = ('title', 'description', 'url')
        widgets = {
            'url':forms.HiddenInput
        }

        # Check Image Url
        def clean_url(self):
            url = self.cleaned_data["url"]    
            valid_extentions = ['jpg', 'jpeg']
            extentions = url.rsplit('.')[1].lower()
            # Check Image Format
            if extentions not in valid_extentions:
                raise forms.ValidationError('Url Is Not Correct!')
            return url
        
        # Save Image
        def save(self, force_insert=False, force_update=False, commit=True):
            image = super().save(commit=False)
            image_url = self.cleaned_data('url')
            name = slugify(image.title)
            extentions = image_url.rsplit('.')[1].lower()
            image_name = f'{name}.{extentions}'

            response = request.urlopen(image_url)
            image.image.save(image_name, ContentFile(response.read()), save=False)

            if commit:
                image.save()
            return image

