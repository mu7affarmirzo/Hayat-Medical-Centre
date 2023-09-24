import React from "react";
import "./Header.css";

import Logo from "../../assets/logo/logo.svg";
import { NavLink, useNavigate } from "react-router-dom";
function Header() {
  const navigate = useNavigate();
  const handleLogOut = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };
  return (
    <header>
      <div className="header-left">
        <div className="logo">
          <NavLink to={"/"}>
            <img src={Logo} alt="logo" />
          </NavLink>
        </div>
        <div className="header-links">
          <NavLink className={"header-link header-link-active"}>
            Служба приёма
          </NavLink>
          <NavLink className={"header-link"}>Задачи</NavLink>
          <NavLink className={"header-link"}>Гостиница</NavLink>
          <NavLink className={"header-link"}>Клиенты</NavLink>
          <NavLink className={"header-link"}>Oтчёты</NavLink>
        </div>
      </div>
      <div className="header-right">
        <div className="header__search">
          <svg
            width="16"
            height="16"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M11.5 21C16.7467 21 21 16.7467 21 11.5C21 6.25329 16.7467 2 11.5 2C6.25329 2 2 6.25329 2 11.5C2 16.7467 6.25329 21 11.5 21Z"
              stroke="black"
              strokeOpacity="0.38"
              strokeWidth={1.5}
              strokeLinecap="round"
              strokeLinejoin="round"
            />
            <path
              d="M22 22L20 20"
              stroke="black"
              strokeOpacity="0.38"
              strokeWidth={1.5}
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          </svg>
          <input
            type="text"
            placeholder="Быстрый поиск..."
            style={{ outline: "none", border: "none" }}
          />
        </div>
        <div className="dropdown">
          <button
            className="dropdown-toggle profile-btn"
            type="button"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            Mухиддинов
          </button>
          <ul className="dropdown-menu">
            <li onClick={handleLogOut} className="dropdown-item cursor-pointer">
              Выйти
            </li>
          </ul>
        </div>
      </div>
    </header>
  );
}

export default Header;
