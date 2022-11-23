import base64
from typing import Any, Dict

from meditations.models import Audio, Meditation, MeditationParameter
from rest_framework import serializers


class MeditationParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeditationParameter
        exclude = ["meditation"]


class MeditationRetrieveSerializer(serializers.ModelSerializer):

    audio_base64 = serializers.SerializerMethodField()

    def get_audio_base64(self, meditation_obj):

        with open(str(meditation_obj.audio_file.file.path), "rb") as f:
            return base64.b64encode(f.read())

    class Meta:
        model = Meditation
        fields = ["audio_base64"]


class MeditationSerializer(serializers.HyperlinkedModelSerializer):

    # parameters = serializers.StringRelatedField(many=True, read_only=True)
    user = serializers.StringRelatedField()
    audio_file = serializers.SlugRelatedField(
        slug_field="activity", queryset=Audio.objects.all()
    )

    parameters = MeditationParamSerializer(many=True)

    class Meta:
        model = Meditation
        fields = "__all__"

    def create(self, validated_data: Dict[str, Any]):

        med_params = validated_data.pop("parameters")

        meditation = super().create(validated_data)

        MeditationParameter.objects.bulk_create(
            [
                MeditationParameter(**{**x, **{"meditation": meditation}})
                for x in med_params
            ]
        )

        return meditation


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = "__all__"
