"""
Module with forms for our blog
"""
from django import forms
from. models import Blog, Comment, Post


class BlogForm(forms.ModelForm):
    """
    This form is for creating new blog instance
    """
    class Meta:
        model = Blog
        fields = ('title',)


class PostForm(forms.ModelForm):
    """
    This form is for creating new post instance
    """
    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
    """
    This form is for creating new comment instance
    """
    class Meta:
        model = Comment
        fields = ('text',)
