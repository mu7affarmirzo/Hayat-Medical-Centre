import React from "react";
import "./Sidebar.css";
import { useLocation, useNavigate } from "react-router-dom";
import routes from "../../Routes/sidebar";
function Sidebar() {
  const navigate = useNavigate();
  const location = useLocation();
  return (
    <aside className="d-flex flex-column justify-content-between" style={{}}>
      <div className="d-flex flex-column gap-1">
        <div className="section__top">
          <button>Создать бронь</button>
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
    </aside>
  );
}

export default Sidebar;
