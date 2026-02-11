(() => {
  const storedTheme = localStorage.getItem("theme");
  const preferredTheme =
    storedTheme ||
    (window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light");

  document.documentElement.setAttribute("data-bs-theme", preferredTheme);

  // Store the theme state for immediate use when DOM is ready
  window.__initialTheme = preferredTheme;
})();
