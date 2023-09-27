import React, { useEffect, useState } from "react";
import "./Sidebar.css";
import { Link, useLocation, useNavigate } from "react-router-dom";
import { extraRoutes, routes } from "../../Routes/sidebar";
function Sidebar({ activeRoutes, setActiveRoutes }) {
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    // Add the current location to the active routes array if it's not already there
    if (!activeRoutes.includes(location.pathname)) {
      setActiveRoutes((prevRoutes) => [...prevRoutes, location.pathname]);
    }
  }, [location, activeRoutes]);
  const sortedRoutes = [...extraRoutes].filter((a, b) =>
    activeRoutes.includes(a.path) ? 1 : activeRoutes.includes(b.path) ? -1 : 0
  );

  return (
    <aside className="d-flex flex-column justify-content-between">
      <div className="d-flex flex-column gap-1">
        <div className="section__top">
          <button onClick={() => navigate("/booking_wizard")}>
            Создать бронь
          </button>
        </div>
        {routes.map((route, k) => {
          return (
            <button
              key={k}
              style={{ display: "flex", alignItems: "center", gap: 4 }}
              className={
                location.pathname === route.path
                  ? "dispatching-side__btn dispatching-side__btn-active"
                  : "dispatching-side__btn"
              }
              onClick={() => navigate(route.path)}
            >
              {route.icon} {route.name}
            </button>
          );
        })}
      </div>

      {/* = SECTION BOTTOM = */}
      {sortedRoutes ? (
        <div className="d-flex flex-column gap-1">
          <label htmlFor="">Открытые карточки</label>
          {sortedRoutes.map((route, index) => (
            <button
              key={index}
              className={
                location.pathname === route.path
                  ? "dispatching-side__btn dispatching-side__btn-active"
                  : "dispatching-side__btn"
              }
              onClick={() => navigate(route.path)}
              style={{
                display: "flex",
                alignItems: "center",
                gap: 4,
                border: "none",
              }}
            >
              {route?.icon} {route?.name}
            </button>
          ))}
        </div>
      ) : (
        <></>
      )}
    </aside>
  );
}

export default Sidebar;
