import os
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from portfolio_project import settings
from .models import Document, Project, Skill

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    document = Document.objects.all()
    return render(request, 'portfolio_app/index.html', {'projects': projects, 'skills': skills, 'document': document})

def download_document(request):
    document = get_object_or_404(Document)
    file_path = os.path.join(settings.MEDIA_ROOT, str(document.file))
    print("File Path:", file_path)
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/doc')
        response['Content-Disposition'] = f'attachment; filename="{document.file.name}"'
    return response