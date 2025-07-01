from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from home.models import *

# Create your views here.
def homepage(request):

    show_item = Category.objects.all()
    food_item = Food.objects.all()
    context = {
    'show': show_item,
    'fshow': food_item
    }

    return render(request, 'index.html', context)


def aboutpage(request):
    return render(request, 'about.html')


def loginpage(request):

    if request.method == 'POST':

        emailv = request.POST.get('emailh')
        passv = request.POST.get('passh')

        if not User.objects.filter(username = emailv):
            messages.error(request, 'User Not registered! Please register first.')
            return redirect('loginp')
        
        user = authenticate(username = emailv, password = passv)

        if user is None:
            messages.error(request, 'Invalid Password.')
            return redirect('loginp')
        else:
            login(request, user)
            return redirect('homep')
        
    return render(request, "login.html")


def registerpage(request):

    if request.method == 'POST':

        fnamev = request.POST.get('fnameh')
        lnamev = request.POST.get('lnameh')
        emailv = request.POST.get('emailh')
        passv = request.POST.get('passh')
        cpassv = request.POST.get('cpassh')
        
        
        if passv == cpassv:

            if User.objects.filter(email = emailv):
                messages.error(request, "User already exixsts! Try with other email.")
                return redirect('registerp') 
            
            newuser = User(first_name = fnamev, last_name = lnamev, username = emailv, email = emailv, )
            newuser.set_password(cpassv)
            newuser.save()

            return redirect('loginp')
        
        else:
            messages.error(request, 'Invalid Password!!!')
            return redirect('registerp')
        
    return render(request, 'register.html')


def logoutpage(request):
    logout(request)
    return redirect('homep')


def feedbackpage(request):

    if request.method == 'POST':

        fnamev = request.POST.get('fnameh')
        emailv = request.POST.get('emailh')
        numberv = request.POST.get('phoneh')
        subjectv = request.POST.get('subjecth')
        messagev = request.POST.get('messageh')

        store_feed = Contact.objects.create(
            name = fnamev, email = emailv, number = numberv, subject = subjectv, message = messagev
        )
        store_feed.save()

        messages.success(request, "Thank you for giving Valuable Feedback......")
        return redirect('feedbackp')
        
    return render(request, 'feedback.html')


def categorypage(request):

    show_item = Category.objects.all()
    
    if request.GET.get('searchnameh'):
        show_item = show_item.filter(cat_name__icontains = request.GET.get('searchnameh'))
    context = {'sitem':show_item}

    

    return render(request, 'categories.html', context)


@login_required(login_url=loginpage)
def foodpage(request):

    food_item = Food.objects.all()
    
    if request.GET.get('foodsearch'):
        food_item = food_item.filter(food_name__icontains = request.GET.get('foodsearch'))

    cart_items = CartItem.objects.filter(user=request.user)
    context = {'fitem' : food_item, 'citem': cart_items}
    return render(request, 'foods.html', context)


@login_required(login_url=loginpage)
def add_to_cart(request, product_id):
    product = get_object_or_404(Food, id=product_id)
    quantity = int(request.POST.get('quantity', 1))  # Default to 1 if not sent

    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()
    return redirect('view_cart')


@login_required(login_url=loginpage)
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price for item in cart_items)
    if request.method == 'POST':
        mobile = request.POST.get('mobileh')
        address = request.POST.get('addressh')

        # Get cart items from DB, not session
        cart_items = CartItem.objects.filter(user=request.user)

        if not cart_items.exists():
            return render(request, 'view_cart.html', {'error': 'Cart is empty'})


        for item in cart_items:
            total = item.product.price * item.quantity
            OrderItem.objects.create(
                user=request.user,
                food=item.product,
                quantity=item.quantity,
                total=total,
                mobile=mobile,
                address=address,
                usermail=request.user.email
            )
        cart_items.delete()

        return redirect('homep')


    return render(request, 'view_cart.html', {'cart_items': cart_items, 'total': total})


@login_required(login_url=loginpage)
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('view_cart') 


@login_required(login_url=loginpage)
def userprofilepage(request):
    current_user = request.user
    print(current_user.username)  

    context = {
        'user': current_user,
    }
    
    return render(request, "userprofile.html", context)


@login_required(login_url=loginpage)
def updatedprofilepage(request):
    return render(request, "updateprofile.html")


@login_required(login_url=loginpage)
def update_item(request, id):
    usr = User.objects.get(id =id)
    if request.method == 'POST':
        usr.first_name = request.POST.get('fnameh')
        usr.last_name = request.POST.get('lnameh')
        usr.email = request.POST.get('emailh')
        usr.username = request.POST.get('emailh')
        usr.save()
        return redirect('userp')

    return render(request, 'updateprofile.html', {'usrinfo': usr})