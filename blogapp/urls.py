from django.urls import path
from .views import(
    index,
    upload,
    update_post,
    delete_post,
    post_list,
    post_detail
)


urlpatterns = [
    path('', index),
    path('list/upload/', upload),
    path('update/<int:id>/',update_post),
    path('delete/<int:id>/',delete_post),
    path('list/',post_list),
    path('list/detail/<int:id>',post_detail)
]
