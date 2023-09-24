import React, { Suspense, lazy } from "react";
import SuspenseContent from "./SuspenseContent";
import routes from "../Routes/Routes";
import { Route, Routes } from "react-router-dom";

const Page404 = lazy(() => import("../pages/404/404"));
function PageContent() {
  return (
    <div>
      <main className="q-100">
        <Suspense fallback={<SuspenseContent />}>
          <Routes>
            {routes.map((route, key) => {
              return (
                <Route
                  key={key}
                  exact={true}
                  path={`${route.path}`}
                  element={<route.component />}
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
