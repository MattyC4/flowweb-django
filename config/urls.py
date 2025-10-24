from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls", namespace="core")),
    path("users/", include("apps.users.urls", namespace="users")),
    path("dashboard/", include("apps.dashboard.urls", namespace="dashboard")),  # ← nuevo
]
