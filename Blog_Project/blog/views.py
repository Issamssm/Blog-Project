from django.shortcuts import render,get_object_or_404, redirect
from .models import Post,CommentSysteme
from .forms import PostCreatForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages



def home(request):
    l_post = Post.objects.all()
    paginator = Paginator(l_post, 5)
    page = request.GET.get('page')
    try:
        l_post = paginator.page(page)
    except PageNotAnInteger:
        l_post = paginator.page(1)
    except EmptyPage:
        l_post = paginator.page(paginator.num_pages)
        
    context = {
        'title' : 'home',
        'l_post': l_post,
        'page' : page,
        
    }
    return render(request , 'blog/index.html', context)


def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comment.all()
    if request.method == 'POST':
        user = request.user

        body = request.POST.get('body')

        comment = CommentSysteme(name=user, post=post, body=body)

        comment.save()

        return redirect('detaile',post_id)
    
    else: 
        return render(request, 'blog/detail.html',context = {
            'title' : post.title,
            'post' : post,
            'comments':comments,
        })






# Category
def dev(request):
    l_post = Post.objects.all()
    paginator = Paginator(l_post, 5)
    page = request.GET.get('page')
    try:
        l_post = paginator.page(page)
    except PageNotAnInteger:
        l_post = paginator.page(1)
    except EmptyPage:
        l_post = paginator.page(paginator.num_pages)
    context = {
        'title' : 'Developpment',
        'l_post' : Post.objects.filter(categry='programming'),
        'page' : page,
    }
    return render(request , 'Category/Dev.html', context)

def EH(request):
    l_post = Post.objects.all()
    paginator = Paginator(l_post, 5)
    page = request.GET.get('page')
    try:
        l_post = paginator.page(page)
    except PageNotAnInteger:
        l_post = paginator.page(1)
    except EmptyPage:
        l_post = paginator.page(paginator.num_pages)
    context = {
        'title' : 'Ethical Hacking',
        'l_post' : Post.objects.filter(categry='Ethical Hacking'),
        'page' : page,
    }
    return render(request , 'Category/Eh.html', context)

def Mark(request):
    l_post = Post.objects.all()
    paginator = Paginator(l_post, 5)
    page = request.GET.get('page')
    try:
        l_post = paginator.page(page)
    except PageNotAnInteger:
        l_post = paginator.page(1)
    except EmptyPage:
        l_post = paginator.page(paginator.num_pages)
    context = {
        'title' : 'Marketing',
        'l_post' : Post.objects.filter(categry='Marketing'),
        'page' : page,
    }
    return render(request , 'Category/Mark.html', context)

def Another(request):
    l_post = Post.objects.all()
    paginator = Paginator(l_post, 5)
    page = request.GET.get('page')
    try:
        l_post = paginator.page(page)
    except PageNotAnInteger:
        l_post = paginator.page(1)
    except EmptyPage:
        l_post = paginator.page(paginator.num_pages)
    context = {
        'title' : 'Another',
        'l_post' : Post.objects.filter(categry='Another'),
        'page' : page,
    }
    return render(request , 'Category/Another.html', context)




class PostCreatView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['title', 'content', 'image','categry']
    template_name = 'blog/new_post.html'
    form_class = PostCreatForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # to add context to class
    # def get_context_data(self, **kwargs):
    #     contact = ContactUs.objects.all()
    #     context = super().get_context_data(**kwargs)
    #     context['message'] = contact
    #     return context



class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    form_class = PostCreatForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Check if the user is the owner of the post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
        
    # to add context to class
    # def get_context_data(self, **kwargs):
    #     contact = ContactUs.objects.all()
    #     context = super().get_context_data(**kwargs)
    #     context['message'] = contact
    #     return context
    



class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    # to add context to class
    # def get_context_data(self, **kwargs):
    #     contact = ContactUs.objects.all()
    #     context = super().get_context_data(**kwargs)
    #     context['message'] = contact
    #     return context
    
    
    

def contact(request):
        
    context = {
        'title' : 'contact',
    }
    return render(request , 'blog/contact.html', context)





