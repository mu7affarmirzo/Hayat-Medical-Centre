import React from "react";
import Header from "../views/Header/Header";
import Siderbar from "../views/Sidebar/Sidebar";
import PageContent from "./PageContent";

function Layout() {
  return (
    <div>
      <Header />
      <div className="d-flex">
        <Siderbar />
        <PageContent />
      </div>
    </div>
  );
}

export default Layout;
