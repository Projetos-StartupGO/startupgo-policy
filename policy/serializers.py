from rest_framework import serializers

from . import models


class PrivacySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Privacy
        fields = (
            'pk',
            'content',
            'version',
            'created',
            'last_updated',
        )


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Term
        fields = (
            'pk',
            'content',
            'version',
            'created',
            'last_updated',
        )


class PrivacyAcceptanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PrivacyAcceptance
        fields = (
            'pk',
            'privacy',
            'member',
            'version',
            'created',
        )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['privacy_data'] = \
            PrivacySerializer().to_representation(instance.privacy)
        return rep


class TermAcceptanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TermAcceptance
        fields = (
            'pk',
            'member',
            'term',
            'created',
        )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['term_data'] = TermSerializer().to_representation(instance.term)
        return rep

    def validate(self, attrs):
        attrs = super().validate(attrs)

        term = attrs.get('term')
        if term:
            attrs['version'] = term.version

        return attrs
