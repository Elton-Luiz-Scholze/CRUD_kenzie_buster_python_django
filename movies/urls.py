from django.urls import path
from .views import MoviesView, SpecificMovieView

urlpatterns = [
    path("movies/", MoviesView.as_view()),
    path("movies/<int:movie_id>/", SpecificMovieView.as_view()),
]
