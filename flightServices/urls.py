from django.contrib import admin
from django.urls import path, include
from flightapp import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('flights', views.FlightViewSet)
router.register('passenger', views.PassengerViewSet)
router.register('reservation', views.ReservationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('search', views.FlightSearch.as_view(), name='search'),
    path('gettoken', obtain_auth_token, name='gettoken')
]
