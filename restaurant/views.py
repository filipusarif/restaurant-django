from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Restaurant, Review
from .forms import AddRestaurantForm, AddReviewForm
from django.db.models import Avg
from .decorators import user_is_customer, user_is_owner


# 1. Menambahkan Restoran Baru
@login_required
@user_is_owner
def add_restaurant(request):
    if request.method == 'POST':
        form = AddRestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.owner = request.user
            restaurant.save()
            # messages.success(request, 'Restoran berhasil ditambahkan!')
            return redirect('restaurant:owner_restaurant_list')
    else:
        form = AddRestaurantForm()
    return render(request, 'restaurant/add_restaurant.html', {'form': form})

# 2. Menghapus Restoran
@login_required
@user_is_owner
def delete_restaurant(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk, owner=request.user)
    if request.method == 'POST':
        restaurant.delete()
        # messages.success(request, 'Restoran berhasil dihapus.')
        return redirect('restaurant:owner_restaurant_list')
    return render(request, 'restaurant/restaurant_confirm_delete.html', {'restaurant': restaurant})

# 3. Melihat Statistik Restoran
@login_required
@user_is_owner
def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk, owner=request.user)
    reviews = restaurant.reviews.all()
    total_reviews = reviews.count()
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0  # Use Avg directly
    return render(request, 'restaurant/restaurant_detail.html', {
        'restaurant': restaurant,
        'reviews': reviews,
        'total_reviews': total_reviews,
        'average_rating': average_rating,
    })

# List restoran
@login_required
@user_is_owner
def owner_restaurant_list(request):
    restaurants = Restaurant.objects.filter(owner=request.user)
    return render(request, 'restaurant/owner_restaurant_list.html', {'restaurants': restaurants})

@login_required
@user_is_customer
def customer_restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant/customer_restaurant_list.html', {'restaurants': restaurants})





@login_required
@user_is_customer
def add_review(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)

    if request.method == 'POST':
        form = AddReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.user = request.user
            review.save()
            # messages.success(request, 'Review berhasil ditambahkan!')
            return redirect('main:show_main')
    else:
        form = AddReviewForm()

    return render(request, 'restaurant/add_review.html', {
        'form': form,
        'restaurant': restaurant,
    })
