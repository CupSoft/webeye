/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'purple': '#7214FF',
        'purple-dark': '#6004EE',
        'green': '#41E88D',
        'red': '#FF334B',
        'gray-light': '#8f9bb773',
        'blue': '#2D55FB',
        'gray-dark': '#1b2434'
      },
      transitionTimingFunction: {
        DEFAULT: 'ease-in-out'
      },
      transitionDuration: {
        DEFAULT: '50ms'
      }
    },
  },
  plugins: [],
}
