from django.shortcuts import render
from django.contrib import auth

# Create your views here.
def courses(request):
    return render(request, "courses.html", locals());

def index(request):
    return render(request, "index.html", locals());

def login(request):
    if request.method == "POST":
        username = request.POST["username"];
        password = request.POST["password"];
        user = auth.authenticate(username = username, password = password);
        if user is not None:
            if user.is_active:
                auth.login(request, user);
                return render(request, "index.html", locals());
                message = "登入成功";
            else:
                message = "帳號尚未啟用！";
        else:
            message = "登入失敗！";
    return render(request, "login.html", locals());

def logout(request):
    auth.logout(request)
    return render(request, "index.html", locals());
