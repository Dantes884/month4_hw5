from django.shortcuts import get_object_or_404
from . import models, forms
from django.views import generic


class BookView(generic.ListView):
    """
    Вывод неполной информации
    """
    template_name = 'book.html'
    queryset = models.Book.objects.all()

    def get_queryset(self):
        return models.Book.objects.all()


class BookFullView(generic.DetailView):
    """
    Вывод полной информации
    """
    template_name = 'book_full.html'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)


class BookCreateView(generic.CreateView):
    """
    Добавление книг в базу данных
    """
    template_name = 'add_book.html'
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = '/book/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form=form)


class BookUpdateView(generic.UpdateView):
    """
    Изменение данных о книге
    """
    template_name = 'update_book.html'
    form_class = forms.BookForm
    success_url = '/book/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookUpdateView, self).form_valid(form=form)


class BookDeleteView(generic.DeleteView):
    """
    Удаление книги
    """
    template_name = 'confirm_to_delete.html'
    success_url = '/book/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)


class CreateCommentView(generic.CreateView):
    """
    Добавление отзыва к книге
    """
    template_name = 'add_comment.html'
    form_class = forms.CommentForm
    queryset = models.RatingBook.objects.all()
    success_url = '/book/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateCommentView, self).form_valid(form=form)
