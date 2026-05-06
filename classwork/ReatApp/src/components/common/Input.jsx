import React from 'react';
import { twMerge } from 'tailwind-merge';

const Input = ({ label, error, className, ...props }) => {
  return (
    <div className="w-full space-y-1.5">
      {label && (
        <label className="text-sm font-semibold text-gray-700 dark:text-gray-300 ml-1">
          {label}
        </label>
      )}
      <input
        className={twMerge(
          'w-full px-4 py-2.5 rounded-xl border border-gray-200 bg-white/50 backdrop-blur-sm outline-none transition-all duration-300 focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500 dark:bg-slate-900/50 dark:border-slate-800 dark:text-white',
          error && 'border-red-500 focus:ring-red-500/20 focus:border-red-500',
          className
        )}
        {...props}
      />
      {error && <p className="text-xs text-red-500 ml-1 mt-1">{error}</p>}
    </div>
  );
};

export default Input;
