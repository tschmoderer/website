from django.urls import path
from . import views 

app_name = 'blog'

urlpatterns = [
	path('', views.ListArticles.as_view(), name='home'),
	path('article/<int:pk>', views.ReadArticle.as_view(), name='read_article'), 
	path('article/<int:pk>/edit', views.edit_article, name='edit'),
	path('add/', views.add_article, name='add'),
	path('delete/<int:pk>', views.delete_article, name='delete_article'),
]