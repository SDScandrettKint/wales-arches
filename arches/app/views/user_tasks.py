from django.views.generic import View
from arches.app.utils.response import JSONResponse
from arches.app.models import models


class UserTaskView(View):
    action = ""

    def get(self, request):
        if request.user.is_authenticated:
            if request.GET.get("action", None) == "get_all":
                tasks = models.UserXTask.objects.all()
            else:
                tasks = models.UserXTask.objects.filter(user_id=request.user.id)
            return JSONResponse({"success": True, "tasks": tasks}, status=200)

        return JSONResponse({"error": "User not authenticated. Access denied."}, status=401)
