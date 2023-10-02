import React, { Suspense, lazy } from "react";
import SuspenseContent from "./SuspenseContent";
import routes from "../Routes/Routes";
import { Route, Routes } from "react-router-dom";

const Page404 = lazy(() => import("../pages/404/404"));
function PageContent({ activeRoutes, setActiveRoutes }) {
  return (
    <div className="" style={{ width: "84%" }}>
      <main className="w-100">
        <Suspense fallback={<SuspenseContent />}>
          <Routes>
            {routes.map((route, key) => {
              return (
                <Route
                  key={key}
                  exact={true}
                  path={`${route.path}`}
                  element={
                    <route.component
                      activeRoutes={activeRoutes}
                      setActiveRoutes={setActiveRoutes}
                    />
                  }
                />
              );
            })}
            <Route path="*" element={<Page404 />} />
          </Routes>
        </Suspense>
        <div className=""></div>
      </main>
    </div>
  );
}

export default PageContent;
