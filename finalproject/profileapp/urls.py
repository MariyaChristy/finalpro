from django.urls import path
from profileapp import views
app_name='profile_app'

urlpatterns=[
     path('profile',views.profile,name='profile'),
     path('edit_profile/<int:id>/',views.edit_profile,name='edit_profile'),
]