(() => {
  "use strict";

  const storedTheme = localStorage.getItem("theme");

  const getPreferredTheme = () => {
    if (storedTheme) {
      return storedTheme;
    }
    return window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  };

  const setTheme = function (theme) {
    if (theme === "auto") {
      document.documentElement.setAttribute(
        "data-bs-theme",
        window.matchMedia("(prefers-color-scheme: dark)").matches
          ? "dark"
          : "light"
      );
    } else {
      document.documentElement.setAttribute("data-bs-theme", theme);
    }
  };

  const setStyle = function (theme) {
    const is_dark = theme === "dark";
    document.getElementById("div-table").classList.toggle("shadow", !is_dark);
    document.getElementById("div-table").classList.toggle("border", is_dark);
  };

  setTheme(getPreferredTheme());

  window
    .matchMedia("(prefers-color-scheme: dark)")
    .addEventListener("change", () => {
      if (storedTheme !== "light" || storedTheme !== "dark") {
        setTheme(getPreferredTheme());
        setStyle(theme);
      }
    });

  window.addEventListener("DOMContentLoaded", () => {
    document.getElementById("themeMode").checked =
      getPreferredTheme() === "dark";
    setStyle(getPreferredTheme());

    document.getElementById("themeMode").addEventListener("change", () => {
      const theme = document.getElementById("themeMode").checked
        ? "dark"
        : "light";
      localStorage.setItem("theme", theme);
      setTheme(theme);
      setStyle(theme);
    });

    if (document.querySelector("a.active")) {
      document.querySelector("a.active").classList.remove("active");
    }
    if (document.querySelector("a[href='" + location.pathname + "']")) {
      document
        .querySelector("a[href='" + location.pathname + "']")
        .classList.add("active");
    }
  });
})();
