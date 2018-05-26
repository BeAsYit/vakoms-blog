from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail

from django.shortcuts import render, get_object_or_404, redirect
from allauth.account.decorators import verified_email_required
# from allauth.
from .forms import PostForm, CommentForm, BlogForm
from .models import Post, Comment, Blog


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs':blogs})


def post_list(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/post_list.html', {'blog': blog})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})


@verified_email_required
def blog_new(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog/blog_edit.html', {'form': form})


@verified_email_required
def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('post_detail', pk=blog.pk)
    else:
        form = PostForm(instance=blog)
    return render(request, 'blog/blog_edit.html', {'form': form})


@verified_email_required
def post_new(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = blog
            post.save()
            return redirect('post_list', pk=blog.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})


@verified_email_required
def post_edit(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})


@verified_email_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            # send message to author
            if post.author != request.user:
                user = get_object_or_404(User, id=post.author.author_id)
                subject = 'Your post {} was commented by {}'.format(post.title, request.user)
                message = '{} check your blog post faster, {} left a comment!'.format(user.username, request.user)
                from_email = settings.EMAIL_HOST_USER
                to_list = [user.email]
                send_mail(subject, message, from_email, to_list, fail_silently=True)
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})


@verified_email_required
def reply_to_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.post = get_object_or_404(Post, pk=comment.post_id)
            reply.author = request.user
            reply.parent_id = comment.id
            reply.save()
            return redirect('post_detail', pk=comment.post_id)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form':form})