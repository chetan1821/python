import React, { useState, useEffect } from 'react';
import { IndianRupee, Search, Download, Filter, Loader2, Calendar, History, Wallet, CheckCircle2, ChevronLeft, ChevronRight } from 'lucide-react';
import Card from '../components/common/Card';
import Button from '../components/common/Button';
import { getStudents, getStudentInstallments, addInstallment, getDashboardStats } from '../data/api';
import { useAuth } from '../context/AuthContext';
import { generateReceipt } from '../utils/receiptGenerator';

const Fees = () => {
  const { user } = useAuth();
  const [loading, setLoading] = useState(true);
  const [isStudent, setIsStudent] = useState(false);
  const [studentData, setStudentData] = useState(null);
  const [installments, setInstallments] = useState([]);
  
  // Management states
  const [allStudents, setAllStudents] = useState([]);
  const [stats, setStats] = useState({ total: 0, collected: 0, pending: 0 });
  const [searchTerm, setSearchTerm] = useState('');
  
  // Pagination state
  const [currentPage, setCurrentPage] = useState(1);
  const [paginationInfo, setPaginationInfo] = useState({
    count: 0,
    next: null,
    previous: null
  });

  useEffect(() => {
    fetchData(currentPage, searchTerm);
  }, [currentPage]);

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
      if (user?.role === 'student') {
        setIsStudent(true);
        const res = await getStudents();
        const studentList = res.data.results || res.data;
        const me = studentList.find(s => s.email === user.email);
        if (me) {
          setStudentData(me);
          const payRes = await getStudentInstallments(me.id);
          setInstallments(payRes.data.results || payRes.data);
        }
      } else {
        const [studentsRes, statsRes] = await Promise.all([
            getStudents({ page, search }),
            getDashboardStats()
        ]);

        if (studentsRes.data.results) {
            setAllStudents(studentsRes.data.results);
            setPaginationInfo({
                count: studentsRes.data.count,
                next: studentsRes.data.next,
                previous: studentsRes.data.previous
            });
        } else {
            setAllStudents(studentsRes.data);
        }

        if (statsRes.data) {
            setStats({
                total: statsRes.data.totalExpected || 0,
                collected: statsRes.data.feesCollected || 0,
                pending: statsRes.data.pendingFees || 0
            });
        }
      }
    } catch (error) {
      console.error("Error fetching fee data:", error);
    } finally {
      setLoading(false);
    }
  };

  if (loading && !allStudents.length) return <div className="h-[60vh] flex items-center justify-center"><Loader2 className="animate-spin text-indigo-600" size={40} /></div>;

  if (isStudent) {
    return (
      <div className="space-y-8">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <h1 className="text-3xl font-bold dark:text-white tracking-tight">Financial Status</h1>
            <p className="text-gray-500 mt-1">Review your course fees and payment history.</p>
          </div>
          <Button onClick={() => window.print()} variant="secondary">
            <Download size={18} /> Statement of Account
          </Button>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <Card className="bg-premium-gradient border-none text-white shadow-xl shadow-indigo-500/20">
            <div className="flex items-center gap-3 mb-4">
              <div className="p-2 bg-white/20 rounded-lg">
                <IndianRupee size={20} />
              </div>
              <p className="text-sm font-bold opacity-80 uppercase">Total Fees</p>
            </div>
            <h2 className="text-4xl font-black">₹{studentData?.total_fees || 0}</h2>
            <p className="text-xs mt-4 opacity-60">Base amount for {studentData?.course_name}</p>
          </Card>
          
          <Card className="bg-green-500 border-none text-white shadow-xl shadow-green-500/20">
            <div className="flex items-center gap-3 mb-4">
              <div className="p-2 bg-white/20 rounded-lg">
                <CheckCircle2 size={20} />
              </div>
              <p className="text-sm font-bold opacity-80 uppercase">Fees Paid</p>
            </div>
            <h2 className="text-4xl font-black">₹{studentData?.fees_paid || 0}</h2>
            <div className="mt-4 h-1.5 w-full bg-white/20 rounded-full overflow-hidden">
              <div className="h-full bg-white" style={{ width: `${((studentData?.fees_paid || 0) / (studentData?.total_fees || 1)) * 100}%` }}></div>
            </div>
          </Card>

          <Card className="bg-orange-500 border-none text-white shadow-xl shadow-orange-500/20">
            <div className="flex items-center gap-3 mb-4">
              <div className="p-2 bg-white/20 rounded-lg">
                <Wallet size={20} />
              </div>
              <p className="text-sm font-bold opacity-80 uppercase">Remaining</p>
            </div>
            <h2 className="text-4xl font-black">₹{(studentData?.total_fees || 0) - (studentData?.fees_paid || 0)}</h2>
            <p className="text-xs mt-4 opacity-80 font-bold underline">Due immediately</p>
          </Card>
        </div>

        <Card>
          <div className="flex items-center gap-3 mb-8">
            <div className="p-2 bg-indigo-100 dark:bg-indigo-900/30 text-indigo-600 rounded-xl">
              <History size={20} />
            </div>
            <h3 className="font-bold text-xl dark:text-white">Transaction History</h3>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-left">
              <thead>
                <tr className="border-b border-gray-100 dark:border-slate-800 text-xs text-gray-500 uppercase font-bold">
                  <th className="pb-4">Payment Date</th>
                  <th className="pb-4">Reference ID</th>
                  <th className="pb-4">Amount</th>
                  <th className="pb-4">Remarks</th>
                  <th className="pb-4 text-right">Receipt</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-50 dark:divide-slate-800/50">
                {installments.length > 0 ? installments.map((pay) => (
                  <tr key={pay.id} className="group hover:bg-gray-50/50 dark:hover:bg-slate-800/30 transition-colors">
                    <td className="py-4 dark:text-white font-medium">{pay.payment_date}</td>
                    <td className="py-4 text-xs text-gray-500 font-mono">#PAY-{pay.id.toString().padStart(6, '0')}</td>
                    <td className="py-4 font-bold text-green-600 dark:text-green-400">₹{pay.amount}</td>
                    <td className="py-4 text-sm text-gray-500">{pay.remarks || 'Standard Installment'}</td>
                    <td className="py-4 text-right">
                      <button 
                        onClick={() => generateReceipt(studentData, pay)}
                        className="p-2 hover:bg-indigo-50 dark:hover:bg-indigo-900/20 text-indigo-600 dark:text-indigo-400 rounded-lg"
                      >
                        <Download size={18} />
                      </button>
                    </td>
                  </tr>
                )) : (
                  <tr>
                    <td colSpan="5" className="py-20 text-center text-gray-500 italic">No transactions found.</td>
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
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold dark:text-white">Fees Management</h1>
          <p className="text-gray-500">Track payments and generate receipts.</p>
        </div>
        <div className="flex items-center gap-3">
          <Button variant="secondary">
            <Filter size={18} /> Filters
          </Button>
          <Button onClick={() => window.print()}>
            <Download size={18} /> Financial Report
          </Button>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <Card className="bg-premium-gradient text-white border-none shadow-lg">
          <p className="text-indigo-100 text-xs font-bold uppercase tracking-wider">Total Expected</p>
          <h2 className="text-3xl font-black mt-1">₹{stats.total.toLocaleString()}</h2>
          <div className="mt-4 flex items-center gap-2 text-[10px] text-indigo-100 font-bold">
            <span className="bg-white/20 px-2 py-0.5 rounded-full uppercase">All Active Students</span>
          </div>
        </Card>
        <Card>
          <p className="text-gray-500 text-xs font-bold uppercase tracking-wider">Collected</p>
          <h2 className="text-3xl font-black mt-1 dark:text-white text-green-600">₹{stats.collected.toLocaleString()}</h2>
          <div className="mt-4 h-2 w-full bg-gray-100 dark:bg-slate-800 rounded-full overflow-hidden">
            <div className="h-full bg-green-500" style={{ width: `${(stats.collected / (stats.total || 1)) * 100}%` }}></div>
          </div>
        </Card>
        <Card>
          <p className="text-gray-500 text-xs font-bold uppercase tracking-wider">Pending</p>
          <h2 className="text-3xl font-black mt-1 dark:text-white text-orange-600">₹{stats.pending.toLocaleString()}</h2>
          <div className="mt-4 h-2 w-full bg-gray-100 dark:bg-slate-800 rounded-full overflow-hidden">
            <div className="h-full bg-orange-500" style={{ width: `${(stats.pending / (stats.total || 1)) * 100}%` }}></div>
          </div>
        </Card>
      </div>

      <Card>
        <div className="flex items-center gap-4 mb-6">
          <div className="relative flex-1">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" size={18} />
            <input 
              type="text" 
              placeholder="Search by student name..." 
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full bg-gray-50 dark:bg-slate-800/50 border border-gray-200 dark:border-slate-800 rounded-xl py-2.5 pl-10 pr-4 outline-none focus:ring-2 focus:ring-indigo-500/20 dark:text-white"
            />
          </div>
        </div>

        <div className="overflow-x-auto min-h-[400px] relative">
          {loading && (
            <div className="absolute inset-0 bg-white/50 dark:bg-slate-900/50 backdrop-blur-sm z-10 flex items-center justify-center rounded-xl">
                <Loader2 className="w-10 h-10 text-indigo-600 animate-spin" />
            </div>
          )}
          
          <table className="w-full text-left">
            <thead>
              <tr className="border-b border-gray-100 dark:border-slate-800 text-xs text-gray-500 uppercase font-bold">
                <th className="pb-4">Student</th>
                <th className="pb-4">Total Fee</th>
                <th className="pb-4 text-center">Paid</th>
                <th className="pb-4">Status</th>
                <th className="pb-4 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-50 dark:divide-slate-800/50">
              {allStudents.map((student) => (
                <tr key={student.id} className="hover:bg-gray-50/50 dark:hover:bg-slate-800/20 transition-colors">
                  <td className="py-4">
                    <p className="font-bold dark:text-white">{student.name}</p>
                    <p className="text-[10px] text-gray-500 uppercase">{student.course_name}</p>
                  </td>
                  <td className="py-4 font-bold dark:text-white text-sm">₹{student.total_fees}</td>
                  <td className="py-4">
                    <div className="flex flex-col items-center">
                      <p className="text-sm font-black text-indigo-600">₹{student.fees_paid}</p>
                      <div className="w-16 h-1 bg-gray-100 dark:bg-slate-800 rounded-full mt-1 overflow-hidden">
                        <div className="h-full bg-indigo-600" style={{ width: `${(student.fees_paid / student.total_fees) * 100}%` }}></div>
                      </div>
                    </div>
                  </td>
                  <td className="py-4">
                    <span className={`px-3 py-1 rounded-full text-[10px] font-bold uppercase ${
                      student.fees_status === 'Paid' 
                        ? 'bg-green-100 text-green-700 dark:bg-green-900/20' 
                        : student.fees_status === 'Partial' ? 'bg-blue-100 text-blue-700 dark:bg-blue-900/20' : 'bg-red-100 text-red-700 dark:bg-red-900/20'
                    }`}>
                      {student.fees_status}
                    </span>
                  </td>
                  <td className="py-4 text-right">
                    <Button variant="ghost" className="text-indigo-600 font-bold text-xs" onClick={() => generateReceipt(student, { amount: student.fees_paid, payment_date: 'Latest', id: 'LAST' })}>
                      <Download size={14} /> Receipt
                    </Button>
                  </td>
                </tr>
              ))}
              {allStudents.length === 0 && !loading && (
                <tr>
                    <td colSpan="5" className="py-20 text-center text-gray-500 italic">No students found.</td>
                </tr>
              )}
            </tbody>
          </table>

          {/* Pagination Controls */}
          <div className="mt-8 flex items-center justify-between border-t border-gray-100 dark:border-slate-800 pt-6">
              <p className="text-sm text-gray-500">
                  Showing <span className="font-bold text-gray-700 dark:text-gray-300">{(currentPage - 1) * 10 + 1}</span> to <span className="font-bold text-gray-700 dark:text-gray-300">{Math.min(currentPage * 10, paginationInfo.count)}</span> of <span className="font-bold text-gray-700 dark:text-gray-300">{paginationInfo.count}</span> records
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
        </div>
      </Card>
    </div>
  );
};

export default Fees;
