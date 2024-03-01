from django.shortcuts import render, redirect
from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Замініть 'post_list' на URL вашого списку дописів
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
# Create your views here.
