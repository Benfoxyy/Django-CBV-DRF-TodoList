from django.urls import path,include
from . import views

app_name = 'accounts'
urlpatterns = [
     path('sign_up/',views.Sign_Up.as_view(),name='sign_up'),
     path('api/v1/',include('accounts.api.v1.urls'))
]
 