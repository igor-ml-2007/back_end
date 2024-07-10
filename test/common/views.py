from rest_framework.generics import ListAPIView
from common.serializers import *
from common.models import *

class SettingsListAPIView(ListAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer

    def get_object(self):
        return Settings.objects.first()



