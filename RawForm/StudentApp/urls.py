from django.urls import path
from . import views

urlpatterns=[
    path("show/",views.showView),
    path("add/",views.AddView.as_view()),
    path("update/<i>/",views.UpdateView.as_view()),
    path("delete/<i>/",views.deleteView)
]