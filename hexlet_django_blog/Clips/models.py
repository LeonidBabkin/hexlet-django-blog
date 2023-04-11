from django.db import models
from django.db.models import Avg, Max, Min, Count

class Clip(models.Model):
    title = models.CharField(max_length=200)

    def like(self):
        # на основе экземпляра класса Clip создаётся новая запись в таблице класса Cliplike/ClipDislike
        # в таблицу заносятся титул и id экземпляра класса 
        # на основе титула и id в последствии можно делать выборку 
        ClipLike.objects.create(clip=self)

    def dislike(self):
        ClipDislike.objects.create(clip=self)

    @classmethod
    def rates_for(cls, **kwargs) -> (int, int):
        """
        Returns a tuple of integers (likes, dislikes)
        for the clip(s) filtered by provided kwargs.
        """
# в cls (классе Clip) содержаться все его экземпляры класса. Мы ищем этот экземпляр через фильтр и аннотируем его 
# по количеству случаев он был добавлен в таблицу Cliplike или ClipDislike

        likeclips = cls.objects.filter(
            **kwargs).annotate(num_cliplike=Count(
                "cliplike", distinct=True))
        dislikeclips = cls.objects.filter(
            **kwargs).annotate(num_clipdislike=Count(
                "clipdislike", distinct=True))
        return likeclips[0].num_cliplike, dislikeclips[0].num_clipdislike


class ClipLike(models.Model):
    clip = models.ForeignKey(Clip, on_delete=models.CASCADE)


class ClipDislike(models.Model):  # на основе экземпляра класса Clip создаётся новая запись в таблице класса Cliplike/ClipDislike
    clip = models.ForeignKey(Clip, on_delete=models.CASCADE)
