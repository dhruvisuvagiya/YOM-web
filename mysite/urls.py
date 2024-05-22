"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from layout.views import index
from layout.views import index_2
from layout.views import services
from layout.views import clients
from layout.views import blog
from layout.views import blog_grid
from layout.views import blog_single
from layout.views import about
from layout.views import work_3columns
from layout.views import work_4columns
from layout.views import single_project
from layout.views import contact
from layout.views import data_contact
from layout.views import edit_contact
from layout.views import delete_contact
from layout.views import index1
from layout.views import login
from layout.views import register
from layout.views import forgot_password
from layout.views import recover_password
from layout.views import general
from layout.views import data_slider
from layout.views import edit_slider
from layout.views import delete_slider
from layout.views import offer_form
from layout.views import data_offer
from layout.views import edit_offer
from layout.views import delete_offer
from layout.views import photos_form
from layout.views import data_photos
from layout.views import edit_photos
from layout.views import delete_photos
from layout.views import post_form
from layout.views import data_post
from layout.views import edit_post
from layout.views import delete_post
from layout.views import category_form
from layout.views import data_category
from layout.views import edit_category
from layout.views import delete_category
from layout.views import work_form
from layout.views import data_work
from layout.views import edit_work
from layout.views import delete_work
from layout.views import getuserdata
from layout.views import getsliderdata
from layout.views import getofferdata
from layout.views import getphotosdata
from layout.views import getpostdata
from layout.views import getcontactdata
from layout.views import getcategorydata
from layout.views import getworkdata
from layout.views import sendmaildata
from layout.views import mailpass,ajaxdata,get_data

urlpatterns = [
    path('', index),
    path('index-2/', index_2),
    path('services/', services),
    path('clients/', clients),
    path('blog/', blog),
    path('blog-grid/', blog_grid),
    path('blog-single/<int:id>', blog_single),
    path('about/', about),
    path('work-3columns/<id>', work_3columns),
    path('work-4columns/', work_4columns),
    path('single-project/', single_project),
    path('contact/', contact),
    path('data_contact/', data_contact),
    path('edit_contact/<int:id>', edit_contact),
    path('delete_contact/<int:id>', delete_contact),
    path('index1/', index1),
    path('login/', login),
    path('register/', register),
    path('forgot-password/', forgot_password),
    path('recover-password/<int:id>', recover_password),
    path('general/', general),
    path('data_slider/', data_slider),
    path('edit_slider/<int:id>', edit_slider),
    path('delete_slider/<int:id>', delete_slider),
    path('offer/', offer_form),
    path('data_offer/', data_offer),
    path('edit_offer/<int:id>', edit_offer),
    path('delete_offer/<int:id>', delete_offer),
    path('photos/', photos_form),
    path('data_photos/', data_photos),
    path('edit_photos/<int:id>', edit_photos),
    path('delete_photos/<int:id>', delete_photos),
    path('post/', post_form),
    path('data_post/', data_post),
    path('edit_post/<int:id>', edit_post),
    path('delete_post/<int:id>', delete_post),
    path('category/', category_form),
    path('data_category/', data_category),
    path('edit_category/<int:id>', edit_category),
    path('delete_category/<int:id>', delete_category),
    path('work/', work_form),
    path('data_work/', data_work),
    path('edit_work/<int:id>', edit_work),
    path('delete_work/<int:id>', delete_work),
    path('sendmail/', sendmaildata),
    path('admin/', admin.site.urls),
    path('userdata/', getuserdata),
    path('sliderdata/', getsliderdata),
    path('offerdata/', getofferdata),
    path('photosdata/', getphotosdata),
    path('postdata/', getpostdata),
    path('contactdata/', getcontactdata),
    path('categorydata/', getcategorydata),
    path('workdata/', getworkdata),
    path('mail/', mailpass),
    path('adata/', ajaxdata),
    path('gdata/', get_data),
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)