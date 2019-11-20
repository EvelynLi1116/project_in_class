from django.http import HttpResponse

from .models import Pet

def all_pets(request):
    response_text='Check out these pets!'
    for pet in Pet.objects.all():
        response_text += f'{pet.species}, '
    return HttpResponse(response_text)

def pet_details(request,pet_id):
    pet = Pet.objects.get(id=pet_id)
    return HttpResponse(f"Hi, i'm pet {pet.id}")
