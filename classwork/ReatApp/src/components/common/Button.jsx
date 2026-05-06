import React from 'react';
import { clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

const Button = ({ children, variant = 'primary', className, ...props }) => {
  const variants = {
    primary: 'bg-premium-gradient text-white shadow-lg shadow-indigo-500/30 hover:shadow-indigo-500/50 hover:brightness-110',
    secondary: 'bg-white text-gray-700 border border-gray-200 hover:bg-gray-50 dark:bg-slate-800 dark:text-gray-200 dark:border-slate-700 dark:hover:bg-slate-700',
    danger: 'bg-red-500 text-white shadow-lg shadow-red-500/30 hover:bg-red-600',
    ghost: 'bg-transparent hover:bg-gray-100 dark:hover:bg-slate-800 text-gray-600 dark:text-gray-400',
  };

  return (
    <button
      className={twMerge(
        'premium-button flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed',
        variants[variant],
        className
      )}
      {...props}
    >
      {children}
    </button>
  );
};

export default Button;
