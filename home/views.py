from django.shortcuts import render , HttpResponse
from .models import Contact
from django.contrib import messages
from . models import Product , Order

from math import ceil
import logging
logger = logging.getLogger(__name__)



def home(request):
    allProds = []
    
    # Fetch distinct product categories and their IDs
    catProds = Product.objects.values('product_category', 'id')
    cats = {item['product_category'] for item in catProds}  # Create a set of unique categories
    
    for cat in cats:
        # Filter products by category
        prod = Product.objects.filter(product_category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))  # Number of slides (pagination)
        allProds.append([prod, range(1, nSlides), nSlides])
    
    # Prepare context data to be passed to the template
    params = {'allProds': allProds}
    
    return render(request, "home/home.html", params)  # Render the response with the template

def searchMatch(query, item):
    if query in item.description.lower() or query in item.product_name.lower() or query in item.product_category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search', '')
    print(query)
    print(query)
    allProds = []
    catprods = Product.objects.values('product_category', 'id')
    cats = {item['product_category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(product_category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<2:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'home/search.html', params)





def about(request):
    return render(request, 'home/about.html')



def contact(request):
    if request.method == 'POST':
        name=request.POST.get('username', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        content=request.POST.get('content', '')
        contact = Contact(name=name ,email=email, phone=phone, content=content)
        contact.save()
        messages.success(request , "your message send successfully")
    return render(request, 'home/contact.html')
    



def productView(request, myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request, "home/prodView.html", {'product': product[0]})



def checkout(request):
    if request.method == "POST":
        # Handling the form submission (POST request)
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        # Save the order to the database
        order = Order(
            items_json=items_json, 
            name=name, 
            email=email, 
            address=address, 
            city=city, 
            state=state, 
            zip_code=zip_code, 
            phone=phone,
            amount=amount
        )
        order.save()

        # Variables for the success message
        thank = True
        id = order.order_id

        # Return the response with the success message and order ID
        return render(request, 'home/checkout.html', {'thank': thank, 'id': id})
    
    else:
        # Handling the GET request (when the user first visits the checkout page)
        return render(request, 'home/checkout.html')

