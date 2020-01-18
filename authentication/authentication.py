import json

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from jwt import decode, algorithms
from rest_framework.authentication import (
    BaseAuthentication,
    get_authorization_header,
    exceptions,
)

from .user import JWTUser


class JWTAuthentication(BaseAuthentication):
    """
    Simple JWT based authentication.

    Clients should authenticate by passing the JWT token key in the
    "Authorization" HTTP header, prepended with the string "JWT ". For example:

        Authorization: Bearer <JTW token>
    """

    keyword = 'Bearer'

    def authenticate(self, request):

        if hasattr(settings, 'AUTHENTICATION_PUBLIC_KEY') is False:
            msg = _('JTW settings misconfigured: AUTHENTICATION_PUBLIC_KEY'
                    ' does not exist in settings.')
            raise exceptions.AuthenticationFailed(msg)

        auth_header = get_authorization_header(request).split()

        if not auth_header or \
                auth_header[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth_header) == 1:
            msg = _('Invalid JWT token header. No token provided.')
            raise exceptions.AuthenticationFailed(msg)

        elif len(auth_header) > 2:
            msg = _('Invalid JTW token header. Token string should not'
                    ' contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth_header[1].decode()

        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain'
                    ' invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    @staticmethod
    def authenticate_credentials(token):
        try:
            public_key = json.dumps(settings.AUTHENTICATION_PUBLIC_KEY)
            public_key = algorithms.RSAAlgorithm.from_jwk(public_key)
            decoded = decode(token, public_key, algorithms=["RS256"])

        except Exception as e:
            from pprint import pprint
            pprint(e)
            raise exceptions.AuthenticationFailed(_('Invalid JWT token.'))

        return JWTUser(
            pk=decoded.get('id'),
            email=decoded.get('email'),
            first_name=decoded.get('firstName'),
            last_name=decoded.get('lastName'),
            admin=decoded.get('admin', False) is True,
            is_superuser=decoded.get('superuser', False) is True,
        ), token

    def authenticate_header(self, request):
        return self.keyword
