from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectList = [
    {
        'id' : '1',
        'title' : 'First project'
    },
    {
        'id' : '2',
        'title' : 'Second project'
    },
    {
        'id' : '3',
        'title' : 'Third project'
    }
]

projectList = Project.objects.all()

def projects(request):
    return render(request, 'projects/projects.html', {'projects': projectList})
    
def project(request, pk):
    theproject = Project.objects.get(id=pk)

    return render(request, 'projects/project.html', {'project': theproject})