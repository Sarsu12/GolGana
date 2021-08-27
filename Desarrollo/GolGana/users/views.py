from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls.base import reverse_lazy, reverse
from .forms import LoginCaptcha, UserCreationFormWithEmail
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

UserModel = get_user_model()
#Funcion vista de activacion de cuenta
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        # Redirect user to login
        messages.success(request, 'Email confirmado correctamente, ahora puedes ingresar.')
        return HttpResponseRedirect(reverse('user:login'))
    else:
        return HttpResponse('Activation link is invalid!')


class createUserView(generic.CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/sign-up.html'
    

    def get_success_url(self):
        return reverse_lazy('user:login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated: return redirect('user:profile')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Gguarda el usurio en la base de datos pero con is_active = False
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        # Send confirmation email
        current_site = get_current_site(self.request)
        subject = 'Activate Your ' + current_site.domain + ' Account'
        message = render_to_string('registration/email_confirmation.html',
        {
        "domain": current_site.domain,
        "user": user,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": default_token_generator.make_token(user),},
        )
        to_email = form.cleaned_data.get('email')
        send_mail(subject, message, 'golganaco@gmail.com', [to_email])

        return HttpResponseRedirect(reverse('user:login'))    

class CLoginView(LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True
    authentication_form = LoginCaptcha
    
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(LoginRequiredMixin, generic.TemplateView):
    success_url = reverse_lazy('user:profile')
    template_name = 'registration/profile_form.html'






       



