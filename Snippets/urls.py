from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='main'),
    path('snippets/add', views.add_snippet_page, name='snippet_add'),
    path('snippets/<int:item_id>/', views.render_snippet_page, name='snippet'),
    path('snippets/<int:item_id>/edit/', views.snippet_edit, name='snippet_edit'),
    path('snippets/<int:item_id>/delete/', views.snippet_delete, name='snippet_delete'),
    path('snippets/list', views.render_snippet_list, name='snippet_list'),
    path('snippets/user/<int:user_id>/snippets', views.render_my_snippets, name='my_snippets'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.create_user, name='create_user')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
