import React, { useState, useEffect } from 'react';
import { 
  Users, 
  BookOpen, 
  IndianRupee, 
  Clock, 
  TrendingUp,
  ArrowUpRight,
  ArrowDownRight,
  Loader2
} from 'lucide-react';
import { motion } from 'framer-motion';
import { 
  AreaChart, 
  Area, 
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  ResponsiveContainer
} from 'recharts';
import Card from '../components/common/Card';
import { getDashboardStats } from '../data/api';
import { useAuth } from '../context/AuthContext';
import StudentPortal from './StudentPortal';

const StatCard = ({ title, value, icon: Icon, trend, color, delay }) => (
  <Card delay={delay} className="group relative overflow-hidden flex items-center gap-4 hover:shadow-2xl hover:-translate-y-1 transition-all duration-300">
    <div className={`absolute -right-4 -top-4 w-24 h-24 rounded-full ${color} opacity-[0.03] group-hover:scale-150 transition-transform duration-700`} />
    <div className={`p-4 rounded-2xl ${color} bg-opacity-10 text-${color.split('-')[1]}-600 dark:text-${color.split('-')[1]}-400 group-hover:scale-110 transition-transform duration-300`}>
      <Icon size={28} />
    </div>
    <div className="flex-1">
      <p className="text-sm font-medium text-gray-500 dark:text-gray-400">{title}</p>
      <div className="flex items-baseline gap-2">
        <h3 className="text-2xl font-bold dark:text-white">{value}</h3>
        {trend && (
          <span className={`text-xs flex items-center gap-0.5 font-bold ${trend > 0 ? 'text-green-500' : 'text-red-500'}`}>
            {trend > 0 ? <ArrowUpRight size={14} /> : <ArrowDownRight size={14} />}
            {Math.abs(trend)}%
          </span>
        )}
      </div>
    </div>
  </Card>
);

