from django.urls import path
from api.views import student_function_base_view, employee_function_base_view, student_class_base_view


urlpatterns = [
    path('fbv-students/', student_function_base_view.studentView),
    # path('fbv-students/<int:pk>', function_base_view.student_detail),
    path('fbv-student/<int:student_id>', student_function_base_view.student),

    path('fbv-employees/', employee_function_base_view.EmployeeView),
    path('fbv-employee/<int:emp_id>', employee_function_base_view.employee),

    path('cbv-students/', student_class_base_view.Students.as_view()),
     path('cbv-student/<int:pk>', student_class_base_view.StudentDetail.as_view()),
]