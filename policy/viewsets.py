import uuid

from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from authentication.authentication import JWTAuthentication
from . import serializers


class TermViewset(ReadOnlyModelViewSet):
    queryset = serializers.TermSerializer.Meta.model.objects.all()
    serializer_class = serializers.TermSerializer


class PrivacyViewset(ReadOnlyModelViewSet):
    queryset = serializers.PrivacySerializer.Meta.model.objects.all()
    serializer_class = serializers.PrivacySerializer


class AcceptanceMixin(ModelViewSet):

    def get_serializer(self, *args, **kwargs):
        kwargs.update({'user': self.request.user})
        return super().get_serializer(*args, **kwargs)

    def list(self, request, *args, **kwargs):
        member = request.query_params.get('member', None)
        version = request.query_params.get('version', None)

        if not member and not version:
            content = {'detail': [_('You cannot list all acceptances.')]}
            return Response(content, status=status.HTTP_403_FORBIDDEN)

        if member:
            try:
                uuid.UUID(member)
            except ValueError:
                content = {
                    'details': ["Member provided is not a valid uuid", ]
                }
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

        queryset = self.get_queryset()

        if member:
            queryset = queryset.filter(member=member)

        if version:
            queryset = queryset.filter(version=version)

        page = self.paginate_queryset(self.filter_queryset(queryset))
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        content = {'detail': _('You cannot edit an acceptance.')}
        return Response(content, status=status.HTTP_403_FORBIDDEN)


class TermAcceptanceViewset(AcceptanceMixin):
    queryset = serializers.TermAcceptanceSerializer.Meta.model.objects.all()
    serializer_class = serializers.TermAcceptanceSerializer
    authentication_classes = (
        JWTAuthentication,
    )
    permission_classes = (IsAuthenticated,)


class PrivacyAcceptanceViewset(AcceptanceMixin):
    queryset = serializers.PrivacyAcceptanceSerializer.Meta.model.objects.all()
    serializer_class = serializers.PrivacyAcceptanceSerializer
    authentication_classes = (
        JWTAuthentication,
    )
    permission_classes = (IsAuthenticated,)
