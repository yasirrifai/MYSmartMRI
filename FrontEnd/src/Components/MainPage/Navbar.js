import React from 'react';
import logo from '../../assets/MYSmartMRI.png';


function Navbar() {
  return (
    <header className="p-4 bg-white shadow-md flex justify-between items-center">
        <img src={logo} alt="Logo" className="h-10" />
        <nav className="space-x-6">
          <a href="#home" className="text-gray-600">Home</a>
          <a href="#about" className="text-gray-600">About Us</a>
          <a href="#services" className="text-gray-600">Service</a>
          <a href="#contact" className="text-gray-600">Contact Us</a>
          <a href="#login" className="text-gray-600">Login</a>
        </nav>
      </header>
  );
}

export default Navbar;
