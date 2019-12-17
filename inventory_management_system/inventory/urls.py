from django.conf.urls import url
from .views import * 

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^dbms', display_DBMS, name="dbms"),
    url(r'^daa$', display_DAA, name="daa"),
    url(r'^ds$', display_DS, name="ds"),

    url(r'^add_dbms$', add_DBMS, name="add_dbms"),
    url(r'^add_daa$', add_DAA, name="add_daa"),
    url(r'^add_ds$', add_DS, name="add_ds"),

    url(r'^dbms/edit_item/(?P<pk>\d+)$', edit_dbms, name="edit_dbms"),
    url(r'^daa/edit_item/(?P<pk>\d+)$', edit_daa, name="edit_daa"),
    url(r'^ds/edit_item/(?P<pk>\d+)$', edit_ds, name="edit_ds"),

    url(r'^dbms/delete/(?P<pk>\d+)$', delete_dbms, name="delete_dbms"),
    url(r'^daa/delete/(?P<pk>\d+)$', delete_daa, name="delete_daa"),
    url(r'^ds/delete/(?P<pk>\d+)$', delete_ds, name="delete_ds")

]
