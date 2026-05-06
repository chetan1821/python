from rest_framework import permissions

class IsAdminOrTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and 
            (request.user.is_staff or request.user.is_superuser or hasattr(request.user, 'teacher_profile'))
        )

class IsAdminTeacherOrStudentReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
            
        # Admin, Superusers and Teachers have full access
        if request.user.is_staff or request.user.is_superuser or hasattr(request.user, 'teacher_profile'):
            return True
            
        # Students only have read access (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return hasattr(request.user, 'student_profile')
            
        return False
