from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import *
from typing import Any
from .forms import ProjectForm, PortfolioForm

# Create your views here.
def index(request):
    student_active_portfolios = Student.objects.select_related('Portfolio').filter(Portfolio__is_active=True)
    
    return render ( request, 'portfolio_app/home.html', {'student_active_portfolios':student_active_portfolios})

def createProject(request, portfolio_id):
    form = ProjectForm()
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    
    if request.method == "POST":
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id
        form = ProjectForm(project_data)
        if form.is_valid():
            project = form.save(commit=False)
            project.portfolio = portfolio
            project.save()

            return redirect('portfolio_details', portfolio_id)
    
    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)

def updateProject(request, portfolio_id, project_id):
    form = ProjectForm()
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    project = Project.objects.get(pk=project_id)

    if request.method == "POST":
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id
        form = ProjectForm(project_data, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.portfolio = portfolio
            project.save()

            return redirect('portfolio_details', portfolio_id)
    
    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)

def deleteProject(request, portfolio_id, project_id):
    project = Project.objects.get(pk=project_id)

    if request.method == 'POST':
        project.delete()
        return redirect('portfolio_details', portfolio_id)
    else:
        context = {'project':project, "portfolio_id":portfolio_id}
        return render(request, 'portfolio_app/delete_project.html', context)
    
def updatePortfolio(request, portfolio_id):
    form = PortfolioForm()
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    
    if request.method == "POST":
        portfolio_data = request.POST.copy()
        portfolio_data['portfolio_id'] = portfolio_id
        form = PortfolioForm(portfolio_data, instance=portfolio)
        if form.is_valid():
            project = form.save(commit=False)
            project.portfolio = portfolio
            project.save()

            return redirect('student_details', portfolio_id)
    
    context = {'form': form}
    return render(request, 'portfolio_app/portfolio_form.html', context)


class PortfolioDetailView(generic.DetailView):
    model=Portfolio
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all().filter(portfolio=self.object)
        return context

class PortfolioListView(generic.ListView):
    model=Portfolio

class ProjectListView(generic.ListView):
    model=Project

class ProjectDetailView(generic.DetailView):
    model=Project

class StudentListView(generic.ListView):
    model=Student

class StudentDetailView(generic.DetailView):
    model=Student
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["portfolio"] = self.object.Portfolio
        return context