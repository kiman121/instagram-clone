from django.forms import ModelForm
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description', 'post_image', 'tag']
        widgets ={
            'tag': forms.Select()
        }