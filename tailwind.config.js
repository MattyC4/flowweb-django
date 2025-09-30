/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.{html,js}",
    "./apps/**/*.{html,py,js}",
  ],
  theme: { extend: {} },
  plugins: [require("daisyui"), require("preline/plugin")],  // 👈 añade preline
  daisyui: { themes: ["emerald","cupcake","light","dark"] }
}