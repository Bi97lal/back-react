from django .urls import path

from .import views



urlpatterns = [
    path("post_student/",views.post_student,name="post_student"),
    path("get_courses/",views.get_courses,name="get_courses"),
    path("get_details/<int:id>/",views.get_details,name="get_details"),
    path("deleteItem/<int:id>/",views.deleteItem,name="deleteItem")
]
