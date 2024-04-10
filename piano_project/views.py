from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import *
from .forms import teacherForm

# Create your views here.
def index(request):
    active_teachers = teacher.objects.all()
    return render(request, 'piano_project/home.html', {'active_teachers':active_teachers})

class teacherDetailView(generic.DetailView):
    model = teacher

def createTeacher(request):
    form = teacherForm()
    
    if request.method == "POST":
        form = teacherForm(request.POST, request.FILES)
        if form.is_valid():
            new_teacher = form.save(commit=False)
            new_teacher.save()
            
            return redirect('teacher_details', slug=new_teacher.slug)
    
    context = {'form': form}
    return render(request, 'piano_project/teacher_form.html', context)

def updateTeacher(request, slug):
    target_teacher = teacher.objects.get(slug=slug)

    form = teacherForm(instance=target_teacher)

    if request.method == "POST":
        print("working?")
        form = teacherForm(request.POST, request.FILES, instance=target_teacher)
        if form.is_valid():
            updated_teacher = form.save(commit=False)
            updated_teacher.slug = slugify(updated_teacher.name)
            updated_teacher.active = True
            print(updated_teacher)
            updated_teacher.save()
            
            return redirect('teacher_details', slug=updated_teacher.slug)
    
    context = {'form': form}
    return render(request, 'piano_project/teacher_form.html', context)

def deleteTeacher(request, slug):
    teacher_delete = teacher.objects.get(slug=slug)

    if request.method == 'POST':
        teacher_delete.delete()
        return redirect('index')
    else:
        context = {'teacher': teacher_delete}
        return render(request, 'piano_project/delete_teacher.html', context)