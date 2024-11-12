from django.urls import path

from .views import Contact_Page_View, Info_Page_View, TestPage, test1
from .views import home, custom_404_view, about, sign, team, testimonials, services, portfolio, pricing

handler404 = custom_404_view
urlpatterns = [
    path('', home, name="home_page"),
    path('about/', about, name="about"),
    path('sign/', sign, name="sign"),
    path('team/', team, name="team"),
    path('testimonials/', testimonials, name="testimonials"),
    path('services/', services, name="services"),
    path('portfolio/', portfolio, name="portfolio"),
    path('pricing/', pricing, name="pricing"),
    path('contact/', Contact_Page_View.as_view(), name="contact"),
    path('info/<slug:slug>/', Info_Page_View.as_view(), name="info"),
    path('test/', TestPage.as_view(), name="test"),
    path('test1/', test1, name="test1"),
]
