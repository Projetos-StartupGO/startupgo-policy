from rest_framework import serializers

from authentication.user import JWTUser
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
            'created',
        )

    def __init__(self, user: JWTUser, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        privacy_data = PrivacySerializer().to_representation(instance.privacy)
        del privacy_data['content']

        rep['privacy_data'] = privacy_data
        return rep

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['member'] = self.user.pk
        privacy = attrs.get('privacy')

        model_class = self.Meta.model

        if privacy:
            attrs['version'] = privacy.version
            try:
                self.instance = model_class.objects.get(
                    member=self.user.pk,
                    privacy=privacy,
                    version=privacy.version,
                )
            except model_class.DoesNotExist:
                pass

        return attrs


class TermAcceptanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TermAcceptance
        fields = (
            'pk',
            'term',
            'created',
        )

    def __init__(self, user: JWTUser, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        term_data = TermSerializer().to_representation(instance.term)
        del term_data['content']

        rep['term_data'] = term_data
        return rep

    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['member'] = self.user.pk
        term = attrs.get('term')

        model_class = self.Meta.model
        if term:
            attrs['version'] = term.version
            try:
                self.instance = model_class.objects.get(member=self.user.pk,
                                                        term=term,
                                                        version=term.version)
            except model_class.DoesNotExist:
                pass

        return attrs
