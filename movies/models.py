from django.db import models


class MovieRating(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC_17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20,
        choices=MovieRating.choices,
        default=MovieRating.G,
    )
    synopsis = models.TextField(null=True, default=None)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
    )

    user_order = models.ManyToManyField(
        "users.User",
        through="movies.MovieOrder",
        related_name="purchased_movies",
    )

    def __repr__(self) -> str:
        return f"<Movie [{self.id}] - {self.title}>"


class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="movie_order",
    )

    user_movie = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_movie_order",
    )

    def __repr__(self) -> str:
        return f"<MovieOrder [{self.id}] - R${self.price} - {self.buyed_at}>"
