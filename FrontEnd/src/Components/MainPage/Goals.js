import React from 'react';
import goalImage1 from '../../assets/goal1.jpg'
import goalImage2 from '../../assets/goal2.png'
import goalImage3 from '../../assets/goal3.avif'

function Goals() {
  return (
    <section className="py-12 bg-gray-100 text-center">
    <h2 className="text-3xl font-semibold mb-6">Our Goals</h2>
    <div className="flex justify-center space-x-8 max-w-4xl mx-auto">
      <div className="bg-white p-4 rounded-lg shadow-lg w-1/3">
        <img src={goalImage1} alt="Goal 1" className="h-24 mx-auto" />
        <h3 className="mt-4 font-semibold">MRI Image Analysis</h3>
        <p className="text-sm mt-2">Providing accurate MRI image interpretations with AI.</p>
      </div>
      <div className="bg-white p-4 rounded-lg shadow-lg w-1/3">
        <img src={goalImage2} alt="Goal 2" className="h-24 mx-auto" />
        <h3 className="mt-4 font-semibold">Diagnostic Reports</h3>
        <p className="text-sm mt-2">Generate detailed reports for each MRI analysis.</p>
      </div>
      <div className="bg-white p-4 rounded-lg shadow-lg w-1/3">
        <img src={goalImage3} alt="Goal 3" className="h-24 mx-auto" />
        <h3 className="mt-4 font-semibold">Training Resources</h3>
        <p className="text-sm mt-2">Providing resources for medical professionals to learn AI technology.</p>
      </div>
    </div>
  </section>
  );
}

export default Goals;
