import uuid

from django.db import models
from django.urls import reverse

# Create your models here.


class Genre(models.Model):
    """Model of music genre."""
    name = models.CharField(max_length=20, help_text='Music Genre', null=False)

    def __str__(self):
        return self.name


class Producer(models.Model):
    stage_name = models.CharField(max_length=20, help_text='Stage Name')
    first_name = models.CharField(max_length=20, help_text='First Name')
    last_name = models.CharField(max_length=20, help_text='Last Name')
    career_start = models.DateField(null=True, blank=True)
    career_end = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['stage_name', 'career_start']

    def get_absolute_url(self):
        """Returns the url to access a particular producer instance."""
        return reverse('producer-detail', args=[str(self.id)])

    def __str__(self):
        return self.stage_name


class Track(models.Model):
    name = models.CharField(max_length=50, help_text='Track Name', null=False)
    genre = models.ManyToManyField(Genre, help_text='Select a genre of music')
    pub_date = models.DateField(null=True, blank=True)
    producer = models.ForeignKey('Producer', on_delete=models.SET_NULL,
                                 null=True)
    description = models.TextField(max_length=1000,
                                   help_text='Say something about this track')
    _number_of_listener = 0
    number_of_listener = models.IntegerField(editable=False,
                                             default=_number_of_listener)

    class Meta:
        ordering = ['name', 'number_of_listener', '-pub_date']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this track."""
        return reverse('track-detail', args=[str(self.id)])


class TrackInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    track = models.ForeignKey('Track', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['track']

    def __str__(self):
        return f'{self.track.name}({self.id})'
