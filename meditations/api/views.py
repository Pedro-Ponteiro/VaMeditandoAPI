from meditations.api.permissions import IsAdminOrReadOnly, IsAuthenticatedAndOwner
from meditations.api.serializers import (
    AudioSerializer,
    MeditationRetrieveSerializer,
    MeditationSerializer,
)
from meditations.models import Audio, Meditation
from rest_framework import mixins, viewsets


class MeditationListCreateAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Meditation.objects.all().order_by("-id")
    permission_classes = [IsAuthenticatedAndOwner]
    serializer_class = MeditationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class MeditationRetrieveAPIView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Meditation.objects.all()
    permission_classes = [IsAuthenticatedAndOwner]
    serializer_class = MeditationRetrieveSerializer


class AudioModelViewset(viewsets.ModelViewSet):

    queryset = Audio.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = AudioSerializer
