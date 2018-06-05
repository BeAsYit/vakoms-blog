from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
# imports for django-allauth
from allauth.account.decorators import verified_email_required
from users.models import CustomUser
from .forms import PostForm, CommentForm, BlogForm
from .models import Post, Comment, Blog


def blog_list(request):
    """
    View to show our blogs
    """
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs':blogs})


def post_list(request, pk):
    """
    View to show posts of specific blog
    """
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/post_list.html', {'blog': blog})


def post_detail(request, pk):
    """
    View to show details of specific post
    """
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})


@verified_email_required
def blog_new(request):
    """
    View to create a new blog
    Requires verified email and logged in status
    """
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
    """
    View to edit a specific blog
    Requires verified email and logged in status
    User must be owner of this blog
    """
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/blog_edit.html', {'form': form})


@verified_email_required
def post_new(request, pk):
    """
    View to make a new post in a specific blog
    Requires verified email and logged in status
    User must be owner of this blog
    """
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
    """
    View to edit a post in a specific blog
    Requires verified email and logged in status
    User must be owner of this blog
    """
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_new.html', {'form': form})


@verified_email_required
def add_comment_to_post(request, pk):
    """
    View to left a comment under specific post
    Requires verified email and logged in status
    If user is not author and commented this post we will send notification to post owner email
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            # send message to author
            user = get_object_or_404(CustomUser, id=post.author.author_id)
            if user.username != str(request.user):
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
    """
    View to reply specific comment
    Requires verified email and logged in status
    """
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