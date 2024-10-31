import React from 'react';
import heroImage from '../../assets/hero.jpg'


function Hero() {
  return (
    <section className="bg-cover bg-center h-96 flex items-center text-center text-black" style={{ backgroundImage: `url(${heroImage})` }}>
    <div>
      <h1 className="text-4xl font-bold">Welcome to MYSmartMRI Diagnostics</h1>
      <p className="mt-4 text-lg">Using AI to enhance diagnostic accuracy in MRI interpretation.</p>
    </div>
  </section>
  );
}

export default Hero;
