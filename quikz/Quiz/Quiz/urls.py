from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from django.views.generic import RedirectView

urlpatterns = [
 path('admin/', admin.site.urls),
 path('', include("App.urls")),
 path('catalog/', RedirectView.as_view(url='/login')),
 path('cats/', RedirectView.as_view(url='/login')),

]