from django.shortcuts import render
from realpal.users.models import City


def serve_cities(request):
    cities = City.objects.all()
    return render(
        request,
        'mainapp/onboarding_prepare/areas.html',
        {'cities': cities}
    )
