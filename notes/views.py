from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from .models import Notes
from django.core.serializers import serialize
# Create your views here.


class NotesView(View):

    def get(self, *args, **kwargs):
        notes = Notes.objects.all()
        serialiers = serialize('json', notes)
        return JsonResponse(serialiers)

    def post(self, *args, **kwargs):
        
        response = {}
        return JsonResponse(response)
    

    
