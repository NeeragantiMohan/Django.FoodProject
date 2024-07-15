from django.shortcuts import render
from django.http import HttpResponse
from FoodApp.models import Item
from FoodApp.forms import ItemForm
from django import forms
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    item_list=Item.objects.all()
    context={
        'item_list':item_list,
    }
    return render(request,'FoodApp/index.html',context)


# class Based View
class IndexClassView(ListView):
    model= Item;
    template_name='FoodApp/index.html'
    context_object_name='item_list'

def item(request):
    return HttpResponse('<h1>This is an item view</h1>')

def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request,'FoodApp/detail.html',context)

#class Based View
class FoodDetail(DetailView):
    model=Item
    template_name='FoodApp/detail.html'

def create_item(request):
    form = ItemForm(request.POST or None)
 
    if form.is_valid():
        form.save()
        return redirect('FoodApp:index')
 
    return render(request,'FoodApp/item-form.html',{'form':form})

#class Based View
class CreateItem(CreateView):
    model = Item;
    fields = ['item_name','item_desc','item_price','item_image']
    template_name = 'FoodApp/item-form.html'

    def from_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)


def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
 
    if form.is_valid():
        form.save()
        return redirect('FoodApp:index')
 
    return render(request,'FoodApp/item-form.html',{'form':form,'item':item})
 
def delete_item(request,id):
    item = Item.objects.get(id=id)
 
    if request.method == 'POST':
        item.delete()
        return redirect('FoodApp:index')
 
    return render(request,'FoodApp/item-delete.html',{'item':item})