from django.urls import path
from . import views

urlpatterns = [
    path("question/",views.question,name="que"),
    path("askquestion/",views.askquestion,name="ask_que"),
    path("description_que/id=<int:id>/",views.que_desc,name="que_desc"),
    path("contact/",views.contact,name="contact"),
    path("about/",views.about,name="about"),
    path("teams/",views.teams,name="teams"),
    path("product/",views.product,name="product"),
    path("giveans/",views.give_ans,name="ans"),
    path("search/",views.search,name="search"),
    path("deleteanswer/",views.delete_ans,name="dlans"),
    path("deletequestion/",views.delete_que,name="dlque"),
    path("likequestion/",views.likes_ques,name="lkque"),
    path("dislikequestion/",views.dislikes_ques,name="dlkque"),
    path("tag/<str:tag>/",views.tagrelated,name="tagr"),
    path('*',views.page404,name="page404")
]
