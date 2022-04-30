from django.shortcuts import render
from django.conf import settings # 추천!
from django.http import HttpResponse
from user.models import Member

def hello(request):
    context = {}    
    login_session = request.session.get('login_session', '')
    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] = True
        # username 가져오기
        context['username'] = Member.objects.get(user_id = login_session)

    return render(request, 'home/base.html', context)