from aioauth_fastapi.users.crypto import authenticate
from starlette.authentication import AuthCredentials, AuthenticationBackend

from ..config import settings
from .models import User, UserAnonymous


class CookiesAuthenticationBackend(AuthenticationBackend):
    async def authenticate(self, request):
        token: str = request.cookies.get("token")

        if not token:
            return AuthCredentials(), UserAnonymous()

        key = settings.JWT_PUBLIC_KEY

        is_authenticated, decoded_token = authenticate(token=token, key=key)

        if is_authenticated:
            return AuthCredentials(), User(
                id=decoded_token["sub"],
                is_superuser=decoded_token["is_superuser"],
                is_blocked=decoded_token["is_blocked"],
                is_active=decoded_token["is_active"],
                username=decoded_token["username"],
            )

        return AuthCredentials(), UserAnonymous()
