from django.db import models, transaction


class Project(models.Model):
    name = models.CharField(max_length=200)


    @classmethod
    def reorganize(cls, assignments):
        # BEGIN (write your solution here)
        with transaction.atomic():
            for worker_id, project_id in assignments.items():
                Worker.objects.filter(id=worker_id).update(project=project_id)

            Worker.objects.exclude(id__in=assignments).update(project=None)
        # END


class Worker(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(
        Project,
        null=True,
        on_delete=models.SET_NULL,
    )
