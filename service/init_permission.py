from django.conf import settings


def init_permission(current_user,request):
    # 用户权限信息初始化
    # 当前用户所有权限
    permission_queryset = current_user.roles.filter(permissions__isnull=False).values("permissions__id",
                                                                                      "permissions__title",
                                                                                      "permissions__is_menu",
                                                                                      "permissions__icon",
                                                                                      "permissions__url",
                                                                                      ).distinct()
    # 获取权限中所有的URL
    # permission_list = []
    # for item in permission_queryset:
    #     permission_list.append(item['permissions__url'])
    menu_list=[]
    permission_list = []
    for item in permission_queryset:
        permission_list.append(item["permissions__url"])
        if item["permissions__is_menu"]:
            temp={
                "title":item['permissions__title'],
                "icon":item['permissions__icon'],
                "url":item['permissions__url'],
            }
            menu_list.append(temp)
    print(menu_list)
    print(permission_list)
    # permission_list = [item['permissions__url'] for item in permission_queryset]
    request.session[settings.PERMISSION_SESSION_KEY] = permission_list
    request.session[settings.MENU_SESSION_KEY] = menu_list

