# Copyright: (c) OpenSpug Organization. https://github.com/openspug/spug
# Copyright: (c) <spug.dev@gmail.com>
# Released under the AGPL-3.0 License.
from django.conf.urls import url

from apps.exec.views import *
from apps.exec.transfer import TransferView

urlpatterns = [
    url(r'template/$', TemplateView.as_view()),
    url(r'history/$', get_histories),
    url(r'do/$', do_task),
    url(r'transfer/$', TransferView.as_view()),
]
