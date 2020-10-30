from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
# import the Itel form
from .forms import ItemForm

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == 'POST':
        # populate the form with the request.post data
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect them back to the updated to do list
            return redirect('get_todo_list')

    #  create an instance of the form in the add_item view
    form = ItemForm()
    # create a context which contains the empty form
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    """  get a copy of the item from the database. using a built
        in django shortcut called get_object_or_404
        Which we'll use to say we want to get an instance of the item model.
    """
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        # populate the form with specific instance to upsate
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            # redirect them back to the updated to do list
            return redirect('get_todo_list')

    #  create an instance of the form in the add_item view
    # prepopulate it with item current details
    form = ItemForm(instance=item)
    # create a context which contains the empty form
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')
