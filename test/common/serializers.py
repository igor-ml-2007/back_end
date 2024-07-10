from rest_framework import serializers
from common.models import *

class MediaURLSerializer(serializers.Serializer):
    def to_representation(self, media):
        if not media:
            return None
        try:
            return self.context["request"].build_absolute_uri(media.file.url)
        except Exception:
            return "http://testserver" + str(media.file.url)


class SettingsSerializer(serializers.ModelSerializer):
    back_image = MediaURLSerializer()
    class Meta:
        model = Settings
        fields = '__all__'

