import React from 'react';

function WhoWeAre() {
  return (
    <section className="py-12 bg-gray-100 text-center">
        <h2 className="text-3xl font-semibold">Who are we?</h2>
        <div className="flex justify-center mt-8 space-x-8 max-w-4xl mx-auto">
          <div className="bg-white p-4 rounded-lg shadow-lg w-1/3">
            <h3 className="font-semibold">Overview</h3>
            <p className="text-sm mt-2">MYSmartMRI Diagnostics offers advanced MRI interpretation with AI.</p>
          </div>
          <div className="bg-white p-4 rounded-lg shadow-lg w-1/3">
            <h3 className="font-semibold">Why Choose Us?</h3>
            <p className="text-sm mt-2">Our AI technology provides precise, fast, and reliable MRI diagnostics.</p>
          </div>
          <div className="bg-white p-4 rounded-lg shadow-lg w-1/3">
            <h3 className="font-semibold">Project Background</h3>
            <p className="text-sm mt-2">Developed to improve diagnostic accuracy and streamline healthcare.</p>
          </div>
        </div>
      </section>
  );
}

export default WhoWeAre;
