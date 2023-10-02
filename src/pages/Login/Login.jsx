import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./Login.css";

import LoginImg from "../../assets/imgs/logus-img.png";
import EyeIcon from "../../assets/icons/remove-red-eye.svg";

function Login() {
  const navigate = useNavigate();
  const [showPassword, setShowPassword] = useState(false);

  const handleTogglePassword = () => {
    setShowPassword(!showPassword);
  };

  const handleLogin = (e) => {
    e.preventDefault();
    localStorage.setItem("token", "12345");
    navigate("/reception");
  };
  return (
    <div className="login">
      <div className="login-left">
        <div className="login-form">
          <h1>Вход в систему Госпиталь</h1>
          <h2>Hayat Medical Center</h2>
          <form action="" className="mt-3" onSubmit={handleLogin}>
            <div className="form-floating mb-3 w-100">
              <input
                type="text"
                className="form-control"
                id="floatingInput"
                placeholder="login"
              />
              <label htmlFor="floatingInput">Логин</label>
            </div>
            <div className="form-floating w-100">
              <input
                type={showPassword ? "text" : "password"}
                className="form-control"
                id="floatingPassword"
                placeholder="Password"
              />
              <label htmlFor="floatingPassword">Пароль</label>
              <img onClick={handleTogglePassword} src={EyeIcon} alt="icon" />
            </div>
            <div className="form-bottom">
              <div className="form-check">
                <input
                  className="form-check-input"
                  type="checkbox"
                  id="gridCheck"
                />
                <label className="form-check-label" htmlFor="gridCheck">
                  Запомните пароль
                </label>
              </div>
              <Link to={""}>Забыли пароль ?</Link>
            </div>
            <button id="loginButton">Вход в систему</button>
          </form>
        </div>
      </div>
      <div className="login-right">
        <img src={LoginImg} alt="img" />
      </div>
    </div>
  );
}

export default Login;
