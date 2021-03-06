"""
This is module with unittests for blog.forms
"""
from django.test import TestCase
from blog.forms import BlogForm, PostForm, CommentForm


class TestForms(TestCase):
    def test_BlogForm(self):
        """
        Tests for BlogForm
        """
        form_data = {'title': 'sometitle'}
        form = BlogForm(data=form_data)
        self.assertTrue(form.is_valid())
        empty_form = BlogForm()
        self.assertFalse(empty_form.is_valid())

    def test_PostForm(self):
        """
        Tests for PostForm
        """
        form_data = {'title': 'sometitle', 'text': 'sometext'}
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())
        bad_form_data = {'title': 'sometitle'}
        bad_form = PostForm(data=bad_form_data)
        self.assertFalse(bad_form.is_valid())

    def test_CommentForm(self):
        """
        Tests for CommentForm
        """
        form_data = {'text': 'sometext'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())
        empty_form = CommentForm()
        self.assertFalse(empty_form.is_valid())