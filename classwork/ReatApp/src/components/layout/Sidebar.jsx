import React from 'react';
import { NavLink } from 'react-router-dom';
import { 
  LayoutDashboard, 
  Users, 
  GraduationCap, 
  BookOpen, 
  CalendarCheck, 
  Wallet, 
  Bell, 
  Settings,
  ChevronLeft,
  ChevronRight,
  LogOut,
  FileText
} from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import { useAuth } from '../../context/AuthContext';

const Sidebar = ({ isOpen, setIsOpen }) => {
  const { logout, user } = useAuth();
  
  const allNavItems = [
    { name: 'Dashboard', icon: LayoutDashboard, path: '/dashboard', roles: ['admin', 'student', 'teacher'] },
    { name: 'Students', icon: Users, path: '/students', roles: ['admin'] },
    { name: 'Teachers', icon: GraduationCap, path: '/teachers', roles: ['admin'] },
    { name: 'Courses', icon: BookOpen, path: '/courses', roles: ['admin', 'student', 'teacher'] },
    { name: 'Attendance', icon: CalendarCheck, path: '/attendance', roles: ['admin', 'student', 'teacher'] },
    { name: 'Fees', icon: Wallet, path: '/fees', roles: ['admin', 'student'] },
    { name: 'Notices', icon: Bell, path: '/notices', roles: ['admin', 'student', 'teacher'] },
    { name: 'Exams', icon: FileText, path: '/exams', roles: ['admin', 'student', 'teacher'] },
    { name: 'Settings', icon: Settings, path: '/settings', roles: ['admin', 'student', 'teacher'] },
  ];

  const navItems = allNavItems.filter(item => {
    const userRole = user?.role?.toLowerCase();
    return item.roles.some(role => role.toLowerCase() === userRole);
  });

  console.log("Current User Role:", user?.role);
  console.log("Filtered Nav Items:", navItems.length);

  return (
    <motion.aside
      initial={false}
      animate={{ width: isOpen ? 260 : 80 }}
      className="bg-white dark:bg-slate-900 border-r border-gray-200 dark:border-slate-800 flex flex-col transition-colors duration-300 relative z-50"
    >
      <div className="p-6 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-premium-gradient flex items-center justify-center text-white font-bold text-xl shadow-lg">
            E
          </div>
          {isOpen && (
            <motion.span 
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="font-bold text-xl bg-gradient-to-r from-red-600 to-orange-600 bg-clip-text text-transparent truncate"
            >
              Enjoy
            </motion.span>
          )}
        </div>
      </div>

      <nav className="flex-1 px-4 space-y-2 overflow-y-auto">
        {navItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={({ isActive }) => 
              `sidebar-link ${isActive ? 'active' : ''} ${!isOpen ? 'justify-center px-0' : ''}`
            }
            title={!isOpen ? item.name : ''}
          >
            <item.icon size={22} />
            {isOpen && <span className="font-medium">{item.name}</span>}
          </NavLink>
        ))}
      </nav>

      <div className="p-4 space-y-4">
        {/* Support Card */}
        {isOpen && (
          <motion.div 
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className="p-4 rounded-2xl bg-gradient-to-br from-indigo-600 to-purple-700 text-white shadow-lg"
          >
            <p className="text-xs font-bold opacity-80 uppercase tracking-wider mb-1">Need Help?</p>
            <p className="text-sm font-medium mb-3">Our support team is available 24/7</p>
            <button className="w-full py-2 bg-white/20 hover:bg-white/30 backdrop-blur-md rounded-xl text-xs font-bold transition-colors">
              Contact Support
            </button>
          </motion.div>
        )}

        <button
          onClick={logout}
          className={`sidebar-link w-full text-red-500 hover:text-red-600 hover:bg-red-50 dark:hover:bg-red-900/10 ${!isOpen ? 'justify-center px-0' : ''}`}
        >
          <LogOut size={22} />
          {isOpen && <span className="font-medium">Logout</span>}
        </button>
      </div>

      <button
        onClick={() => setIsOpen(!isOpen)}
        className="absolute -right-3 top-20 w-6 h-6 bg-white dark:bg-slate-800 border border-gray-200 dark:border-slate-700 rounded-full flex items-center justify-center shadow-md hover:bg-gray-50 dark:hover:bg-slate-700"
      >
        {isOpen ? <ChevronLeft size={14} /> : <ChevronRight size={14} />}
      </button>
    </motion.aside>
  );
};

export default Sidebar;
