from django.urls import path

from . import views


app_name = 'post'
urlpatterns = [
    path('',views.index,name='index'),
    path('tags/<slug:tag_slug>/',views.tagIndex, name='index_tag'),
    path('create/',views.create,name='create'),
    path('<int:post_id>/', views.detail,name='detail'),
    path('edit/<int:post_id>/',views.edit, name= 'edit'),
    path('edit/tags/',views.editTags,name='edit_tag'),
    path('delete/<int:pk>/',views.PostDelete.as_view(),name='delete'),
]
