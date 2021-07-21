from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    product_id_from_form = float(request.POST["product_id"])
    
    for product in Product.objects.all():
        if product.id == product_id_from_form:
            charge = product.price
    total_charge =quantity_from_form * charge
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect ("/final_checkout")
def final (request):
    total_items = 0
    total_price = 0 
    for order in Order.objects.all():
        total_items += order.quantity_ordered
        total_price += order.total_price
    context = {
        "all_products": Product.objects.all(),
        "this_order" : Order.objects.last(),
        "total_price" : total_price,
        "total_items" : total_items
    }
    return render (request, "store/checkout.html", context)