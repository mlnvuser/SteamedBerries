from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage
from cart.forms import CartAddProductForm


def popular_products(request):
    products = Product.objects.filter(available=True)[:3]
    return render(request, template_name='main/index/index.html',context={'products':products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_product_form  = CartAddProductForm
    return render(request, template_name='main/product/detail.html', context={'product':product,
                                                                              'cart_product_form':cart_product_form})

def product_list(request, category_slug = None):
    page_number = request.GET.get('page', 1)
    category = None
    products = Product.objects.all()
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, 2)  # 10 продуктов на страницу
    try:
        current_page = paginator.page(int(page_number))
    except (ValueError, EmptyPage):
        current_page = paginator.page(paginator.num_pages)

    return render(request, template_name='main/product/list.html', context={
        'category':category,
        'products':current_page,
        'categories':categories,
        'slug_url':category_slug
    })


