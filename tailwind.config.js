/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './contacts/templates/**/*.{html,js}',
    './contacts/forms.py'
  ],
  theme: {
    extend: {},
  },
  plugins: [require('daisyui')],
}

