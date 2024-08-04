from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from apps.account.models import AccountRolesModel


def role_required(role, login_url=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Check if the user is authenticated
            if not request.user.is_authenticated:
                return login_required(view_func)(request, login_url, *args, **kwargs)
            # Check if the user has the required role
            try:
                target_role = AccountRolesModel.objects.get(user=request.user)
            except:
                return redirect(login_url)

            target_role = target_role.role.name

            if target_role == 'admin':
                return view_func(request, *args, **kwargs)

            if not target_role == role:
                return redirect(login_url)

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator
