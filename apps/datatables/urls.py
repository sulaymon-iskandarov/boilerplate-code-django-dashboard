from django.urls import re_path
from apps.datatables.views import TransactionView

urlpatterns = [

    re_path(r'^transactions/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', TransactionView.as_view(),
            name='transactions'),
]