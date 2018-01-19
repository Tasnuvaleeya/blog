from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post
from django.db.models import Q


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    paginate_by = 10
    queryset = Post.objects.all()

    def get_queryset(self, *args,**kwargs):
        qs = Post.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(body__icontains=query) |
                Q(short_description__icontains=query)
            )
        return qs


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.all()

# def about(request):
#     return render(request, 'blog/about.html')
class AboutView(TemplateView):
    template_name = 'blog/about.html'

class SamplePostView(TemplateView):
    template_name = 'blog/sample_post_view.html'

class ContactView(TemplateView):
    template_name = 'blog/contact_view.html'
