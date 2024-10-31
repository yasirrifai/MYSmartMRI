import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import DashboardLayout from './Components/Admin/DashboardLayout';
import Dashboard from './Components/Admin/Dashboard';
import Scans from './Components/Admin/Scans';
import Patients from './Components/Admin/Patients';
import Reports from './Components/Admin/Reports';
import Navbar from './Components/MainPage/Navbar';
import Hero from './Components/MainPage/Hero';
import WhoWeAre from './Components/MainPage/WhoWeAre';
import PartneringHospitals from './Components/MainPage/PartneringHospitals';
import Goals from './Components/MainPage/Goals';
import Feedback from './Components/MainPage/FeedBack';
import Team from './Components/MainPage/Team';
import Contact from './Components/MainPage/Contact';
import Footer from './Components/MainPage/Footer';

function App() {
  return (
    <Router>
      <Routes>
        {/* Main Website Routes */}
        <Route
          path="/"
          element={
            <div className="App">
              <Navbar />
              <Hero />
              <WhoWeAre />
              <PartneringHospitals />
              <Goals />
              <Feedback />
              <Team />
              <Contact />
              <Footer />
            </div>
          }
        />
        

        {/* Admin Dashboard Routes */}
        <Route path="/admin" element={<DashboardLayout/>}>
          <Route path="dashboard" element={<Dashboard />} />
          <Route path="patients" element={<Patients />} />
          <Route path="scans" element={<Scans />} />
          <Route path="reports" element={<Reports />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
