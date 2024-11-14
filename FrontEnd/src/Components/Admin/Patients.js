import React from 'react';

function Patients() {
  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h1 className="text-3xl font-bold mb-4">All Patients</h1>
      <table className="min-w-full bg-white shadow-md rounded-lg overflow-hidden">
        <thead>
          <tr className="bg-gray-200 text-left text-sm font-semibold">
            <th className="p-3">Patient Name</th>
            <th className="p-3">Disease</th>
            <th className="p-3">Phone Number</th>
            <th className="p-3">Email</th>
            <th className="p-3">Hospital</th>
            <th className="p-3">Status</th>
          </tr>
        </thead>
        <tbody>
          <tr className="border-b">
            <td className="p-3">Jane Cooper</td>
            <td className="p-3">Brain Tumor</td>
            <td className="p-3">(205) 555-0100</td>
            <td className="p-3">jane@example.com</td>
            <td className="p-3">Lanka Hospital</td>
            <td className="p-3 text-green-600">Detected</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default Patients;
