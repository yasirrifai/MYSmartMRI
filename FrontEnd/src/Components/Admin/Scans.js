import React, { useState, Fragment } from 'react';
import { jsPDF } from 'jspdf';
import 'jspdf-autotable';
import { Dialog, Transition } from '@headlessui/react';
import logoImg from "../../assets/MYSmartMRI.png"

function Scans() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [analysisResult, setAnalysisResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [isModalOpen, setIsModalOpen] = useState(false);

  // Handle file selection
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file && (file.name.endsWith('.dcm') || file.name.endsWith('.dicom'))) {
      setSelectedFile(file);
      setAnalysisResult(null); // Clear previous result when a new file is selected
    } else {
      alert("Please upload a valid DICOM file (.dcm or .dicom).");
    }
  };

  // Simulate a scan result
  const generateMockResult = () => {
    return {
      patientName: "John Doe",
      age: Math.floor(Math.random() * (90 - 20 + 1)) + 20, // Random age between 20 and 90
      sex: Math.random() > 0.5 ? "Male" : "Female",
      sequenceType: "T2-weighted",
      diseease: "Brain Tumor",
      diseaseProbability: (Math.random() * 100).toFixed(2), // 
      confidenceLevel: `${(Math.random() * (90 - 70) + 70).toFixed(2)}%` // Confidence between 70-90%Random probability between 0 and 100%
    };
  };

  // Handle the scan button click
  const handleScan = () => {
    if (!selectedFile) {
      alert("Please upload a DICOM MRI image before scanning.");
      return;
    }

    setLoading(true);
    setTimeout(() => {
      const mockData = generateMockResult(); // Generate mock result data
      setAnalysisResult(mockData);
      setIsModalOpen(true); // Open the modal with the mock data
      setLoading(false);
    }, 1000); // Simulate a short delay
  };

  // Generate PDF Report
  // Import jsPDF


  const handleDownloadPDF = () => {
    if (!analysisResult) return;
  
    const doc = new jsPDF();
    const pageWidth = doc.internal.pageSize.getWidth();
  
    // Function to get the image as Base64
    const getBase64Image = (imgPath, callback) => {
      const img = new Image();
      img.src = imgPath;
      img.crossOrigin = 'Anonymous'; // Allows cross-origin images
  
      img.onload = () => {
        const canvas = document.createElement('canvas');
        canvas.width = img.width;
        canvas.height = img.height;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(img, 0, 0);
        const dataURL = canvas.toDataURL('image/png');
        callback(dataURL);
      };
    };
  
    // Company Logo Section
    getBase64Image(logoImg, (base64Logo) => {
      doc.setFillColor(60, 120, 180); // Header background color
      doc.rect(0, 0, pageWidth, 40, 'F'); // Header background rectangle
      doc.addImage(base64Logo, 'PNG', 10, 5, 20, 20); // Logo at top-left
      doc.setFontSize(20);
      doc.setTextColor(255, 255, 255);
      doc.text("MRI Analysis Report", 40, 15);
      doc.setFontSize(12);
      doc.text("Original", 40, 25);
  
      // Patient Demographics Section
      doc.setTextColor(0, 0, 0); // Black text
      doc.setFontSize(14);
      doc.text("Patient Demographics", 10, 50);
  
      doc.setFontSize(12);
      doc.autoTable({
        startY: 55,
        margin: { left: 15, right: 15 }, // Margin for consistent layout
        styles: { fontSize: 10, cellPadding: 2 },
        body: [
          ["Name", analysisResult.patientName, "Gender", analysisResult.sex],
          ["ID No.", "1234565", "Date of Birth", "March 9, 1989"],
          ["Visit No.", "2024-10-01-001", "Age", analysisResult.age],
          ["Location", "MRI Ward", "Nationality", "Not Provided"],
        ],
        theme: 'grid',
      });
  
      // Additional Information Rows
      doc.setFillColor(230, 230, 230); // Light gray background for info boxes
      doc.rect(15, doc.autoTable.previous.finalY + 5, pageWidth - 30, 10, 'F');
      doc.setTextColor(0, 0, 0);
      doc.text("Allergies: None reported", 20, doc.autoTable.previous.finalY + 12);
  
    //   doc.rect(15, doc.autoTable.previous.finalY + 15, pageWidth - 30, 10, 'F');
    //   doc.text("Medical Alerts: None reported", 20, doc.autoTable.previous.finalY + 22);
  
      // Medical / Surgical / Family History Section
      doc.setFillColor(60, 120, 180); // Section background color
      doc.rect(0, doc.autoTable.previous.finalY + 30, pageWidth, 10, 'F');
      doc.setTextColor(255, 255, 255);
      doc.text("Medical Details", 10, doc.autoTable.previous.finalY + 37);
  
      doc.setTextColor(0, 0, 0);
      doc.setFontSize(12);
      doc.text("Disease Details", 10, doc.autoTable.previous.finalY + 50);
  
      doc.autoTable({
        startY: doc.autoTable.previous.finalY + 55,
        margin: { left: 15, right: 15 },
        styles: { fontSize: 10, cellPadding: 2 },
        body: [
          ["Scanned Date / Time", "October 1, 2024 / 14:45"],
          ["Consulted Doctor", "Dr. Michael Nguyen"],
          ["Reason for Scan", "Follow-up on previous injury"],
          ["Principal Diagnosis", "Post-traumatic Brain Injury"],
          ["Secondary Diagnosis", "Cerebral Edema"],
          ["Other Diagnosis", "Intracranial Pressure"],
          ["Predicted Diagnosis", "Vascular Dementia (Early Stage)"],
          ["Disease Probability", analysisResult.diseaseProbability],
          ["Confidence level", analysisResult.confidenceLevel],
        ],
        theme: 'grid',
      });
  
      // Clinical Summary Section
      doc.setFillColor(230, 230, 230); // Gray background for Clinical Summary
      doc.rect(15, doc.autoTable.previous.finalY + 10, pageWidth - 30, 10, 'F');
      doc.setFontSize(14);
      doc.setTextColor(0, 0, 0);
      doc.text("Clinical Summary", 20, doc.autoTable.previous.finalY + 17);
  
      doc.setFontSize(10);
      doc.text(
        "Sample clinical summary for patient. This text area can be expanded based on the actual content received from the MRI analysis, detailing the patient's condition, symptoms, and findings based on the MRI scan results.",
        15,
        doc.autoTable.previous.finalY + 30,
        { maxWidth: pageWidth - 30 }
      );
  
      // Discharge / Report Summary Section
      doc.setFillColor(60, 120, 180); // Section header color
      doc.rect(0, doc.autoTable.previous.finalY + 60, pageWidth, 10, 'F');
      doc.setTextColor(255, 255, 255);
      doc.text("Report Summary", 10, doc.autoTable.previous.finalY + 67);
  
      doc.setTextColor(0, 0, 0);
      doc.setFontSize(12);
      doc.text(`Date of Issue: October 30, 2024`, 15, doc.autoTable.previous.finalY + 80);
      doc.text(`Condition at Discharge: Stable`, 15, doc.autoTable.previous.finalY + 90);
  
      // Footer
      doc.setFontSize(10);
      doc.setTextColor(0, 0, 0);
      doc.text("1-800-765-7678 // 1500 San Pablo Street", 15, 285);
      doc.text("Page 1", pageWidth - 20, 285);
  
      // Save the PDF
      doc.save("MRI_Analysis_Report.pdf");
    });
  };
  

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h1 className="text-3xl font-bold mb-4">Upload and Scan</h1>
      <div className="flex items-center space-x-4">
        <input
          type="file"
          accept=".dcm,.dicom" // Restrict file types to .dcm and .dicom
          onChange={handleFileChange}
          className="border border-gray-300 p-2 rounded-lg"
        />
        <button
          onClick={handleScan}
          className="bg-green-500 text-white px-4 py-2 rounded-lg"
          disabled={loading}
        >
          {loading ? "Scanning..." : "Scan"}
        </button>
      </div>

      {/* Modal for displaying analysis result */}
      <Transition appear show={isModalOpen} as={Fragment}>
        <Dialog as="div" className="relative z-10" onClose={() => setIsModalOpen(false)}>
          <Transition.Child
            as={Fragment}
            enter="ease-out duration-300"
            enterFrom="opacity-0"
            enterTo="opacity-100"
            leave="ease-in duration-200"
            leaveFrom="opacity-100"
            leaveTo="opacity-0"
          >
            <div className="fixed inset-0 bg-black bg-opacity-25" />
          </Transition.Child>

          <div className="fixed inset-0 overflow-y-auto">
            <div className="flex min-h-full items-center justify-center p-4 text-center">
              <Transition.Child
                as={Fragment}
                enter="ease-out duration-300"
                enterFrom="opacity-0 scale-95"
                enterTo="opacity-100 scale-100"
                leave="ease-in duration-200"
                leaveFrom="opacity-100 scale-100"
                leaveTo="opacity-0 scale-95"
              >
                <Dialog.Panel className="w-full max-w-md transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all">
                  <Dialog.Title as="h3" className="text-lg font-medium leading-6 text-gray-900">
                    MRI Analysis Report
                  </Dialog.Title>
                  <div className="mt-4">
                    <p><strong>Patient Name/ID:</strong> {analysisResult?.patientName}</p>
                    <p><strong>Age:</strong> {analysisResult?.age}</p>
                    <p><strong>Sex:</strong> {analysisResult?.sex}</p>
                    <p><strong>MRI Sequence Type:</strong> {analysisResult?.sequenceType}</p>
                    <p><strong>Disease:</strong> {analysisResult?.diseease}</p>
                    <p><strong>Disease Probability:</strong> {analysisResult?.diseaseProbability}%</p>
                    <p><strong>Confidence Level:</strong> {analysisResult?.confidenceLevel}</p>

                  </div>

                  <div className="mt-4 flex justify-end space-x-4">
                    <button
                      onClick={() => setIsModalOpen(false)}
                      className="bg-gray-200 text-gray-800 px-4 py-2 rounded-lg"
                    >
                      Close
                    </button>
                    <button
                      onClick={handleDownloadPDF}
                      className="bg-blue-500 text-white px-4 py-2 rounded-lg"
                    >
                      Download as PDF
                    </button>
                  </div>
                </Dialog.Panel>
              </Transition.Child>
            </div>
          </div>
        </Dialog>
      </Transition>
    </div>
  );
}

export default Scans;
