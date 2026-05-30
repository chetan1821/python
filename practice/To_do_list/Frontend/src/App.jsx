import { useState, useEffect, useMemo } from 'react'
import { 
  ListTodo, Plus, Trash2, Edit3, Search, Sparkles, 
  AlertCircle, CheckCircle2, Circle, Clock, Check, X, 
  RefreshCw
} from 'lucide-react'
import './App.css'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/todo/tasks/';

function App() {
  const [tasks, setTasks] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  
  // Search & Filter State
  const [searchQuery, setSearchQuery] = useState('')
  const [filter, setFilter] = useState('all') // 'all' | 'active' | 'completed'
  
  // Form State
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')
  const [editingTask, setEditingTask] = useState(null)
  const [submitting, setSubmitting] = useState(false)
  
  // Toast notifications state
  const [toasts, setToasts] = useState([])

  // Toast Helper
  const addToast = (message, type = 'success') => {
    const id = Date.now()
    setToasts(prev => [...prev, { id, message, type }])
    setTimeout(() => {
      removeToast(id)
    }, 4000)
  }

  const removeToast = (id) => {
    setToasts(prev => prev.filter(toast => toast.id !== id))
  }

  // Fetch all tasks
  const fetchTasks = async () => {
    setLoading(true)
    setError(null)
    try {
      const response = await fetch(API_URL)
      if (!response.ok) {
        throw new Error(`Failed to fetch tasks: ${response.status} ${response.statusText}`)
      }
      const data = await response.json()
      setTasks(data)
    } catch (err) {
      console.error(err)
      setError('Could not connect to the backend server. Please make sure the Django server is running on http://localhost:8000')
      addToast('Backend connection failed', 'error')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchTasks()
  }, [])

  // Add or Update Task
  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!title.trim()) return

    setSubmitting(true)
    const taskData = {
      title: title.trim(),
      description: description.trim(),
      completed: editingTask ? editingTask.completed : false
    }

    try {
      let url = API_URL
      let method = 'POST'

      if (editingTask) {
        url = `${API_URL}${editingTask.id}/`
        method = 'PUT'
      }

      const response = await fetch(url, {
        method,
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(taskData)
      })

      if (!response.ok) {
        throw new Error('Failed to save the task.')
      }

      const savedTask = await response.json()

      if (editingTask) {
        setTasks(prev => prev.map(t => t.id === editingTask.id ? savedTask : t))
        addToast('Task updated successfully', 'success')
      } else {
        setTasks(prev => [savedTask, ...prev])
        addToast('Task created successfully', 'success')
      }

      // Reset form
      handleCancelEdit()
    } catch (err) {
      console.error(err)
      addToast('Failed to save task. Try again.', 'error')
    } finally {
      setSubmitting(false)
    }
  }

  // Delete Task
  const handleDelete = async (id) => {
    const originalTasks = [...tasks]
    // Optimistic UI update
    setTasks(prev => prev.filter(t => t.id !== id))
    addToast('Task deleted', 'info')

    try {
      const response = await fetch(`${API_URL}${id}/`, {
        method: 'DELETE'
      })

      if (!response.ok) {
        throw new Error('Failed to delete')
      }
    } catch (err) {
      console.error(err)
      // Rollback
      setTasks(originalTasks)
      addToast('Failed to delete task from server', 'error')
    }
  }

  // Toggle Completed status
  const handleToggleComplete = async (task) => {
    const updatedStatus = !task.completed
    const originalTasks = [...tasks]

    // Optimistic update
    setTasks(prev => prev.map(t => t.id === task.id ? { ...t, completed: updatedStatus } : t))
    addToast(updatedStatus ? 'Task completed! 🎉' : 'Task marked active', 'success')

    try {
      const response = await fetch(`${API_URL}${task.id}/`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ completed: updatedStatus })
      })

      if (!response.ok) {
        throw new Error('Failed to update status')
      }
    } catch (err) {
      console.error(err)
      // Rollback
      setTasks(originalTasks)
      addToast('Failed to sync completion status', 'error')
    }
  }

  const handleEditClick = (task) => {
    setEditingTask(task)
    setTitle(task.title)
    setDescription(task.description || '')
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }

  const handleCancelEdit = () => {
    setEditingTask(null)
    setTitle('')
    setDescription('')
  }

  // Statistics calculation
  const stats = useMemo(() => {
    const total = tasks.length
    const completed = tasks.filter(t => t.completed).length
    const pending = total - completed
    const rate = total > 0 ? Math.round((completed / total) * 100) : 0
    return { total, completed, pending, rate }
  }, [tasks])

  // Filter and Search logic
  const filteredTasks = useMemo(() => {
    return tasks
      .filter(task => {
        if (filter === 'completed') return task.completed
        if (filter === 'active') return !task.completed
        return true
      })
      .filter(task => {
        const query = searchQuery.toLowerCase()
        return (
          task.title.toLowerCase().includes(query) ||
          (task.description && task.description.toLowerCase().includes(query))
        )
      })
  }, [tasks, filter, searchQuery])

  const formatDate = (dateString) => {
    const date = new Date(dateString)
    return date.toLocaleDateString(undefined, {
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    })
  }

  return (
    <div className="app-container">
      {/* Toast Notifications */}
      <div className="toasts-container">
        {toasts.map(toast => (
          <div key={toast.id} className={`toast ${toast.type}`}>
            <span className={`toast-icon ${toast.type}`}>
              {toast.type === 'success' && <Check size={18} />}
              {toast.type === 'error' && <AlertCircle size={18} />}
              {toast.type === 'info' && <Sparkles size={18} />}
            </span>
            <div className="toast-content">{toast.message}</div>
            <button className="toast-close" onClick={() => removeToast(toast.id)}>
              <X size={14} />
            </button>
          </div>
        ))}
      </div>

      {/* Header */}
      <header className="app-header">
        <div className="brand">
          <ListTodo className="brand-icon" size={32} />
          <div>
            <h1>TaskFlow</h1>
            <p>Manage your tasks with premium speed & visual clarity</p>
          </div>
        </div>
        <button 
          className="btn-icon" 
          onClick={fetchTasks} 
          title="Refresh tasks from server"
          disabled={loading}
        >
          <RefreshCw size={18} className={loading ? 'spin' : ''} />
        </button>
      </header>

      {/* Statistics Banner */}
      <section className="stats-grid">
        <div className="stat-card">
          <div className="stat-icon total">
            <ListTodo size={22} />
          </div>
          <div className="stat-info">
            <span className="stat-label">Total Tasks</span>
            <span className="stat-value">{stats.total}</span>
          </div>
        </div>
        <div className="stat-card">
          <div className="stat-icon completed">
            <CheckCircle2 size={22} />
          </div>
          <div className="stat-info">
            <span className="stat-label">Completed</span>
            <span className="stat-value">{stats.completed}</span>
          </div>
        </div>
        <div className="stat-card">
          <div className="stat-icon pending">
            <Circle size={22} />
          </div>
          <div className="stat-info">
            <span className="stat-label">Pending</span>
            <span className="stat-value">{stats.pending}</span>
          </div>
        </div>
        <div className="stat-card">
          <div className="stat-icon rate">
            <Sparkles size={22} />
          </div>
          <div className="stat-info">
            <span className="stat-label">Success Rate</span>
            <span className="stat-value">{stats.rate}%</span>
          </div>
        </div>
      </section>

      {/* Main Content Grid */}
      <main className="main-layout">
        
        {/* Sidebar Form */}
        <section className="task-form-sidebar">
          <form className="task-form-container" onSubmit={handleSubmit}>
            <h2 className="form-title">
              <Sparkles size={18} className="brand-icon" />
              {editingTask ? 'Edit Task' : 'Create New Task'}
            </h2>

            <div className="form-group">
              <label htmlFor="task-title">Task Title</label>
              <input
                id="task-title"
                type="text"
                placeholder="What needs to be done?"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                maxLength={200}
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="task-desc">Description (Optional)</label>
              <textarea
                id="task-desc"
                placeholder="Add more details about this task..."
                value={description}
                onChange={(e) => setDescription(e.target.value)}
              />
            </div>

            <div className="form-actions">
              <button 
                type="submit" 
                className="btn-primary"
                disabled={submitting || !title.trim()}
              >
                {editingTask ? <Check size={18} /> : <Plus size={18} />}
                {submitting ? 'Saving...' : editingTask ? 'Update Task' : 'Add Task'}
              </button>
              
              {editingTask && (
                <button 
                  type="button" 
                  className="btn-secondary" 
                  onClick={handleCancelEdit}
                >
                  Cancel Edit
                </button>
              )}
            </div>
          </form>
        </section>

        {/* Tasks List Section */}
        <section className="tasks-feed">
          {/* Toolbar */}
          <div className="toolbar">
            <div className="search-box">
              <Search className="search-icon" size={16} />
              <input
                type="text"
                className="search-input"
                placeholder="Search tasks..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
              />
            </div>

            <div className="filter-tabs">
              <button
                className={`filter-tab ${filter === 'all' ? 'active' : ''}`}
                onClick={() => setFilter('all')}
              >
                All
              </button>
              <button
                className={`filter-tab ${filter === 'active' ? 'active' : ''}`}
                onClick={() => setFilter('active')}
              >
                Active
              </button>
              <button
                className={`filter-tab ${filter === 'completed' ? 'active' : ''}`}
                onClick={() => setFilter('completed')}
              >
                Completed
              </button>
            </div>
          </div>

          {/* Loading, Error or List Content */}
          {loading ? (
            <div className="loading-container">
              <div className="loader"></div>
              <p>Fetching tasks from server...</p>
            </div>
          ) : error ? (
            <div className="error-container">
              <AlertCircle size={32} />
              <h3>Server Connection Offline</h3>
              <p>{error}</p>
              <button className="btn-primary" onClick={fetchTasks} style={{ marginTop: '8px' }}>
                <RefreshCw size={16} style={{ marginRight: '6px' }} /> Retry Connection
              </button>
            </div>
          ) : filteredTasks.length === 0 ? (
            <div className="empty-state">
              <ListTodo size={40} className="empty-icon" />
              <h3>No tasks found</h3>
              <p>
                {searchQuery 
                  ? 'No tasks match your search query.' 
                  : filter === 'completed' 
                    ? 'You have not completed any tasks yet.' 
                    : filter === 'active' 
                      ? 'No active tasks! Enjoy your free time.' 
                      : 'Get started by creating your first task in the left sidebar!'}
              </p>
            </div>
          ) : (
            <div className="tasks-list">
              {filteredTasks.map(task => (
                <div key={task.id} className={`task-card ${task.completed ? 'completed' : ''}`}>
                  
                  {/* Status checkbox */}
                  <label className="checkbox-container">
                    <input
                      type="checkbox"
                      checked={task.completed}
                      onChange={() => handleToggleComplete(task)}
                    />
                    <span className="checkmark"></span>
                  </label>

                  {/* Task Content */}
                  <div className="task-content">
                    <div className="task-title">{task.title}</div>
                    {task.description && (
                      <div className="task-desc">{task.description}</div>
                    )}
                    <div className="task-meta">
                      <div className="task-meta-item">
                        <Clock size={12} />
                        <span>{formatDate(task.created_at)}</span>
                      </div>
                    </div>
                  </div>

                  {/* Actions */}
                  <div className="task-actions">
                    <button 
                      className="btn-icon edit" 
                      onClick={() => handleEditClick(task)}
                      title="Edit task title/description"
                    >
                      <Edit3 size={16} />
                    </button>
                    <button 
                      className="btn-icon delete" 
                      onClick={() => handleDelete(task.id)}
                      title="Delete task permanently"
                    >
                      <Trash2 size={16} />
                    </button>
                  </div>

                </div>
              ))}
            </div>
          )}
        </section>

      </main>
    </div>
  )
}

export default App
