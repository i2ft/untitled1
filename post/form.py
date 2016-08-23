from django import forms

<<<<<<< HEAD
=======

from markdownx.fields import MarkdownxFormField
>>>>>>> a4dcd9e59c954e93355bd41a657dcd062f2a5d67
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "parent",
        ]
