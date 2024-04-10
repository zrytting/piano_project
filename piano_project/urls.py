from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
path('', views.index, name='index'),
path('<slug:slug>/details', views.teacherDetailView.as_view(), name='teacher_details'),
path('teacher/create', views.createTeacher, name='create_teacher'),
path('teacher/update/<slug:slug>', views.updateTeacher, name='update_teacher'),
path('teacher/delete/<slug:slug>', views.deleteTeacher, name='delete_teacher')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
