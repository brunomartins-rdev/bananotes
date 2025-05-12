from django.shortcuts import render

from .models import Note

# Create your views here.
def index(request):
    notes_list = Note.objects.order_by('-created_at')
    print(notes_list)
    context = {'notes_list': notes_list}
    return render(request, 'notes.html', context)

