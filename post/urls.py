from django.urls import path

from post.views import PostList, PostUpdate, PostDelete, PostCreate

urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("<pk>/update", PostUpdate.as_view(), name="post_update"),
    path("<pk>/delete", PostDelete.as_view(), name="post_delete"),
    path("create", PostCreate.as_view(), name="post_create")
]
