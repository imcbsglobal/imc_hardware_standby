from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, ItemImage

# LIST ITEMS
def item_list(request):
    items = Item.objects.prefetch_related('images').all()
    return render(request, 'addtable.html', {'items': items})

# ADD ITEM
def add_item(request):
    if request.method == "POST":
        name = request.POST.get('itemname')
        serial_number = request.POST.get('serialnumber')
        notes = request.POST.get('notes')
        stock = request.POST.get('stock')

        item = Item.objects.create(
            name=name,
            serial_number=serial_number,
            notes=notes,
            stock=stock
        )

        for image in request.FILES.getlist('images'):
            ItemImage.objects.create(item=item, image=image)

        return redirect('item_list')

    return render(request, 'add.html')

# EDIT ITEM
def item_edit(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == "POST":
        item.name = request.POST.get('itemname')
        item.serial_number = request.POST.get('serialnumber')
        item.notes = request.POST.get('notes')
        item.stock = request.POST.get('stock')
        item.save()

        # Delete selected images
        delete_ids = request.POST.get('delete_images', '')
        if delete_ids:
            ids = delete_ids.split(',')
            ItemImage.objects.filter(id__in=ids, item=item).delete()

        # Add new images
        for image in request.FILES.getlist('images'):
            ItemImage.objects.create(item=item, image=image)

        return redirect('item_list')

    return render(request, 'edit.html', {'item': item})

# DELETE ITEM
def item_delete(request, item_id):
    if request.method == "POST":
        item = get_object_or_404(Item, id=item_id)
        item.delete()
    return redirect('item_list')

