import React, { useState, useEffect } from 'react';
import { Plus, Search, Edit2, Trash2, Download, Loader2, Phone, MapPin, Wallet, IndianRupee, History, Calendar, ChevronLeft, ChevronRight } from 'lucide-react';
import Card from '../components/common/Card';
import Button from '../components/common/Button';
import Input from '../components/common/Input';
import Modal from '../components/common/Modal';
import { getStudents, addStudent, updateStudent, deleteStudent, getCourses, addInstallment, getStudentInstallments } from '../data/api';
import { generateReceipt } from '../utils/receiptGenerator';

const Students = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [students, setStudents] = useState([]);
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isPayModalOpen, setIsPayModalOpen] = useState(false);
  const [isHistoryModalOpen, setIsHistoryModalOpen] = useState(false);
  const [editingStudent, setEditingStudent] = useState(null);
  const [selectedStudent, setSelectedStudent] = useState(null);
  const [historyData, setHistoryData] = useState([]);
  const [successMessage, setSuccessMessage] = useState('');
  
  // Pagination state
  const [currentPage, setCurrentPage] = useState(1);
  const [paginationInfo, setPaginationInfo] = useState({
    count: 0,
    next: null,
    previous: null
  });
  
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    mobile: '',
    address: '',
    course: '',
    fees_paid: 0,
    fees_status: 'Pending',
    joined_date: new Date().toISOString().split('T')[0]
  });

  const [installmentData, setInstallmentData] = useState({
    amount: '',
    remarks: '',
    payment_date: new Date().toISOString().split('T')[0]
  });

  useEffect(() => {
    fetchData(currentPage, searchTerm);
  }, [currentPage]);

  // Handle search with debounce or just on enter/button
  useEffect(() => {
    const timer = setTimeout(() => {
      if (currentPage !== 1) {
        setCurrentPage(1);
      } else {
        fetchData(1, searchTerm);
      }
    }, 500);
    return () => clearTimeout(timer);
  }, [searchTerm]);

  const fetchData = async (page = 1, search = '') => {
    setLoading(true);
    try {
      const [studentsRes, coursesRes] = await Promise.all([
          getStudents({ page, search }),
          getCourses()
      ]);
      
      // Handle paginated response
      if (studentsRes.data.results) {
          setStudents(studentsRes.data.results);
          setPaginationInfo({
              count: studentsRes.data.count,
              next: studentsRes.data.next,
              previous: studentsRes.data.previous
          });
      } else {
          setStudents(studentsRes.data);
      }
      setCourses(coursesRes.data);
    } catch (error) {
      console.error("Failed to fetch data:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleAddClick = () => {
    setEditingStudent(null);
    setSuccessMessage('');
    setFormData({
      name: '',
      email: '',
      mobile: '',
      address: '',
      course: courses[0]?.id || '',
      fees_paid: 0,
      fees_status: 'Pending',
      joined_date: new Date().toISOString().split('T')[0]
    });
    setIsModalOpen(true);
  };

  const handleEditClick = (student) => {
    setEditingStudent(student);
    setSuccessMessage('');
    setFormData({
      name: student.name,
      email: student.email,
      mobile: student.mobile || '',
      address: student.address || '',
      course: student.course || '',
      fees_paid: student.fees_paid || 0,
      fees_status: student.fees_status,
      joined_date: student.joined_date
    });
    setIsModalOpen(true);
  };

  const handlePayClick = (student) => {
    setSelectedStudent(student);
    setSuccessMessage('');
    setInstallmentData({
      amount: '',
      remarks: 'Installment Payment',
      payment_date: new Date().toISOString().split('T')[0]
    });
    setIsPayModalOpen(true);
  };

  const handleHistoryClick = async (student) => {
    setSelectedStudent(student);
    try {
      const res = await getStudentInstallments(student.id);
      setHistoryData(res.data);
      setIsHistoryModalOpen(true);
    } catch (error) {
      alert('Failed to fetch payment history');
    }
  };

  const handleDeleteClick = async (id) => {
    if (window.confirm('Are you sure you want to delete this student?')) {
      try {
        await deleteStudent(id);
        fetchData(currentPage, searchTerm);
      } catch (error) {
        alert('Failed to delete student');
      }
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSuccessMessage('');
    try {
      if (editingStudent) {
        await updateStudent(editingStudent.id, formData);
        fetchData(currentPage, searchTerm);
        setIsModalOpen(false);
      } else {
        await addStudent(formData);
        fetchData(currentPage, searchTerm);
        setSuccessMessage(`Student registered successfully! \n\nUsername: ${formData.email}\nPassword: password123`);
      }
    } catch (error) {
      const errorMsg = error.response?.data ? 
        Object.values(error.response.data).flat().join(' ') : 
        'Failed to save student data';
      alert(errorMsg);
    }
  };

  const handlePaySubmit = async (e) => {
    e.preventDefault();
    const amount = parseFloat(installmentData.amount);
    const remaining = selectedStudent.total_fees - selectedStudent.fees_paid;

    if (amount <= 0) {
      alert('Amount must be greater than zero!');
      return;
    }

    if (amount > remaining + 0.01) {
      alert(`Invalid Amount! Maximum allowed is ₹${remaining}`);
      return;
    }

    try {
      await addInstallment({
        student: selectedStudent.id,
        ...installmentData
      });
      fetchData(currentPage, searchTerm);
      setSuccessMessage(`Payment of ₹${amount} recorded successfully for ${selectedStudent.name}.`);
    } catch (error) {
      const errorMsg = error.response?.data ? 
        Object.values(error.response.data).flat().join(' ') : 
        'Failed to record payment';
      alert(errorMsg);
    }
  };

  return (
    <div className="space-y-6">
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold dark:text-white">Student Management</h1>
          <p className="text-gray-500">Manage students, details, and installments.</p>
        </div>
        <Button onClick={handleAddClick}>
          <Plus size={18} /> Add Student
        </Button>
      </div>

      <Card>
        <div className="mb-6 relative">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" size={18} />
          <input 
            type="text" 
            placeholder="Search by name, email or mobile..." 
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full bg-gray-50 dark:bg-slate-800/50 border border-gray-200 dark:border-slate-800 rounded-xl py-2.5 pl-10 pr-4 outline-none focus:ring-2 focus:ring-indigo-500/20 dark:text-white"
          />
        </div>

        <div className="overflow-x-auto min-h-[400px]">
          {loading ? (
            <div className="h-64 flex items-center justify-center">
                <Loader2 className="w-10 h-10 text-indigo-600 animate-spin" />
            </div>
          ) : (
            <>
              <table className="w-full text-left">
                <thead>
                  <tr className="border-b border-gray-100 dark:border-slate-800">
                    <th className="pb-4 font-semibold text-gray-500 dark:text-gray-400">Student Info</th>
                    <th className="pb-4 font-semibold text-gray-500 dark:text-gray-400">Course</th>
                    <th className="pb-4 font-semibold text-gray-500 dark:text-gray-400">Fees Paid</th>
                    <th className="pb-4 font-semibold text-gray-500 dark:text-gray-400">Status</th>
                    <th className="pb-4 font-semibold text-gray-500 dark:text-gray-400 text-right">Actions</th>
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
                            <p className="text-[10px] text-gray-500 flex items-center gap-1">
                              <Phone size={10} /> {student.mobile || 'N/A'}
                            </p>
                          </div>
                        </div>
                      </td>
                      <td className="py-4">
                        <p className="text-sm dark:text-gray-300 font-medium">{student.course_name}</p>
                        <p className="text-[10px] text-gray-500">{student.joined_date}</p>
                      </td>
                      <td className="py-4">
                        <div className="flex items-center gap-1.5 text-sm font-bold dark:text-white">
                          <span>₹{student.fees_paid}</span>
                          <span className="text-gray-400 font-normal">/ ₹{student.total_fees}</span>
                        </div>
                      </td>
                      <td className="py-4">
                        <span className={`px-3 py-1 rounded-full text-[10px] font-bold uppercase ${
                          student.fees_status === 'Paid' ? 'bg-green-100 text-green-700 dark:bg-green-900/20' :
                          student.fees_status === 'Partial' ? 'bg-blue-100 text-blue-700 dark:bg-blue-900/20' :
                          'bg-yellow-100 text-yellow-700 dark:bg-yellow-900/20'
                        }`}>
                          {student.fees_status}
                        </span>
                      </td>
                      <td className="py-4 text-right">
                        <div className="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                          <button onClick={() => handleHistoryClick(student)} className="p-2 hover:bg-blue-50 dark:hover:bg-blue-900/20 rounded-lg text-blue-600" title="Payment History">
                            <History size={16} />
                          </button>
                          <button onClick={() => handlePayClick(student)} className="p-2 hover:bg-green-50 dark:hover:bg-green-900/20 rounded-lg text-green-600" title="Collect Fee">
                            <IndianRupee size={16} />
                          </button>
                          <button onClick={() => handleEditClick(student)} className="p-2 hover:bg-gray-100 dark:hover:bg-slate-800 rounded-lg text-gray-600 dark:text-gray-400">
                            <Edit2 size={16} />
                          </button>
                          <button onClick={() => handleDeleteClick(student.id)} className="p-2 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg text-red-500">
                            <Trash2 size={16} />
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>

              {/* Pagination Controls */}
              <div className="mt-8 flex items-center justify-between border-t border-gray-100 dark:border-slate-800 pt-6">
                  <p className="text-sm text-gray-500">
                      Showing <span className="font-bold text-gray-700 dark:text-gray-300">{(currentPage - 1) * 10 + 1}</span> to <span className="font-bold text-gray-700 dark:text-gray-300">{Math.min(currentPage * 10, paginationInfo.count)}</span> of <span className="font-bold text-gray-700 dark:text-gray-300">{paginationInfo.count}</span> students
                  </p>
                  <div className="flex gap-2">
                      <button 
                        disabled={!paginationInfo.previous}
                        onClick={() => setCurrentPage(prev => prev - 1)}
                        className={`p-2 rounded-xl border border-gray-200 dark:border-slate-800 transition-all ${!paginationInfo.previous ? 'opacity-50 cursor-not-allowed' : 'hover:bg-gray-50 dark:hover:bg-slate-800 active:scale-95'}`}
                      >
                          <ChevronLeft size={20} className="dark:text-gray-400" />
                      </button>
                      <button 
                        disabled={!paginationInfo.next}
                        onClick={() => setCurrentPage(prev => prev + 1)}
                        className={`p-2 rounded-xl border border-gray-200 dark:border-slate-800 transition-all ${!paginationInfo.next ? 'opacity-50 cursor-not-allowed' : 'hover:bg-gray-50 dark:hover:bg-slate-800 active:scale-95'}`}
                      >
                          <ChevronRight size={20} className="dark:text-gray-400" />
                      </button>
                  </div>
              </div>
            </>
          )}
        </div>
      </Card>

      {/* Main Registration Modal */}
      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} title={editingStudent ? 'Update Details' : 'Register Student'}>
        {successMessage ? (
          <div className="space-y-6 py-4 text-center">
            <div className="w-16 h-16 bg-green-500 text-white rounded-2xl flex items-center justify-center mx-auto shadow-lg rotate-12">
              <Plus size={32} className="rotate-45" />
            </div>
            <div>
              <h4 className="text-xl font-bold dark:text-white">Done!</h4>
              <p className="text-sm text-gray-500 whitespace-pre-line mt-2">{successMessage}</p>
            </div>
            <Button className="w-full" onClick={() => setIsModalOpen(false)}>Close</Button>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="md:col-span-2"><Input label="Full Name" value={formData.name} onChange={e => setFormData({...formData, name: e.target.value})} required /></div>
            <Input label="Email" type="email" value={formData.email} onChange={e => setFormData({...formData, email: e.target.value})} required />
            <Input label="Mobile Number" value={formData.mobile} onChange={e => setFormData({...formData, mobile: e.target.value})} required />
            <div className="md:col-span-2"><Input label="Address" value={formData.address} onChange={e => setFormData({...formData, address: e.target.value})} required /></div>
            
            <div className="space-y-1.5">
              <label className="text-xs font-bold text-gray-500 uppercase">Course</label>
              <select className="w-full bg-gray-50 dark:bg-slate-800 border-none rounded-xl px-4 py-2.5 outline-none dark:text-white" value={formData.course} onChange={e => setFormData({...formData, course: e.target.value})} required>
                <option value="">Select Course</option>
                {courses.map(c => <option key={c.id} value={c.id}>{c.name} (₹{c.fees})</option>)}
              </select>
            </div>

            <Input label="Paid Amount (₹)" type="number" min="0" value={formData.fees_paid} onChange={e => setFormData({...formData, fees_paid: e.target.value})} required />
            
            <Input label="Joined Date" type="date" value={formData.joined_date} onChange={e => setFormData({...formData, joined_date: e.target.value})} required />

            <div className="md:col-span-2 flex gap-3 pt-4">
              <Button type="button" variant="secondary" className="flex-1" onClick={() => setIsModalOpen(false)}>Cancel</Button>
              <Button type="submit" className="flex-1">{editingStudent ? 'Save Changes' : 'Register Now'}</Button>
            </div>
          </form>
        )}
      </Modal>

      {/* Pay Installment Modal */}
      <Modal 
        isOpen={isPayModalOpen} 
        onClose={() => { setIsPayModalOpen(false); setSuccessMessage(''); }} 
        title="Collect Installment"
      >
        {successMessage ? (
          <div className="space-y-6 py-4 text-center">
            <div className="w-16 h-16 bg-green-500 text-white rounded-full flex items-center justify-center mx-auto shadow-lg">
              <Plus size={32} className="rotate-45" />
            </div>
            <div>
              <h4 className="text-xl font-bold dark:text-white">Payment Received!</h4>
              <p className="text-sm text-gray-500 whitespace-pre-line mt-2">{successMessage}</p>
            </div>
            <Button className="w-full" onClick={() => { setIsPayModalOpen(false); setSuccessMessage(''); }}>Done</Button>
          </div>
        ) : (
          <>
            <div className="mb-6 p-4 bg-indigo-50 dark:bg-indigo-900/20 rounded-2xl">
              <p className="text-xs font-bold text-indigo-600 uppercase mb-1">Collecting for</p>
              <h4 className="font-bold dark:text-white">{selectedStudent?.name}</h4>
              <div className="mt-2 flex justify-between text-xs dark:text-gray-400">
                <span>Total: ₹{selectedStudent?.total_fees}</span>
                <span>Paid: ₹{selectedStudent?.fees_paid}</span>
                <span className="font-bold text-indigo-600">Pending: ₹{selectedStudent?.total_fees - selectedStudent?.fees_paid}</span>
              </div>
            </div>
            <form onSubmit={handlePaySubmit} className="space-y-4">
              <Input 
                label="Installment Amount (₹)" 
                type="number" 
                min="1"
                value={installmentData.amount} 
                onChange={e => setInstallmentData({...installmentData, amount: e.target.value})} 
                required 
                max={selectedStudent?.total_fees - selectedStudent?.fees_paid}
              />
              <Input 
                label="Remarks" 
                value={installmentData.remarks} 
                onChange={e => setInstallmentData({...installmentData, remarks: e.target.value})} 
              />
              <Input 
                label="Payment Date" 
                type="date" 
                value={installmentData.payment_date} 
                onChange={e => setInstallmentData({...installmentData, payment_date: e.target.value})} 
                required 
              />
              <div className="flex gap-3 pt-4">
                <Button type="button" variant="secondary" className="flex-1" onClick={() => setIsPayModalOpen(false)}>Cancel</Button>
                <Button type="submit" className="flex-1 text-green-600">Confirm Payment</Button>
              </div>
            </form>
          </>
        )}
      </Modal>

      {/* Payment History Modal */}
      <Modal 
        isOpen={isHistoryModalOpen} 
        onClose={() => setIsHistoryModalOpen(false)} 
        title={`Payment History: ${selectedStudent?.name}`}
      >
        <div className="space-y-6">
          <div className="grid grid-cols-2 gap-4">
            <div className="p-3 bg-gray-50 dark:bg-slate-800 rounded-xl">
              <p className="text-[10px] text-gray-500 uppercase font-bold">Total Fees</p>
              <p className="text-lg font-bold dark:text-white">₹{selectedStudent?.total_fees}</p>
            </div>
            <div className="p-3 bg-indigo-50 dark:bg-indigo-900/20 rounded-xl">
              <p className="text-[10px] text-indigo-600 uppercase font-bold">Remaining</p>
              <p className="text-lg font-bold text-indigo-600">₹{selectedStudent?.total_fees - selectedStudent?.fees_paid}</p>
            </div>
          </div>

          <div className="overflow-hidden rounded-xl border border-gray-100 dark:border-slate-800">
            <table className="w-full text-left text-sm">
              <thead className="bg-gray-50 dark:bg-slate-800/50">
                <tr>
                  <th className="px-4 py-3 font-bold text-gray-500">Date</th>
                  <th className="px-4 py-3 font-bold text-gray-500">Amount</th>
                  <th className="px-4 py-3 font-bold text-gray-500">Remark</th>
                  <th className="px-4 py-3 font-bold text-gray-500 text-right">Action</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-100 dark:divide-slate-800">
                {historyData.length > 0 ? historyData.map((item) => (
                  <tr key={item.id}>
                    <td className="px-4 py-3 dark:text-gray-300">{item.payment_date}</td>
                    <td className="px-4 py-3 font-bold dark:text-white">₹{item.amount}</td>
                    <td className="px-4 py-3 text-xs text-gray-500">{item.remarks || '-'}</td>
                    <td className="px-4 py-3 text-right">
                      <button 
                        onClick={() => generateReceipt(selectedStudent, item)}
                        className="text-indigo-600 hover:text-indigo-700 text-xs font-bold flex items-center justify-end gap-1 ml-auto"
                      >
                        <Download size={14} /> Receipt
                      </button>
                    </td>
                  </tr>
                )) : (
                  <tr>
                    <td colSpan="3" className="px-4 py-8 text-center text-gray-500">No installments found.</td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
          
          <Button className="w-full" onClick={() => setIsHistoryModalOpen(false)}>Close</Button>
        </div>
      </Modal>
    </div>
  );
};

export default Students;