const AdminDashboard = () => {
  const { user } = useAuth();
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    const fetchStats = async () => {
      try {
        const res = await getDashboardStats();
        setStats(res.data);
      } catch (error) {
        console.error("Error fetching dashboard stats:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchStats();
  }, []);

  const getGreeting = () => {
    const hour = new Date().getHours();
    if (hour < 12) return 'Good Morning';
    if (hour < 18) return 'Good Afternoon';
    return 'Good Evening';
  };

  const quickActions = [
    { name: 'Add Student', icon: Users, color: 'bg-blue-500', path: '/students' },
    { name: 'Mark Attendance', icon: Clock, color: 'bg-orange-500', path: '/attendance' },
    { name: 'Collect Fee', icon: IndianRupee, color: 'bg-green-500', path: '/fees' },
    { name: 'Post Notice', icon: BookOpen, color: 'bg-purple-500', path: '/notices' },
  ];

  if (loading) return (
    <div className="h-[60vh] flex flex-col items-center justify-center gap-4">
      <Loader2 className="animate-spin text-indigo-600" size={40} />
      <p className="text-gray-500 font-medium animate-pulse">Gathering institute insights...</p>
    </div>
  );

  return (
    <div className="space-y-8 pb-10">
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <motion.div 
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.5 }}
        >
          <h1 className="text-3xl md:text-4xl font-extrabold dark:text-white tracking-tight">
            {getGreeting()}, <span className="bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent capitalize">{user?.first_name || user?.username || 'Admin'}!</span>
          </h1>
          <p className="text-gray-500 dark:text-gray-400 mt-2 flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span>
            Here's what's happening in your institute today.
          </p>
        </motion.div>
        
        <motion.div 
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          className="flex items-center gap-2 text-sm font-semibold px-4 py-2 bg-white dark:bg-slate-900 rounded-2xl shadow-sm border border-gray-100 dark:border-slate-800"
        >
          <TrendingUp className="text-green-500" size={18} />
          <span className="dark:text-gray-300">Live Analytics Enabled</span>
        </motion.div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <StatCard title="Total Students" value={stats?.totalStudents?.toLocaleString() || 0} icon={Users} trend={12} color="bg-blue-500" delay={0.1} />
        <StatCard title="Active Courses" value={stats?.totalCourses || 0} icon={BookOpen} trend={5} color="bg-purple-500" delay={0.2} />
        <StatCard title="Fees Collected" value={`₹${stats?.feesCollected?.toLocaleString() || 0}`} icon={IndianRupee} trend={8} color="bg-green-500" delay={0.3} />
        <StatCard title="Pending Fees" value={`₹${stats?.pendingFees?.toLocaleString() || 0}`} icon={Clock} trend={-2} color="bg-orange-500" delay={0.4} />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2 space-y-8">
          <Card className="h-[420px] flex flex-col" delay={0.5}>
            <div className="flex items-center justify-between mb-8">
              <div>
                <h3 className="font-bold text-xl dark:text-white">Enrollment Trends</h3>
                <p className="text-xs text-gray-500">Student registration over last 6 months</p>
              </div>
            </div>
            <div className="flex-1 -ml-4">
              <ResponsiveContainer width="100%" height="100%">
                <AreaChart data={stats?.studentGrowth || []}>
                  <defs>
                    <linearGradient id="colorStudents" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="5%" stopColor="#6366f1" stopOpacity={0.3}/>
                      <stop offset="95%" stopColor="#6366f1" stopOpacity={0}/>
                    </linearGradient>
                  </defs>
                  <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e2e8f0" strokeOpacity={0.5} />
                  <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{fill: '#94a3b8', fontSize: 12}} dy={10} />
                  <YAxis axisLine={false} tickLine={false} tick={{fill: '#94a3b8', fontSize: 12}} />
                  <Tooltip contentStyle={{ borderRadius: '16px', border: 'none', boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.1)', backgroundColor: 'rgba(255, 255, 255, 0.9)', backdropFilter: 'blur(8px)', padding: '12px' }} />
                  <Area type="monotone" dataKey="students" stroke="#6366f1" strokeWidth={4} fillOpacity={1} fill="url(#colorStudents)" />
                </AreaChart>
              </ResponsiveContainer>
            </div>
          </Card>

          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {quickActions.map((action, i) => (
              <Card key={action.name} delay={0.6 + (i * 0.1)} className="flex flex-col items-center justify-center gap-3 p-4 hover:bg-indigo-50 dark:hover:bg-indigo-900/20 cursor-pointer group border-dashed">
                <div className={`p-3 rounded-2xl ${action.color} bg-opacity-10 text-${action.color.split('-')[1]}-600 dark:text-${action.color.split('-')[1]}-400 group-hover:scale-110 transition-transform`}>
                  <action.icon size={24} />
                </div>
                <span className="text-xs font-bold dark:text-gray-300">{action.name}</span>
              </Card>
            ))}
          </div>
        </div>

        <div className="space-y-8">
          <Card delay={0.7} className="overflow-hidden">
            <h3 className="font-bold text-lg mb-6 dark:text-white">Top Performing Courses</h3>
            <div className="space-y-6">
              {(stats?.courseStats || []).map((course) => (
                <div key={course.name} className="space-y-3">
                  <div className="flex justify-between items-end">
                    <div>
                      <p className="text-sm font-bold dark:text-gray-200">{course.name}</p>
                      <p className="text-[10px] text-gray-500">{course.students} students enrolled</p>
                    </div>
                    <span className="text-xs font-bold text-indigo-600 dark:text-indigo-400">{course.progress}%</span>
                  </div>
                  <div className="h-2 w-full bg-gray-100 dark:bg-slate-800 rounded-full overflow-hidden">
                    <motion.div initial={{ width: 0 }} animate={{ width: `${course.progress}%` }} transition={{ duration: 1.5, ease: "easeOut", delay: 1 }} className={`h-full ${course.color} rounded-full`} />
                  </div>
                </div>
              ))}
              {(!stats?.courseStats || stats.courseStats.length === 0) && (
                <p className="text-xs text-gray-500 italic text-center py-4">No course data available.</p>
              )}
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
};

const Dashboard = () => {
  const { user } = useAuth();
  
  if (user?.role === 'student') {
    return <StudentPortal />;
  }

  return <AdminDashboard />;
};

export default Dashboard;
