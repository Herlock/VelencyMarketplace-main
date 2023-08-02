from django.urls import path
from . import views

urlpatterns = [
    # log/reg pages
    path('logout/', views.logoutUser, name="logoutUser"),
    # product pages
    path('product-list/<int:category_id>', views.view_all, name="product-list"),
    path('sub-product-list/', views.sub_view_all, name="sub-product-list"),
    path('trends-list/', views.trends, name="trends-list"),
    path('all-product-list/', views.all_product_list, name="all-product-list"),
    # customer details
    path('profile/', views.my_profile, name="profile"),
    path('orders/', views.orders, name="orders"),
    # searsh
    path('search/', views.search, name="search"),
    # product details
    path('product/<str:id>', views.product_details, name="product-details"),
    # comments
    path('addcomment/<int:id>', views.addComment, name="addcomment"),
    # wishlist
    path('wishlist/', views.wishlist, name="wishlist"),
    path('add-to-wishlist/', views.addToWishlist, name="add-to-wishlist"),
    path('delete-from-wishlist/', views.DeleteFormWishList,
         name="delete-from-wishlist"),
    # suggestions
    path('offers/', views.offers, name="offers"),
    # support
    path('support/', views.support, name="support"),
    # packages
    path('packages/', views.packages, name="packages"),
    # politic
    path('politic/', views.politic, name="politic"),

    # main pages
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('packages/packet_buy/', views.packet_buy, name="packet_buy"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('customer_form/', views.account, name='customer_form'),
    # #moralis reg

    path('my_profile/', views.my_profile, name='my_profile'),

    path('send_email/', views.send_email, name='send_email'),
    path('trainers/', views.trainers, name='trainers'),
    path('schedule/', views.schedule, name='schedule'),
    path('tasks/', views.tasks, name='tasks'),

    # walletConnect
    path('authenticate_wallet/', views.authenticate_wallet,
         name='authenticate_wallet'),

]
