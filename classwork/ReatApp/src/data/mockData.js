export const mockStats = {
  totalStudents: 1250,
  totalCourses: 24,
  feesCollected: 450000,
  pendingFees: 75000,
  studentGrowth: [
    { name: 'Jan', students: 400 },
    { name: 'Feb', students: 600 },
    { name: 'Mar', students: 800 },
    { name: 'Apr', students: 1000 },
    { name: 'May', students: 1250 },
  ],
  revenueData: [
    { name: 'Jan', amount: 50000 },
    { name: 'Feb', amount: 80000 },
    { name: 'Mar', amount: 45000 },
    { name: 'Apr', amount: 90000 },
    { name: 'May', amount: 75000 },
  ],
};

export const mockStudents = [
  { id: 1, name: 'Alice Johnson', email: 'alice@example.com', course: 'React Mastery', fees: 'Paid', joinedDate: '2026-01-15' },
  { id: 2, name: 'Bob Smith', email: 'bob@example.com', course: 'UI/UX Design', fees: 'Pending', joinedDate: '2026-02-10' },
  { id: 3, name: 'Charlie Brown', email: 'charlie@example.com', course: 'Full Stack Dev', fees: 'Paid', joinedDate: '2026-03-05' },
  { id: 4, name: 'Diana Prince', email: 'diana@example.com', course: 'React Mastery', fees: 'Pending', joinedDate: '2026-03-20' },
  { id: 5, name: 'Ethan Hunt', email: 'ethan@example.com', course: 'Data Science', fees: 'Paid', joinedDate: '2026-04-12' },
];

export const mockTeachers = [
  { id: 1, name: 'Dr. Sarah Connor', subject: 'Computer Science', courses: 4, joinedDate: '2025-11-01' },
  { id: 2, name: 'Prof. Xavier', subject: 'Psychology', courses: 2, joinedDate: '2025-12-15' },
  { id: 3, name: 'Tony Stark', subject: 'Robotics', courses: 5, joinedDate: '2026-01-10' },
];

export const mockCourses = [
  { id: 1, name: 'React Mastery', teacher: 'Dr. Sarah Connor', duration: '3 Months', fees: 15000 },
  { id: 2, name: 'UI/UX Design', teacher: 'Prof. Xavier', duration: '2 Months', fees: 10000 },
  { id: 3, name: 'Full Stack Dev', teacher: 'Tony Stark', duration: '6 Months', fees: 45000 },
];

export const mockNotices = [
  { id: 1, title: 'Summer Vacations', content: 'The institute will be closed from June 1st to June 15th.', date: '2026-05-01', priority: 'High' },
  { id: 2, title: 'New Batch Alert', content: 'New React Mastery batch starts from June 20th.', date: '2026-05-02', priority: 'Medium' },
];
export const mockExams = [
  { id: 1, title: 'React Basics Quiz', course: 'React Mastery', duration: '30 mins', totalMarks: 50, date: '2026-05-10', status: 'Upcoming' },
  { id: 2, title: 'CSS Layouts Mastery', course: 'UI/UX Design', duration: '45 mins', totalMarks: 100, date: '2026-05-04', status: 'Active' },
  { id: 3, title: 'Node.js Fundamentals', course: 'Full Stack Dev', duration: '60 mins', totalMarks: 100, date: '2026-04-25', status: 'Completed' },
];

export const mockResults = [
  { id: 1, studentName: 'Alice Johnson', examTitle: 'Node.js Fundamentals', marks: 85, total: 100, grade: 'A' },
  { id: 2, studentName: 'Charlie Brown', examTitle: 'Node.js Fundamentals', marks: 92, total: 100, grade: 'A+' },
];
