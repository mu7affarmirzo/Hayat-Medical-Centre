from uuid import uuid4

from django.db import models


class UnsupportedFormat(Exception):
    pass


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    if ext.lower() in ['doc', 'png', 'pdf', 'xml', 'jpeg', 'mp4', 'jpg', 'mov', 'm4v']:
        file_path = f"files/img/{uuid4().hex}.{ext}"
        return file_path
    else:
        raise UnsupportedFormat


class ContainerColorModel(models.Model):
    color = models.CharField(max_length=255)
    color_hex = models.CharField(max_length=255, null=True, blank=True)
    img = models.ImageField(upload_to=upload_location, blank=True, null=True)

    def __str__(self):
        return self.color


class ContainerGroupModel(models.Model):
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.color


class ContainerModel(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True)
    short_name = models.CharField(max_length=255, blank=True, null=True)
    color = models.ForeignKey(ContainerColorModel, on_delete=models.SET_NULL, null=True, blank=True)
    capacity = models.IntegerField()
    is_archive = models.BooleanField(default=False)
    is_group = models.BooleanField(default=False)
    is_aliquoted = models.BooleanField(default=True)
    container_group = models.ForeignKey(ContainerGroupModel, on_delete=models.SET_NULL, null=True, blank=True)

    suffix = models.CharField(max_length=255, blank=True, null=True)
    nomenclature_name = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.name

