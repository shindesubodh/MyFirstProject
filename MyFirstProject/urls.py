
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls')),    # this command ensures that all the urls mentioned in the urls.py
                                    # file of our app crm can be referred

]
