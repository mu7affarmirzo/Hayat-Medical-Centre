import React, { useState } from "react";
import Header from "../views/Header/Header";
import Sidebar from "../views/Sidebar/Sidebar";
import PageContent from "./PageContent";
import { useLocation } from "react-router";

function Layout() {
  const [activeRoutes, setActiveRoutes] = useState([]);
  return (
    <div>
      <Header />
      <div className="d-flex">
        <Sidebar
          activeRoutes={activeRoutes}
          setActiveRoutes={setActiveRoutes}
        />
        <PageContent
          activeRoutes={activeRoutes}
          setActiveRoutes={setActiveRoutes}
        />
      </div>
    </div>
  );
}

export default Layout;
