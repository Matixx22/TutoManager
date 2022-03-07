from django.db import models

# Create your models here.
from django.utils import formats, timezone, dateformat


class Entry(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField(default=dateformat.format(timezone.now(), 'Y-m-d H:m'))
    price = models.IntegerField(default=30)

    def __str__(self):
        formatted_date = formats.date_format(self.date, "SHORT_DATETIME_FORMAT")
        return f'{self.name}, {formatted_date}, {self.price} PLN'
