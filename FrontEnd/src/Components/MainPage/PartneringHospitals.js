import React from 'react';
import partner1 from '../../assets/partner1.png';
import partner2 from '../../assets/partner2.png';
import partner3 from '../../assets/partner3.jpeg';


function PartneringHospitals() {
  return (
    <section className="py-12 bg-blue-200 text-center">
    <h2 className="text-3xl font-semibold mb-6">Partnering Hospitals</h2>
    <div className="flex justify-center space-x-6">
      <img src={partner1} alt="Partner 1" className="h-24 w-auto" />
      <img src={partner2} alt="Partner 2" className="h-24 w-auto" />
      <img src={partner3} alt="Partner 3" className="h-24 w-auto" />
    </div>
  </section>
  );
}

export default PartneringHospitals;
