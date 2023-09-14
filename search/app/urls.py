from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('detail_page/<int:id>', views.detail_page, name='detail_page'), 
    # path('getProfiles', views.getProfiles, name='getProfiles'),
]
