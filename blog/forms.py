from django import forms
from. models import Blog, Comment, Post


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title',)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
