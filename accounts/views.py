from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.db import IntegrityError

User = get_user_model()


# =========================
# Register View
# =========================
@csrf_protect
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        phone = request.POST.get("phone", "").strip()
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # =========================
        # Validation
        # =========================
        if not all([username, phone, password1, password2]):
            messages.error(request, "جميع الحقول مطلوبة")
            return redirect("accounts:register")

        if password1 != password2:
            messages.error(request, "كلمتا المرور غير متطابقتين")
            return redirect("accounts:register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم موجود مسبقًا")
            return redirect("accounts:register")

        if User.objects.filter(phone=phone).exists():
            messages.error(request, "رقم الجوال مستخدم مسبقًا")
            return redirect("accounts:register")

        # =========================
        # Create User
        # =========================
        try:
            User.objects.create_user(
                username=username,
                phone=phone,
                password=password1,
                is_customer=True
            )
        except IntegrityError:
            # حماية إضافية (Race Condition)
            messages.error(request, "حدث خطأ غير متوقع، حاول مرة أخرى")
            return redirect("accounts:register")

        messages.success(request, "تم إنشاء الحساب بنجاح، يمكنك تسجيل الدخول الآن")
        return redirect("accounts:login")

    return render(request, "accounts-1/register.html")


# =========================
# Login View
# =========================
@csrf_protect
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password")

        if not username or not password:
            messages.error(request, "يرجى إدخال اسم المستخدم وكلمة المرور")
            return redirect("accounts:login")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "تم تسجيل الدخول بنجاح")
            return redirect("home")

        messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيحة")
        return redirect("accounts:login")

    return render(request, "accounts-1/login.html")


# =========================
# Logout View
# =========================
def logout_view(request):
    logout(request)
    messages.success(request, "تم تسجيل الخروج بنجاح")
    return redirect("accounts:login")
