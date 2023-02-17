from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer
from .models import User
from django.shortcuts import get_object_or_404
from movies.permissions import IsEmployeePermission
from .permissions import IsUserPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class UserView(APIView):
    def post(self, req: Request):
        serializer = UserSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class SpecificUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeePermission, IsUserPermission, IsAuthenticated]

    def get(self, req: Request, user_id):
        user = get_object_or_404(User, pk=user_id)

        self.check_object_permissions(req, user)

        serializer = UserSerializer(user)

        return Response(serializer.data)

    def patch(self, req: Request, user_id):
        user = get_object_or_404(User, pk=user_id)

        self.check_object_permissions(req, user)

        serializer = UserSerializer(user, req.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
