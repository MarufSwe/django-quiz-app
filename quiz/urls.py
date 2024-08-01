from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Home page
    path('quiz/<str:topic_name>/', views.quiz_view, name='quiz-view'),
    path('quiz-result/<str:topic_name>/', views.quiz_result, name='quiz-result'),

]
