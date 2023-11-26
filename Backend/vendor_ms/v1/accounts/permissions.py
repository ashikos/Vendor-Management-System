import jwt

from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import exceptions

from v1.accounts.models import ProjectUser


class IsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        
        token = request.COOKIES.get("jwt")
        if not token:
            raise exceptions.NotFound(default_detail="Token Not Found")
        
        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])
            user = ProjectUser.objects.get(id=payload['id'])
        except:
            raise AuthenticationFailed

        request.user = user
        view.kwargs["user"] = user

        return True
