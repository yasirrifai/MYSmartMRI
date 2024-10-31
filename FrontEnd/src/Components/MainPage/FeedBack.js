import React from 'react';
import feedbackImage1 from '../../assets/feedback1.jpg';

import feedbackImage2 from '../../assets/feedback2.jpg';

import feedbackImage3 from '../../assets/feedback3.jpeg';

function Feedback() {
  return (
    <section className="py-12 bg-blue-200 text-center">
        <h2 className="text-3xl font-semibold mb-6">Occupationist Feedback</h2>
        <div className="flex justify-center space-x-8 max-w-4xl mx-auto">
          <div className="bg-white p-4 rounded-lg shadow-lg w-1/3">
            <img src={feedbackImage1} alt="Feedback 1" className="h-24 mx-auto rounded-full" />
            <p className="text-sm mt-4">"The AI technology provides accurate results that enhance our confidence in diagnosis."</p>
            <p className="mt-2 font-semibold">- Dr. Jane Doe</p>
          </div>
          <div className="bg-white p-4 rounded-lg shadow-lg w-1/3">
            <img src={feedbackImage2} alt="Feedback 2" className="h-24 mx-auto rounded-full" />
            <p className="text-sm mt-4">"Impressed with the reliability and speed of MRI analysis using this AI system."</p>
            <p className="mt-2 font-semibold">- Dr. John Smith</p>
          </div>
          <div className="bg-white p-4 rounded-lg shadow-lg w-1/3">
            <img src={feedbackImage3} alt="Feedback 3" className="h-24 mx-auto rounded-full" />
            <p className="text-sm mt-4">"This tool saves time and delivers dependable diagnostic reports."</p>
            <p className="mt-2 font-semibold">- Dr. Sarah Lee</p>
          </div>
        </div>
      </section>
  );
}

export default Feedback;
