import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { 
  Users, 
  BookOpen, 
  Calendar, 
  Bell, 
  CheckCircle2, 
  Clock,
  ArrowRight,
  MessageSquare,
  ClipboardList,
  Plus
} from 'lucide-react';
import Card from '../components/common/Card';
import Button from '../components/common/Button';
import { getStudents, getTeachers, getCourses } from '../data/api';
import { useAuth } from '../context/AuthContext';

const TeacherPortal = () => {
  const { user } = useAuth();
  const [teacherData, setTeacherData] = useState(null);
  const [students, setStudents] = useState([]);
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPortalData = async () => {
      try {
        const [teachersRes, studentsRes, coursesRes] = await Promise.all([
          getTeachers(),
          getStudents({ page_size: 1000 }),
          getCourses()
        ]);

        if (!user?.email) return;
        const studentList = studentsRes.data.results || studentsRes.data;
        const me = teachersRes.data.find(t => t.email === user.email);
        setTeacherData(me);

        if (me) {
          // Filter students assigned to this teacher
          const teacherStudents = studentList.filter(s => s.teacher_name === me.name);
          setStudents(teacherStudents);
          
          // Filter courses assigned to this teacher
          const teacherCourses = coursesRes.data.filter(c => c.teacher === me.id);
          setCourses(teacherCourses);
        }
      } catch (error) {
        console.error("Error fetching teacher portal data:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchPortalData();
  }, [user.email]);

  if (loading) return <div className="h-[60vh] flex items-center justify-center dark:text-white">Loading Portal...</div>;

  const stats = [
    { label: 'Total Students', value: students.length, icon: Users, color: 'text-blue-600', bg: 'bg-blue-100' },
    { label: 'Active Courses', value: courses.length, icon: BookOpen, color: 'text-indigo-600', bg: 'bg-indigo-100' },
    { label: 'Classes Today', value: '3', icon: Clock, color: 'text-orange-600', bg: 'bg-orange-100' },
    { label: 'Pending Result', value: '1', icon: ClipboardList, color: 'text-red-600', bg: 'bg-red-100' },
  ];

  return (
    <div className="space-y-8 pb-10">
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <motion.div 
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
        >
          <h1 className="text-3xl font-extrabold dark:text-white tracking-tight">
            Welcome, <span className="text-indigo-600 dark:text-indigo-400 capitalize">{teacherData?.name || user.username}!</span>
          </h1>
          <p className="text-gray-500 mt-2">Manage your classes and monitor student performance.</p>
        </motion.div>
        
        <div className="flex items-center gap-3">
          <Button variant="secondary" className="gap-2">
            <MessageSquare size={18} /> Announcements
          </Button>
          <Button className="gap-2">
            <Plus size={18} /> New Schedule
          </Button>
        </div>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        {stats.map((stat, i) => (
          <Card key={i} delay={i * 0.1}>
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-500 mb-1">{stat.label}</p>
                <h3 className="text-2xl font-bold dark:text-white">{stat.value}</h3>
              </div>
              <div className={`p-3 rounded-2xl ${stat.bg} ${stat.color} dark:bg-opacity-20`}>
                <stat.icon size={24} />
              </div>
            </div>
          </Card>
        ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Student Roster */}
        <div className="lg:col-span-2">
          <Card>
            <div className="flex items-center justify-between mb-6">
              <h3 className="text-xl font-bold dark:text-white flex items-center gap-2">
                <Users size={22} className="text-indigo-600" />
                Your Student Roster
              </h3>
              <button className="text-sm text-indigo-600 font-bold flex items-center gap-1 hover:underline">
                View All <ArrowRight size={14} />
              </button>
            </div>
            
            <div className="overflow-x-auto">
              <table className="w-full text-left">
                <thead>
                  <tr className="border-b border-gray-100 dark:border-slate-800 text-xs text-gray-500 uppercase font-bold">
                    <th className="pb-4">Student</th>
                    <th className="pb-4">Course</th>
                    <th className="pb-4">Attendance</th>
                    <th className="pb-4 text-right">Status</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-50 dark:divide-slate-800/50">
                  {students.map((student) => (
                    <tr key={student.id} className="group hover:bg-gray-50/50 dark:hover:bg-slate-800/30 transition-colors">
                      <td className="py-4">
                        <div className="flex items-center gap-3">
                          <div className="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/30 text-indigo-600 dark:text-indigo-400 flex items-center justify-center font-bold">
                            {student.name[0]}
                          </div>
                          <div>
                            <p className="font-semibold dark:text-white">{student.name}</p>
                            <p className="text-[10px] text-gray-500">ID: #{student.id.toString().padStart(4, '0')}</p>
                          </div>
                        </div>
                      </td>
                      <td className="py-4">
                        <p className="text-sm dark:text-gray-300">{student.course_name}</p>
                      </td>
                      <td className="py-4">
                        <div className="flex items-center gap-2">
                          <div className="flex-1 h-1.5 w-20 bg-gray-100 dark:bg-slate-800 rounded-full overflow-hidden">
                            <div className="h-full bg-green-500 w-[85%]"></div>
                          </div>
                          <span className="text-[10px] font-bold dark:text-white">85%</span>
                        </div>
                      </td>
                      <td className="py-4 text-right">
                        <span className={`px-2 py-1 rounded-full text-[10px] font-bold uppercase ${
                          student.fees_status === 'Paid' ? 'bg-green-100 text-green-700' : 'bg-orange-100 text-orange-700'
                        }`}>
                          {student.fees_status}
                        </span>
                      </td>
                    </tr>
                  ))}
                  {students.length === 0 && (
                    <tr>
                      <td colSpan="4" className="py-10 text-center text-gray-500 italic">No students assigned to your courses yet.</td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          </Card>
        </div>

        {/* Side Panel: Schedule & Notices */}
        <div className="space-y-8">
          <Card>
            <h3 className="text-lg font-bold dark:text-white flex items-center gap-2 mb-6">
              <Calendar size={20} className="text-orange-500" />
              Today's Schedule
            </h3>
            <div className="space-y-4">
              {courses.map((course, i) => (
                <div key={i} className="p-4 rounded-2xl bg-gray-50 dark:bg-slate-800/50 border-l-4 border-indigo-600 group hover:bg-white dark:hover:bg-slate-800 transition-all shadow-sm hover:shadow-md">
                  <div className="flex justify-between items-start mb-1">
                    <p className="font-bold text-sm dark:text-white">{course.name}</p>
                    <span className="text-[10px] font-bold text-indigo-600 bg-indigo-50 dark:bg-indigo-900/30 px-2 py-1 rounded-lg">10:00 AM</span>
                  </div>
                  <p className="text-[10px] text-gray-500 flex items-center gap-1">
                    <Clock size={10} /> 1.5 Hours
                  </p>
                </div>
              ))}
              {courses.length === 0 && <p className="text-sm text-gray-500 italic text-center py-4">No classes scheduled.</p>}
            </div>
          </Card>

          <Card className="bg-premium-gradient border-none text-white">
            <h3 className="text-lg font-bold flex items-center gap-2 mb-4">
              <Bell size={20} />
              Recent Notices
            </h3>
            <div className="space-y-3">
              <div className="p-3 bg-white/10 rounded-xl backdrop-blur-sm border border-white/10">
                <p className="text-xs font-bold">New Exam Material</p>
                <p className="text-[10px] opacity-70 mt-1">Uploaded for React Mastery Batch A</p>
              </div>
            </div>
            <button className="w-full mt-4 py-2 bg-white text-indigo-600 rounded-xl text-xs font-bold hover:bg-indigo-50 transition-colors">
              Post Announcement
            </button>
          </Card>
        </div>
      </div>
    </div>
  );
};

export default TeacherPortal;
