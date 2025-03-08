from django.urls import path
from . import views

urlpatterns = [
    path(
        'DjTraders', 
        views.DjTradersHome, 
        name='DjTraders.Home'),
    
    path(
        'DjTraders/Customers', 
         views.DjTradersCustomersView.as_view(), 
         name='DjTraders.Customers'),
    
    path(
        'DjTraders/CustomersJSON', 
         views.CustomersListJSON.as_view(), 
         name='DjTraders.CustomersJSON'),
    
    path(
        'DjTraders/TopTenCustomers', 
         views.CustomerOrders.as_view(), 
         name='DjTraders.TopCustomerOrders'),
    
    #v3.1
    path(
        'DjTraders/OrdersPlaced',
        views.OrdersPlaced,
        name='DjTraders.OrdersPlaced'),
    
    path(
        'DjTraders/OrdersByDate',
        views.OrdersByDate,
        {'selOrderYear': ""},
        name='DjTraders.OrdersByDate'),

    path(
        'DjTraders/OrdersByCategory',
        views.OrdersByCategory,
        name='DjTraders.OrdersByCategory'),

    path(
        'DjTraders/OrdersByProduct',
        views.OrdersByProduct,
        name='DjTraders.OrdersByProduct'),

    # v2.1 
    # Add path to Form for add and edit customers
    path(
        route = 'DjTraders/Customers/new', 
        view = views.DjTradersCustomerCreate.as_view(), 
        name='DjTraders.CustomerAdd'),

    path(
        route = 'DjTraders/Customers/<int:pk>/Edit', 
        view = views.DjTradersCustomerEdit.as_view(), 
        name='DjTraders.CustomerEdit'),

    path(
        route = 'DjTraders/Customers/<int:pk>/Delete', 
        view = views.DjTradersCustomerDelete.as_view(), 
        name='DjTraders.CustomerDelete'),

    path(
        'DjTraders/CustomerDetail/<int:pk>', 
        views.DjTradersCustomerDetailView.as_view(), 
        name='DjTraders.CustomerDetail'),
    
    #Add path to form for all and edit products

    path(
        'DjTraders/Products', 
        views.DjTradersProductsView.as_view(), 
        name='DjTraders.Products'),
    
     path(
        route = 'DjTraders/Products/new', 
        view = views.DjTradersProductCreate.as_view(), 
        name='DjTraders.ProductAdd'),
     
      path(
        route = 'DjTraders/Products/<int:pk>/Edit', 
        view = views.DjTradersProductEdit.as_view(), 
        name='DjTraders.ProductEdit'),

    path(
        route = 'DjTraders/Products/<int:pk>/Delete', 
        view = views.DjTradersProductDelete.as_view(), 
        name='DjTraders.ProductDelete'),

    path(
        'DjTraders/ProductDetail/<int:pk>', 
        views.DjTradersProductDetailView.as_view(), 
        name='DjTraders.ProductDetail'),
    
    
    # Extra credit 2 - Customer Purchase Summary
    
    path(
        route='DjTraders/ProductPurchaseSummary/<int:pk>',
        view= views.DjTradersProdsPurchasedView.as_view(),
        name='DjTraders.ProductPurchaseSummary'),
    
    
    #Assignment 3
    path(
        route='DjTraders/ProductSalesAnalysis/<int:pk>',
        view= views.product_sales_analysis,
        name='DjTraders.ProductSalesAnalysis'
    ),
     
    path(
        'DjTraders/TopBottomAnalysis/',
        views.plot_top_bottom_revenue_products,
        {'selOrderYear': ""},
        name='DjTraders.TopBottomAnalysis'),
    
    path(
        route ='DjTraders/ProductAnnualMonthlySales/<int:pk>',
        view =views.ProductAnnualMonthlySales,
        name='DjTraders.ProductAnnualMonthlySales'
    ),
    
    path(
        route ='DjTraders/ProductCategorySalesAnalysis/<int:pk>',
        view =views.ProductCategoryAnalysis,
        name='DjTraders.ProductCategorySalesAnalysis'
    ),
]
