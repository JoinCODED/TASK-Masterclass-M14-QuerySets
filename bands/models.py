from typing import TYPE_CHECKING, Optional, Union

from django.db import models

from shared.models import TimestampMixin


if TYPE_CHECKING:
    from django.db.models.expressions import Combinable
    from django.db.models.manager import RelatedManager

    from albums.models import Album, Song
    from shared.models import GenreM2M


BandForeignKey = models.ForeignKey[Union["Band", "Combinable"], "Band"]


class Band(TimestampMixin, models.Model):
    albums: "RelatedManager[Album]"
    members: "RelatedManager[BandMember]"

    name = models.CharField(max_length=50)
    genre: "GenreM2M" = models.ManyToManyField(
        "shared.Genre", related_name="bands"
    )

    def __str__(self) -> str:
        return self.name

    @classmethod
    def get_top_ten(cls) -> models.QuerySet["Band"]:
        return cls.objects.all()

    @property
    def singles(self) -> models.QuerySet["Song"]:
        from albums.models import Song

        return Song.objects.all()

    @property
    def features(self) -> models.QuerySet["Song"]:
        from albums.models import Song

        return Song.objects.all()

    @property
    def top_single(self) -> Optional["Song"]:
        return None

    @property
    def top_feature(self) -> Optional["Song"]:
        return None


class BandMember(TimestampMixin, models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    band: BandForeignKey = models.ForeignKey(
        "bands.Band", on_delete=models.CASCADE, related_name="members"
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
