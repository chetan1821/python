import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import Input from '../components/common/Input';
import Button from '../components/common/Button';
import { LogIn } from 'lucide-react';

const Login = () => {
  const [username, setUsername] = useState('admin');
  const [password, setPassword] = useState('password123');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    const result = await login(username, password);
    
    if (result.success) {
      navigate('/dashboard');
    } else {
      setError(result.error);
    }
    setLoading(false);
  };

  return (
    <div className="space-y-6">
      <div className="text-center space-y-2">
        <h1 className="text-3xl font-bold text-white tracking-tight">Welcome to <span className="text-orange-400">Enjoy</span></h1>
        <p className="text-indigo-100/70">Login to manage your institute</p>
      </div>

      <form onSubmit={handleSubmit} className="space-y-4">
        {error && (
          <div className="bg-red-500/20 border border-red-500/50 text-red-200 p-3 rounded-xl text-sm text-center">
            {error}
          </div>
        )}
        
        <Input
          label="Username"
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="admin"
          className="bg-white/20 border-white/10 text-white placeholder:text-indigo-200/50 focus:border-white/50"
        />

        <Input
          label="Password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="••••••••"
          className="bg-white/20 border-white/10 text-white placeholder:text-indigo-200/50 focus:border-white/50"
        />

        <div className="text-right">
          <a href="#" className="text-sm text-indigo-100 hover:underline">Forgot password?</a>
        </div>

        <Button 
          type="submit" 
          disabled={loading}
          className="w-full py-3 text-lg font-bold"
        >
          {loading ? 'Logging in...' : (
            <span className="flex items-center gap-2">
              <LogIn size={20} /> Sign In
            </span>
          )}
        </Button>
      </form>

      <div className="text-center text-indigo-100/60 text-sm">
        Don't have an account? <a href="#" className="text-white font-semibold hover:underline">Contact Support</a>
      </div>
    </div>
  );
};

export default Login;
