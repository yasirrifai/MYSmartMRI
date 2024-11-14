import { Disclosure, DisclosureButton, DisclosurePanel, Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/react';
import { MagnifyingGlassIcon } from '@heroicons/react/20/solid';
import { Bars3Icon, BellIcon, XMarkIcon } from '@heroicons/react/24/outline';
import { Link, Outlet, useLocation, useNavigate } from 'react-router-dom';
import logo from "../../assets/MYSmartMRI.png";
import avatar from "../../assets/teamImage1.jpg";

const user = {
  name: 'Yasir Rifai',
  email: 'tom@example.com',
  imageUrl: avatar,
};

const navigation = [
  { name: 'Dashboard', href: '/admin/dashboard' },
  { name: 'Patients', href: '/admin/patients' },
  { name: 'Scans', href: '/admin/scans' },
  { name: 'Reports', href: '/admin/reports' },
];

const userNavigation = [
  { name: 'Your Profile', href: '#' },
  { name: 'Settings', href: '#' },
  { name: 'Sign out', href: '#' }, 
];

function classNames(...classes) {
  return classes.filter(Boolean).join(' ');
}

export default function Example() {
  const location = useLocation();
  const navigate = useNavigate();

  const currentPage = navigation.find((item) => location.pathname === item.href);
  const pageTitle = currentPage ? currentPage.name : 'Dashboard';

  const handleSignOut = () => {
    localStorage.removeItem('authToken');
    navigate('/');
  };

  return (
    <>
      <div className="min-h-full">
        <div className="bg-blue-300 pb-32">
          <Disclosure as="nav" className="border-b border-blue-300 border-opacity-25 bg-blue-400 lg:border-none">
            <div className="mx-auto max-w-7xl px-2 sm:px-4 lg:px-8">
              <div className="relative flex h-16 items-center justify-between lg:border-b lg:border-blue-400 lg:border-opacity-25">
                <div className="flex items-center px-2 lg:px-0">
                  <div className="flex-shrink-0">
                    <img alt="MYSmartMRI" src={logo} className="block h-8 w-8" />
                  </div>
                  <div className="hidden lg:ml-10 lg:block">
                    <div className="flex space-x-4">
                      {navigation.map((item) => (
                        <Link
                          key={item.name}
                          to={item.href}
                          className={classNames(
                            location.pathname === item.href ? 'bg-blue-500 text-white' : 'text-white hover:bg-blue-600 hover:bg-opacity-75',
                            'rounded-md px-3 py-2 text-sm font-medium'
                          )}
                          aria-current={location.pathname === item.href ? 'page' : undefined}
                        >
                          {item.name}
                        </Link>
                      ))}
                    </div>
                  </div>
                </div>
                <div className="flex flex-1 justify-center px-2 lg:ml-6 lg:justify-end">
                  <div className="w-full max-w-lg lg:max-w-xs">
                    <label htmlFor="search" className="sr-only">
                      Search
                    </label>
                    <div className="relative text-gray-400 focus-within:text-gray-600">
                      <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
                        <MagnifyingGlassIcon aria-hidden="true" className="h-5 w-5" />
                      </div>
                      <input
                        id="search"
                        name="search"
                        type="search"
                        placeholder="Search"
                        className="block w-full rounded-md border-0 bg-white py-1.5 pl-10 pr-3 text-gray-900 focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-blue-600 sm:text-sm/6"
                      />
                    </div>
                  </div>
                </div>
                <div className="flex lg:hidden">
                  <DisclosureButton className="group relative inline-flex items-center justify-center rounded-md bg-blue-600 p-2 text-blue-200 hover:bg-blue-500 hover:bg-opacity-75 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-blue-600">
                    <span className="absolute -inset-0.5" />
                    <span className="sr-only">Open main menu</span>
                    <Bars3Icon aria-hidden="true" className="block h-6 w-6 group-data-[open]:hidden" />
                    <XMarkIcon aria-hidden="true" className="hidden h-6 w-6 group-data-[open]:block" />
                  </DisclosureButton>
                </div>
                <div className="hidden lg:ml-4 lg:block">
                  <div className="flex items-center">
                    <Menu as="div" className="relative ml-3 flex-shrink-0">
                      <div>
                        <MenuButton className="relative flex rounded-full bg-blue-600 text-sm text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-blue-600">
                          <span className="absolute -inset-1.5" />
                          <span className="sr-only">Open user menu</span>
                          <img alt="" src={user.imageUrl} className="h-8 w-8 rounded-full" />
                        </MenuButton>
                      </div>
                      <MenuItems
                        transition
                        className="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 transition focus:outline-none data-[closed]:scale-95 data-[closed]:transform data-[closed]:opacity-0 data-[enter]:duration-100 data-[leave]:duration-75 data-[enter]:ease-out data-[leave]:ease-in"
                      >
                        {userNavigation.map((item) => (
                          <MenuItem key={item.name}>
                            {item.name === 'Sign out' ? (
                              <button
                                onClick={handleSignOut}
                                className="block w-full px-4 py-2 text-left text-sm text-gray-700 hover:bg-gray-100"
                              >
                                {item.name}
                              </button>
                            ) : (
                              <a
                                href={item.href}
                                className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                              >
                                {item.name}
                              </a>
                            )}
                          </MenuItem>
                        ))}
                      </MenuItems>
                    </Menu>
                  </div>
                </div>
              </div>
            </div>

            <DisclosurePanel className="lg:hidden">
              <div className="space-y-1 px-2 pb-3 pt-2">
                {navigation.map((item) => (
                  <DisclosureButton
                    key={item.name}
                    as={Link}
                    to={item.href}
                    className={classNames(
                      location.pathname === item.href ? 'bg-blue-500 text-white' : 'text-white hover:bg-blue-600',
                      'block px-3 py-2 rounded-md text-base font-medium'
                    )}
                    aria-current={location.pathname === item.href ? 'page' : undefined}
                  >
                    {item.name}
                  </DisclosureButton>
                ))}
              </div>
              <div className="border-t border-blue-500 pb-3 pt-4">
                <div className="flex items-center px-5">
                  <div className="flex-shrink-0">
                    <img alt="" src={user.imageUrl} className="h-10 w-10 rounded-full" />
                  </div>
                  <div className="ml-3">
                    <div className="text-base font-medium text-white">{user.name}</div>
                    <div className="text-sm font-medium text-blue-300">{user.email}</div>
                  </div>
                  <button
                    type="button"
                    className="relative ml-auto flex-shrink-0 rounded-full bg-blue-500 p-1 text-blue-200 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-blue-600"
                  >
                    <span className="absolute -inset-1.5" />
                    <span className="sr-only">View notifications</span>
                    <BellIcon aria-hidden="true" className="h-6 w-6" />
                  </button>
                </div>
                <div className="mt-3 space-y-1 px-2">
                  {userNavigation.map((item) => (
                    <DisclosureButton
                      key={item.name}
                      as="button"
                      onClick={item.name === 'Sign out' ? handleSignOut : undefined}
                      className="block w-full px-3 py-2 rounded-md text-base font-medium text-white hover:bg-blue-500 hover:bg-opacity-75"
                    >
                      {item.name}
                    </DisclosureButton>
                  ))}
                </div>
              </div>
            </DisclosurePanel>
          </Disclosure>
          <header className="py-10">
            <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
              <h1 className="text-3xl font-bold tracking-tight text-white">{pageTitle}</h1>
            </div>
          </header>
        </div>

        <main className="-mt-32">
          <div className="mx-auto max-w-7xl px-4 pb-12 sm:px-6 lg:px-8">
            <div className="rounded-lg bg-white px-5 py-6 shadow sm:px-6">
              <Outlet />
            </div>
          </div>
        </main>
      </div>
    </>
  );
}
