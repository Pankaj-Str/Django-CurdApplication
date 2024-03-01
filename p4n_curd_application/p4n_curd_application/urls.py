from django.contrib import admin
from django.urls import path
from cwp_enroll import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.add_show, name="add_show"),
]
