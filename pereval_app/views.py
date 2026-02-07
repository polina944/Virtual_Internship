from rest_framework.viewsets import ModelViewSet

from pereval_app.models import Pereval, User, Coords, Level, Images
from pereval_app.serializers import PerevalSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = PerevalSerializer


class CoordsViewSet(ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = PerevalSerializer


class LevelViewSet(ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = PerevalSerializer


class ImagesViewSet(ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = PerevalSerializer


class PerevalViewSet(ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

