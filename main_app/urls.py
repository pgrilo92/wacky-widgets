from django.urls import path, include
from . import views
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    path('', views.wacky_widgets_index, name='wacky_widgets_index'),
    path('add_wacky_widget/', views.add_wacky_widget, name='add_wacky_widget'),
    path('<int:wacky_widget_id>/delete_wacky_widget/', views.delete_wacky_widget, name='delete_wacky_widget')

]