import React from 'react';
import teamImage1 from '../../assets/teamImage1.jpg';
import teamImage2 from '../../assets/teamImage2.jpg';
import teamImage3 from '../../assets/teamImage3.jpg';

function Team() {
  return (
    <section className="py-12 bg-gray-100 text-center">
    <h2 className="text-3xl font-semibold mb-6">Our Team Behind</h2>
    <div className="flex justify-center space-x-8 max-w-3xl mx-auto">
      <div className="w-1/3">
        <img src={teamImage1} alt="Team 1" className="h-24 mx-auto rounded-full" />
        <p className="mt-4 font-semibold">Yasir Rifai</p>
        <p className="text-sm">Founder & CEO</p>
      </div>
      <div className="w-1/3">
        <img src={teamImage2} alt="Team 2" className="h-24 mx-auto rounded-full" />
        <p className="mt-4 font-semibold">Amna Barshad</p>
        <p className="text-sm">Manager</p>
      </div>
      <div className="w-1/3">
        <img src={teamImage3} alt="Team 3" className="h-24 mx-auto rounded-full" />
        <p className="mt-4 font-semibold">Yarah Rifai</p>
        <p className="text-sm">Lead AI Researcher</p>
      </div>
    </div>
  </section>
  );
}

export default Team;
