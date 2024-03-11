from django.urls import path
from MovieApp import views
app_name='Movie_App'
urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('categories/',views.category_detail,name='category_list'),
    path('category/<int:category_id>/',views.detail_category,name='detail_category'),
    path('add_comment/<int:movie_id>',views.add_comment,name='add_comment'),
    path('delete_comment/<int:comment_id>/',views.delete_comment,name='delete_comment'),
    path('favorite_move/<int:movie_id>/',views.favourite_move,name='favorite_move'),
    path('remove_favourite/<int:favourite_id>/',views.remove_favourite,name='remove_favourite'),
    path('favourite_list',views.favourite_list,name='favourite_list')
]
