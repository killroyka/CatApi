from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    description = models.TextField(max_length=500, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=100, blank=True, null=True)
    breed = models.ForeignKey("cats.Breed", null=True, on_delete=models.DO_NOTHING, related_name="cats")

    class Meta:
        verbose_name = "кот"
        verbose_name_plural = "коты"

    def __str__(self):
        return self.name


class Grade(models.Model):
    cat = models.ForeignKey("cats.Cat", on_delete=models.CASCADE, related_name="grades")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="grades")
    grade = models.PositiveIntegerField(validators=[MaxValueValidator(5)])

    class Meta:
        verbose_name = "оценка"
        verbose_name_plural = "оценки"
        unique_together = (("user", "cat"),)

    def __str__(self):
        return f"{self.cat} {self.cat.name}"


class Breed(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = "порода"
        verbose_name_plural = "породы"

    def __str__(self):
        return self.name
