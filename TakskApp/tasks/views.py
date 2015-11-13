from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.
from django.http import HttpResponse
from .models import Item
from .forms import PostForm,getData

def add_task(request):
    """Adds a new task to the list."""
    latest_item_list = Item.objects.order_by('title')
    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['Task_Description']
            completed = form.cleaned_data['completed']
            post = Item.objects.create(title=title,completed=completed)
            return HttpResponseRedirect('/tasks/')

    return render(request, 'tasks/index.html', {'form': form,'latest_item_list': latest_item_list,})

def update_task(request,item_id):
    """Updates an existing task in the list."""
    item = get_object_or_404(Item, pk=item_id)
    form = getData(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            title = form.cleaned_data['Edit_Task_Description']
            updatetask_desc = Item.objects.get(id=item_id)
            updatetask_desc.title = title
            updatetask_desc.save()
            return HttpResponseRedirect(".")
    else:
        form = getData()

    return render(request, 'tasks/detail.html', {'item': item,'form': form,})

def deleteTask(request,item_id):
    """Delete a task in the list."""
    item = Item.objects.get(pk=item_id)
    item.delete()
    return HttpResponseRedirect('/tasks/')

def markIt(request,item_id):
    """Mark a task in the list as completed."""
    item = Item.objects.get(pk=item_id)
    item.completed = True
    item.save()
    return HttpResponseRedirect('/tasks/')
