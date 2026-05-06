import React, { useState, useEffect } from 'react';
import { Calendar, Check, X, Loader2, BookOpen, Clock as ClockIcon, CheckCircle2 } from 'lucide-react';
import Card from '../components/common/Card';
import Button from '../components/common/Button';
import { getCourses, getStudents, markAttendance, getStudentAttendanceStats } from '../data/api';
import { motion, AnimatePresence } from 'framer-motion';
import { useAuth } from '../context/AuthContext';

const Attendance = () => {
  const { user } = useAuth();
  const [courses, setCourses] = useState([]);
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedCourse, setSelectedCourse] = useState('');
  const [attendance, setAttendance] = useState({});
  const [submitting, setSubmitting] = useState(false);
  const [showSuccess, setShowSuccess] = useState(false);
  const [studentStats, setStudentStats] = useState(null);
  const [isStudent, setIsStudent] = useState(false);

  useEffect(() => {
    fetchInitialData();
  }, []);

  const fetchInitialData = async () => {
    try {
      if (user?.role === 'student') {
        setIsStudent(true);
        // For student, we need their student ID. We find it by their email.
        const studentsRes = await getStudents();
        const studentList = studentsRes.data.results || studentsRes.data;
        const me = studentList.find(s => s.email === user.email);
        if (me) {
          const statsRes = await getStudentAttendanceStats(me.id);
          setStudentStats(statsRes.data);
        }
      } else {
        const [coursesRes, studentsRes] = await Promise.all([
          getCourses(),
          getStudents({ page_size: 1000 }) // Fetch more to ensure we get all students for attendance marking
        ]);
        
        const studentList = studentsRes.data.results || studentsRes.data;
        let availableCourses = coursesRes.data;
        if (user?.role === 'teacher') {
          // Filter courses to only show those taught by this teacher
          availableCourses = coursesRes.data.filter(c => studentList.some(s => s.course === c.id));
        }
        
        setCourses(availableCourses);
        setStudents(studentList);
        if (availableCourses.length > 0) {
          setSelectedCourse(availableCourses[0].id.toString());
        }
      }
    } catch (error) {
      console.error("Error fetching attendance data:", error);
    } finally {
      setLoading(false);
    }
  };

  // Filter students based on selected course
  const filteredStudents = students.filter(s => s.course?.toString() === selectedCourse?.toString());

  const handleMark = (id, status) => {
    setAttendance(prev => ({ ...prev, [id]: status }));
  };

  const handleSaveAttendance = async () => {
    const attendanceArray = filteredStudents.map(s => ({
      student_id: s.id,
      status: attendance[s.id] || 'absent' // Default to absent if not marked
    }));

    if (attendanceArray.length === 0) return;

    setSubmitting(true);
    try {
      await markAttendance({
        date: new Date().toISOString().split('T')[0],
        attendance: attendanceArray
      });
      setShowSuccess(true);
      setTimeout(() => setShowSuccess(false), 3000);
    } catch (error) {
      alert("Failed to save attendance");
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) return <div className="h-[60vh] flex items-center justify-center"><Loader2 className="animate-spin text-indigo-600" /></div>;

  if (isStudent) {
    return (
      <div className="space-y-8">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <h1 className="text-3xl font-bold dark:text-white tracking-tight">My Attendance</h1>
            <p className="text-gray-500 mt-1">Track your presence and academic consistency.</p>
          </div>
          <div className="flex items-center gap-2 bg-white dark:bg-slate-900 px-4 py-2 rounded-xl border border-gray-200 dark:border-slate-800 shadow-sm">
            <Calendar size={18} className="text-indigo-600" />
            <span className="font-bold text-sm dark:text-white">Overall: {studentStats?.percentage || 0}%</span>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <Card className="bg-premium-gradient border-none text-white">
            <p className="text-xs opacity-80 font-bold uppercase mb-1">Total Days</p>
            <h3 className="text-3xl font-black">{studentStats?.total || 0}</h3>
          </Card>
          <Card className="bg-green-500 border-none text-white">
            <p className="text-xs opacity-80 font-bold uppercase mb-1">Days Present</p>
            <h3 className="text-3xl font-black">{studentStats?.present || 0}</h3>
          </Card>
          <Card className="bg-red-500 border-none text-white">
            <p className="text-xs opacity-80 font-bold uppercase mb-1">Days Absent</p>
            <h3 className="text-3xl font-black">{studentStats?.absent || 0}</h3>
          </Card>
        </div>

        <Card>
          <h3 className="font-bold text-xl dark:text-white mb-6">Attendance History</h3>
          <div className="overflow-x-auto">
            <table className="w-full text-left">
              <thead>
                <tr className="border-b border-gray-100 dark:border-slate-800 text-xs text-gray-500 uppercase font-bold">
                  <th className="pb-4">Date</th>
                  <th className="pb-4">Day</th>
                  <th className="pb-4 text-center">Status</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-50 dark:divide-slate-800/50">
                {studentStats?.history?.length > 0 ? studentStats.history.map((record, i) => (
                  <tr key={i}>
                    <td className="py-4 dark:text-white font-medium">{record.date}</td>
                    <td className="py-4 text-gray-500 text-sm">
                      {new Date(record.date).toLocaleDateString('en-US', { weekday: 'long' })}
                    </td>
                    <td className="py-4">
                      <div className="flex justify-center">
                        <span className={`px-3 py-1 rounded-full text-[10px] font-bold uppercase ${
                          record.status === 'present' 
                          ? 'bg-green-100 text-green-700 dark:bg-green-900/20' 
                          : 'bg-red-100 text-red-700 dark:bg-red-900/20'
                        }`}>
                          {record.status}
                        </span>
                      </div>
                    </td>
                  </tr>
                )) : (
                  <tr>
                    <td colSpan="3" className="py-10 text-center text-gray-500 italic">No attendance records found.</td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </Card>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* ... existing management UI ... */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold dark:text-white tracking-tight">Attendance System</h1>
          <p className="text-gray-500 mt-1">Manage daily student presence across courses.</p>
        </div>
        <div className="flex items-center gap-3">
          <div className="flex items-center gap-2 bg-white dark:bg-slate-900 px-4 py-2 rounded-xl border border-gray-200 dark:border-slate-800 shadow-sm">
            <Calendar size={18} className="text-indigo-600" />
            <span className="font-bold text-sm dark:text-white">{new Date().toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' })}</span>
          </div>
          <Button onClick={handleSaveAttendance} disabled={submitting || filteredStudents.length === 0}>
            {submitting ? <Loader2 size={18} className="animate-spin" /> : 'Save Attendance'}
          </Button>
        </div>
      </div>

      <AnimatePresence>
        {showSuccess && (
          <motion.div 
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="bg-green-500 text-white p-4 rounded-2xl shadow-lg flex items-center gap-3 font-bold"
          >
            <CheckCircle2 /> Attendance recorded successfully!
          </motion.div>
        )}
      </AnimatePresence>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Course Selection */}
        <div className="lg:col-span-1 space-y-6">
          <Card>
            <h3 className="font-bold text-lg dark:text-white mb-6 flex items-center gap-2">
              <BookOpen size={20} className="text-indigo-600" />
              Select Course
            </h3>
            <div className="space-y-3">
              {courses.map(course => (
                <button
                  key={course.id}
                  onClick={() => setSelectedCourse(course.id.toString())}
                  className={`w-full text-left p-4 rounded-2xl border-2 transition-all ${
                    selectedCourse === course.id.toString()
                    ? 'border-indigo-600 bg-indigo-50 dark:bg-indigo-900/20'
                    : 'border-transparent bg-gray-50 dark:bg-slate-800/50 hover:bg-gray-100 dark:hover:bg-slate-800'
                  }`}
                >
                  <p className={`font-bold ${selectedCourse === course.id.toString() ? 'text-indigo-600 dark:text-indigo-400' : 'text-gray-700 dark:text-gray-300'}`}>
                    {course.name}
                  </p>
                  <p className="text-[10px] text-gray-500 mt-1 uppercase font-bold">
                    Students: {students.filter(s => s.course?.toString() === course.id?.toString()).length}
                  </p>
                </button>
              ))}
            </div>
          </Card>

          <Card className="bg-premium-gradient border-none text-white">
            <div className="flex items-center gap-3 mb-4">
              <ClockIcon size={20} />
              <h3 className="font-bold">Batch Stats</h3>
            </div>
            <div className="space-y-4">
              <div className="flex justify-between text-sm">
                <span className="opacity-80">Marked Today</span>
                <span className="font-bold">{Object.keys(attendance).length} / {filteredStudents.length}</span>
              </div>
              <div className="h-2 w-full bg-white/20 rounded-full overflow-hidden">
                <div 
                  className="h-full bg-white" 
                  style={{ width: `${(Object.keys(attendance).length / (filteredStudents.length || 1)) * 100}%` }}
                />
              </div>
            </div>
          </Card>
        </div>

        {/* Student List */}
        <div className="lg:col-span-2">
          <Card>
            <div className="flex items-center justify-between mb-8">
              <h3 className="font-bold text-xl dark:text-white">Student Roster</h3>
              <div className="flex gap-2">
                <Button variant="secondary" size="sm" onClick={() => {
                  const allPresent = {};
                  filteredStudents.forEach(s => allPresent[s.id] = 'present');
                  setAttendance(allPresent);
                }}>Mark All Present</Button>
              </div>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-left">
                <thead>
                  <tr className="border-b border-gray-100 dark:border-slate-800 text-xs text-gray-500 uppercase font-bold">
                    <th className="pb-4">Student</th>
                    <th className="pb-4">Roll No</th>
                    <th className="pb-4 text-center">Status</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-50 dark:divide-slate-800/50">
                  {filteredStudents.map((student) => (
                    <tr key={student.id} className="group">
                      <td className="py-4">
                        <div className="flex items-center gap-3">
                          <div className="w-10 h-10 rounded-xl bg-indigo-100 dark:bg-indigo-900/30 text-indigo-600 dark:text-indigo-400 flex items-center justify-center font-bold">
                            {student.name[0]}
                          </div>
                          <div>
                            <p className="font-bold dark:text-white">{student.name}</p>
                            <p className="text-[10px] text-gray-500">#{student.id.toString().padStart(4, '0')}</p>
                          </div>
                        </div>
                      </td>
                      <td className="py-4 text-sm dark:text-gray-400 font-medium">STU-{student.id}</td>
                      <td className="py-4">
                        <div className="flex items-center justify-center gap-3">
                          <button 
                            onClick={() => handleMark(student.id, 'present')}
                            className={`px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1 ${
                              attendance[student.id] === 'present' 
                                ? 'bg-green-500 text-white shadow-lg shadow-green-500/20' 
                                : 'bg-gray-100 dark:bg-slate-800 text-gray-400 hover:bg-green-100 hover:text-green-500'
                            }`}
                          >
                            <Check size={14} /> Present
                          </button>
                          <button 
                            onClick={() => handleMark(student.id, 'absent')}
                            className={`px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1 ${
                              attendance[student.id] === 'absent' 
                                ? 'bg-red-500 text-white shadow-lg shadow-red-500/20' 
                                : 'bg-gray-100 dark:bg-slate-800 text-gray-400 hover:bg-red-100 hover:text-red-500'
                            }`}
                          >
                            <X size={14} /> Absent
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))}
                  {filteredStudents.length === 0 && (
                    <tr>
                      <td colSpan="3" className="py-20 text-center text-gray-500 italic">
                        No students enrolled in this course yet.
                      </td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
};

export default Attendance;
