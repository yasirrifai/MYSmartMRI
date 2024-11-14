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
import Team from './Components/MainPage/Team';
import Footer from './Components/MainPage/Footer';
import Authentication from './Components/Admin/Authentication';
import Contact from './Components/MainPage/Contact';
import ProtectedRoute from './ProtectedRoutes';
import Feedback from './Components/MainPage/FeedBack';

function App() {
  return (
    <Router>
      <Routes>
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
        <Route path="/login" element={<Authentication />} />
        <Route path="/admin" element={<ProtectedRoute><DashboardLayout /></ProtectedRoute>}>
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
