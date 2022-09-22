/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
      backgroundImage: {
        logo: "/img/its.png",
        kapal: "/img/logo.png",
        logo1: "/img/logo1.png",
        ship: "/img/ship.png",
      },
    },
  },
  plugins: [],
};
