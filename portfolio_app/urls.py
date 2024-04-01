from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('student/<int:pk>/portfolio', views.PortfolioDetailView.as_view(), name='portfolio_details'),
    path('student/<int:pk>/portfolio/project', views.ProjectDetailView.as_view(), name='project_details'),
    path('student/<int:portfolio_id>/portfolio/project/<int:project_id>/delete', views.deleteProject, name='delete_project'),
    path('student/<int:portfolio_id>/portfolio/project/create', views.createProject, name='create_project'),
    path('student/<int:portfolio_id>/portfolio/project<int:project_id>/update', views.updateProject, name='update_project'),
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('student/<int:pk>/details', views.StudentDetailView.as_view(), name='student_details'),
    path('student/<int:portfolio_id>/portfolio/update', views.updatePortfolio, name='update_portfolio')
]
