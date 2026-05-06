import React, { useState, useEffect } from 'react';
import { Plus, BookOpen, Clock, User, IndianRupee, Loader2, Star, CheckCircle2, Edit2, Trash2 } from 'lucide-react';
import Card from '../components/common/Card';
import Button from '../components/common/Button';
import Input from '../components/common/Input';
import Modal from '../components/common/Modal';
import { getCourses, getStudents, getTeachers, addCourse, updateCourse, deleteCourse } from '../data/api';
import { useAuth } from '../context/AuthContext';

const Courses = () => {
  const { user } = useAuth();
  const [courses, setCourses] = useState([]);
  const [teachers, setTeachers] = useState([]);
  const [studentData, setStudentData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [isStudent, setIsStudent] = useState(false);
  const isAdmin = user?.role === 'admin';
  
  // Modal states
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingCourse, setEditingCourse] = useState(null);
  const [formData, setFormData] = useState({
    name: '',
    teacher: '',
    duration: '',
    fees: ''
  });

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const [coursesRes, studentsRes, teachersRes] = await Promise.all([
        getCourses(),
        getStudents(),
        getTeachers()
      ]);
      setCourses(coursesRes.data);
      setTeachers(teachersRes.data);
      
      if (user?.role === 'student') {
        setIsStudent(true);
        const me = (studentsRes.data.results || studentsRes.data).find(s => s.email === user.email);
        setStudentData(me);
      }
    } catch (error) {
      console.error("Error fetching courses:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleAddClick = () => {
    setEditingCourse(null);
    setFormData({ name: '', teacher: '', duration: '', fees: '' });
    setIsModalOpen(true);
  };

  const handleEditClick = (course) => {
    setEditingCourse(course);
    setFormData({
      name: course.name,
      teacher: course.teacher,
      duration: course.duration,
      fees: course.fees
    });
    setIsModalOpen(true);
  };

  const handleDeleteClick = async (id) => {
    if (window.confirm('Are you sure you want to delete this course?')) {
      try {
        await deleteCourse(id);
        fetchData();
      } catch (error) {
        alert('Failed to delete course');
      }
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editingCourse) {
        await updateCourse(editingCourse.id, formData);
      } else {
        await addCourse(formData);
      }
      setIsModalOpen(false);
      fetchData();
    } catch (error) {
      alert('Failed to save course');
    }
  };

  if (loading) return <div className="h-[60vh] flex items-center justify-center"><Loader2 className="animate-spin text-indigo-600" /></div>;

  const myCourseId = studentData?.course;

  return (
    <div className="space-y-8">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold dark:text-white tracking-tight">
            {isStudent ? 'Academic Programs' : 'Course Management'}
          </h1>
          <p className="text-gray-500 mt-1">
            {isStudent ? 'Explore and manage your educational journey.' : 'Create and manage academic programs.'}
          </p>
        </div>
        {isAdmin && (
          <Button onClick={handleAddClick}>
            <Plus size={18} /> New Course
          </Button>
        )}
      </div>

      {isStudent && studentData && (
        <div className="space-y-6">
          <h2 className="text-xl font-bold dark:text-white flex items-center gap-2">
            <Star className="text-yellow-500" size={20} /> My Active Course
          </h2>
          <div className="grid grid-cols-1">
            {courses.filter(c => c.id === myCourseId).map(course => (
              <Card key={course.id} className="bg-premium-gradient border-none text-white overflow-hidden relative">
                <div className="absolute top-0 right-0 p-8 opacity-10">
                  <BookOpen size={160} />
                </div>
                <div className="relative z-10 flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
                  <div>
                    <span className="bg-white/20 text-white px-3 py-1 rounded-full text-[10px] font-bold uppercase tracking-widest mb-4 inline-block">
                      Currently Enrolled
                    </span>
                    <h3 className="text-3xl font-black mb-2">{course.name}</h3>
                    <div className="flex flex-wrap gap-6 mt-4">
                      <div className="flex items-center gap-2 text-indigo-100">
                        <User size={18} />
                        <span className="font-medium">Instructor: <b>{course.teacher_name}</b></span>
                      </div>
                      <div className="flex items-center gap-2 text-indigo-100">
                        <Clock size={18} />
                        <span className="font-medium">Duration: <b>{course.duration}</b></span>
                      </div>
                    </div>
                  </div>
                  <Button className="bg-white text-indigo-600 hover:bg-indigo-50 border-none px-8 py-4 text-lg font-bold">
                    View Course Portal
                  </Button>
                </div>
              </Card>
            ))}
          </div>
          
          <h2 className="text-xl font-bold dark:text-white pt-6">Other Available Courses</h2>
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
        {courses.filter(c => c.id !== myCourseId).map((course, index) => (
          <Card key={course.id} delay={index * 0.1} className="hover:shadow-indigo-500/10 transition-shadow group">
            <div className="flex justify-between items-start mb-4">
              <div className="p-3 rounded-xl bg-indigo-50 dark:bg-indigo-900/20 text-indigo-600 dark:text-indigo-400 group-hover:scale-110 transition-transform">
                <BookOpen size={24} />
              </div>
              <span className="bg-green-100 text-green-700 dark:bg-green-900/20 dark:text-green-400 px-3 py-1 rounded-full text-[10px] font-bold uppercase">
                Open
              </span>
            </div>
            
            <h3 className="text-xl font-bold mb-2 dark:text-white group-hover:text-indigo-600 transition-colors">{course.name}</h3>
            
            <div className="space-y-3 mb-6">
              <div className="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-400">
                <User size={16} className="text-indigo-600" />
                <span>Instructor: <b>{course.teacher_name}</b></span>
              </div>
              <div className="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-400">
                <Clock size={16} className="text-indigo-600" />
                <span>Duration: <b>{course.duration}</b></span>
              </div>
              <div className="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-400">
                <IndianRupee size={16} className="text-indigo-600" />
                <span>Fees: <b>₹{parseFloat(course.fees).toLocaleString()}</b></span>
              </div>
            </div>

            <div className="flex gap-2">
              <Button variant="secondary" className="flex-1 justify-center gap-2" onClick={() => isStudent ? null : handleEditClick(course)}>
                {isStudent ? 'Enroll Now' : <><Edit2 size={14} /> Edit</>}
              </Button>
              {isAdmin && (
                <Button variant="danger" className="bg-red-500/10 text-red-500 shadow-none hover:bg-red-500 hover:text-white" onClick={() => handleDeleteClick(course.id)}>
                  <Trash2 size={14} />
                </Button>
              )}
            </div>
          </Card>
        ))}
      </div>

      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title={editingCourse ? 'Edit Course' : 'Add New Course'}>
        <form onSubmit={handleSubmit} className="space-y-4">
          <Input label="Course Name" value={formData.name} onChange={e => setFormData({...formData, name: e.target.value})} required />
          
          <div className="space-y-1.5">
            <label className="text-sm font-bold text-gray-700 dark:text-gray-300">Instructor</label>
            <select 
              className="w-full bg-gray-50 dark:bg-slate-800/50 border border-gray-200 dark:border-slate-800 rounded-xl py-2.5 px-4 outline-none focus:ring-2 focus:ring-indigo-500/20 dark:text-white"
              value={formData.teacher}
              onChange={e => setFormData({...formData, teacher: e.target.value})}
              required
            >
              <option value="">Select Instructor</option>
              {teachers.map(t => (
                <option key={t.id} value={t.id}>{t.name} ({t.subject})</option>
              ))}
            </select>
          </div>

          <Input label="Duration (e.g. 3 Months)" value={formData.duration} onChange={e => setFormData({...formData, duration: e.target.value})} required />
          <Input label="Course Fees (₹)" type="number" value={formData.fees} onChange={e => setFormData({...formData, fees: e.target.value})} required />
          
          <div className="flex gap-3 pt-4">
            <Button type="button" variant="secondary" className="flex-1" onClick={() => setIsModalOpen(false)}>Cancel</Button>
            <Button type="submit" className="flex-1">{editingCourse ? 'Save Changes' : 'Create Course'}</Button>
          </div>
        </form>
      </Modal>
    </div>
  );
};

export default Courses;
