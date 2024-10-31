import React from 'react';

function Footer() {
  return (
    <footer className="py-4 bg-blue-500 text-white text-center">
    <p>© 2024 MYSmartMRI. All Rights Reserved.</p>
    <div className="flex justify-center space-x-4 mt-4">
      <a href="#" className="text-white">Home</a>
      <a href="#" className="text-white">About Us</a>
      <a href="#" className="text-white">Service</a>
      <a href="#" className="text-white">Contact Us</a>
    </div>
  </footer>

  );
}

export default Footer;
