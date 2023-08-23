from django.urls import path

from .views import CategoryList, CategoryCreate, CategoryUpdate, CategoryDelete


urlpatterns = [
    path('', CategoryList.as_view(), name='category_list'),
    path('<pk>/update', CategoryUpdate.as_view(), name='category_update'),
    path('<pk>/delete', CategoryDelete.as_view(), name='category_delete'),
    path('create', CategoryCreate.as_view(), name='category_create'),
]