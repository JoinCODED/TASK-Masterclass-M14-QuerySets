from decimal import Decimal
from typing import TYPE_CHECKING, Optional

from django.db import models


if TYPE_CHECKING:
    from bands.models import BandForeignKey
    from shared.models import GenreM2M


class Album(models.Model):
    name = models.CharField(max_length=50)
    band: "BandForeignKey" = models.ForeignKey(
        "bands.Band", on_delete=models.CASCADE, related_name="albums"
    )
    genre: "GenreM2M" = models.ManyToManyField(
        "shared.Genre", related_name="albums"
    )
    purchase_count = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name

    @property
    def singles(self) -> models.QuerySet["Song"]:
        return Song.objects.all()

    @property
    def features(self) -> models.QuerySet["Song"]:
        return Song.objects.all()

    @property
    def top_single(self) -> Optional["Song"]:
        return None

    @property
    def price(self) -> Decimal:
        return Decimal()


class Song(models.Model):
    name = models.CharField(max_length=100)
    genre: "GenreM2M" = models.ManyToManyField(
        "shared.Genre", related_name="songs"
    )
    price = models.DecimalField(max_digits=6, decimal_places=3)
    purchase_count = models.PositiveIntegerField(default=0)
    is_single = models.BooleanField()

    def __str__(self) -> str:
        return self.name

    @classmethod
    def get_top_ten(cls) -> models.QuerySet["Song"]:
        return cls.objects.all()
