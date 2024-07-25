from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='main'),
    path('snippets/add', views.add_snippet_page, name='snippet_add'),
    path('snippets/<int:item_id>/', views.render_snippet_page, name='snippet'),
    path('snippets/edit/<int:item_id>/', views.snippet_edit, name='snippet_edit'),
    path('snippets/delete/<int:item_id>/', views.snippet_delete, name='snippet_delete'),
    path('snippets/list', views.render_snippet_list, name='snippet_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
