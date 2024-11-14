import React from 'react';
import logo from '../../assets/MYSmartMRI.png';
import { Link } from 'react-router-dom';


function Navbar() {
  return (
    <header className="p-4 bg-white shadow-md flex justify-between items-center">
        <img src={logo} alt="Logo" className="h-10" />
        <nav className="space-x-6">
          <a href="#home" className="text-gray-600">Home</a>
          <a href="#about" className="text-gray-600">About Us</a>
          <a href="#services" className="text-gray-600">Service</a>
          <a href="#contact" className="text-gray-600">Contact Us</a>
          <Link to="/login" className="text-gray-600">Login</Link>
        </nav>
      </header>
  );
}

export default Navbar;
