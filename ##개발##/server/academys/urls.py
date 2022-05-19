from django.urls import path
from .views import AcademyRegistrationView
from . import views

app_name = 'academys'

urlpatterns = [
    path('signup/academys/', AcademyRegistrationView.as_view()),
    # 전체 조회 및 생성
    path('educations/', views.education_list_or_create),
    path('educations/<int:education_pk>/', views.education_detail_or_update_or_delete),
    # Category
    # 조회 및 생성
    path('category/', views.category_list_or_create),
    path('category/<int:category_pk>/', views.category_detail_or_update_or_delete),
]