import requests
from rest_framework.permissions import BasePermission


class CustomAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        user_data_req = requests.get("http://127.0.0.1:8001/users/get_user_id/", headers=request.headers)
        try:
            setattr(request, 'user_data', user_data_req.json())
        except:
            pass
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request, 'user_data') and request.user_data['is_admin']


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request, 'user_data') and request.user_data
