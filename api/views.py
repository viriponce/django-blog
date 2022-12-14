from django.views.generic.edit import ( 
    CreateView, 
    UpdateView, 
    DeleteView )

from .models import Article
from .forms import ArticleForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = '/api/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    success_url = '/api/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ArticleUpdateView, self).form_valid(form)

class ArticleDeleteView(DeleteView):
    model = Article
    form_class = ArticleForm
    success_url = '/api/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ArticleDeleteView, self).form_valid(form)

class ArticleView(ListView):
    model = Article
    template_name = 'api/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(author=self.request.user)
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'api/post.html'