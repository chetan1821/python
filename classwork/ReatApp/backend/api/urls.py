from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TeacherViewSet, CourseViewSet, StudentViewSet, 
    AttendanceViewSet, ExamViewSet, ResultViewSet, NoticeViewSet, InstallmentViewSet, UserViewSet, DashboardStatsViewSet
)

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'results', ResultViewSet)
router.register(r'notices', NoticeViewSet)
router.register(r'installments', InstallmentViewSet)
router.register(r'users', UserViewSet)
router.register(r'dashboard-stats', DashboardStatsViewSet, basename='dashboard-stats')

urlpatterns = [
    path('', include(router.urls)),
]
