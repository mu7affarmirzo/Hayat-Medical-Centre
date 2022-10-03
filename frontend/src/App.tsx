import React from 'react';
import {BrowserRouter} from "react-router-dom";
import AppRouting from "./routes/AppRouting";

function App() {
  return (
      <BrowserRouter>
          <AppRouting/>
      </BrowserRouter>
  );
}

export default App;
