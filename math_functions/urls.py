from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('linear/<str:k>/<str:b>/', views.math_linear_function), #  一次函数，p正数，m负数:/mathfunctions/linear/m3/p5/ 传递就是-3和+5
    path('inverse/<str:k>/', views.inverse_proportion_function), #  反比例函数，p正数，m负数:/mathfunctions/inverseproportion/m3/ 传递就是-3
    path('quadratic/<str:a>/<str:b>/<str:c>/', views.quadratic_function), #  反比例函数，p正数，m负数:/mathfunctions/inverseproportion/m3/ 传递就是-3
]