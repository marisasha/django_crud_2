from django.urls import path
from django_app import views

urlpatterns = [
    path('form/',views.form , name="form"),
    path('save_form/',views.save_form , name="save_form"),
    path('statements/',views.statements,name = "statements"),
    path('statement/<str:pk>/',views.statement,name = "statement"),
    path('statement_delete/<str:pk>/',views.statement_delete,name = "statement_delete")
]
