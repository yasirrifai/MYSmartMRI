import React from 'react';
import { Link } from 'react-router-dom';

function Sidebar() {
  return (
    <aside className="bg-white w-64 p-6 shadow-md">
      <h2 className="text-2xl font-bold mb-6">MYSmartMRI</h2>
      <nav className="flex flex-col space-y-2">
        <Link to="/dashboard" className="text-gray-700 hover:bg-gray-200 p-2 rounded-lg">Dashboard</Link>
        <Link to="/scans" className="text-gray-700 hover:bg-gray-200 p-2 rounded-lg">Scan</Link>
        <Link to="/patients" className="text-gray-700 hover:bg-gray-200 p-2 rounded-lg">Patients</Link>
        <Link to="/reports" className="text-gray-700 hover:bg-gray-200 p-2 rounded-lg">Reports</Link>
      </nav>
    </aside>
  );
}

export default Sidebar;
