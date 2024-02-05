from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Photo
from .forms import PhotoForm

def add_photo_to_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.product = product
            photo.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = PhotoForm()

    return render(request, 'your_template/add_photo_to_product.html', {'form': form, 'product': product})

def delete_photo(request, product_id, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    product_id = photo.product.id
    photo.delete()
    return redirect('product_detail', product_id=product_id)
