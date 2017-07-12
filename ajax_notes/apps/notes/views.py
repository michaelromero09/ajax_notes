from django.shortcuts import render, HttpResponse, redirect
from .models import Notes

# Create your views here.
def index(request):
  notes = Notes.objects.all()
  print 'Page refreshed'
  context = {
    'notes' : notes,
  }
  return render(request, 'notes/index.html', context)

def add_note(request):
  title = request.POST['title']
  description = request.POST['description']
  Notes.objects.create(title = title, description = description)
  notes = Notes.objects.all()
  context = {
    'notes' : notes
  }
  return render(request, 'notes/notes_index.html', context)

def delete(request):
  print 'Deleting'
  if 'note_id' not in request.POST:
    print 'nobody here but us chickens'
    return redirect('/')
  note_id = request.POST['note_id']
  Notes.objects.get(id = note_id).delete()
  notes = Notes.objects.all()
  context = {
    'notes' : notes
  }
  return render(request, 'notes/notes_index.html', context)

def edit(request):
  if request.is_ajax():
    if request.method == 'POST':
      print 'Editing'

  return redirect('/')