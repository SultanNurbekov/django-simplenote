from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/note-list/',
		'Detail View':'/note-detail/<int:pk>/',
		'Create':'/note-create/',
		'Update':'/note-update/<int:pk>/',
		'Delete':'/note-delete/<int:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def notesList(request):
    notes = Note.objects.all().order_by('-id')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def noteDetail(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def noteCreate(request):
	serializer = NoteSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def noteDelete(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Succesfuly delete!)')





