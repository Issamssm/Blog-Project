from django.shortcuts import render,redirect
from .forms import RegisterForm, loginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.forms import UserCreationForm
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, f'Congratulations {user}, your registration has been completed successfully')
            login(request,user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html',{
        'title' : 'Register',
        'form' : form,
        })
    
def login_user(request):
    if request.method == 'POST':
        form = loginForm()
        username = request.POST['username']
        password = request.POST['password']
        user_auth = authenticate(request, username=username, password=password)
        if user_auth is not None:
            login(request,user_auth)
            return redirect('home')
        else:
            messages.warning(request,'There is an error in the username and password')
    else:
        form = loginForm()    
    return render(request, 'user/login.html',{
        'title': 'Login',
        'form':form
    })

        
        
def logout_user(request):
    logout(request)
    return render(request,'user/logout.html',{
        'title' : 'Logout'
    })
    
@login_required(login_url='login')
def profile(request):
    posts = Post.objects.filter(author=request.user)
    post_list = Post.objects.filter(author=request.user)
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    
    return render(request,'user/profile.html',{
        'title' : 'Profile',
        'posts' : posts,
        'post_list' : post_list,
        'page' : page,
    })
    
@login_required(login_url='login')
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance= request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES, instance= request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(request, f'your profile is updated')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance= request.user)
        profile_form = ProfileUpdateForm(instance= request.user.profile)
    
    context = {
        'title' : 'Profile update',
        'user_form' : user_form,
        'profile_form' : profile_form,
    }
    
    return render(request, 'user/profile_update.html', context)