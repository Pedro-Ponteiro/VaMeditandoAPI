from django.contrib import admin
from django.urls import include, path
from meditations.api.views import (
    AudioModelViewset,
    MeditationListCreateAPIView,
    MeditationRetrieveAPIView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"meditations", MeditationListCreateAPIView)
router.register(r"meditations", MeditationRetrieveAPIView)
router.register(r"audios", AudioModelViewset)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
