from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
from django.http import JsonResponse
from datetime import date

from .forms import BlogPostForm, ProfileForm
from .models import BlogPost, Profile, Like, AppUser


def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        birthdate = request.POST.get('birthdate')

        if password != cpassword:
            messages.error(request, 'Passwords do not match')
            return render(request, 'signup.html')
        elif AppUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return render(request, 'signup.html')
        else:
            try:
                user = AppUser.objects.create_user(
                    email=email,
                    name=name,
                    phone=phone,
                    address=address,
                    gender=gender,
                    password=password,
                    birthdate=birthdate,
                )
                messages.success(request, 'Registration successful! You can now login.')
                return redirect('login')
            except Exception as e:
                messages.error(request, f"Error: {e}")
                return render(request, 'signup.html')
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('blog_homepage')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')


def blog_homepage(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def landing(request):
    return render(request, 'Landing.html')


@login_required
def blog_list(request):
    query = request.GET.get('q')
    if query:
        posts = BlogPost.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).order_by('-created_at')
    else:
        posts = BlogPost.objects.all().order_by('-created_at')

    for post in posts:
        post.profile = Profile.objects.filter(user=post.user).first()

    return render(request, 'Blog.html', {'posts': posts, 'query': query})


@login_required
def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog_detail.html', {'post': post})


@login_required
def write_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.user = request.user
            blog_post.save()
            messages.success(request, 'Your blog post has been published!')
            return redirect('blog_list')
    else:
        form = BlogPostForm()

    return render(request, 'write_blog.html', {'form': form})


@login_required
def like_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({'liked': liked, 'like_count': post.likes.count()})


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    like_count = post.likes.count()
    return render(request, 'post_detail.html', {'post': post, 'like_count': like_count})


@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    blogs = BlogPost.objects.filter(user=request.user)
    return render(request, 'profile.html', {'profile': profile, 'blogs': blogs})


@login_required
def update_profile(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'update_profile.html', {'form': form})


@login_required
def update_blog(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', post_id=post.id)
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'update_blog.html', {'form': form, 'post': post})


@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id, user=request.user)
    blog.delete()
    return redirect('profile_view')