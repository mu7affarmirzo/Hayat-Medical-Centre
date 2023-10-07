import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./Login.css";

import LoginImg from "../../assets/imgs/logus-img.png";
import EyeIcon from "../../assets/icons/remove-red-eye.svg";
import axios from "axios";
import { BASE_URL } from "../../constants/constants";

import { BiErrorCircle } from "react-icons/bi";
import { HiXMark } from "react-icons/hi2";

function Login() {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const [showPassword, setShowPassword] = useState(false);

  const handleTogglePassword = () => {
    setShowPassword(!showPassword);
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      axios
        .post(`${BASE_URL}/api/v1/token/`, {
          email: email,
          password: password,
        })
        .then((res) => {
          if (res?.data) {
            localStorage.setItem("access-token", res?.data?.access);
            localStorage.setItem("refresh-token", res?.data?.refresh);

            navigate("/reception");
          } else {
          }
        })
        .catch((err) => {
          console.log(err);
          setError(err);
        });
    } catch (error) {
      setError(error);
    }
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
                style={{
                  border: error
                    ? "2px solid var(--03-error-main, #F44336)"
                    : "",
                }}
                id="floatingInput"
                placeholder="login"
                onChange={(e) => setEmail(e.target.value)}
              />
              <label htmlFor="floatingInput">Логин</label>
            </div>
            <div className="form-floating w-100">
              <input
                style={{
                  border: error
                    ? "2px solid var(--03-error-main, #F44336)"
                    : "",
                }}
                type={showPassword ? "text" : "password"}
                className="form-control"
                id="floatingPassword"
                placeholder="Password"
                onChange={(e) => setPassword(e.target.value)}
              />
              <label htmlFor="floatingPassword">Пароль</label>
              <img onClick={handleTogglePassword} src={EyeIcon} alt="icon" />
            </div>
            {error ? (
              <div className="error__alert">
                <div className="d-flex align-items-center gap-2 font-white">
                  <BiErrorCircle /> Логин или пароль введен неправильно
                </div>
                <button onClick={() => setError(null)}>
                  <HiXMark />
                </button>
              </div>
            ) : (
              ""
            )}

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
            <button type="submit" id="loginButton">
              Вход в систему
            </button>
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
