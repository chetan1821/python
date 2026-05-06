import React, { useState, useEffect } from 'react';
import { NavLink } from 'react-router-dom';
import { motion } from 'framer-motion';
import { 
  BookOpen, 
  CalendarCheck, 
  Wallet, 
  Bell, 
  FileText,
  Clock,
  CheckCircle2,
  AlertCircle,
  History,
  Download,
  ArrowRight,
  ClipboardList
} from 'lucide-react';
import Card from '../components/common/Card';
import Button from '../components/common/Button';
import { 
  getAttendance, 
  getExams, 
  getNotices, 
  getStudentInstallments,
  getStudents,
  getStudentAttendanceStats
} from '../data/api';
import { useAuth } from '../context/AuthContext';
import { generateReceipt } from '../utils/receiptGenerator';

const StudentPortal = () => {
  const { user } = useAuth();
  const [studentData, setStudentData] = useState(null);
  const [installments, setInstallments] = useState([]);
  const [attendanceStats, setAttendanceStats] = useState(null);
  const [notices, setNotices] = useState([]);
  const [exams, setExams] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const studentRes = await getStudents({ page_size: 1000 });
        if (!user?.email) return;
        const studentList = studentRes.data.results || studentRes.data;
        const me = studentList.find(s => s.email === user.email);
        setStudentData(me);
        
        if (me) {
          const [paymentsRes, attendanceRes, noticesRes, examsRes] = await Promise.all([
            getStudentInstallments(me.id),
            getStudentAttendanceStats(me.id),
            getNotices(),
            getExams()
          ]);
          setInstallments(paymentsRes.data);
          setAttendanceStats(attendanceRes.data);
          setNotices(noticesRes.data);
          setExams(examsRes.data);
        }
      } catch (error) {
        console.error("Error fetching portal data:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [user.email]);

  if (loading) return <div className="h-[60vh] flex items-center justify-center dark:text-white">Loading Portal...</div>;

  return (
    <div className="space-y-8 pb-10">
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <motion.div 
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
        >
          <h1 className="text-3xl font-extrabold dark:text-white tracking-tight">
            Welcome back, <span className="text-indigo-600 dark:text-indigo-400 capitalize">{studentData?.name || user.username}!</span>
          </h1>
          <p className="text-gray-500 mt-2">Check your academic progress and updates.</p>
        </motion.div>
        
        <div className="flex items-center gap-3">
          <div className="px-4 py-2 bg-white dark:bg-slate-900 rounded-xl shadow-sm border border-gray-100 dark:border-slate-800 flex items-center gap-2">
            <Clock size={16} className="text-indigo-600" />
            <span className="text-sm font-bold dark:text-white">{new Date().toLocaleDateString()}</span>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Course Info & Fee Status */}
        <div className="lg:col-span-2 space-y-8">
          <Card className="relative overflow-hidden">
            <div className="absolute top-0 right-0 p-6 opacity-5">
              <BookOpen size={120} />
            </div>
            <div className="flex items-center justify-between mb-6">
              <div className="flex items-center gap-4">
                <div className="p-3 bg-indigo-100 dark:bg-indigo-900/30 text-indigo-600 dark:text-indigo-400 rounded-2xl">
                  <BookOpen size={24} />
                </div>
                <div>
                  <h3 className="font-bold text-lg dark:text-white">Active Program</h3>
                  <div className="flex items-center gap-2">
                    <p className="text-indigo-600 dark:text-indigo-400 font-medium">{studentData?.course_name || 'Not Enrolled'}</p>
                    {studentData?.teacher_name && (
                      <span className="text-[10px] bg-indigo-50 dark:bg-indigo-900/30 px-2 py-0.5 rounded-full text-indigo-600 dark:text-indigo-400 font-bold uppercase">
                        By {studentData.teacher_name}
                      </span>
                    )}
                  </div>
                </div>
              </div>
              <NavLink to="/courses">
                <Button variant="ghost" className="text-indigo-600 text-xs font-bold gap-1">
                  Explore More <ArrowRight size={14} />
                </Button>
              </NavLink>
            </div>
            
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
              <div className="p-4 bg-gray-50 dark:bg-slate-800/50 rounded-2xl border border-gray-100 dark:border-slate-800">
                <p className="text-[10px] text-gray-500 mb-1 font-bold uppercase tracking-wider">Total Fees</p>
                <div className="flex items-center gap-2">
                  <span className="text-xl font-bold dark:text-white">₹{studentData?.total_fees || 0}</span>
                </div>
              </div>
              <div className="p-4 bg-green-50 dark:bg-green-900/10 rounded-2xl border border-green-100 dark:border-green-900/20">
                <p className="text-[10px] text-green-600 mb-1 font-bold uppercase tracking-wider">Paid</p>
                <div className="flex items-center gap-2 text-green-600">
                  <CheckCircle2 size={16} />
                  <span className="text-xl font-bold">₹{studentData?.fees_paid || 0}</span>
                </div>
              </div>
              <div className="p-4 bg-orange-50 dark:bg-orange-900/10 rounded-2xl border border-orange-100 dark:border-orange-900/20">
                <p className="text-[10px] text-orange-600 mb-1 font-bold uppercase tracking-wider">Due</p>
                <div className="flex items-center gap-2 text-orange-600">
                  <Wallet size={16} />
                  <span className="text-xl font-bold">₹{(studentData?.total_fees || 0) - (studentData?.fees_paid || 0)}</span>
                </div>
              </div>
            </div>
            
            <div className="mt-6 pt-6 border-t border-gray-100 dark:border-slate-800 flex items-center justify-between">
              <div className="flex items-center gap-4">
                <div className="h-8 w-8 rounded-full bg-indigo-50 dark:bg-indigo-900/30 flex items-center justify-center text-indigo-600">
                  <ClipboardList size={16} />
                </div>
                <div>
                  <p className="text-xs font-bold dark:text-white">Next Batch Module</p>
                  <p className="text-[10px] text-gray-500">Advanced React Patterns</p>
                </div>
              </div>
              <Button size="sm" className="text-xs">Access Learning Materials</Button>
            </div>
          </Card>

          {/* Attendance Stats Card */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-8">
            <Card className="flex flex-col justify-between">
              <div className="flex items-center gap-3 mb-6">
                <div className="p-2 bg-green-100 dark:bg-green-900/30 text-green-600 rounded-xl">
                  <CalendarCheck size={20} />
                </div>
                <h3 className="font-bold dark:text-white">Attendance Overview</h3>
              </div>
              
              <div className="flex items-end justify-between">
                <div>
                  <p className="text-4xl font-black text-green-600">{attendanceStats?.percentage || 0}%</p>
                  <p className="text-xs text-gray-500 font-medium mt-1">Overall Attendance</p>
                </div>
                <div className="text-right text-sm space-y-1">
                  <p className="dark:text-gray-400">Present: <span className="font-bold text-green-600">{attendanceStats?.present || 0}</span></p>
                  <p className="dark:text-gray-400">Total Days: <span className="font-bold dark:text-white">{attendanceStats?.total || 0}</span></p>
                </div>
              </div>
              
              <div className="mt-6 h-2 w-full bg-gray-100 dark:bg-slate-800 rounded-full overflow-hidden">
                <motion.div 
                  initial={{ width: 0 }}
                  animate={{ width: `${attendanceStats?.percentage || 0}%` }}
                  className="h-full bg-green-500 rounded-full"
                />
              </div>
            </Card>

            <Card className="flex flex-col justify-between">
              <div className="flex items-center gap-3 mb-6">
                <div className="p-2 bg-blue-100 dark:bg-blue-900/30 text-blue-600 rounded-xl">
                  <Clock size={20} />
                </div>
                <h3 className="font-bold dark:text-white">Quick Stats</h3>
              </div>
              <div className="space-y-4">
                <div className="flex justify-between items-center text-sm">
                  <span className="text-gray-500">Days Absent</span>
                  <span className="font-bold text-red-500">{attendanceStats?.absent || 0}</span>
                </div>
                <div className="flex justify-between items-center text-sm">
                  <span className="text-gray-500">Last 10 Days</span>
                  <span className="font-bold dark:text-white">
                    {attendanceStats?.history?.filter(h => h.status === 'present').length || 0}/10
                  </span>
                </div>
              </div>
              <Button variant="secondary" className="mt-6 w-full text-xs py-2">View Full History</Button>
            </Card>
          </div>

          {/* Payment History */}
          <Card>
            <div className="flex items-center justify-between mb-6">
              <div className="flex items-center gap-3">
                <div className="p-2 bg-indigo-100 dark:bg-indigo-900/30 text-indigo-600 rounded-xl">
                  <History size={20} />
                </div>
                <h3 className="font-bold dark:text-white">Payment History</h3>
              </div>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-left">
                <thead>
                  <tr className="text-xs text-gray-500 uppercase font-bold border-b border-gray-100 dark:border-slate-800">
                    <th className="pb-3">Date</th>
                    <th className="pb-3">Amount</th>
                    <th className="pb-3">Status</th>
                    <th className="pb-3 text-right">Action</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-50 dark:divide-slate-800/50">
                  {installments.length > 0 ? installments.map((pay) => (
                    <tr key={pay.id} className="text-sm">
                      <td className="py-4 dark:text-gray-300">{pay.payment_date}</td>
                      <td className="py-4 font-bold dark:text-white">₹{pay.amount}</td>
                      <td className="py-4">
                        <span className="px-2 py-1 bg-green-100 text-green-700 dark:bg-green-900/20 text-[10px] font-bold rounded-lg uppercase">Success</span>
                      </td>
                      <td className="py-4 text-right">
                        <button 
                          onClick={() => generateReceipt(studentData, pay)}
                          className="text-indigo-600 dark:text-indigo-400 hover:underline flex items-center gap-1 ml-auto"
                        >
                          <Download size={14} /> Receipt
                        </button>
                      </td>
                    </tr>
                  )) : (
                    <tr>
                      <td colSpan="4" className="py-8 text-center text-gray-500 italic">No payments recorded yet.</td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          </Card>
        </div>

        {/* Sidebar info */}
        <div className="space-y-8">
          <Card>
            <div className="flex items-center gap-3 mb-6">
              <Bell size={20} className="text-orange-500" />
              <h3 className="font-bold dark:text-white">Notice Board</h3>
            </div>
            <div className="space-y-4">
              {notices.length > 0 ? notices.map((notice, i) => (
                <div key={notice.id} className={`p-4 bg-gray-50 dark:bg-slate-800/50 rounded-xl border-l-4 ${
                  notice.priority === 'High' ? 'border-red-500' : 
                  notice.priority === 'Medium' ? 'border-orange-500' : 'border-indigo-600'
                }`}>
                  <p className="font-bold text-sm dark:text-white">{notice.title}</p>
                  <p className="text-xs text-gray-500 mt-1">{notice.date}</p>
                </div>
              )) : (
                <p className="text-xs text-gray-500 italic text-center py-4">No recent notices.</p>
              )}
            </div>
          </Card>

          <Card>
            <div className="flex items-center gap-3 mb-6">
              <FileText size={20} className="text-indigo-600" />
              <h3 className="font-bold dark:text-white">Upcoming Exams</h3>
            </div>
            <div className="space-y-3">
              {exams.length > 0 ? exams.filter(e => e.status !== 'Completed').slice(0, 3).map(exam => (
                <div key={exam.id} className="flex items-center justify-between p-3 rounded-xl bg-indigo-50 dark:bg-indigo-900/10">
                  <span className="text-sm font-medium dark:text-gray-300">{exam.title}</span>
                  <span className="text-xs font-bold text-indigo-600">{exam.date}</span>
                </div>
              )) : (
                <p className="text-xs text-gray-500 italic text-center py-4">No upcoming exams.</p>
              )}
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
};

export default StudentPortal;
