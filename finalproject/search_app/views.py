from django.shortcuts import render
from MovieApp.models import Movie,CategoryMovie
from django.db.models import Q
# Create your views here.
def searchReasult(request):
        query = request.GET.get('q', '')

        if query:
            movies = Movie.objects.filter(Q(title__icontains=query) | Q(category__name__icontains=query))
        else:
            movies = Movie.objects.all()

        context = {
            'movies': movies,
            'search_query': query,
        }

        return render(request, 'search.html', context)


