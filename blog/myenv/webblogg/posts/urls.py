from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/<slug:slug>/', views.detail_view, name='detail_page'),
    path('publish-secret-99/',views.add_article, name='add_article'),
    path('article/edit/<int:id>/', views.edit_article, name='edit_article'),
    path('article/delete/<int:id>/', views.delete_article, name='delete_article')
]
# urlpatterns = [
#     path('', views.article_list, name='article_list'),
#     path('article/<int:id>/', views.detail_view, name='detail_page'),
#     path('publish-secret-99/',views.add_article, name='add_article'),
#     path('article/edit/<int:id>/', views.edit_article, name='edit_article'),
#     path('article/delete/<int:id>/', views.delete_article, name='delete_article')
# ]
