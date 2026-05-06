import React, { useState, useEffect } from 'react';
import { Plus, Edit2, Trash2, Loader2, Users, BookOpen, Calendar, Phone, Mail, GraduationCap } from 'lucide-react';
import Card from '../components/common/Card';
import Button from '../components/common/Button';
import Input from '../components/common/Input';
import Modal from '../components/common/Modal';
import { getTeachers, getStudents, addTeacher, updateTeacher, deleteTeacher } from '../data/api';
import { useAuth } from '../context/AuthContext';

const Teachers = () => {
  const { user } = useAuth();
  const [teachers, setTeachers] = useState([]);
  const [loading, setLoading] = useState(true);
  const isAdmin = user?.role === 'admin';
  const [selectedTeacher, setSelectedTeacher] = useState(null);
  const [roster, setRoster] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isRosterOpen, setIsRosterOpen] = useState(false);
  const [rosterLoading, setRosterLoading] = useState(false);
  const [editingTeacher, setEditingTeacher] = useState(null);
  const [successMessage, setSuccessMessage] = useState('');

  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    joined_date: new Date().toISOString().split('T')[0]
  });

  useEffect(() => {
    fetchTeachers();
  }, []);

  const fetchTeachers = async () => {
    try {
      const response = await getTeachers();
      setTeachers(response.data);
    } catch (error) {
      console.error('Error fetching teachers:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleAddClick = () => {
    setEditingTeacher(null);
    setSuccessMessage('');
    setFormData({
      name: '',
      email: '',
      subject: '',
      joined_date: new Date().toISOString().split('T')[0]
    });
    setIsModalOpen(true);
  };

  const handleEditClick = (teacher) => {
    setEditingTeacher(teacher);
    setSuccessMessage('');
    setFormData({
      name: teacher.name,
      email: teacher.email || '',
      subject: teacher.subject,
      joined_date: teacher.joined_date
    });
    setIsModalOpen(true);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editingTeacher) {
        await updateTeacher(editingTeacher.id, formData);
        fetchTeachers();
        setIsModalOpen(false);
      } else {
        await addTeacher(formData);
        fetchTeachers();
        setSuccessMessage(`Teacher profile created successfully!\n\nUsername: ${formData.email}\nPassword: password123`);
      }
    } catch (error) {
      console.error("Save Teacher Error:", error.response?.data || error.message);
      const msg = error.response?.data ? JSON.stringify(error.response.data) : error.message;
      alert('Failed to save teacher data: ' + msg);
    }
  };

  const handleDeleteClick = async (id) => {
    if (window.confirm('Delete this teacher profile?')) {
      try {
        await deleteTeacher(id);
        setTeachers(teachers.filter(t => t.id !== id));
      } catch (error) {
        alert('Failed to delete teacher');
      }
    }
  };

  const handleViewRoster = async (teacher) => {
    setSelectedTeacher(teacher);
    setIsRosterOpen(true);
    setRosterLoading(true);
    try {
      const res = await getStudents({ teacher: teacher.id });
      setRoster(res.data);
    } catch (error) {
      console.error("Error fetching roster:", error);
    } finally {
      setRosterLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="h-[60vh] flex items-center justify-center">
        <Loader2 className="w-10 h-10 text-indigo-600 animate-spin" />
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold dark:text-white tracking-tight">Faculty Management</h1>
          <p className="text-gray-500 mt-1">Manage your teachers and their student assignments.</p>
        </div>
        {isAdmin && (
          <Button onClick={handleAddClick} className="shadow-lg shadow-indigo-500/20">
            <Plus size={18} /> Add Teacher
          </Button>
        )}
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {teachers.map((teacher, index) => (
          <Card key={teacher.id} delay={index * 0.1}>
            <div className="flex items-center gap-4 mb-6">
              <div className="w-16 h-16 rounded-2xl bg-indigo-100 dark:bg-indigo-900/30 flex items-center justify-center text-indigo-600 dark:text-indigo-400 font-bold text-2xl">
                {teacher.name[0]}
              </div>
              <div>
                <h3 className="font-bold text-lg dark:text-white">{teacher.name}</h3>
                <p className="text-indigo-600 dark:text-indigo-400 text-sm font-medium">{teacher.subject}</p>
              </div>
            </div>
            
            <div className="space-y-3 mb-6">
              <div className="flex items-center justify-between p-3 rounded-xl bg-gray-50 dark:bg-slate-800/50 border border-gray-100 dark:border-slate-800">
                <div className="flex items-center gap-2 text-xs text-gray-500">
                  <Mail size={14} /> Email
                </div>
                <span className="text-xs font-semibold dark:text-white truncate max-w-[150px]">{teacher.email || 'N/A'}</span>
              </div>
              <div className="flex items-center justify-between p-3 rounded-xl bg-gray-50 dark:bg-slate-800/50 border border-gray-100 dark:border-slate-800">
                <div className="flex items-center gap-2 text-xs text-gray-500">
                  <Calendar size={14} /> Joined
                </div>
                <span className="font-bold dark:text-white">{teacher.joined_date}</span>
              </div>
            </div>

            <div className="space-y-3">
              <Button 
                variant="secondary" 
                className="w-full justify-center gap-2 bg-indigo-50 dark:bg-indigo-900/20 text-indigo-600 dark:text-indigo-400 border-none hover:bg-indigo-600 hover:text-white transition-all duration-300"
                onClick={() => handleViewRoster(teacher)}
              >
                <Users size={16} /> View Students
              </Button>
              {isAdmin && (
                <div className="flex gap-2">
                  <Button variant="secondary" className="flex-1 py-2 text-sm" onClick={() => handleEditClick(teacher)}>
                    <Edit2 size={14} /> Edit
                  </Button>
                  <Button variant="danger" className="flex-1 py-2 text-sm bg-red-500/10 text-red-500 shadow-none hover:bg-red-500 hover:text-white" onClick={() => handleDeleteClick(teacher.id)}>
                    <Trash2 size={14} /> Delete
                  </Button>
                </div>
              )}
            </div>
          </Card>
        ))}
      </div>

      {/* Add/Edit Modal */}
      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title={editingTeacher ? 'Edit Teacher' : 'Add New Teacher'}>
        {successMessage ? (
          <div className="space-y-6 py-4 text-center">
            <div className="w-16 h-16 bg-green-500 text-white rounded-2xl flex items-center justify-center mx-auto shadow-lg rotate-12">
              <GraduationCap size={32} />
            </div>
            <div>
              <h4 className="text-xl font-bold dark:text-white">Profile Created!</h4>
              <p className="text-sm text-gray-500 whitespace-pre-line mt-2">{successMessage}</p>
            </div>
            <Button className="w-full" onClick={() => setIsModalOpen(false)}>Close</Button>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="space-y-4">
            <Input label="Full Name" value={formData.name} onChange={e => setFormData({...formData, name: e.target.value})} required />
            <Input label="Email Address" type="email" value={formData.email} onChange={e => setFormData({...formData, email: e.target.value})} required />
            <Input label="Subject / Department" value={formData.subject} onChange={e => setFormData({...formData, subject: e.target.value})} required />
            <Input label="Joining Date" type="date" value={formData.joined_date} onChange={e => setFormData({...formData, joined_date: e.target.value})} required />
            
            <div className="flex gap-3 pt-4">
              <Button type="button" variant="secondary" className="flex-1" onClick={() => setIsModalOpen(false)}>Cancel</Button>
              <Button type="submit" className="flex-1">{editingTeacher ? 'Save Changes' : 'Create Profile'}</Button>
            </div>
          </form>
        )}
      </Modal>

      {/* Roster Modal */}
      <Modal isOpen={isRosterOpen} onClose={() => setIsRosterOpen(false)} title={`Students under ${selectedTeacher?.name}`}>
        <div className="space-y-4">
          {rosterLoading ? (
            <div className="py-10 text-center">
              <Loader2 className="w-8 h-8 text-indigo-600 animate-spin mx-auto" />
            </div>
          ) : roster.length > 0 ? (
            <div className="space-y-3">
              <p className="text-xs font-bold text-gray-500 uppercase">Total Students: {roster.length}</p>
              <div className="max-h-[400px] overflow-y-auto space-y-2 pr-2 custom-scrollbar">
                {roster.map(student => (
                  <div key={student.id} className="p-4 bg-gray-50 dark:bg-slate-800 rounded-xl border border-gray-100 dark:border-slate-700 flex items-center justify-between">
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 rounded-full bg-indigo-100 dark:bg-indigo-900/30 text-indigo-600 dark:text-indigo-400 flex items-center justify-center font-bold">
                        {student.name[0]}
                      </div>
                      <div>
                        <p className="font-bold text-sm dark:text-white">{student.name}</p>
                        <p className="text-[10px] text-gray-500 flex items-center gap-1"><Phone size={10} /> {student.mobile || 'No Mobile'}</p>
                      </div>
                    </div>
                    <div className="text-right">
                      <p className="text-[10px] font-bold text-indigo-600 uppercase">{student.course_name}</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          ) : (
            <div className="py-10 text-center bg-gray-50 dark:bg-slate-800 rounded-2xl">
              <Users size={40} className="text-gray-300 mx-auto mb-2" />
              <p className="text-gray-500 font-medium">No students enrolled.</p>
            </div>
          )}
          <Button className="w-full" onClick={() => setIsRosterOpen(false)}>Close</Button>
        </div>
      </Modal>
    </div>
  );
};

export default Teachers;
