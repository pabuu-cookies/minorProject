from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from django.views.decorators.http import require_POST
from core.models import CustomUser, Admin, Student, Teacher

def login_view(request):
    return render(request, 'login/login.html')

def loginaction(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Attempting login with username: {email}, password: {password}")
        try:
            custom_user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            custom_user = None

        if custom_user is not None and custom_user.check_password(password):
            print(f"User {custom_user.email} authenticated successfully")
            print(f" usertype: {custom_user.usertype}")
            usertype = custom_user.usertype

            if usertype == 'student':
                student = Student.objects.get(user=custom_user)
                print(reverse('s_dashboard', kwargs={'user': student.id}))
                return redirect(reverse('s_dashboard', kwargs={'user': student.id}))
            elif usertype == 'teacher':
                teacher = Teacher.objects.get(user=custom_user)
                print(reverse('t_dashboard', kwargs={'user': teacher.id}))
                return redirect(reverse('t_dashboard', kwargs={'user': teacher.id}))
            elif usertype == 'admin':
                if Admin.objects.filter(user=custom_user).exists():
                    admin_instance = Admin.objects.get(user=custom_user)
                    if admin_instance.role == 'staff':
                        print("Redirecting to canteen")
                        print(reverse('s_canteen', kwargs={'user': admin_instance.id}))
                        return redirect(reverse('s_canteen', kwargs={'user': admin_instance.id}))
                    elif admin_instance.role == 'exam':
                        print("Redirecting to examsection")
                        print(reverse('examsection_view', kwargs={'user': admin_instance.id}))
                        return redirect(reverse('examsection_view', kwargs={'user': admin_instance.id}))

    else:
        print("Authentication failed")
        return render(request, 'login/login.html', {'error_message': 'Invalid login credentials. Please try again.'})

    print("outside the if..else statement in loginaction")
    raise Http404 ("user not found")