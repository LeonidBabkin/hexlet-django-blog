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
#         first solution
#         key = list(kwargs)
#         if isinstance(kwargs[key[0]], int):
#             likeclips = cls.objects.filter(id=kwargs[key[0]]).annotate(num_cliplike=Count("cliplike", distinct=True))
#             dislikeclips = cls.objects.filter(id=kwargs[key[0]]).annotate(num_clipdislike=Count("clipdislike", distinct=True))
#             return tuple([likeclips[0].num_cliplike, dislikeclips[0].num_clipdislike])
#         else:
#             likeclips = cls.objects.filter(title=kwargs[key[0]]).annotate(num_cliplike=Count("cliplike", distinct=True))
#             dislikeclips = cls.objects.filter(title=kwargs[key[0]]).annotate(num_clipdislike=Count("clipdislike", distinct=True))
#             return tuple([likeclips[0].num_cliplike, dislikeclips[0].num_clipdislike])
           
#       second solution
        likeclips = cls.objects.filter(**kwargs).annotate(num_cliplike=Count("cliplike", distinct=True))
        dislikeclips = cls.objects.filter(**kwargs).annotate(num_clipdislike=Count("clipdislike", distinct=True))
        return likeclips[0].num_cliplike, dislikeclips[0].num_clipdislike

        # aggregate = cls.objects.filter(
        #     **kwargs,
        # ).annotate(
        #     likes=models.Count('cliplike', distinct=True),
        #     dislikes=models.Count('clipdislike', distinct=True),
        # ).aggregate(
        #     models.Sum('likes'),
        #     models.Sum('dislikes'),
        # )
        # return (aggregate['likes__sum'], aggregate['dislikes__sum'])

# Обычно используют одну модель как для положительных реакций, так и для отрицательных. Однако в рамках этого упражнения
# две отдельные модели использовать удобнее. В реальных проектах такое тоже встречается, когда некое явление пользователю
# позволено оценить одновременно и положительно, и отрицательно.

class ClipLike(models.Model):
    clip = models.ForeignKey(Clip, on_delete=models.CASCADE)


class ClipDislike(models.Model):
    clip = models.ForeignKey(Clip, on_delete=models.CASCADE)
