from django.urls import path

from apps.redirect.views import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(), name='redirect'),
]
