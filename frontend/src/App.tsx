import React from 'react';
import Login from "./views/registaration/Login";
import {BrowserRouter} from "react-router-dom";
import AppRouting from "./AppRouting";

function App() {
  return (
      <BrowserRouter>
          <AppRouting/>
      </BrowserRouter>
  );
}

export default App;
