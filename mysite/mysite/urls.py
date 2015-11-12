from django.conf.urls import patterns, include, url
from books.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    ('^home/$', Home),
    ('^addauthorpage/$', AddAuthorpage),
    ('^addauthor/$', AddAuthor),
    ('^addbookpage/$', AddBookpage),
    ('^addbook/$', AddBook),
    ('^searchauthor/$', SearchAuthor),
    ('^searchbook/$', SearchBook),
    ('^delete/$', Delete),
    ('^information/$', Information),
)
