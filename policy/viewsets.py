from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from authentication.authentication import JWTAuthentication
from . import serializers


class TermViewset(ReadOnlyModelViewSet):
    queryset = serializers.TermSerializer.Meta.model.objects.all()
    serializer_class = serializers.TermSerializer
    authentication_classes = (
        JWTAuthentication,
    )
    permission_classes = (IsAuthenticated,)


class PrivacyViewset(ReadOnlyModelViewSet):
    queryset = serializers.PrivacySerializer.Meta.model.objects.all()
    serializer_class = serializers.PrivacySerializer


class TermAcceptanceViewset(ModelViewSet):
    queryset = serializers.TermAcceptanceSerializer.Meta.model.objects.all()
    serializer_class = serializers.TermAcceptanceSerializer
    authentication_classes = (
        JWTAuthentication,
    )
    permission_classes = (IsAuthenticated,)


class PrivacyAcceptanceViewset(ModelViewSet):
    queryset = serializers.PrivacyAcceptanceSerializer.Meta.model.objects.all()
    serializer_class = serializers.PrivacyAcceptanceSerializer
    authentication_classes = (
        JWTAuthentication,
    )
    permission_classes = (IsAuthenticated,)
