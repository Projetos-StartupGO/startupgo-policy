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
            'created',
        )

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        privacy_data = PrivacySerializer().to_representation(instance.privacy)
        del privacy_data['content']

        rep['privacy_data'] = privacy_data
        return rep

    def validate(self, attrs):
        attrs = super().validate(attrs)

        privacy = attrs.get('privacy')
        if privacy:
            attrs['version'] = privacy.version

        return attrs



class TermAcceptanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TermAcceptance
        fields = (
            'pk',
            'term',
            'member',
            'created',
        )

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        term_data = TermSerializer().to_representation(instance.term)
        del term_data['content']

        rep['term_data'] = term_data
        return rep

    def validate(self, attrs):
        attrs = super().validate(attrs)

        term = attrs.get('term')
        if term:
            attrs['version'] = term.version

        return attrs
