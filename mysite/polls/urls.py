from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:number>/', views.problem_statement, name='problemStatement'),
    path('submissionset/<int:subID>/', views.veiw_submission , name='veiwSubmission'),
    path('submissionset/', views.submission_set, name='submissionSet'),
]