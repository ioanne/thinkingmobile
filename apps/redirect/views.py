from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from apps.redirect.models import Redirect


class RedirectView(View):
    def get(self, request):
        key = request.GET.get('key')
        redirect = None
        if not key:
            return JsonResponse(data={}, status=400)

        if key:
            redirect = Redirect.get_redirect(key)

        if not redirect:
            return JsonResponse(data={}, status=404)

        return JsonResponse(redirect, status=200)
