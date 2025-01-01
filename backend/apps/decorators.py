from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from apps.account.models import AccountRolesModel


def role_required(role, login_url=None, fix_role=False):
    """
    role_required(role, login_url=None) -> function

    A decorator to restrict access to a view based on user roles.

    Parameters:
    role (list): A list of allowed roles required to access the view.
    login_url (str, optional): The URL to redirect to for login if the user is not authenticated or does not have the required role. Defaults to None.

    Returns:
    function: The decorated view function.

    Behavior:
    - If the user is not authenticated, they will be redirected to the login page.
    - If the user does not have the required role, they will be redirected to the login page.
    - If the user has the required role, the original view function is called.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Check if the user is authenticated
            if not request.user.is_authenticated:
                return login_required(view_func)(request, login_url, *args, **kwargs)
            # Check if the user has the required role
            try:
                target_role = AccountRolesModel.objects.filter(user=request.user)
            except:
                return redirect(login_url)

            target_role = target_role.first()
            target_role = target_role.role.name

            if target_role == 'admin':
                return view_func(request, *args, **kwargs)

            if not fix_role:
                if not set(role).issubset(set(target_role)):
                    return redirect(login_url)

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator
