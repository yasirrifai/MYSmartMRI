import React, { useState, Fragment } from 'react';
import { jsPDF } from 'jspdf';
import 'jspdf-autotable';
import { Dialog, Transition } from '@headlessui/react';
import logoImg from "../../assets/MYSmartMRI.png"
import axios from 'axios'
import Alert from '../Utilis/Alert'; 

function Scans() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [analysisResult, setAnalysisResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [alert, setAlert] = useState(null); 

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file && (file.name.endsWith('.dcm') || file.name.endsWith('.dicom'))) {
      setSelectedFile(file);
      setAnalysisResult(null); 
    } else {
      setAlert({
        title: "Invalid File",
        message: "Please upload a valid DICOM file (.dcm or .dicom).",
        type: "error",
      });    }
  };

  const handleScan = async () => {
    if (!selectedFile) {
      setAlert({
        title: "No File Selected",
        message: "Please upload a DICOM MRI image before scanning.",
        type: "error",
      });      return;
    }
  
    setLoading(true);
  
    const formData = new FormData();
    formData.append('file', selectedFile);
  
    try {
      const authToken = localStorage.getItem('authToken');
  
      if (!authToken) {
        setAlert({
          title: "Unauthorized",
          message: "You must be logged in to perform this action.",
          type: "error",
        });        setLoading(false);
        return;
      }
  
      const response = await axios.post('http://127.0.0.1:5000/predict', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          'Authorization': `${authToken}`, 
        },
      });
  
      const resultData = response.data;
      console.log(resultData);
      setAnalysisResult(resultData); 
      setIsModalOpen(true); 
    } catch (error) {
      console.error(error);
      setAlert({
        title: "Scan Failed",
        message: "Failed to analyze the DICOM file. Please try again.",
        type: "error",
      });    } finally {
      setLoading(false);
    }
  };
  

  const handleDownloadPDF = () => {
    if (!analysisResult) return;
  
    const doc = new jsPDF();
    const pageWidth = doc.internal.pageSize.getWidth();
  
    const getBase64Image = (imgPath, callback) => {
      const img = new Image();
      img.src = imgPath;
      img.crossOrigin = 'Anonymous'; 
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
  
    getBase64Image(logoImg, (base64Logo) => {
      doc.setFillColor(60, 120, 180); 
      doc.rect(0, 0, pageWidth, 40, 'F'); 
      doc.addImage(base64Logo, 'PNG', 10, 5, 20, 20); 
      doc.setFontSize(20);
      doc.setTextColor(255, 255, 255);
      doc.text("MRI Analysis Report", 40, 15);
      doc.setFontSize(12);
      doc.text("Original", 40, 25);
  
      doc.setTextColor(0, 0, 0); 
      doc.setFontSize(14);
      doc.text("Patient Demographics", 10, 50);
  
      doc.setFontSize(12);
      doc.autoTable({
        startY: 55,
        margin: { left: 15, right: 15 }, 
        styles: { fontSize: 10, cellPadding: 2 },
        body: [
          ["Name", analysisResult.PatientInfo.Name, "Gender", analysisResult.PatientInfo.Sex],
          ["ID No.", "1234565", "Date of Birth", "March 9, 1989"],
          ["Visit No.", "2024-10-01-001", "Age", analysisResult.PatientInfo.Age],
          ["Location", "MRI Ward", "Nationality", "Not Provided"],
        ],
        theme: 'grid',
      });
  
      doc.setFillColor(230, 230, 230); 
      doc.rect(15, doc.autoTable.previous.finalY + 5, pageWidth - 30, 10, 'F');
      doc.setTextColor(0, 0, 0);
      doc.text("Allergies: None reported", 20, doc.autoTable.previous.finalY + 12);
  

      doc.setFillColor(60, 120, 180); 
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
          ["Disease Probability", analysisResult.Prediction.Disease.Confidence],
          ["Confidence level", analysisResult.Prediction.Sequence.Confidence],
        ],
        theme: 'grid',
      });
  
      doc.setFillColor(230, 230, 230);
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
  
      doc.setFillColor(60, 120, 180); 
      doc.rect(0, doc.autoTable.previous.finalY + 60, pageWidth, 10, 'F');
      doc.setTextColor(255, 255, 255);
      doc.text("Report Summary", 10, doc.autoTable.previous.finalY + 67);
  
      doc.setTextColor(0, 0, 0);
      doc.setFontSize(12);
      doc.text(`Date of Issue: October 30, 2024`, 15, doc.autoTable.previous.finalY + 80);
      doc.text(`Condition at Discharge: Stable`, 15, doc.autoTable.previous.finalY + 90);
  
      doc.setFontSize(10);
      doc.setTextColor(0, 0, 0);
      doc.text("1-800-765-7678 // 1500 San Pablo Street", 15, 285);
      doc.text("Page 1", pageWidth - 20, 285);
  
      doc.save("MRI_Analysis_Report.pdf");
    });
  };
  

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h1 className="text-3xl font-bold mb-4">Upload and Scan</h1>
      {alert && (
        <Alert
          title={alert.title}
          message={alert.message}
          type={alert.type}
          onDismiss={() => setAlert(null)}
        />
      )}
      <div className="flex items-center space-x-4">
        <input
          type="file"
          accept=".dcm,.dicom" 
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
                    <p><strong>Patient Name/ID:</strong> {analysisResult?.PatientInfo?.Name || " Not Mentioned"} </p>
                    <p><strong>Age:</strong> {analysisResult?.PatientInfo?.Age || " Not Mentioned"}</p>
                    <p><strong>Sex:</strong> {analysisResult?.PatientInfo?.Sex || " Not Mentioned"}</p>
                    <p><strong>MRI Sequence Type:</strong> {analysisResult?.Prediction?.Sequence?.Name                    }</p>
                    <p><strong>Disease:</strong> {analysisResult?.Prediction?.Disease?.Name}</p>
                    <p><strong>Disease Probability:</strong> {analysisResult?.Prediction?.Disease?.Confidence}%</p>
                    <p><strong>Confidence Level:</strong> {analysisResult?.Prediction?.Sequence?.Confidence}</p>

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
