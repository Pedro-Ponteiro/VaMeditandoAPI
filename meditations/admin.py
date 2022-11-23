from django.contrib import admin

from meditations.models import Audio, Meditation, MeditationParameter

admin.site.register(Audio)
admin.site.register(Meditation)
admin.site.register(MeditationParameter)
