from django.forms import ModelForm
from django import forms
from .models import Post,Comment,Like

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description', 'post_image', 'tag']
        widgets ={
            'tag': forms.Select()
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'bg-transparent max-h-10 shadow-none'})

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like()
        fields = ['user','post']