"""defines url patterns for learning_logs"""
from django.urls import path
from . import views
app_name='learning_logs'#distinguish this urls.py file from files of the same name in other apps within the prjt.
urlpatterns = [
    #This is a list of individual web pages that can be requested from learning_logs app.
    # home page
    path('',views.index, name='index'),#routes the request to a view at view.py
    #the first argument is a string that help django to route.
    #Django ignores the base URL for the project (http://localhost:8000/), so the empty string ('') matches the base URL
    #When a requested URL matches the pattern we’re defining, Django calls the index() function from views.py.
    #3rd argument shows the text above the weblink in the website.


    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #page for adding new topic
    path('new_topics/',views.new_topic,name="new_topic"),
    #page for adding new entry
    path("new_entry/<int:topic_id>/",views.new_entry,name="new_entry"),
    #page for editing an existing entry
    path("edit_entry/<int:entry_id>/",views.edit_entry,name="edit_entry")

]
