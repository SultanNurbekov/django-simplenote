from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
    path("note-list/", views.notesList, name="note-list"),
    path("note-detail/<int:pk>", views.noteDetail, name="note-detail") ,
    path("note-create/", views.noteCreate, name="note-create"),
    path("note-delete/<int:pk>", views.noteDelete, name="note-delete")
]
