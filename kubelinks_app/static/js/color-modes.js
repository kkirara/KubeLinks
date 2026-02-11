(() => {
  "use strict";
  
  const getPreferredTheme = () => {
    const storedTheme = localStorage.getItem("theme");
    if (storedTheme) {
      return storedTheme;
    }
    return window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  };
  
  const setTheme = (theme) => {
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
  
  const setStyle = (theme) => {
    const divTable = document.getElementById("div-table");
    if (divTable) {
      const is_dark = theme === "dark";
      divTable.classList.toggle("shadow", !is_dark);
      divTable.classList.toggle("border", is_dark);
    }
  };
  
  // Wait for DOM to be ready
  window.addEventListener("DOMContentLoaded", () => {
    const themeModeElement = document.getElementById("themeMode");
    const currentTheme = getPreferredTheme();
    
    // Apply styles
    setStyle(currentTheme);
    
    // Theme toggle handler
    if (themeModeElement) {
      themeModeElement.addEventListener("change", () => {
        const theme = themeModeElement.checked ? "dark" : "light";
        localStorage.setItem("theme", theme);
        setTheme(theme);
        setStyle(theme);
      });
    }
    
    // Active link handler
    const activeLink = document.querySelector("a.active");
    if (activeLink) {
      activeLink.classList.remove("active");
    }
    
    const currentLink = document.querySelector("a[href='" + location.pathname + "']");
    if (currentLink) {
      currentLink.classList.add("active");
    }
  });
  
  // System theme change listener
  window
    .matchMedia("(prefers-color-scheme: dark)")
    .addEventListener("change", () => {
      const storedTheme = localStorage.getItem("theme");
      // Only update if no stored preference exists
      if (!storedTheme || storedTheme === "auto") {
        const newTheme = getPreferredTheme();
        setTheme(newTheme);
        setStyle(newTheme);
        
        // Update switcher position
        const themeModeElement = document.getElementById("themeMode");
        if (themeModeElement) {
          themeModeElement.checked = newTheme === "dark";
        }
      }
    });
})();