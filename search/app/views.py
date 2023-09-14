from django.shortcuts import render, get_object_or_404
from . models import *
from django.db.models import Q 
from django.http import JsonResponse


def home(request):

    title = request.GET.get('search')
    if title:
        movies = Movies.objects.filter(Q(title__icontains=title))
    else:
        # movies[:5]
        movies = Movies.objects.all()[:5]
        x = slice(5)
        print(movies[x])

    context = {
        'movies':movies,
    }

    return render(request, 'app/index.html', context)


def detail_page(request, id):

    detail = get_object_or_404(Movies, pk=id)


    context={
        "detail":detail,
    }

    return render(request, 'app/detail_page.html', context)

# def getProfiles(request):

#     profiles = Profile.objects.all()

#     # args ={
#     #     "profiles": list(profiles.value())
#     # }
#     return JsonResponse({"profiles": list(profiles.value())})