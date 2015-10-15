#coding:utf8
__author__ = 'Di LUO'

from django.http import HttpResponseRedirect



list_role={
        1:"超级管理员",
        2:"系统管理员",
        3:"普通用户",
}


def is_super_user(request):
    if request.session.get('user_role') == 1:
        return True
    else:
        return False


def is_system_admin(request):
    if request.session.get('user_role') == 2:
        return True
    else:
        return False



def is_common_user(request):
    if request.session.get('user_role') == 3:
        return True
    else:
        return False




def require_login(func):
    """要求登录的装饰器"""
    def _deco(request, *args, **kwargs):
        if not request.session.get('user_name'):
            return HttpResponseRedirect('/account/login/')
        return func(request, *args, **kwargs)
    return _deco










