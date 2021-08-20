from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import PerfilUsuario
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.urls.base import reverse_lazy
from .forms import UserCreationFormWithEmail
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect


class createUserView(generic.CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/sign-up.html'

    def get_success_url(self):
        return reverse_lazy('user:login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('user:profile')

        return super().dispatch(request, *args, **kwargs)
    

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(LoginRequiredMixin, generic.TemplateView):
    success_url = reverse_lazy('user:profile')
    template_name = 'registration/profile_form.html'






       



