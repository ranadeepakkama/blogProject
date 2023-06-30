from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .form import ContentForm,CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required


# Create your views here.

#register page 
def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'new user created for ' + user)
            return redirect('login')
            
    context = {'form' : form}
    return render(request, 'register.html', context)

#login  
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,"invalid username or password")
            return redirect('login')
    context = {}
    return render(request,'login.html',context)

def logoutRequest(request):
    logout(request)
    return redirect('logout')

#blog_page 
def blog_page(request,id):
    data = get_object_or_404(Post,id = id) 
    context = {'data': data}
    return render(request,'blog.html',context)
    
#home_page 

def blogPage(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        image = request.FILES.get('image')
        if image is not None and image != '':
            k = Post(title=title, content=content, author=author,image=image)
            k.save()
            messages.success(request,"new post created   "+ title)
        return redirect('home')
    return render(request, 'index.html')
    
def page(request):
    data = Post.objects.all()
    context = {'data': data}
    return render(request,'page.html',context)


#edit 
def edit(request,id):
    data = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = ContentForm(request.POST)

        if form.is_valid():
            data.content = form.cleaned_data['content']
            data.save()
            return redirect('blog_page',id = data.id )
    
    else :
        data = get_object_or_404(Post, id=id)
        return render(request,'edit.html', {'data' : data})
    
#edit_image
def edit_image(request, id):
    new_image = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        data = request.FILES.get('image')
        new_image.image = data 
        new_image.save()
        return redirect('blog_page',id = new_image.id) 
    else:
        image = get_object_or_404(Post,id= id)
    context = {'image':image}
    return render(request,'img_edit.html',context)


def delete(request,id = id):
    data = get_object_or_404(Post, id=id)
    data.delete()
    return redirect('page_list')

def search(request):
    query = request.GET.get('q')
    if query:
        filter_posts = Post.objects.filter(title__icontains=query)
    else:
        filter_posts = None

    return render(request, 'page.html',{'filter_posts': filter_posts})