import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import CssBaseline from "@mui/material/CssBaseline";
import { BrowserRouter } from "react-router-dom";
import { BabysitterProvider } from "./context/BabysitterContext";

import "./index.css";
import "@fontsource/roboto/300.css";
import "@fontsource/roboto/400.css";
import "@fontsource/roboto/500.css";
import "@fontsource/roboto/700.css";

ReactDOM.createRoot(document.getElementById("root")).render(
  <BabysitterProvider>
    <BrowserRouter>
      <CssBaseline />
      <App />
    </BrowserRouter>
  </BabysitterProvider>,
);
