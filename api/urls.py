
# from .views import approve_ticket
from django.urls import path
from .views import (
    GetCountries,
    GetStates,
    GetCities,

)

urlpatterns = [
   
    path("address/", GetCountries.as_view(), name="address"),
    path("states/", GetStates.as_view(), name="state"),
    path("cities/", GetCities.as_view(), name="city"),

]
