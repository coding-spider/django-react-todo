from django.conf.urls import url
from rest_framework.authtoken import views as drf_views
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import TodoListView, TodoListItemView

app_name = 'api'

urlpatterns = [
    url(r'^todoLists/$', TodoListView.as_view()),
    url(r'^todoListItems/$', TodoListItemView.as_view()),
    url(r'^auth$', drf_views.obtain_auth_token, name='auth'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
