/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {
      transitionProperty: {
        'scroll': 'transform',
      },
      transitionDuration: {
        'scroll': '2000ms',
      },
    },
  },
  plugins: [
    require('flowbite/plugin'),
    function({ addUtilities }) {
      addUtilities({
        '.scroll-delay': {
          'scroll-behavior': 'smooth',
          'transition': 'transform 2s ease-in-out',
        },
      }, ['responsive', 'hover']);
    },
  ],
}

