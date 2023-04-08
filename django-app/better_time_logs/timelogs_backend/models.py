from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    total_spend = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class TimeLog(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    duration = models.IntegerField()
    added = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.task_name

    def __repr__(self):
        return self.task_name