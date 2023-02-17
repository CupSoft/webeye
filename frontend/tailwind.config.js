/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'purple': '#8390ca',
        'purple-dark': '#6004EE',
        'green': '#41E88D',
        'red': '#FF5367',
        'gray-light': '#8f9bb773',
        'blue': '#657BDB',
        'gray-dark': '#16213A',
        'gray-card': '#1B253E',
        'gray-input': '#212D48',
        'focus-input': '#2C3854',
        'light-gray-card': '#282D45',
        'light-text': '#949EB5'
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
