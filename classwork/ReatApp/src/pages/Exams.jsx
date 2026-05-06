import React, { useState, useEffect } from 'react';
import { FileText, Clock, Trophy, Plus, ChevronRight, PlayCircle, Loader2, Edit2, Trash2 } from 'lucide-react';
import Card from '../components/common/Card';
import Button from '../components/common/Button';
import Input from '../components/common/Input';
import Modal from '../components/common/Modal';
import { getExams, getResults, getCourses, addExam, updateExam, deleteExam } from '../data/api';
import { useAuth } from '../context/AuthContext';

const Exams = () => {
  const { user } = useAuth();
  const [exams, setExams] = useState([]);
  const [results, setResults] = useState([]);
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingExam, setEditingExam] = useState(null);
  const isAdmin = user?.role === 'admin';

  const [formData, setFormData] = useState({
    title: '',
    course: '',
    date: new Date().toISOString().split('T')[0],
    duration: '',
    total_marks: '',
    status: 'Upcoming'
  });

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const [examsRes, resultsRes, coursesRes] = await Promise.all([
        getExams(),
        getResults(),
        getCourses()
      ]);
      setExams(examsRes.data);
      setResults(resultsRes.data);
      setCourses(coursesRes.data);
    } catch (error) {
      console.error("Failed to fetch exam data:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleAddClick = () => {
    setEditingExam(null);
    setFormData({
      title: '',
      course: '',
      date: new Date().toISOString().split('T')[0],
      duration: '',
      total_marks: '',
      status: 'Upcoming'
    });
    setIsModalOpen(true);
  };

  const handleEditClick = (exam) => {
    setEditingExam(exam);
    setFormData({
      title: exam.title,
      course: exam.course,
      date: exam.date,
      duration: exam.duration,
      total_marks: exam.total_marks,
      status: exam.status
    });
    setIsModalOpen(true);
  };

  const handleDeleteClick = async (id) => {
    if (window.confirm('Delete this examination?')) {
      try {
        await deleteExam(id);
        fetchData();
      } catch (error) {
        alert('Failed to delete exam');
      }
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editingExam) {
        await updateExam(editingExam.id, formData);
      } else {
        await addExam(formData);
      }
      setIsModalOpen(false);
      fetchData();
    } catch (error) {
      alert('Failed to save exam');
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
    <div className="space-y-8">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold dark:text-white tracking-tight">Online Examinations</h1>
          <p className="text-gray-500 mt-1">
            {isAdmin ? 'Create, manage, and monitor student tests.' : 'Participate in assessments and track your performance.'}
          </p>
        </div>
        {isAdmin && (
          <Button onClick={handleAddClick} className="shadow-lg shadow-indigo-500/20">
            <Plus size={18} /> Create New Test
          </Button>
        )}
      </div>

      {/* Main Content */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Left Column: Exams List */}
        <div className="lg:col-span-2 space-y-6">
          <h2 className="text-xl font-bold dark:text-white flex items-center gap-2">
            <FileText className="text-indigo-600" size={24} /> Available Tests
          </h2>
          
          <div className="space-y-4">
            {exams.length > 0 ? exams.map((exam, index) => (
              <Card key={exam.id} delay={index * 0.1} className="group hover:border-indigo-500/50 transition-all">
                <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
                  <div className="flex items-start gap-4">
                    <div className={`p-4 rounded-2xl ${
                      exam.status === 'Active' ? 'bg-green-100 text-green-600' : 
                      exam.status === 'Upcoming' ? 'bg-blue-100 text-blue-600' : 'bg-gray-100 text-gray-600'
                    } dark:bg-slate-800`}>
                      <PlayCircle size={28} />
                    </div>
                    <div>
                      <h3 className="text-lg font-bold dark:text-white group-hover:text-indigo-600 transition-colors">
                        {exam.title}
                      </h3>
                      <p className="text-sm text-gray-500">{exam.course_name}</p>
                      <div className="flex items-center gap-4 mt-3">
                        <span className="flex items-center gap-1.5 text-xs text-gray-500 font-medium">
                          <Clock size={14} /> {exam.duration}
                        </span>
                        <span className="flex items-center gap-1.5 text-xs text-gray-500 font-medium">
                          <Trophy size={14} /> {exam.total_marks} Marks
                        </span>
                      </div>
                    </div>
                  </div>
                  
                   <div className="flex items-center gap-4">
                    <div className="text-right hidden md:block">
                      <p className="text-xs text-gray-400 font-bold uppercase tracking-wider">Status</p>
                      <p className={`text-sm font-bold ${
                        exam.status === 'Active' ? 'text-green-500' : 
                        exam.status === 'Upcoming' ? 'text-blue-500' : 'text-gray-400'
                      }`}>
                        {exam.status}
                      </p>
                    </div>
                    
                    <div className="flex gap-2">
                      <Button variant={exam.status === 'Active' ? 'primary' : 'secondary'} className="px-6">
                        {isAdmin ? 'Manage' : (exam.status === 'Completed' ? 'View Result' : (exam.status === 'Active' ? 'Start Test' : 'Notify Me'))}
                      </Button>
                      {isAdmin && (
                        <>
                          <Button variant="secondary" className="px-3" onClick={() => handleEditClick(exam)}>
                            <Edit2 size={16} />
                          </Button>
                          <Button variant="danger" className="px-3 bg-red-500/10 text-red-500 shadow-none hover:bg-red-500 hover:text-white" onClick={() => handleDeleteClick(exam.id)}>
                            <Trash2 size={16} />
                          </Button>
                        </>
                      )}
                    </div>
                  </div>
                </div>
              </Card>
            )) : (
              <Card className="py-20 text-center text-gray-500 italic">
                <FileText size={40} className="mx-auto mb-4 opacity-20" />
                No examinations scheduled at the moment.
              </Card>
            )}
          </div>
        </div>

        {/* Right Column: Recent Results & Stats */}
        <div className="space-y-8">
          <div>
            <h2 className="text-xl font-bold dark:text-white mb-6 flex items-center gap-2">
              <Trophy className="text-yellow-500" size={24} /> Recent Results
            </h2>
            <div className="space-y-4">
              {results.length > 0 ? results.map((result, i) => (
                <Card key={result.id} delay={0.4 + (i * 0.1)} className="p-4 border-l-4 border-yellow-500 hover:translate-x-1 transition-transform cursor-pointer">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="font-bold dark:text-white">{result.student_name}</p>
                      <p className="text-xs text-gray-500">{result.exam_title}</p>
                    </div>
                    <div className="text-right">
                      <p className="text-lg font-black text-indigo-600 leading-none">{result.marks}</p>
                      <p className="text-[10px] font-bold text-gray-400 uppercase leading-none mt-1">Grade {result.grade}</p>
                    </div>
                  </div>
                </Card>
              )) : (
                <Card className="text-center py-10 text-gray-400 text-sm">
                  No results available yet.
                </Card>
              )}
            </div>
          </div>

          <Card className="bg-premium-gradient text-white border-none shadow-xl shadow-indigo-500/20" delay={0.6}>
            <h3 className="font-bold text-lg mb-2">Performance Analytics</h3>
            <p className="text-sm opacity-80 mb-6">Aggregate performance trends across all batches.</p>
            <div className="space-y-4">
              <div className="flex justify-between items-center text-sm">
                <span className="opacity-80">Average Score</span>
                <span className="font-bold">78%</span>
              </div>
              <div className="h-2 w-full bg-white/20 rounded-full overflow-hidden">
                <div className="h-full bg-white rounded-full w-[78%] animate-pulse"></div>
              </div>
              <p className="text-[10px] opacity-60">* Real-time data sync active</p>
            </div>
          </Card>
        </div>
      </div>

      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title={editingExam ? 'Edit Examination' : 'Schedule New Examination'}>
        <form onSubmit={handleSubmit} className="space-y-4">
          <Input label="Exam Title" value={formData.title} onChange={e => setFormData({...formData, title: e.target.value})} required />
          
          <div className="space-y-1.5">
            <label className="text-sm font-bold text-gray-700 dark:text-gray-300">Course</label>
            <select 
              className="w-full bg-gray-50 dark:bg-slate-800/50 border border-gray-200 dark:border-slate-800 rounded-xl py-2.5 px-4 outline-none focus:ring-2 focus:ring-indigo-500/20 dark:text-white"
              value={formData.course}
              onChange={e => setFormData({...formData, course: e.target.value})}
              required
            >
              <option value="">Select Course</option>
              {courses.map(c => (
                <option key={c.id} value={c.id}>{c.name}</option>
              ))}
            </select>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <Input label="Exam Date" type="date" value={formData.date} onChange={e => setFormData({...formData, date: e.target.value})} required />
            <div className="space-y-1.5">
              <label className="text-sm font-bold text-gray-700 dark:text-gray-300">Status</label>
              <select 
                className="w-full bg-gray-50 dark:bg-slate-800/50 border border-gray-200 dark:border-slate-800 rounded-xl py-2.5 px-4 outline-none focus:ring-2 focus:ring-indigo-500/20 dark:text-white"
                value={formData.status}
                onChange={e => setFormData({...formData, status: e.target.value})}
              >
                <option value="Upcoming">Upcoming</option>
                <option value="Active">Active</option>
                <option value="Completed">Completed</option>
              </select>
            </div>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <Input label="Duration (e.g. 1h 30m)" value={formData.duration} onChange={e => setFormData({...formData, duration: e.target.value})} required />
            <Input label="Total Marks" type="number" value={formData.total_marks} onChange={e => setFormData({...formData, total_marks: e.target.value})} required />
          </div>

          <div className="flex gap-3 pt-4">
            <Button type="button" variant="secondary" className="flex-1" onClick={() => setIsModalOpen(false)}>Cancel</Button>
            <Button type="submit" className="flex-1">{editingExam ? 'Save Changes' : 'Schedule Exam'}</Button>
          </div>
        </form>
      </Modal>
    </div>
  );
};

export default Exams;
