from django.shortcuts import render, get_object_or_404
from . models import Article


# Create your views here.

def main(request):
	return render(request, 'blog/main.html')

def article_list(request):
	articles = Article.objects.all()
	context = {'articles': articles}
	return render(request, 'blog/article_list.html', context)

def article_detail(request, article_id):
	article = get_object_or_404(Article, id=article_id)
	context = {'article': article}
	return render(request, 'blog/article_detail.html', context)