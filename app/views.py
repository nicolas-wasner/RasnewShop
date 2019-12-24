from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView, FormView

from app.forms.register import FormRegister
from app.models import Example, SignUpForm, Personne


class IndexView(TemplateView):
    template_name = 'index.html'
    model = Example

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'Titre page'
        result['Example'] = Example.objects.all()  # all() = "SELECT * FROM Cocktail"

        # result['ingredient'] = CocktailIngredientUnit.objects.all()

        return result


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = FormRegister

    def form_valid(self, form):
        email = form.cleaned_data['username']
        password_1 = form.cleaned_data['password_1']
        password_2 = form.cleaned_data['password_2']
        user = User.objects.create_user(email=email,
                                 password=password_1)
        # raise ValidationError() "Leve une erreur de validation / Mais pas conseillé"
        person = Personne.object.create(user=user)
        person.save
        return super().form_valid(form)