from random import randint

from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.forms import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView

from config import settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def get_success_url(self):
        return reverse('users:verify_email', args=[self.object.pk])

    def form_valid(self, form):
        self.object = form.save()
        if form.is_valid():
            verification_code = self.object.verification_code
            send_mail(
                    subject=f'Подтверждение регистрации',
                    message=f'Для подтверждения электронной почты введите следующий код на сайте:\n{verification_code}',
                    recipient_list=[self.object.email],
                    from_email=settings.EMAIL_HOST_USER,
                    fail_silently=False
                )
            print('EMAIL SENT')
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('catalog:index')

    def get_object(self, queryset=None):
        return self.request.user


def verify_email(request, pk):
    if request.method == 'POST':
        check_code = request.POST['check_code']
        user = User.objects.get(pk=pk)
        verification_code = user.verification_code
        if check_code == verification_code:
            user.is_active = True
            user.save()
            return redirect('catalog:index')
        else:
            context = {
                'error': 'Код некорректный'
            }
            return render(request, 'users/verify_email.html', context)
    return render(request, 'users/verify_email.html')


def reset_email(request):
    if request.method == 'POST':
        check_email = request.POST['check_email']
        user = User.objects.filter(email=check_email)
        if user:
            user = user[0]
            new_pass = User.objects.make_random_password()
            print(new_pass)
            user.set_password(new_pass)
            user.save()
            send_mail(
                    subject=f'Новый пароль',
                    message=f'Ваш новый пароль: {new_pass}',
                    recipient_list=[check_email],
                    from_email=settings.EMAIL_HOST_USER,
                    fail_silently=False
                )
            context = {
                'success': 'Новый пароль отправлен Вам на почту!'
            }
            return render(request, 'users/reset_email.html', context)
        else:
            context = {
                'error': 'Некорректный email'
            }
            return render(request, 'users/reset_email.html', context)
    return render(request, 'users/reset_email.html')
