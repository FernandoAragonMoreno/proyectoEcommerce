from django.urls import path
from orders.views import CityListView


urlpatterns = [
    path("listView/", CityListView.as_view(), name="listView"),
]