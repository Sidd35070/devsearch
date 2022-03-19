from django.shortcuts import render
from django.http import HttpResponse

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

def projects(request):
    return render(request, 'projects/projects.html', {'projects': projectList})
    
def project(request, pk):
    theproject = None
    for project in projectList:
        if project['id'] == pk:
            theproject = project

    return render(request, 'projects/project.html', {'project': theproject})