from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
# Create your views here.

def index(request):
    content = Movie.objects.order_by('pk')
    context = {
        'contents' : content,
    }
    return render(request, 'reviews/index.html', context)

def create(request):
    if request.method == "POST":
        movieform = MovieForm(request.POST)

        if movieform.is_valid():
            movieform.save()
            return redirect('reviews:index')
    else:
        movieform = MovieForm()
    context = {
        'movieform':movieform,
    }

    return render(request, 'reviews/create.html', context)

def info(request, pk):
    contentt = Movie.objects.get(pk=pk)
    context = {
        'content':contentt,
    }
    return render(request, 'reviews/info.html', context)

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        movieform = MovieForm(request.POST, instance=movie)
        if movieform.is_valid():
            movieform.save()
            return redirect('reviews:info', movie.pk)
    else:
        movieform = MovieForm(instance=movie)
    context = {
        'movieform': movieform,
    }
    return render(request, 'reviews/update.html', context)

def delete(request, pk):
    Movie.objects.get(pk=pk).delete()
    return redirect('reviews:index')

def main(request):
    return render(request, 'reviews/main.html')