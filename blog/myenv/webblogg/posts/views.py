from django.shortcuts import render, get_object_or_404
from .models import PostsArticle
# Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import ArticleForm

@login_required
def add_article(request):
    # EXTRA SECURITY: Check for your specific username
    if request.user.username != 'rahul_pal':
        raise PermissionDenied  # Shows a "403 Forbidden" error to anyone else
    
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    
    return render(request, 'add_article.html', {'form': form})


def article_list(request):
    articles = PostsArticle.objects.all().order_by('-published_date')
    return render(request, 'article-list.html', {'articles': articles})

# def article_detail(request, slug):
#     article = get_object_or_404(PostsArticle, slug=slug)
#     return render(request, "detail-page.html",{"article":article})

#working with id
# def detail_view(request, id):
#     article = get_object_or_404(PostsArticle, id=id)
#     return render(request, 'detail_page.html', {'article': article})
#slug
def detail_view(request, slug):
    article = get_object_or_404(PostsArticle, slug=slug)
    return render(request, 'detail_page.html', {'article': article})


# # EDIT ARTICLE
# @login_required
# def edit_article(request, id):
#     article = get_object_or_404(PostsArticle, id=id)
#     if request.method == "POST":
#         form = ArticleForm(request.POST, instance=article)
#         if form.is_valid():
#             form.save()
#             return redirect('detail_page', id=article.id)
#     else:
#         form = ArticleForm(instance=article)
#     return render(request, 'add_article.html', {'form': form, 'edit_mode': True})

#with slug 
@login_required
def edit_article(request, id):
    article = get_object_or_404(PostsArticle, id=id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('detail_page', slug=article.slug)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'add_article.html', {'form': form, 'edit_mode': True})

# DELETE ARTICLE
@login_required
def delete_article(request, id):
    article = get_object_or_404(PostsArticle, id=id)
    if request.method == "POST":
        article.delete()
        return redirect('article_list')
    return render(request, 'confirm_delete.html', {'article': article})