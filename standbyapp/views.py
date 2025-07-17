from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib import messages
from .models import Item, ItemImage

# ✅ List all items
def item_list(request):
    items = Item.objects.prefetch_related('images').all()
    return render(request, 'addtable.html', {'items': items})

# ✅ Add new item
def add_item(request):
    if request.method == "POST":
        name = request.POST.get("itemname")
        serial_number = request.POST.get("serialnumber").upper()
        notes = request.POST.get("notes")
        stock = request.POST.get("stock")
        images = request.FILES.getlist("images")

        try:
            item = Item.objects.create(
                name=name,
                serial_number=serial_number,
                notes=notes,
                stock=stock
            )

            for img in images:
                ItemImage.objects.create(item=item, image=img)

            messages.success(request, "Item added successfully!")
            return redirect("item_list")

        except IntegrityError:
            messages.error(request, f"Serial Number '{serial_number}' already exists!")
            return redirect("add")

    return render(request, "add.html")

# ✅ Edit item
def item_edit(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == "POST":
        item.name = request.POST.get('itemname')
        item.serial_number = request.POST.get('serialnumber').upper()
        item.notes = request.POST.get('notes')
        item.stock = request.POST.get('stock')
        try:
            item.save()
        except IntegrityError:
            messages.error(request, "Serial number already exists!")
            return redirect("item_edit", item_id=item.id)

        delete_ids = request.POST.get('delete_images', '')
        if delete_ids:
            ids = delete_ids.split(',')
            ItemImage.objects.filter(id__in=ids, item=item).delete()

        for image in request.FILES.getlist('images'):
            ItemImage.objects.create(item=item, image=image)

        messages.success(request, "Item updated successfully!")
        return redirect('item_list')

    return render(request, 'edit.html', {'item': item})

# ✅ Delete item
def item_delete(request, item_id):
    if request.method == "POST":
        item = get_object_or_404(Item, id=item_id)
        item.delete()
    return redirect('item_list')

# ✅ AJAX check for unique serial number
def check_serial(request):
    serial = request.GET.get('serial', '').upper()
    exists = Item.objects.filter(serial_number=serial).exists()
    return JsonResponse({'exists': exists})

from django.db.models import Q

def item_list(request):
    search_query = request.GET.get('search', '')

    items = Item.objects.all().order_by('-created_at')

    if search_query:
        items = items.filter(
            Q(name__icontains=search_query) | Q(serial_number__icontains=search_query)
        )

    return render(request, 'addtable.html', {'items': items})



