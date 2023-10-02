from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:q_id>/", views.detail, name="detail"),
    path("<int:q_id>/result/", views.result, name="result"),
    path("<int:q_id>/vote/", views.vote, name="vote"),
]
