from django.urls import path

import docs.views
from docs.views import ItemGetView, ItemPostView, ItemDeleteView

app_name = 'docs'
urlpatterns = [
	path('imports', ItemPostView.as_view()),
	path('delete/<pk>', ItemDeleteView.as_view()),
	path('nodes/<pk>', ItemGetView.as_view())
]
