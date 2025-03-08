from django.shortcuts import render
from django.views.generic import ListView,FormView,UpdateView,DeleteView,DetailView
from .models import Post
from django.urls import reverse_lazy
from .forms import CreatePostViewForm,ModifyPostViewForm

# Create your views here.

class PostView(ListView):
    template_name = "posts/index.html"
    model = Post
    context_object_name = "all_posts"

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post_detail"

class CreatePostView(FormView):
    template_name ='posts/create_post.html'
    form_class = CreatePostViewForm
    success_url = reverse_lazy('post')
    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        Post.objects.create(
            title=cleaned_data["title"],
            content = cleaned_data["content"],
        )
        return super().form_valid(form)


class ModifyPostView(UpdateView):
    form_class = ModifyPostViewForm
    template_name = "posts/modify_post.html"
    model = Post
    success_url = reverse_lazy("post")


class DeletePostView(DeleteView):
    template_name = 'posts/delete_post.html'
    model = Post
    success_url = reverse_lazy("post")


class ComentPostView(FormView):
    template_name ='posts/create_coment.html'
    form_class = CreatePostViewForm
    success_url = reverse_lazy('post')
    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        Post.objects.create(
            content=cleaned_data["content"],
        )
        return super().form_valid(form)