

from datetime import timedelta

from django.conf import settings
from django.utils import timezone

from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication


class ExpiringBearerTokenAuthentication(TokenAuthentication):
    '''
    Token based authentication with an expiry duration in
    minutes and configurable using settings.
    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Bearer ".  For example:
        Authorization: Bearer 401f7ac837da42b97f613d789819ff93537bee6a
    '''
    keyword = 'Bearer'

    def authenticate_credentials(self, key):
        user, token = super(ExpiringBearerTokenAuthentication, self).authenticate_credentials(key)

        expires_before = timezone.now() - timedelta(minutes=settings.TOKEN_DURATION_MINS)
        if token.created < expires_before:
            token.delete()
            raise exceptions.AuthenticationFailed('Token expired.')

        return (user, token)