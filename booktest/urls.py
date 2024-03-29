from django.urls import path, register_converter,re_path

from . import views, converters

app_name = 'booktest'
register_converter(converters.FourDigitYearConverter, 'year')
urlpatterns = [
    path('', views.index, name='index'),
    path('<year:year>', views.year),
    path('<int:id>', views.show),
    # path('getTest1', views.getTest1),
    path('postTest2/',views.post),
    path('postTest1/',views.post2),
    path('login/',views.session1),
    path('session2/',views.session2),
    path('session3/',views.session3),
    # path('index2/',views.indexjicheng),
    # path()
    # re_path(),

    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),

]
