from rest_framework.routers import DefaultRouter

from django.urls import path, include
from api.views import student_function_base_view, employee_function_base_view, student_class_base_view, employee_class_base_view, mixins_employee, mixins_students, generic_employee
from api.views import employee_viewset, student_viewset

router = DefaultRouter()
router.register('viewsets-employees', employee_viewset.Employees, basename='viewsets-employees')
router.register('model-viewsets-employees', employee_viewset.EmployeeModelViewSet)
router.register('viewsets-students', student_viewset.Students, basename='viewsets-students')
router.register('model-viewsets-students', student_viewset.StudentModelViewSet)

urlpatterns = [
    path('fbv-students/', student_function_base_view.studentView),
    # path(', student_viewsetfbv-students/<int:pk>', function_base_view.student_detail),
    path('fbv-student/<int:student_id>', student_function_base_view.student),

    path('fbv-employees/', employee_function_base_view.EmployeeView),
    path('fbv-employee/<int:emp_id>', employee_function_base_view.employee),

    path('cbv-students/', student_class_base_view.Students.as_view()),
    path('cbv-student/<int:pk>', student_class_base_view.StudentDetail.as_view()),

    path('cbv-employees/', employee_class_base_view.Employees.as_view()),
    path('cbv-employee/<int:pk>', employee_class_base_view.EmployeeDetail.as_view()),

    path('mixins-employees/', mixins_employee.Employees.as_view()),
    path('mixins-employee-detail/<int:pk>/', mixins_employee.EmployeeDetail.as_view()),

    path('mixins-students/', mixins_students.Students.as_view()),
    path('mixins-student-detail/<int:pk>/', mixins_students.StudentDetail.as_view()),

    path('generic-employees/', generic_employee.Employees.as_view()),
    path('generic-employee-detail/<int:pk>/', generic_employee.EmployeeDetail.as_view()),

    path ('', include(router.urls))
]