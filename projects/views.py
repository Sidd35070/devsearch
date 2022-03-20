from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm



def projects(request):
    projectList = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projectList})
    
def project(request, pk):
    theproject = Project.objects.get(id=pk)

    return render(request, 'projects/project.html', {'project': theproject})

def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        'form':form
    }
    return render(request, 'projects/projectForm.html', context)

def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        'form':form
    }
    return render(request, 'projects/projectForm.html', context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    return render(request, 'projects/deleteTemplate.html')