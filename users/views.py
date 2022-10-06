from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.generic import ListView

from avito import settings
from users.models import User


class UserListView(ListView):
    model = User
    qs = User.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(self, *args, **kwargs)
        self.object_list = self.object_list.order_by("username")
        paginator = Paginator(object_list=self.object_list, per_page=settings.TOTAL_ON_PAGE)
        page = request.GET.get("page")
        page_obj = paginator.get_page(page)

        result_method = []

        for user in page_obj:
            result_method.append(
                {"id": user.id,
                 "first_name": user.first_name,
                 "last_name": user.last_name,
                 "username": user.username,
                 "password": user.password,
                 "role": user.role,
                 "age": user.age,
                 })

        return JsonResponse({"ads": result_method, "Current_page": page_obj.number, "Total_ads": page_obj.paginator.count},
                            safe=False, json_dumps_params={"ensure_ascii": False})

