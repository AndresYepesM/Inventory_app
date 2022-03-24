from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from product.models import Items
from product.forms import ItemForm

# Create your views here.

def inventory_list(request):
    list_items = Items.objects.all()
    context = {'product':list_items}
    return render(request, 'product/inventory_list.html', context)

def FormSuccess(request):
    list_items = Items.objects.all()
    context = {'product':list_items}
    return render(request, 'product/form_success.html', context)

def item_detail(request, pk):
    single_item = get_object_or_404(Items, id=pk)
    context = {'product':single_item}
    return render(request, 'product/item_detail.html', context)

def item_create(request):

    if request.method == 'GET':
      form = ItemForm()
      return render(request, 'product/add_item.html', {'form':form})
    else:
      form = ItemForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('Product:inventory_list')
      else:
         return render(request, 'product/add_item.html', {'form':form})

def item_update(request, pk):
    item = get_object_or_404(Items, id=pk)
    form = ItemForm(request.POST or None, instance=item)
    if request.method == 'GET':
      return render(request, 'product/update_item.html', {'form':form})
    else:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Product:inventory_list'))
        else:
            return render(request, 'product/update_item.html', {'form':form})

def item_delete(request, pk):
    item = get_object_or_404(Items, id=pk)
    item.delete()
    return HttpResponseRedirect(reverse('Product:inventory_list'))


class Inventory(ListView):
    model = Items
    template_name = 'product/inventory_list.html'
    context_object_name = 'product'

class ItemDetail(DetailView):
    model = Items
    template_name = 'product/item_detail.html'
    context_object_name = 'product'

class ItemAdd(CreateView):
    model = Items
    form_class = ItemForm
    template_name = 'product/add_item.html'

class ItemUpdate(UpdateView):
    model = Items
    form_class = ItemForm
    template_name = 'product/update_item.html'

class ItemDelete(DeleteView):
    model = Items
    form_class = ItemForm
    template_name = 'product/inventory_list.html'