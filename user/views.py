from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from user.decorators import login_required
from django.shortcuts import render,redirect
from .models import Member
from .form import LoginForm, RegisterForm, CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
# Create your views here.

def register(request):
    register_form = RegisterForm()
    context = {'forms' : register_form}

    if request.method == 'GET':
        return render(request, 'user/register.html', context)
        
    elif request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = Member(
                user_id = register_form.user_id,
                user_pw = register_form.user_pw,
                user_name = register_form.user_name,
                user_email = register_form.user_email
            )
            user.save()
            return redirect('/home')
        else:
            context['forms'] = register_form
            if register_form.errors:
                for value in register_form.errors.values():
                    context['error'] = value
        return render(request, 'user/register.html', context)

def login(request):
    loginform = LoginForm()
    context = {'forms':loginform}

    if request.method == 'GET':
        return render(request, 'user/login.html', context)

    elif request.method == 'POST':
        loginform = LoginForm(request.POST)

        if loginform.is_valid():
            request.session['login_session'] = loginform.login_session
            request.session.set_expiry(0)
            return redirect('/')
            
        else:
            context['forms'] = loginform
            if loginform.errors:
                for value in loginform.errors.values():
                    context['error'] = value
        return render(request, 'user/login.html', context)

@login_required
def mypage(request):
    login_session = request.session.get('login_session','')
    context = { 'login_session' : login_session }

    member = Member.objects.get(user_id = login_session)
    context['member'] = member
    
    if context['login_session'] == True:
        # username 가져오기
        context['username'] = Member.objects.get(user_id = login_session)
    return render(request,'user/mypage.html', context)
        
def mypage_delete(request):
    login_session = request.session.get('login_session','')
    context = {'login_session' : login_session }

    member = Member.objects.get(user_id = login_session)
    member.delete()
    messages.warning(request, "회원탈퇴 완료.")
    request.session.flush()
    return redirect('/home')

def mypage_modify(request):
    login_session = request.session.get('login_session','')

    member = Member.objects.get(user_id = login_session)
    
    if request.method =='GET':
        return redirect('/')
    elif request.method == 'POST':
        login_form = LoginForm(request.POST)




@login_required

def password_edit_view(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }
    if request.method == 'POST':
        password_change_form = CustomPasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "비밀번호를 성공적으로 변경하였습니다.")
            return redirect('users:profile')
    else:
        # password_change_form = CustomPasswordChangeForm(request.user)
        context = {'password_change_form': CustomPasswordChangeForm(request.user)}
    return render(request, 'user/profile_password.html', context)



def logout(request):
    request.session.flush()
    return redirect('/')

