from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('stories/',views.storyform,name='storyform'),
    path('updatestories/<str:id>/',views.updatestory,name='updatestory'),
    path('deletestory/<str:id>',views.deletestory,name='deletestory'),
    path('userstory/<str:id>',views.userstory,name='userstory'),
    path('story/<str:id>',views.story,name="story")
]