from django.urls import path

from .views import ExamDetailView
from .views import ExamListView
# from .views import ExamResultCreateView
# from .views import ExamResultQuestionView
# from .views import ExamResultDetailView
# from .views import ExamResultUpdateView
# from .views import ExamResultDeleteView

app_name = 'quizzes'

urlpatterns = [
    path('', ExamListView.as_view(), name='list'),
    path('<uuid:uuid>/', ExamDetailView.as_view(), name='details'),
    # path('<uuid:uuid>/results/create/', ExamResultCreateView.as_view(), name='result_create'),
    # path('<uuid:uuid>/results/<uuid:result_uuid>/remove/', ExamResultDeleteView.as_view(), name='result_remove'),    # noqa
    # path('<uuid:uuid>/results/<uuid:result_uuid>/details/', ExamResultDetailView.as_view(), name='result_details'),    # noqa
    # path('<uuid:uuid>/results/<uuid:result_uuid>/update/', ExamResultUpdateView.as_view(), name='result_update'),    # noqa
    # path('<uuid:uuid>/results/<uuid:result_uuid>/questions/next/', ExamResultQuestionView.as_view(), name='question'),    # noqa
]
