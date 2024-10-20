from django.shortcuts import render
from functools import wraps

def user_is_customer(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role == 1:  # 1 untuk owner
            return view_func(request, *args, **kwargs)
        return render(request, 'notfound.html', status=403)
    return _wrapped_view

def user_is_owner(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role == 0:  # 0 untuk buyer
            return view_func(request, *args, **kwargs)
        return render(request, 'notfound.html', status=403)
    return _wrapped_view