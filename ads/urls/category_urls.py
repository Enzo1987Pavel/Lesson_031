from django.urls import path

from ads.views import CategoryView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path("", CategoryView.as_view(), name="category"),
    path("<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),
    path("create/", CategoryCreateView.as_view(), name="create_category"),
    path("update/<int:pk>/", CategoryUpdateView.as_view(), name="update_category"),
    path("delete/<int:pk>/", CategoryDeleteView.as_view(), name="delete_category"),
]
