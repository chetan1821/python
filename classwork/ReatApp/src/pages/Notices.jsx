import React, { useState, useEffect } from 'react';
import { Bell, Plus, Calendar, Flag } from 'lucide-react';
import Card from '../components/common/Card';
import Button from '../components/common/Button';
import { getNotices, addNotice, updateNotice, deleteNotice } from '../data/api';
import { useAuth } from '../context/AuthContext';
import Modal from '../components/common/Modal';
import Input from '../components/common/Input';
import { Loader2 } from 'lucide-react';

const Notices = () => {
  const { user } = useAuth();
  const [notices, setNotices] = useState([]);
  const [loading, setLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingNotice, setEditingNotice] = useState(null);
  const isAdmin = user?.role === 'admin';

  const [formData, setFormData] = useState({
    title: '',
    content: '',
    priority: 'Medium',
    date: new Date().toISOString().split('T')[0]
  });

  useEffect(() => {
    fetchNotices();
  }, []);

  const fetchNotices = async () => {
    setLoading(true);
    try {
      const response = await getNotices();
      setNotices(response.data);
    } catch (error) {
      console.error("Failed to fetch notices:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleAddClick = () => {
    setEditingNotice(null);
    setFormData({
      title: '',
      content: '',
      priority: 'Medium',
      date: new Date().toISOString().split('T')[0]
    });
    setIsModalOpen(true);
  };

  const handleEditClick = (notice) => {
    setEditingNotice(notice);
    setFormData({
      title: notice.title,
      content: notice.content,
      priority: notice.priority,
      date: notice.date
    });
    setIsModalOpen(true);
  };

  const handleDeleteClick = async (id) => {
    if (window.confirm('Are you sure you want to delete this announcement?')) {
      try {
        await deleteNotice(id);
        fetchNotices();
      } catch (error) {
        alert('Failed to delete notice');
      }
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editingNotice) {
        await updateNotice(editingNotice.id, formData);
      } else {
        await addNotice(formData);
      }
      setIsModalOpen(false);
      fetchNotices();
    } catch (error) {
      alert('Failed to save notice');
    }
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold dark:text-white tracking-tight">Announcements</h1>
          <p className="text-gray-500 mt-1">
            {isAdmin ? 'Post and manage institute-wide notices.' : 'Stay updated with the latest institute news.'}
          </p>
        </div>
        {isAdmin && (
          <Button onClick={handleAddClick} className="shadow-lg shadow-indigo-500/20">
            <Plus size={18} /> New Notice
          </Button>
        )}
      </div>

      {loading ? (
        <div className="h-[40vh] flex items-center justify-center">
          <Loader2 className="animate-spin text-indigo-600" size={32} />
        </div>
      ) : (
        <div className="space-y-4">
          {notices.length > 0 ? notices.map((notice, index) => (
          <Card key={notice.id} delay={index * 0.1}>
            <div className="flex items-start gap-4">
              <div className={`p-3 rounded-2xl ${
                notice.priority === 'High' 
                  ? 'bg-red-50 text-red-500 dark:bg-red-900/20' 
                  : 'bg-blue-50 text-blue-500 dark:bg-blue-900/20'
              }`}>
                <Bell size={24} />
              </div>
              <div className="flex-1">
                <div className="flex flex-col md:flex-row md:items-center justify-between gap-2 mb-2">
                  <h3 className="text-xl font-bold dark:text-white">{notice.title}</h3>
                  <div className="flex items-center gap-4">
                    <span className="flex items-center gap-1.5 text-xs text-gray-500">
                      <Calendar size={14} /> {notice.date}
                    </span>
                    <span className={`flex items-center gap-1 text-xs font-bold px-2.5 py-1 rounded-full ${
                      notice.priority === 'High' 
                        ? 'bg-red-100 text-red-700 dark:bg-red-900/30' 
                        : 'bg-blue-100 text-blue-700 dark:bg-blue-900/30'
                    }`}>
                      <Flag size={12} /> {notice.priority}
                    </span>
                  </div>
                </div>
                <p className="text-gray-600 dark:text-gray-400 leading-relaxed">
                  {notice.content}
                </p>
                {isAdmin && (
                  <div className="mt-4 pt-4 border-t border-gray-100 dark:border-slate-800 flex justify-end gap-3">
                    <Button variant="secondary" className="text-xs py-1.5 px-4" onClick={() => handleEditClick(notice)}>Edit</Button>
                    <Button variant="danger" className="text-xs py-1.5 px-4 bg-red-500/10 text-red-500 shadow-none hover:bg-red-500 hover:text-white" onClick={() => handleDeleteClick(notice.id)}>Delete</Button>
                  </div>
                )}
              </div>
            </div>
          </Card>
        )) : (
          <Card className="text-center py-20 text-gray-500 italic">
            <Bell size={40} className="mx-auto mb-4 opacity-20" />
            No recent announcements.
          </Card>
        )}
      </div>
      )}

      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title={editingNotice ? 'Edit Announcement' : 'Post New Announcement'}>
        <form onSubmit={handleSubmit} className="space-y-4">
          <Input label="Title" value={formData.title} onChange={e => setFormData({...formData, title: e.target.value})} required />
          <div className="space-y-1.5">
            <label className="text-sm font-bold text-gray-700 dark:text-gray-300">Priority</label>
            <select 
              className="w-full bg-gray-50 dark:bg-slate-800/50 border border-gray-200 dark:border-slate-800 rounded-xl py-2.5 px-4 outline-none focus:ring-2 focus:ring-indigo-500/20 dark:text-white"
              value={formData.priority}
              onChange={e => setFormData({...formData, priority: e.target.value})}
            >
              <option value="High">High Priority</option>
              <option value="Medium">Medium Priority</option>
              <option value="Low">Low Priority</option>
            </select>
          </div>
          <div className="space-y-1.5">
            <label className="text-sm font-bold text-gray-700 dark:text-gray-300">Message Content</label>
            <textarea 
              className="w-full min-h-[120px] bg-gray-50 dark:bg-slate-800/50 border border-gray-200 dark:border-slate-800 rounded-xl py-2.5 px-4 outline-none focus:ring-2 focus:ring-indigo-500/20 dark:text-white resize-none"
              value={formData.content}
              onChange={e => setFormData({...formData, content: e.target.value})}
              required
            />
          </div>
          <Input label="Display Date" type="date" value={formData.date} onChange={e => setFormData({...formData, date: e.target.value})} required />
          
          <div className="flex gap-3 pt-4">
            <Button type="button" variant="secondary" className="flex-1" onClick={() => setIsModalOpen(false)}>Cancel</Button>
            <Button type="submit" className="flex-1">{editingNotice ? 'Update Notice' : 'Post Notice'}</Button>
          </div>
        </form>
      </Modal>
    </div>
  );
};

export default Notices;
