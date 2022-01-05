from django.urls import path, include
# try:
#     from django.conf.urls import url, patterns
# except ImportError:
#     from django.conf.urls.defaults import url, patterns

"""URLs differ from standart evercookie_<storage_method> to dodge easyprivacy blocking rules"""
from .views import *

urlpatterns = [
    path('ecache',  evercookie_cache, name='ecache'),
    path('epng',    evercookie_png, name='epng'),
    path('ecetag',  evercookie_etag, name='ecetag'),
    path('ecookie', evercookie_core, name='ecookie'),
    path('ecauth',  evercookie_auth, name='ecauth'), 
    ]
