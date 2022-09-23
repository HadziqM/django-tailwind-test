/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
      backgroundImage: {
        logo: "url(img/its.png)",
        kapal: "url(img/logo.png)",
        logo1: "url(img/logo1.png)",
        ship: "url(img/ship.png)",
      },
      fontSize: {
        clamp: "clamp(1.5rem, 2.5vw, 4rem)",
      },
    },
  },
  plugins: [],
};
