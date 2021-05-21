from django.urls import path, include

from . import views

app_name='foodieapp'
urlpatterns = [
    path('', views.allProudCat, name='allProudCat'),
    path('<slug:c_slug>/',views.allProudCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProudCatDetail,name='ProudCatDetail'),

]
