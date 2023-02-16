from rest_framework import serializers
from .models import Movie, MovieRating
import ipdb


class MoviesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    rating = serializers.ChoiceField(
        choices=MovieRating.choices,
        default=MovieRating.G,
        required=False,
    )
    synopsis = serializers.DictField(allow_null=True, default=None)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj: MovieRating):
        return obj.user.email

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
