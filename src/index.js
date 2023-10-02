import React, { Suspense } from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter } from "react-router-dom";
import SuspenseContent from "./Layouts/SuspenseContent";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  // <React.StrictMode>
  <Suspense fallback={<SuspenseContent />}>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </Suspense>
  // {/* </React.StrictMode> */}
);

reportWebVitals();
