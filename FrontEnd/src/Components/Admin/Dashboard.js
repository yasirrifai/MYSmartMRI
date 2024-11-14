import React from 'react';

function Dashboard() {
  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h1 className="text-3xl font-bold mb-4">Welcome To MYSmartMRI !</h1>
      <div className="flex space-x-4 mb-8">
        <div className="bg-green-100 p-4 rounded-lg text-center flex-1">
          <p className="text-4xl font-bold">423</p>
          <p>Total Patients Scanned</p>
        </div>
        <div className="bg-blue-100 p-4 rounded-lg text-center flex-1">
          <p className="text-4xl font-bold">93</p>
          <p>Disease Diagnosed</p>
        </div>
      </div>

    </div>
  );
}

export default Dashboard;
