from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.events, name="events"),
    path('events/', views.events, name="events"),
	path('events/catas-de-vinos/', views.catas, name="catas"),
	path('events/rutas-de-tapas/', views.rutas, name="rutas"),
    
    path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
] 