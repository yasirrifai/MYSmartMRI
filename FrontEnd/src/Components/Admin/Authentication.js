import { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import Alert from '../Utilis/Alert';
import backgroundImage from '../../assets/hero.jpg';


export default function Authentication() {
  const [isRegistering, setIsRegistering] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [alert, setAlert] = useState(null);
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/login', {
        email,
        password,
      });

      if (response.data.token) {
        localStorage.setItem('authToken', response.data.token);
        navigate('/admin/dashboard');
      } else {
        setAlert({
          title: 'Login Failed',
          message: 'Unable to login. Please check your credentials.',
          type: 'error',
        });
      }
    } catch (error) {
      setAlert({
        title: 'Login Error',
        message: 'Invalid login credentials. Please try again.',
        type: 'error',
      });
      console.error(error);
    }
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/register', {
        email,
        password,
      });

      if (response.data.message === 'User registered successfully') {
        setAlert({
          title: 'Registration Successful',
          message: 'Registration successful! You can now log in.',
          type: 'success',
        });
        setIsRegistering(false);
      } else {
        setAlert({
          title: 'Registration Failed',
          message: response.data.error || 'An error occurred during registration.',
          type: 'error',
        });
      }
    } catch (error) {
      setAlert({
        title: 'Registration Error',
        message: 'An error occurred. Please try again later.',
        type: 'error',
      });
      console.error(error);
    }
  };

  const toggleAuthMode = () => {
    setIsRegistering(!isRegistering);
    setAlert(null);
  };

  return (
    <div className="relative min-h-screen bg-cover bg-center" style={{ backgroundImage: `url(${backgroundImage})`}}>
      {/* Overlay */}
      <div className="absolute inset-0 bg-black opacity-50"></div>

      {/* Content */}
      <div className="relative flex min-h-screen items-center justify-center">
        <div className="flex flex-col bg-white bg-opacity-90 rounded-lg shadow-lg p-8 md:w-1/2 lg:w-1/3 z-10">
          <h2 className="mt-8 text-3xl font-bold text-gray-900 text-center">
            {isRegistering ? 'Register' : 'Admin Login'}
          </h2>

          {alert && (
            <Alert
              title={alert.title}
              message={alert.message}
              type={alert.type}
              onDismiss={() => setAlert(null)}
            />
          )}

          <form onSubmit={isRegistering ? handleRegister : handleLogin} className="mt-10 space-y-6">
            <div>
              <label htmlFor="email" className="block text-sm font-medium text-gray-700">
                Email address
              </label>
              <input
                id="email"
                name="email"
                type="email"
                required
                autoComplete="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="mt-2 block w-full rounded-md border border-gray-300 p-2 shadow-sm focus:border-blue-500 focus:ring-blue-500"
              />
            </div>
            <div>
              <label htmlFor="password" className="block text-sm font-medium text-gray-700">
                Password
              </label>
              <input
                id="password"
                name="password"
                type="password"
                required
                autoComplete={isRegistering ? 'new-password' : 'current-password'}
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="mt-2 block w-full rounded-md border border-gray-300 p-2 shadow-sm focus:border-blue-500 focus:ring-blue-500"
              />
            </div>
            <button
              type="submit"
              className="w-full rounded-md bg-blue-600 py-2 text-white font-semibold hover:bg-blue-500 focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
            >
              {isRegistering ? 'Register' : 'Log in'}
            </button>
          </form>
          <p className="mt-6 text-center text-sm text-gray-600">
            {isRegistering ? 'Already have an account?' : "Don't have an account?"}{' '}
            <button
              onClick={toggleAuthMode}
              className="font-medium text-blue-600 hover:text-blue-500"
            >
              {isRegistering ? 'Log in' : 'Register'}
            </button>
          </p>
        </div>
      </div>
    </div>
  );
}
