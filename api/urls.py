from django.urls import path


from .views import ListCategory, DetailCategory
from .views import ListPost, DetailPost

urlpatterns = [
    path("category/", ListCategory.as_view()),
    path("category/<int:pk>/", DetailCategory.as_view()),
    path("post/", ListPost.as_view()),
    path("post/<int:pk>/", DetailPost.as_view())
]