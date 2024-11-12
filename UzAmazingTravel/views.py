from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .forms import ContactForm
from .models import Carusel, Provinces


def home(req):
    carusel = Carusel.objects.all()[:12]
    # print(carusel)
    context = {"carusel": carusel}
    return render(req, 'pages/index.html', context)


def about(req):
    context = {}
    return render(req, 'pages/about.html', context)


def sign(req):
    context = {}
    return render(req, 'pages/sign.html', context)


def team(req):
    context = {}
    return render(req, 'pages/team.html', context)


def testimonials(req):
    context = {}
    return render(req, 'pages/testimonials.html', context)


def services(req):
    context = {}
    return render(req, 'pages/services.html', context)


def portfolio(req):
    context = {}
    return render(req, 'pages/portfolio.html', context)


def pricing(req):
    context = {}
    return render(req, 'pages/pricing.html', context)


def contact(req):
    context = {}
    return render(req, 'pages/contact.html', context)


def custom_404_view(request, exception):
    # product_footer = ServiceModel.objects.all()[:6]
    context = {}
    return render(request, 'pages/404.html', context, status=404)


class Contact_Page_View(TemplateView):
    template_name = "pages/contact.html"

    def get(self, requests, *args, **kwargs):
        form = ContactForm()
        context = {
            "form": form
        }
        return render(requests, "pages/contact.html", context)

    def post(self, requests, *args, **kwargs):
        form = ContactForm(requests.POST)
        if requests.method == "POST" and form.is_valid():
            form.save()
            context = {
                "status_code": 200,
                "message": "Your message has been sent successfully!"
            }
            return render(requests, "pages/contact.html", context, status=200)

        # Form is invalid
        context = {
            "status_code": 400,
            "error": "Please fill out all fields correctly!"
        }
        return render(requests, "pages/contact.html", context, status=400)

    def delete(self, requests, *args, **kwargs):
        if requests.method == "DELETE":
            return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

    def put(self, requests, *args, **kwargs):
        if requests.method == "PUT":
            return JsonResponse({'error': 'Only POST method is allowed'}, status=405)


class Info_Page_View(TemplateView):
    template_name = "pages/provinces.html"

    def get(self, request, *args, **kwargs):
        cl_id = self.kwargs.get('slug')
        carusel = get_object_or_404(Carusel, cl_id=cl_id)
        provinces = get_object_or_404(Provinces, u_id=carusel.provinces.u_id)
        context = {"carusel": carusel, "provinces": provinces}
        return render(request, "pages/provinces.html", context)


class TestPage(TemplateView):
    template_name = "pages/test.html"

    def get(self, request, *args, **kwargs):
        # slug1 = "70b16f33-a68b-4256-a896-59da8b1e5015"
        # carusel = get_object_or_404(Carusel, cl_id=slug1)
        # carusel = get_object_or_404(Carusel, cl_id=carusel.provinces.u_id)
        # context = {"carusel": carusel}
        return render(request, "pages/test.html", {})


def test1(req):
    slug1 = "70b16f33-a68b-4256-a896-59da8b1e5015"
    carusel = get_object_or_404(Carusel, cl_id=slug1)
    provinces = get_object_or_404(Provinces, u_id=carusel.provinces.u_id)
    print(carusel)
    context = {"carusel": carusel}
    return render(req, 'pages/test.html', context)
