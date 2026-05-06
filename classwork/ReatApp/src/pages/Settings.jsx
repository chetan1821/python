import React, { useState, useEffect } from 'react';
import { User, Lock, Bell, Palette, Globe, Shield, Loader2, Camera, GraduationCap, Check } from 'lucide-react';
import Card from '../components/common/Card';
import Button from '../components/common/Button';
import Input from '../components/common/Input';
import { useAuth } from '../context/AuthContext';
import { useTheme } from '../context/ThemeContext';
import { getStudents, getTeachers, updateStudent, updateTeacher, changePassword } from '../data/api';

const Settings = () => {
  const { user } = useAuth();
  const { isDarkMode, toggleDarkMode } = useTheme();
  const [loading, setLoading] = useState(true);
  const [profile, setProfile] = useState(null);
  const [saving, setSaving] = useState(false);
  const [activeTab, setActiveTab] = useState('profile');
  const [passwordData, setPasswordData] = useState({
    old_password: '',
    new_password: '',
    confirm_password: ''
  });

  useEffect(() => {
    fetchProfile();
  }, []);

  const fetchProfile = async () => {
    try {
      if (user?.role === 'student') {
        const res = await getStudents();
        const me = res.data.find(s => s.email === user.email);
        setProfile(me);
      } else if (user?.role === 'teacher') {
        const res = await getTeachers();
        const me = res.data.find(t => t.email === user.email);
        setProfile(me);
      } else {
        // Admin
        setProfile({
          name: user.first_name || user.username,
          email: user.email,
          designation: 'System Administrator'
        });
      }
    } catch (error) {
      console.error("Error fetching profile:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleSave = async (e) => {
    if (e) e.preventDefault();
    setSaving(true);
    try {
      if (user?.role === 'student') {
        await updateStudent(profile.id, profile);
      } else if (user?.role === 'teacher') {
        await updateTeacher(profile.id, profile);
      }
      alert('Settings updated successfully!');
    } catch (error) {
      alert('Failed to update settings');
    } finally {
      setSaving(false);
    }
  };

  const handlePasswordUpdate = async (e) => {
    e.preventDefault();
    if (passwordData.new_password !== passwordData.confirm_password) {
      alert('New passwords do not match!');
      return;
    }
    setSaving(true);
    try {
      await changePassword({
        old_password: passwordData.old_password,
        new_password: passwordData.new_password
      });
      alert('Password updated successfully!');
      setPasswordData({ old_password: '', new_password: '', confirm_password: '' });
    } catch (error) {
      alert(error.response?.data?.error || 'Failed to update password');
    } finally {
      setSaving(false);
    }
  };

  const toggleNotification = (key) => {
    setProfile(prev => ({
      ...prev,
      [key]: !prev[key]
    }));
  };

  const updateAccentColor = (color) => {
    setProfile(prev => ({
      ...prev,
      accent_color: color
    }));
  };

  if (loading) return <div className="h-[60vh] flex items-center justify-center"><Loader2 className="animate-spin text-indigo-600" /></div>;

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold dark:text-white tracking-tight">Account Settings</h1>
          <p className="text-gray-500 mt-1">Manage your personal information and preferences.</p>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="space-y-4">
          {[
            { id: 'profile', label: 'Profile Information', icon: User },
            { id: 'password', label: 'Security & Password', icon: Lock },
            { id: 'notif', label: 'Notifications', icon: Bell },
            { id: 'theme', label: 'Appearance', icon: Palette },
          ].map((item) => (
            <button
              key={item.id}
              onClick={() => setActiveTab(item.id)}
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition-all ${
                activeTab === item.id 
                  ? 'bg-indigo-50 dark:bg-indigo-900/20 text-indigo-600 dark:text-indigo-400 font-bold shadow-sm border border-indigo-100 dark:border-indigo-900/30' 
                  : 'hover:bg-gray-100 dark:hover:bg-slate-800 text-gray-500 dark:text-gray-400'
              }`}
            >
              <item.icon size={20} />
              <span>{item.label}</span>
            </button>
          ))}
        </div>

        <div className="lg:col-span-2 space-y-6">
          {activeTab === 'profile' && (
            <Card>
              <div className="flex items-center gap-6 mb-8 pb-8 border-b border-gray-100 dark:border-slate-800">
                <div className="w-24 h-24 rounded-3xl bg-indigo-100 dark:bg-slate-800 flex items-center justify-center text-indigo-600 dark:text-indigo-400 text-3xl font-black relative">
                  {profile?.name?.[0] || user.username[0]}
                  <button className="absolute -bottom-2 -right-2 p-2.5 bg-white dark:bg-slate-700 border border-gray-200 dark:border-slate-600 rounded-xl shadow-lg hover:scale-110 transition-transform">
                    <Camera size={16} />
                  </button>
                </div>
                <div>
                  <h4 className="text-xl font-bold dark:text-white capitalize">{profile?.name}</h4>
                  <p className="text-sm text-gray-500 mb-3 capitalize">{user.role} • Member since {profile?.joined_date || 'May 2026'}</p>
                  <div className="flex gap-2">
                    <Button variant="secondary" className="py-1.5 px-4 text-xs font-bold">Update Photo</Button>
                  </div>
                </div>
              </div>

              <form onSubmit={handleSave} className="space-y-6">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <Input 
                    label="Full Name" 
                    value={profile?.name || ''} 
                    onChange={e => setProfile({...profile, name: e.target.value})}
                  />
                  <Input 
                    label="Email Address" 
                    value={profile?.email || ''} 
                    readOnly
                    className="opacity-70 bg-gray-50"
                  />
                  {user.role === 'student' && (
                    <>
                      <div className="md:col-span-2">
                        <h4 className="text-sm font-bold text-indigo-600 uppercase tracking-wider mb-4 flex items-center gap-2">
                          <Globe size={14} /> Contact & Location
                        </h4>
                      </div>
                      <Input 
                        label="Phone Number" 
                        value={profile?.mobile || ''} 
                        onChange={e => setProfile({...profile, mobile: e.target.value})}
                      />
                      <div className="md:col-span-2">
                        <Input 
                          label="Residential Address" 
                          value={profile?.address || ''} 
                          onChange={e => setProfile({...profile, address: e.target.value})}
                        />
                      </div>

                      <div className="md:col-span-2 mt-4">
                        <h4 className="text-sm font-bold text-indigo-600 uppercase tracking-wider mb-4 flex items-center gap-2">
                          <GraduationCap size={16} /> Academic Identity
                        </h4>
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 p-4 bg-indigo-50/50 dark:bg-indigo-900/10 rounded-2xl border border-indigo-100 dark:border-indigo-900/30">
                          <div>
                            <p className="text-xs text-gray-500 font-bold uppercase mb-1">Enrolled Program</p>
                            <p className="font-bold dark:text-white">{profile?.course_name || 'N/A'}</p>
                          </div>
                          <div>
                            <p className="text-xs text-gray-500 font-bold uppercase mb-1">Academic Batch</p>
                            <p className="font-bold dark:text-white">Batch-{profile?.id?.toString().padStart(3, '0')}</p>
                          </div>
                          <div>
                            <p className="text-xs text-gray-500 font-bold uppercase mb-1">Student ID</p>
                            <p className="font-bold dark:text-white">STU-2026-{profile?.id}</p>
                          </div>
                          <div>
                            <p className="text-xs text-gray-500 font-bold uppercase mb-1">Assigned Teacher</p>
                            <p className="font-bold dark:text-white">{profile?.teacher_name || 'N/A'}</p>
                          </div>
                        </div>
                      </div>
                    </>
                  )}
                  {user.role === 'teacher' && (
                    <Input 
                      label="Subject" 
                      value={profile?.subject || ''} 
                      onChange={e => setProfile({...profile, subject: e.target.value})}
                    />
                  )}
                  {user.role === 'admin' && (
                    <Input 
                      label="Designation" 
                      value={profile?.designation || ''} 
                      readOnly
                    />
                  )}
                </div>
                
                <div className="pt-4 flex justify-end">
                  <Button type="submit" disabled={saving}>
                    {saving ? <Loader2 className="animate-spin" size={18} /> : 'Save Changes'}
                  </Button>
                </div>
              </form>
            </Card>
          )}

          {activeTab === 'password' && (
            <Card>
              <h3 className="text-lg font-bold mb-6 dark:text-white flex items-center gap-2">
                <Shield size={20} className="text-indigo-600" /> Security Settings
              </h3>
              <div className="space-y-6">
                <div className="flex items-center justify-between p-4 bg-gray-50 dark:bg-slate-800/50 rounded-2xl">
                  <div>
                    <p className="font-bold dark:text-white">Two-Factor Authentication</p>
                    <p className="text-xs text-gray-500">Protect your account with an extra security layer.</p>
                  </div>
                  <div className="w-12 h-6 bg-indigo-600 rounded-full relative cursor-pointer">
                    <div className="absolute right-1 top-1 w-4 h-4 bg-white rounded-full"></div>
                  </div>
                </div>
                
                <form onSubmit={handlePasswordUpdate} className="space-y-4">
                  <Input 
                    label="Current Password" 
                    type="password" 
                    placeholder="••••••••" 
                    value={passwordData.old_password}
                    onChange={e => setPasswordData({...passwordData, old_password: e.target.value})}
                    required
                  />
                  <Input 
                    label="New Password" 
                    type="password" 
                    placeholder="••••••••" 
                    value={passwordData.new_password}
                    onChange={e => setPasswordData({...passwordData, new_password: e.target.value})}
                    required
                  />
                  <Input 
                    label="Confirm New Password" 
                    type="password" 
                    placeholder="••••••••" 
                    value={passwordData.confirm_password}
                    onChange={e => setPasswordData({...passwordData, confirm_password: e.target.value})}
                    required
                  />
                  <Button type="submit" className="w-full" disabled={saving}>
                    {saving ? <Loader2 className="animate-spin" size={18} /> : 'Update Password'}
                  </Button>
                </form>
              </div>
            </Card>
          )}

          {activeTab === 'notif' && (
            <Card>
              <h3 className="text-lg font-bold mb-6 dark:text-white flex items-center gap-2">
                <Bell size={20} className="text-indigo-600" /> Notification Preferences
              </h3>
              <div className="space-y-4">
                {[
                  { id: 'email_notifications', label: 'Email Notifications', desc: 'Receive daily updates via email.' },
                  { id: 'exam_alerts', label: 'Exam Alerts', desc: 'Get notified about upcoming tests.' },
                  { id: 'attendance_reports', label: 'Attendance Reports', desc: 'Weekly summary of your presence.' },
                  { id: 'announcement_notifications', label: 'Institute News', desc: 'New notices and announcements.' },
                ].map((item) => (
                  <div key={item.id} className="flex items-center justify-between p-4 bg-gray-50 dark:bg-slate-800/50 rounded-2xl border border-transparent hover:border-indigo-500/20 transition-all">
                    <div>
                      <p className="font-bold dark:text-white">{item.label}</p>
                      <p className="text-xs text-gray-500">{item.desc}</p>
                    </div>
                    <button 
                      onClick={() => toggleNotification(item.id)}
                      className={`w-12 h-6 rounded-full relative transition-colors duration-300 ${profile?.[item.id] ? 'bg-indigo-600' : 'bg-gray-300 dark:bg-slate-700'}`}
                    >
                      <div className={`absolute top-1 w-4 h-4 bg-white rounded-full transition-all duration-300 ${profile?.[item.id] ? 'right-1' : 'left-1'}`}></div>
                    </button>
                  </div>
                ))}
                <div className="pt-4">
                  <Button className="w-full" onClick={handleSave} disabled={saving}>
                    {saving ? <Loader2 className="animate-spin" size={18} /> : 'Save Preferences'}
                  </Button>
                </div>
              </div>
            </Card>
          )}

          {activeTab === 'theme' && (
            <Card>
              <h3 className="text-lg font-bold mb-6 dark:text-white flex items-center gap-2">
                <Palette size={20} className="text-indigo-600" /> Interface Appearance
              </h3>
              <div className="space-y-8">
                <div className="grid grid-cols-2 gap-4">
                  <button 
                    onClick={() => !isDarkMode && toggleDarkMode()}
                    className={`p-4 rounded-2xl border-2 transition-all text-left ${isDarkMode ? 'border-indigo-600 bg-indigo-50/50 dark:bg-indigo-900/20' : 'border-gray-100 dark:border-slate-800'}`}
                  >
                    <div className="w-full aspect-video bg-slate-900 rounded-lg mb-3 shadow-inner"></div>
                    <p className="font-bold dark:text-white">Dark Mode</p>
                    <p className="text-xs text-gray-500">Easier on the eyes in low light.</p>
                  </button>
                  <button 
                    onClick={() => isDarkMode && toggleDarkMode()}
                    className={`p-4 rounded-2xl border-2 transition-all text-left ${!isDarkMode ? 'border-indigo-600 bg-indigo-50/50' : 'border-gray-100 dark:border-slate-800'}`}
                  >
                    <div className="w-full aspect-video bg-gray-100 rounded-lg mb-3 shadow-inner"></div>
                    <p className="font-bold dark:text-white">Light Mode</p>
                    <p className="text-xs text-gray-500">Classic bright and clean interface.</p>
                  </button>
                </div>

                <div className="space-y-4">
                  <h4 className="font-bold dark:text-white text-sm uppercase tracking-wider opacity-60">Accent Color</h4>
                  <div className="flex gap-4">
                    {['#4f46e5', '#ef4444', '#10b981', '#f59e0b', '#ec4899'].map(color => (
                      <button 
                        key={color}
                        className="w-10 h-10 rounded-full border-4 border-white dark:border-slate-900 shadow-sm transition-all hover:scale-110 flex items-center justify-center relative"
                        style={{ backgroundColor: color }}
                        onClick={() => updateAccentColor(color)}
                      >
                        {profile?.accent_color === color && <Check size={18} className="text-white" />}
                      </button>
                    ))}
                  </div>
                  <div className="pt-4">
                    <Button className="w-full" onClick={handleSave} disabled={saving}>
                      {saving ? <Loader2 className="animate-spin" size={18} /> : 'Apply Theme Settings'}
                    </Button>
                  </div>
                </div>
              </div>
            </Card>
          )}
        </div>
      </div>
    </div>
  );
};

export default Settings;
