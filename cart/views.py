from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    '''a view to render the cart content page'''
    return render(request, 'cart.html')
    
def add_to_cart(request,id):
    '''add quantitl=y of the specific product to the cart '''
    quantity = int(request.POST.get('quantity'))
    
    cart = request.sessions.get('cart', {})
    cart[id] = cart.get(id, quantity)
    
    request.sessions['cart'] = cart
    return redirect(reverse('index'))
    
def adjust_cart(request, id):
    '''adjust the quantity of the product'''
    quantity = int(request.POST.get('quantity'))
    cart = request.sessions.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.sessions['cart'] = cart
    return redirect(reverse('view_cart'))