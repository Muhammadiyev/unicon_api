from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from .fields import OrderField
# Create your models here.


class Draggable(models.Model):
    name = models.CharField(max_length=10000, blank=True)
    status = models.BooleanField(_('status'), default=True)
    created_at = models.DateTimeField(null=False, default=now)

    def __str__(self):
        return "%s" % self.name

    @property
    def draggable(self):
        return self.drag_of_draggable


class DragandDrop(models.Model):
    name = models.CharField(max_length=10000, blank=True)
    description = models.TextField(blank=True)
    draggable = models.ForeignKey(Draggable, on_delete=models.CASCADE, related_name='drag_of_draggable')
    date = models.DateTimeField(null=False, default=now)
    status = models.BooleanField(_('status'), default=True)
    created_at = models.DateTimeField(null=False, default=now)
    position = OrderField(blank=True)

    def __str__(self):
        return "%s" % self.name

    @property
    def draganddropcolor(self):
        return self.color


class AddingColor(models.Model):
    backround = models.TextField(blank=True)
    draganddrop = models.ForeignKey(DragandDrop, on_delete=models.CASCADE, related_name='color')
    status = models.BooleanField(_('status'), default=True)
    created_at = models.DateTimeField(null=False, default=now)

    def __str__(self):
        return "%s" % self.backround
