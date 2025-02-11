from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders, OrderUpadte
from math import ceil
import json

# Create your views here.
def index(request):

    allProds = []

    #It retrieves a queryset of dictionaries from the Product model, containing only the category and id fields of each product.
     
    """[
        {'category': 'Electronics', 'id': 1},
        {'category': 'Clothing', 'id': 2},
        {'category': 'Electronics', 'id': 3},
        {'category': 'Books', 'id': 4},
        {'category': 'Clothing', 'id': 5},
    ]"""

    catProds = Product.objects.values('category', 'id')
    
     
    """
        #This line creates a set of unique categories from the catProds queryset using a set comprehension. Using a set ensures that each category appears only once

        #A set comprehension is similar to a list comprehension, but it creates a set instead of a list.

        #The comprehension iterates over each dictionary (item) in the catProds queryset.

        #For each item, it extracts the value associated with the 'category' key (item['category'])

        #The extracted category values are added to the set cats.

        #Given the example catProds output above, the set comprehension would work as follows:

        #Iteration 1: item = {'category': 'Electronics', 'id': 1}
        #item['category'] is 'Electronics'
        #Add 'Electronics' to the set cats

        #Iteration 2: item = {'category': 'Clothing', 'id': 2}
        # item['category'] is 'Clothing'
        # Add 'Clothing' to the set cats

        # Iteration 3: item = {'category': 'Electronics', 'id': 3}
        # item['category'] is 'Electronics'
        # 'Electronics' is already in the set cats, so it is not added again

        # Iteration 4: item = {'category': 'Books', 'id': 4}
        # item['category'] is 'Books'
        # Add 'Books' to the set cats

        # Iteration 5: item = {'category': 'Clothing', 'id': 5}
        # item['category'] is 'Clothing'
        # 'Clothing' is already in the set cats, so it is not added again

        # Final Result:
        # The final set cats will contain:
        # {'Electronics', 'Clothing', 'Books'}
    """

    cats = {item['category'] for item in catProds}   
    for cat in cats:
        #For each category, it retrieves all products that belong to that category
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n/4) - (n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    
    params = {'allProds': allProds}
    
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if (request.method == "POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, phone = phone, desc = desc)
        contact.save()

    return render(request, 'shop/contact.html')

def tracker(request):
    if (request.method == "POST"):
        orderId = request.POST.get('orderId')
        email = request.POST.get('email')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpadte.objects.filter(order_id=orderId)
                update_list = list(update.values())  # Converts QuerySet to list of dicts
    
                print(f"update list {update_list[0]}")  # Debugging
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc,'time': str(item.timestamp)[: 10]})
                    response = json.dumps(updates, default=str)
                    return HttpResponse(response)
            else:
                return HttpResponse("error")
        except Exception as e:
            return HttpResponse("error")
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def prodView(request, p_id):
    # fetch the product based on the id
    product = Product.objects.get(id = p_id)  
    return render(request, 'shop/prodView.html', {'product': product})

def checkOut(request):
    if (request.method == "POST"):
        items_json = request.POST.get('itemsJson')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        addressline = request.POST.get('addressline')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')

        order = Orders(items_json = items_json, name=name, email=email, phone=phone, address=address, addressline=addressline, city=city, state=state, zip_code=zip_code)
        order.save()

        update = OrderUpadte(order_id=order.order_id, update_desc="This order has been placed")
        update.save()

        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')