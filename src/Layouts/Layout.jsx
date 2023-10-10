import React, { useEffect, useState } from "react";
import Header from "../views/Header/Header";
import Sidebar from "../views/Sidebar/Sidebar";
import PageContent from "./PageContent";
import verifyAccessToken from "../utils/verifyToken";

function Layout() {
  const [activeRoutes, setActiveRoutes] = useState([]);
  useEffect(() => {
    const accessToken = localStorage.getItem("access-token");
    verifyAccessToken(accessToken);
  }, []);

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
