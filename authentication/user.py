from django.contrib import auth
from django.contrib.auth.models import AnonymousUser


# A few helper functions for common logic between User and AnonymousUser.
def _user_get_all_permissions(user, obj):
    permissions = set()
    for backend in auth.get_backends():
        if hasattr(backend, "get_all_permissions"):
            permissions.update(backend.get_all_permissions(user, obj))
    return permissions


class JWTUser(AnonymousUser):

    def __init__(self,
                 pk,
                 email,
                 first_name,
                 last_name,
                 admin=False,
                 is_superuser=False):
        self.pk = pk
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.admin = admin
        self.is_superuser = is_superuser
        self.is_staff = is_superuser is True

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    def get_username(self):
        return self.username

    def save(self):
        raise NotImplementedError(
            "Django doesn't provide a DB representation for JWT User."
        )

    def delete(self):
        raise NotImplementedError(
            "Django doesn't provide a DB representation for JWT User."
        )

    def set_password(self, raw_password):
        raise NotImplementedError(
            "Django doesn't provide a DB representation for JWT User."
        )

    def check_password(self, raw_password):
        raise NotImplementedError(
            "Django doesn't provide a DB representation for JWT User."
        )
