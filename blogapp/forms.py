from django import forms
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    image=forms.ImageField()
    

   
class PostModelForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=['title','content','image']
