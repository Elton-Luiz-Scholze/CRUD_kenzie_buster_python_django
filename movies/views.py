from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from .serializers import MoviesSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsEmployeePermission


class MoviesView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeePermission]

    def post(self, req: Request):
        serializer = MoviesSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=req.user)

        return Response(serializer.data, status.HTTP_201_CREATED)
