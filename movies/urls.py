from django.urls import path
from .views import MovieOrderView, MoviesView, SpecificMovieView

urlpatterns = [
    path("movies/", MoviesView.as_view()),
    path("movies/<int:movie_id>/", SpecificMovieView.as_view()),
    path("movies/<int:movie_id>/orders/", MovieOrderView.as_view()),
]
