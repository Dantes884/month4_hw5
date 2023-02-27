from django.urls import path
from . import views


urlpatterns = [
    path('book/', views.BookView.as_view(), name='book'),
    path('book/<int:id>/', views.BookFullView.as_view(), name='details'),
    path('book/<int:id>/change/', views.BookUpdateView.as_view(), name='update'),
    path('book/<int:id>/delete/', views.BookDeleteView.as_view(), name='delete'),
    path('add-book/', views.BookCreateView.as_view(), name='create'),
    path('add-comment/', views.CreateCommentView.as_view(), name='comment'),
]
