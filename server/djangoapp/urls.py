from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # path for about view

    # path for contact us view

    # path for registration

    # path for login

    # path for logout

    path(route='', view=views.get_dealershipsview, name='index'),
    path(route='static',view=views.staticview,name='static'),
    path(route='about',view=views.aboutview,name='about'),
    path(route='contact',view=views.contactview,name='contact'),
    path(route='login_page',view=views.login_requestview,name='login_page'),
    path(route='loggedin',view=views.logged_inview,name='loggedin'),
    path(route='logoutpage',view=views.logoutview,name='logoutpage'),
    path(route='registration',view=views.registrationview,name='registration'),
    path(route='registered',view=views.registeredview,name='registered'),
    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)