from .forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post
#IMPORTO EL MODELO PERSONA
from .models import Persona
from django.shortcuts import render, get_object_or_404
#IMPORTO LA COSA PARA EL ACCESO CON CLAVE
from django.contrib.auth.decorators import login_required
"""
def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
"""
#Defino el llamado a la lista de personas
def post_list(request):
    personas = Persona.objects.all().order_by('apellido')
    return render(request, 'blog/post_list.html', {'personas': personas})

"""    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
"""    

def post_detail(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    return render(request, 'blog/post_detail.html', {'persona': persona})

"""
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
"""

"""
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
"""

@login_required #REQUIERE LOGUEO
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.author = request.user
            #post.published_date = timezone.now()
            persona.save()
            return redirect('post_detail', pk=persona.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})



"""
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    """
@login_required #REQUIERE LOGUEO
def post_edit(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=persona)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.author = request.user
            #post.published_date = timezone.now()
            persona.save()
            return redirect('post_detail', pk=persona.pk)
    else:
       # form = PostForm(instance=post)
        form = PostForm(instance=persona)
    return render(request, 'blog/post_edit.html', {'form': form})
    
    
"""    
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_draft_list(request):
    personas = Persona.objects.all()
    return render(request, 'blog/post_draft_list.html', {'personas': personas})
"""

"""    
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
"""
def post_publish(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    persona.publish()
    return redirect('post_detail', pk=pk)
    
@login_required #REQUIERE LOGUEO    
def post_remove(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    persona.delete()
    #Te lleva de vuelta a la página principal
    return redirect('post_list')
