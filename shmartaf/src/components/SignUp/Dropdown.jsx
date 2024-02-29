// src/components/Dropdown.jsx
import React from 'react';

const Dropdown = ({ label, options, value, onChange }) => {
    return (
        <div className="mb-4">
            <label className="block text-sm font-medium text-gray-900 dark:text-white">{label}</label>
            <select
                value={value}
                onChange={(e) => onChange(e.target.value)}
                className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            >
                {options.map((option) => (
                    <option key={option.value} value={option.value}>
                        {option.label}
                    </option>
                ))}
            </select>
        </div>
    );
};

export default Dropdown;
