import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/';

const api = axios.create({
  baseURL: API_URL,
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const getStudents = (params = {}) => api.get('students/', { params });
export const addStudent = (data) => api.post('students/', data);
export const updateStudent = (id, data) => api.patch(`students/${id}/`, data);
export const deleteStudent = (id) => api.delete(`students/${id}/`);
export const getTeachers = () => api.get('teachers/');
export const addTeacher = (data) => api.post('teachers/', data);
export const updateTeacher = (id, data) => api.patch(`teachers/${id}/`, data);
export const deleteTeacher = (id) => api.delete(`teachers/${id}/`);
export const getCourses = () => api.get('courses/');
export const addCourse = (data) => api.post('courses/', data);
export const updateCourse = (id, data) => api.put(`courses/${id}/`, data);
export const deleteCourse = (id) => api.delete(`courses/${id}/`);
export const getNotices = () => api.get('notices/');
export const addNotice = (data) => api.post('notices/', data);
export const updateNotice = (id, data) => api.put(`notices/${id}/`, data);
export const deleteNotice = (id) => api.delete(`notices/${id}/`);
export const addInstallment = (data) => api.post('installments/', data);
export const getStudentInstallments = (studentId) => api.get(`installments/?student=${studentId}`);
export const markAttendance = (data) => api.post('attendance/bulk_mark/', data);
export const getStudentAttendanceStats = (studentId) => api.get(`attendance/student_stats/?student_id=${studentId}`);
export const getExams = () => api.get('exams/');
export const addExam = (data) => api.post('exams/', data);
export const updateExam = (id, data) => api.put(`exams/${id}/`, data);
export const deleteExam = (id) => api.delete(`exams/${id}/`);
export const getResults = () => api.get('results/');
export const getAttendance = () => api.get('attendance/');
export const changePassword = (data) => api.post('users/change_password/', data);
export const getDashboardStats = () => api.get('dashboard-stats/');

export default api;
