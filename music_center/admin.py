from django.contrib import admin

from .models import Genre, Producer, Track, TrackInstance

# Register your models here.


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ('stage_name', 'first_name', 'last_name',
                    'career_start', 'career_end')


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'producer', 'pub_date')


@admin.register(TrackInstance)
class TrackInstanceAdmin(admin.ModelAdmin):
    pass
