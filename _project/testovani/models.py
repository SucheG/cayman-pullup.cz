from django.db import models
#
# # Create your models here.
# class ClassA(models.Model):
#   nazev = models.CharField(max_length=100)
#
# class AbstractClass(models.Model):
#   name = models.ManyToManyField(ClassA, related_name='%(class)s_name', through='ClassA_%(class)s')
#
#
# class MyClass(AbstractClass):
#   nazev = models.CharField(max_length=100)
#
#
# class ClassA_MyClass(models.Model):
#   class_a = models.ForeignKey(ClassA, on_delete=models.CASCADE)
#   my_class = models.ForeignKey(MyClass, on_delete=models.CASCADE)