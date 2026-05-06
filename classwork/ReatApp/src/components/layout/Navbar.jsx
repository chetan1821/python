import React from 'react';
import { Menu, Bell, Sun, Moon, Search, User, LogOut } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';
import { useTheme } from '../../context/ThemeContext';

const Navbar = ({ toggleSidebar }) => {
  const { user, logout } = useAuth();
  const { isDarkMode, toggleDarkMode } = useTheme();

  return (
    <header className="bg-white/80 dark:bg-slate-900/80 backdrop-blur-md border-b border-gray-200 dark:border-slate-800 h-20 flex items-center px-6 sticky top-0 z-40 transition-colors duration-300">
      <button 
        onClick={toggleSidebar}
        className="p-2 rounded-xl hover:bg-gray-100 dark:hover:bg-slate-800 lg:hidden"
      >
        <Menu size={24} />
      </button>

      <div className="flex-1 max-w-xl mx-auto px-4 hidden md:block">
        <div className="relative group">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 group-focus-within:text-indigo-500 transition-colors" size={20} />
          <input 
            type="text" 
            placeholder="Search anything..." 
            className="w-full bg-gray-100 dark:bg-slate-800 border-none rounded-2xl py-2.5 pl-11 pr-4 focus:ring-2 focus:ring-indigo-500/20 transition-all outline-none dark:text-white"
          />
        </div>
      </div>

      <div className="flex items-center gap-4 ml-auto">
        <button 
          onClick={toggleDarkMode}
          className="p-2.5 rounded-xl hover:bg-gray-100 dark:hover:bg-slate-800 text-gray-600 dark:text-gray-400 transition-all"
        >
          {isDarkMode ? <Sun size={20} /> : <Moon size={20} />}
        </button>

        <button className="p-2.5 rounded-xl hover:bg-gray-100 dark:hover:bg-slate-800 text-gray-600 dark:text-gray-400 relative group transition-all">
          <Bell size={20} className="group-hover:rotate-12 transition-transform" />
          <span className="absolute top-2 right-2 w-2.5 h-2.5 bg-red-500 rounded-full border-2 border-white dark:border-slate-900 animate-bounce"></span>
        </button>

        <button 
          onClick={logout}
          className="p-2.5 rounded-xl hover:bg-red-50 dark:hover:bg-red-900/10 text-gray-600 dark:text-gray-400 hover:text-red-500 transition-all"
          title="Logout"
        >
          <LogOut size={20} />
        </button>

        <div className="flex items-center gap-3 pl-4 border-l border-gray-200 dark:border-slate-800 group cursor-pointer">
          <div className="hidden sm:block text-right">
            <p className="text-sm font-bold dark:text-white group-hover:text-indigo-600 transition-colors">{user?.first_name || user?.username || 'Admin User'}</p>
            <p className="text-[10px] text-gray-500 uppercase tracking-wider font-bold">{user?.role || 'Administrator'}</p>
          </div>
          <div className="w-10 h-10 rounded-xl bg-premium-gradient p-[2px] shadow-md group-hover:shadow-indigo-500/30 transition-all">
            <div className="w-full h-full rounded-[10px] bg-white dark:bg-slate-900 flex items-center justify-center text-indigo-600">
              <User size={20} />
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Navbar;
