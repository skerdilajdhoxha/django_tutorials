from django.shortcuts import render, get_object_or_404, redirect
from .models import Tutorial, Video, TutorialDetail, Category
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    instance4 = Category.objects.all()
    context = {"instance4": instance4}
    return render(request, "home.html", context)


def tutorial_list(request):
    queryset = Tutorial.objects.all()
    context = {"queryset": queryset}
    return render(request, "tutorial_list.html", context)


def tutorial_detail(request, slug=None):
    instance = get_object_or_404(Tutorial, slug=slug)
    context = {"instance": instance, "slug": slug}
    return render(request, "tutorial_detail.html", context)


def video_detail(request, pk=None, slug=None):
    instance2 = Video.objects.get(pk=pk)
    instance3 = Video.objects.all()
    context = {"instance2": instance2, "instance3": instance3}
    return render(request, "video_detail.html", context)


def about(request):
    return render(request, 'about.html', {})


def category_detail(request, slug=None):
    instance5 = get_object_or_404(Category, slug=slug)
    context = {"instance5": instance5, "slug": slug}
    return render(request, "category_detail.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        name = form.cleaned_data.get("name")
        message = form.cleaned_data.get("message")

        subject = 'DJANGO'
        from_email = settings.EMAIL_HOST_USER
        to_email = ['djangolalalalala@gmail.com']

        contact_message = "%s: %s via %s" % (name, message, email)
        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
        return redirect('contact')
    context = {'form': form}
    return render(request, 'contact.html', context)




