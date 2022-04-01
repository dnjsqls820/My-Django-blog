from django.shortcuts import render
from .models import Posting
from django.utils import timezone
# Create your views here.
# post_list라는 def 를 만들어 request을 넘겨받아 render메서드를 호출한다.
# def post_list는 호출하여 받은 return post/post_list.html 템플릿을 보여준다.
def post_list(request):
    posts = Posting.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post/post_list.html', {'posts':posts})
