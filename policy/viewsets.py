from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from . import serializers


class TermViewset(ReadOnlyModelViewSet):
    queryset = serializers.TermSerializer.Meta.model.objects.all()
    serializer_class = serializers.TermSerializer


class PrivacyViewset(ReadOnlyModelViewSet):
    queryset = serializers.PrivacySerializer.Meta.model.objects.all()
    serializer_class = serializers.PrivacySerializer


class TermAcceptanceViewset(ModelViewSet):
    queryset = serializers.TermAcceptanceSerializer.Meta.model.objects.all()
    serializer_class = serializers.TermAcceptanceSerializer


class PrivacyAcceptanceViewset(ModelViewSet):
    queryset = serializers.PrivacyAcceptanceSerializer.Meta.model.objects.all()
    serializer_class = serializers.PrivacyAcceptanceSerializer
