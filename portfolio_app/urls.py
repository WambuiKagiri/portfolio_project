
from django.urls import path
from django.conf.urls.static import static

from portfolio_project import settings
from .views import home
from .views import download_document

urlpatterns = [
    path('', home, name='home'),
    path('download/', download_document, name='download_document'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
