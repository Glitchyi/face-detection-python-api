// tailwind.config.js
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {
      height: {
        screenWithNav: "calc(100vh - 6rem)",
      },
      colors: {
        background: "#051931",
        backgroundSecondary: "#111B23",
        textInactive: "#757575",
        primary: "#97C7FF",
        secondary: "#29AC85",
        tertiary: "#000715",
        textsecondary: "#DBFFF4",
      },
    },
  },
  plugins: [],
};
