from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from .serializers import MoviesSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsEmployeePermission
from .models import Movie
from django.shortcuts import get_object_or_404


class MoviesView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeePermission]

    def post(self, req: Request):
        serializer = MoviesSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=req.user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, req: Request):
        movies = Movie.objects.all()

        serializer = MoviesSerializer(movies, many=True)

        return Response(serializer.data)


class SpecificMovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeePermission]

    def get(self, req: Request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)

        serializer = MoviesSerializer(movie)

        return Response(serializer.data)

    def delete(self, req: Request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)

        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
