from django.shortcuts import render,redirect,get_object_or_404
from MovieApp.models import Movie,CategoryMovie,FavouriteMovie,Profile
from django.contrib import messages
# Create your views here
from .forms import MovieForm,CommentMovieForm,MovieComment
def index(request):
    movies = Movie.objects.all()
    return render(request,"index.html",{'movies':movies})

def add_movie(request):
    categories = CategoryMovie.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        poster = request.POST.get('poster')
        description = request.POST.get('description')
        release_date = request.POST.get('release_date')
        actors = request.POST.get('actors')
        youtube_trailer_link = request.POST.get('youtube_trailer_link')
        image = request.FILES.get('image')
        category_id = request.POST.get('category')

        try:
            category = CategoryMovie.objects.get(id=category_id)
            movie = Movie.objects.create(
                title=title,
                poster=poster,
                description=description,
                release_date=release_date,
                actors=actors,
                youtube_trailer_link=youtube_trailer_link,
                image=image,
                category=category,
                user=request.user
            )
            messages.success(request, 'Movie added successfully.')
            return redirect('/')
        except CategoryMovie.DoesNotExist:
            messages.warning(request, 'Category does not exist. Please fill out the fields.')
            return redirect('Movie_App:add_movie')

    return render(request, 'add.html', {'categories': categories})

def update(request, id):
    movie = get_object_or_404(Movie, id=id)

    if request.user == movie.user:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('Movie_App:index')
        else:
            form = MovieForm(instance=movie)

        return render(request, 'edit.html', {'form': form})
    else:
        return render(request, 'permission_denied.html')

def delete(request, id):
    movie = get_object_or_404(Movie, id=id)

    if request.user == movie.user:
        movie.delete()
        return redirect('Movie_App:index')
    else:
        return render(request, 'permission_denied.html')
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)

    # comment=MovieComment.objects.all()

    return render(request,"detail.html",{'movie':movie})


def category_detail(request):
    category= CategoryMovie.objects.all()
    context = {
        'category_list':category
    }

    return render(request, "category.html", context)

def detail_category(request, category_id):
    category = get_object_or_404(CategoryMovie, id=category_id)
    movies = Movie.objects.filter(category=category)
    return render(request, "category_movies.html", {'category': category, 'movies': movies})



def add_comment(request,movie_id):
    movie = get_object_or_404(Movie,id=movie_id)

    if request.method == 'POST':
        form = CommentMovieForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
            return redirect('Movie_App:detail', movie_id=movie_id)
    else:
        form = CommentMovieForm()

    return render(request,'add_comment.html', {'form': form, 'movie': movie})


def delete_comment(request, comment_id):
    comment = get_object_or_404(MovieComment, id=comment_id)

    if request.user == comment.user:
        comment.delete()

    return redirect('Movie_App:detail', movie_id=comment.movie.id)

def favourite_move(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.user.is_authenticated:
        user = request.user
        if not FavouriteMovie.objects.filter(user=user, movie=movie).exists():
            FavouriteMovie.objects.create(user=user, movie=movie)
            messages.success(request, 'Movie added to favorites successfully.')
        else:
            messages.warning(request, 'Movie is already in your favorites.')

        return redirect('Movie_App:detail', movie_id=movie_id)
    else:
        messages.info(request, 'Please login to add movies to your favorites.')
        return redirect('Movie_App:detail', movie_id=movie_id)


def remove_favourite(request, favourite_id):
    favourite = get_object_or_404(FavouriteMovie, id=favourite_id)
    if request.user == favourite.user:
        favourite.delete()

    return redirect('Movie_App:favourite_list')

def favourite_list(request):
    user=request.user
    favorites=FavouriteMovie.objects.filter(user=user)

    return render(request,'favourite.html',{'favorites':favorites})