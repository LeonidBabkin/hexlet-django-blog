from django.db import models
from django.db.models import Avg, Max, Min, Count

class Clip(models.Model):
    title = models.CharField(max_length=200)

    def like(self):  # экземпляр класса добавляется в таблицу "нравится" ClipLike
        ClipLike.objects.create(clip=self)

    def dislike(self):  # экземпляр класса добавляется в таблицу "не нравится" ClipDislike
        ClipDislike.objects.create(clip=self)

    @classmethod
    def rates_for(cls, **kwargs) -> (int, int):
        """
        Returns a tuple of integers (likes, dislikes)
        for the clip(s) filtered by provided kwargs.
        """
# отбираем видеоролик(Clip) согласно именованным аргументам(kwargs), аннотируем его посредством подсчета likes & dislikes

        likeclips = cls.objects.filter(
            **kwargs).annotate(num_cliplike=Count(
                "cliplike", distinct=True))
        dislikeclips = cls.objects.filter(
            **kwargs).annotate(num_clipdislike=Count(
                "clipdislike", distinct=True))
        return likeclips[0].num_cliplike, dislikeclips[0].num_clipdislike


class ClipLike(models.Model):
    clip = models.ForeignKey(Clip, on_delete=models.CASCADE)


class ClipDislike(models.Model):
    clip = models.ForeignKey(Clip, on_delete=models.CASCADE)
