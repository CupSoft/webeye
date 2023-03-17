/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // 'purple': '#8390ca',
        'purple': '#7214FF',
        'purple-dark': '#6004EE',
        'green': '#41E88D',
        'red': '#FF5367',
        'gray-light': '#8f9bb773',
        // 'blue': '#657BDB',
        'blue': '#2d55fb',
        'gray-dark': '#16213A',
        // 'gray-card': '#1B253E',
        'gray-card': '#0E1330',
        // 'gray-input': '#212D48',
        'gray-input': '#11152F',
        // 'focus-input': '#2C3854',
        'focus-input': '#0E1330',
        'light-gray-card': '#282D45',
        'light-text': '#949EB5',
        // 'turquoise': '#48A3D6',
        'turquoise': '#FFF',
        // 'yellow': '#FBFE72'
        'yellow': '#FFF'
      },
      transitionTimingFunction: {
        DEFAULT: 'ease-in-out'
      },
      transitionDuration: {
        DEFAULT: '100ms'
      }
    },
  },
  plugins: [],
}
