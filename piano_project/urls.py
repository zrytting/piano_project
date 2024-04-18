from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
path('', views.index, name='index'),
path('<slug:slug>/details', views.teacherDetailView.as_view(), name='teacher_details'),
path('teacher/create', views.createTeacher, name='create_teacher'),
path('teacher/update/<slug:slug>', views.updateTeacher, name='update_teacher'),
path('teacher/delete/<slug:slug>', views.deleteTeacher, name='delete_teacher'),
path('accounts/', include('django.contrib.auth.urls')),
path('accounts/register/', views.registerPage, name='register_page')
#path('user/', views.userPage, name='user_page')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
