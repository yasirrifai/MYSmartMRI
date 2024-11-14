import { CheckCircleIcon, ExclamationTriangleIcon } from '@heroicons/react/20/solid';

const iconStyles = {
  success: 'text-green-400',
  error: 'text-red-400',
};

const backgroundStyles = {
  success: 'bg-green-50',
  error: 'bg-red-50',
};

const textStyles = {
  success: 'text-green-800',
  error: 'text-red-800',
};

export default function Alert({ title, message, type = 'success', onDismiss }) {
  const Icon = type === 'success' ? CheckCircleIcon : ExclamationTriangleIcon;

  return (
    <div className={`rounded-md p-4 ${backgroundStyles[type]}`}>
      <div className="flex">
        <div className="shrink-0">
          <Icon aria-hidden="true" className={`h-5 w-5 ${iconStyles[type]}`} />
        </div>
        <div className="ml-3">
          <h3 className={`text-sm font-medium ${textStyles[type]}`}>{title}</h3>
          <div className={`mt-2 text-sm ${textStyles[type]}`}>
            <p>{message}</p>
          </div>
          <div className="mt-4">
            <div className="-mx-2 -my-1.5 flex">
              <button
                type="button"
                onClick={onDismiss}
                className={`rounded-md px-2 py-1.5 text-sm font-medium ${textStyles[type]} hover:bg-opacity-75 focus:outline-none focus:ring-2 focus:ring-offset-2 ${type === 'success' ? 'focus:ring-green-600 focus:ring-offset-green-50' : 'focus:ring-red-600 focus:ring-offset-red-50'}`}
              >
                Dismiss
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
