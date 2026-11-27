from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Note

@login_required
def index(request):
    if request.method == "POST":
        text = request.POST.get("text", "").strip()[:50]
        if text:
            Note.objects.create(owner=request.user, text=text)
        return redirect("index")

    query = request.GET.get("q", "")
    if query:
        # flaw A03 Injection: user input is pasted into raw SQL.
        # problem: you can use:  %' OR 1=1 --   to see everyone's notes.
        # how to fix the flaw:
        #   if query:
        #       notes = Note.objects.filter(owner=request.user, text__icontains=query).order_by("created")
        #   else:
        #   notes = Note.objects.filter(owner=request.user,).order_by("created")
        sql = (
            "SELECT * FROM notes_note "
            f"WHERE owner_id = {request.user.id} AND text LIKE '%{query}%'"
            "ORDER BY created"
        )
        notes = Note.objects.raw(sql)
    else:
        notes = Note.objects.filter(owner=request.user).order_by("created")

    return render(request, "notes/index.html", {"notes": notes, "query": query})

@login_required
def detail(request, note_id):
    # flaw A01 Broken Access Control: the note is looked up by id only.
    # problem: anyone can see any note if they know the id.
    # how to fix the flaw: get_object_or_404(Note, id=note_id, owner=request.user)
    note = get_object_or_404(Note, pk=note_id)
    return render(request, "notes/detail.html", {"note": note})

@login_required
def delete(request, note_id):
    if request.method == "POST":
        # flaw A01 Broken Access Control: the note is deleted by id only.
        # problem: anyone can delete any note if they know the id.
        # how to fix the flaw: Note.objects.filter(id=note_id, owner=request.user).delete()
        Note.objects.filter(id=note_id).delete()
    return redirect("index")