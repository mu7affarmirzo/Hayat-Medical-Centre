import React from "react";
import "./Bron.css";
function Bron() {
  return (
    <main class="expectation__main">
      <div class="booking__top-box">
        <div class="booking__heading-box">
          <h4>Бронь № 502231</h4>

          <button class="booking__heading-btn">Бронь</button>
        </div>

        <div class="booking__top-btn">
          <button
            class="booking__heading-btn"
            style={{ backgroundColor: "#f79e98" }}
          >
            ЛЮКС
          </button>

          <button class="booking_top_btn">
            <img src="../assets/icons/tags.svg" alt="" />
          </button>

          <button class="booking_top_btn">
            <img src="../assets/icons/user-plus.svg" alt="" />
          </button>

          <button class="booking_top_btn">
            <img src="../assets/icons/file-copy.svg" alt="" />
          </button>

          <button class="booking_top_btn">
            <img src="../assets/icons/refresh-ccw-clock.svg" alt="" />
          </button>

          <button class="booking_top_btn">
            <img src="../assets/icons/printer.svg" alt="" />
          </button>
        </div>
      </div>

      <div className="booking__detail-box">
        <div
          className="d-flex justify-content-between align-items-center"
          style={{ width: "430px" }}
        >
          <label htmlFor="" style={{ fontSize: "14px" }}>
            ФИО гостя
          </label>
          <input
            className="booking_input_bg"
            type="text"
            value="Ким Борис"
            disabled
            style={{
              width: "340px",
              padding: "4px 10px",
              background: "#f8ed8d",
              borderRadius: "4px",
              border: "1px solid rgba(0, 0, 0, 0.23)",
            }}
          />
        </div>

        <div>
          <p
            style={{
              margin: "0",
              color:
                "var(--text-color-light-mode-disabled, rgba(0, 0, 0, 0.38))",
              fontFamily: "Roboto",
              fontSize: "12px",
              fontStyle: "normal",
              fontWeight: "400",
              lineHeight: "20px",
              letterSpacing: "0.4px",
            }}
          >
            Даты проживания
          </p>
          <p
            style={{
              margin: "0",
              color:
                "var(--text-color-light-mode-primary, rgba(0, 0, 0, 0.87))",
              fontFamily: "Roboto",
              fontSize: "14px",
              fontStyle: "normal",
              fontWeight: "400",
              lineHeight: "20px",
              letterSpacing: "0.15px",
            }}
          >
            06-11 май 2023, заезд с 00:00, выезд до 23:59
          </p>
        </div>

        <div>
          <p
            style={{
              margin: "0",
              color:
                "var(--text-color-light-mode-disabled, rgba(0, 0, 0, 0.38))",
              fontFamily: "Roboto",
              fontSize: "12px",
              fontStyle: "normal",
              fontWeight: "400",
              lineHeight: "20px",
              letterSpacing: "0.4px",
            }}
          >
            Схема проживания
          </p>
          <p
            style={{
              margin: "0",
              color:
                "var(--text-color-light-mode-primary, rgba(0, 0, 0, 0.87))",
              fontFamily: "Roboto",
              fontSize: "14px",
              fontStyle: "normal",
              fontWeight: "400",
              lineHeight: "20px",
              letterSpacing: "0.15px",
            }}
          >
            1 взр.
          </p>
        </div>

        <div>
          <p
            style={{
              margin: "0",
              color:
                "var(--text-color-light-mode-disabled, rgba(0, 0, 0, 0.38))",
              fontFamily: "Roboto",
              fontSize: "12px",
              fontStyle: "normal",
              fontWeight: "400",
              lineHeight: "20px",
              letterSpacing: "0.4px",
            }}
          >
            Тариф и скидка
          </p>
          <p
            style={{
              margin: "0",
              color:
                "var(--text-color-light-mode-primary, rgba(0, 0, 0, 0.87))",
              fontFamily: "Roboto",
              fontSize: "14px",
              fontStyle: "normal",
              fontWeight: "400",
              lineHeight: "20px",
              letterSpacing: "0.15px",
            }}
          >
            ЛЮКС
          </p>
        </div>

        <div>
          <p
            style={{
              margin: "0",
              color:
                "var(--text-color-light-mode-disabled, rgba(0, 0, 0, 0.38))",
              fontFamily: "Roboto",
              fontSize: "12px",
              fontStyle: "normal",
              fontWeight: "400",
              lineHeight: "20px",
              letterSpacing: "0.4px",
            }}
          >
            Тип комнаты
          </p>
          <p
            style={{
              display: "flex",
              margin: "0",
              color:
                "var(--text-color-light-mode-primary, rgba(0, 0, 0, 0.87))",
              fontFamily: "Roboto",
              fontSize: "14px",
              fontStyle: "normal",
              fontWeight: "400",
              lineHeight: "20px",
              letterSpacing: "0.15px",
            }}
          >
            <span
              style={{
                display: "inline-block",
                width: "8px",
                height: "20px",
                marginRight: "10px",
                borderRadius: "2px",
                background: "#a4cbfa",
              }}
            ></span>
            СТД.К
          </p>
        </div>

        <div>
          <p
            style={{
              margin: "0",
              color:
                "var(--text-color-light-mode-disabled, rgba(0, 0, 0, 0.38))",
              fontFamily: "Roboto",
              fontSize: "12px",
              fontStyle: "normal",
              fontWeight: "400",
              lineHeight: "20px",
              letterSpacing: "0.4px",
            }}
          >
            Комната
          </p>
          <p
            style={{
              margin: "0",
              color:
                "var(--text-color-light-mode-primary, rgba(0, 0, 0, 0.87))",
              fontFamily: "Roboto",
              fontSize: "14px",
              fontStyle: "normal",
              fontWeight: "400",
              lineHeight: "20px",
              letterSpacing: "0.15px",
            }}
          >
            202.2
          </p>
        </div>
      </div>

      <ul className="nav nav-tabs" id="myTab" role="tablist">
        <li className="nav-item" role="presentation">
          <a href="booking.html">
            <button
              className="nav-link active"
              id="home-tab"
              data-bs-toggle="tab"
              data-bs-target="#home-tab-pane"
              type="button"
              role="tab"
              aria-controls="home-tab-pane"
              aria-selected="true"
            >
              Бронь
            </button>
          </a>
        </li>
        <li className="nav-item" role="presentation">
          <a href="guests.html">
            <button
              className="nav-link"
              id="profile-tab"
              data-bs-toggle="tab"
              data-bs-target="#profile-tab-pane"
              type="button"
              role="tab"
              aria-controls="profile-tab-pane"
              aria-selected="false"
            >
              Гости
            </button>
          </a>
        </li>
        <li className="nav-item" role="presentation">
          <a href="">
            <button
              className="nav-link"
              id="contact-tab"
              data-bs-toggle="tab"
              data-bs-target="#contact-tab-pane"
              type="button"
              role="tab"
              aria-controls="contact-tab-pane"
              aria-selected="false"
            >
              Проживание
              <span style={{ color: "rgba(0, 0, 0, 0.5)" }}>
                6 x 2 000 000 so’m
              </span>
            </button>
          </a>
        </li>
      </ul>

      <div className="d-flex justify-content-between">
        <div className="booking__guest-box">
          <h5
            style={{ marginBottom: "10px", fontSize: "16px", fontWeight: 400 }}
          >
            Информация о госте
          </h5>

          <div
            className="d-flex justify-content-between"
            style={{ width: "650px", padding: "10px", background: "#f5f5f5" }}
          >
            <div className="d-flex flex-column" style={{ width: "300px" }}>
              <label htmlFor="" style={{ color: "rgba(0, 0, 0, 0.54)" }}>
                Телефон
              </label>
              <input
                type="text"
                style={{
                  width: "100%",
                  padding: "8px",
                  border: "1px solid rgba(0, 0, 0, 0.23)",
                  borderRadius: "4px",
                }}
              />
            </div>
            <div className="d-flex flex-column" style={{ width: "300px" }}>
              <label htmlFor="" style={{ color: "rgba(0, 0, 0, 0.54)" }}>
                Email
              </label>
              <input
                type="text"
                style={{
                  width: "100%",
                  padding: "8px",
                  border: "1px solid rgba(0, 0, 0, 0.23)",
                  borderRadius: "4px",
                }}
              />
            </div>
          </div>
        </div>

        <div className="booking__guest-box">
          <h5
            style={{ marginBottom: "10px", fontSize: "16px", fontWeight: 400 }}
          >
            Корпоративный клиент
          </h5>

          <div
            className="d-flex justify-content-between"
            style={{ width: "480px", padding: "10px", background: "#f5f5f5" }}
          >
            <div className="d-flex flex-column" style={{ width: "220px" }}>
              <label htmlFor="" style={{ color: "rgba(0, 0, 0, 0.54)" }}>
                Компания
              </label>
              <input
                type="text"
                value="№300001 - Физлицо"
                style={{
                  width: "100%",
                  padding: "8px",
                  border: "1px solid rgba(0, 0, 0, 0.23)",
                  borderRadius: "4px",
                }}
              />
            </div>
            <div className="d-flex flex-column" style={{ width: "220px" }}>
              <label htmlFor="" style={{ color: "rgba(0, 0, 0, 0.54)" }}>
                Менеджер
              </label>
              <select
                name=""
                id=""
                style={{
                  width: "100%",
                  padding: "8px",
                  border: "1px solid rgba(0, 0, 0, 0.23)",
                  borderRadius: "4px",
                }}
              >
                <option value="">Мухиддинов Ж К.</option>
                <option value=""></option>
              </select>
            </div>
          </div>
        </div>
      </div>

      <div className="d-flex justify-content-between">
        <div className="booking__guest-box">
          <h5
            style={{ marginBottom: "10px", fontSize: "16px", fontWeight: 400 }}
          >
            Маркетинговая информация
          </h5>

          <div
            className="d-flex justify-content-between"
            style={{ width: "650px", padding: "10px", background: "#f5f5f5" }}
          >
            <div className="d-flex flex-column" style={{ width: "150px" }}>
              <label htmlFor="" style={{ color: "rgba(0, 0, 0, 0.54)" }}>
                Сегмент рынка
              </label>
              <select
                name=""
                id=""
                style={{
                  width: "100%",
                  padding: "4px",
                  fontSize: "14px",
                  border: "1px solid rgba(0, 0, 0, 0.23)",
                  borderRadius: "4px",
                }}
              >
                <option value="">ОСН - Основной</option>
                <option value=""></option>
              </select>
            </div>
            <div className="d-flex flex-column" style={{ width: "150px" }}>
              <label htmlFor="" style={{ color: "rgba(0, 0, 0, 0.54)" }}>
                Источник
              </label>
              <select
                name=""
                id=""
                style={{
                  width: "100%",
                  padding: "4px",
                  fontSize: "14px",
                  border: "1px solid rgba(0, 0, 0, 0.23)",
                  borderRadius: "4px",
                }}
              >
                <option value="">РЕКОМ - Рекомендации</option>
                <option value=""></option>
              </select>
            </div>
            <div className="d-flex flex-column" style={{ width: "150px" }}>
              <label htmlFor="" style={{ color: "rgba(0, 0, 0, 0.54)" }}>
                Трек-код
              </label>
              <select
                name=""
                id=""
                style={{
                  width: "100%",
                  padding: "4px",
                  fontSize: "14px",
                  border: "1px solid rgba(0, 0, 0, 0.23)",
                  borderRadius: "4px",
                }}
              >
                <option value="">НВ - Новый врач</option>
                <option value=""></option>
              </select>
            </div>
            <div className="d-flex flex-column" style={{ width: "150px" }}>
              <label htmlFor="" style={{ color: "rgba(0, 0, 0, 0.54)" }}>
                ГЕО
              </label>
              <select
                name=""
                id=""
                style={{
                  width: "100%",
                  padding: "4px",
                  fontSize: "14px",
                  border: "1px solid rgba(0, 0, 0, 0.23)",
                  borderRadius: "4px",
                }}
              >
                <option value="">ТАШ - Ташкент</option>
                <option value=""></option>
              </select>
            </div>
          </div>
        </div>

        <div className="booking__guest-box">
          <h5
            style={{ marginBottom: "10px", fontSize: "16px", fontWeight: 400 }}
          >
            Гарантия
          </h5>

          <div
            className="d-flex justify-content-between"
            style={{ width: "480px", padding: "10px", background: "#f5f5f5" }}
          >
            <div className="d-flex flex-column" style={{ width: "150px" }}>
              <label htmlFor="" style={{ color: "rgba(0, 0, 0, 0.54)" }}>
                Гарантия
              </label>
              <select
                name=""
                id=""
                style={{
                  width: "100%",
                  padding: "4px",
                  fontSize: "14px",
                  border: "1px solid rgba(0, 0, 0, 0.23)",
                  borderRadius: "4px",
                }}
              >
                <option value="">ЗАЕЗД - Оплата при поселении</option>
                <option value=""></option>
              </select>
            </div>
            <div className="d-flex flex-column" style={{ width: "150px" }}>
              <label htmlFor="" style={{ color: "rgba(0, 0, 0, 0.54)" }}>
                Сумма
              </label>
              <input
                type="number"
                style={{
                  width: "100%",
                  padding: "4px",
                  fontSize: "14px",
                  border: "1px solid rgba(0, 0, 0, 0.23)",
                  borderRadius: "4px",
                }}
              />
            </div>
            <div className="d-flex flex-column" style={{ width: "150px" }}>
              <label htmlFor="" style={{ color: "rgba(0, 0, 0, 0.54)" }}>
                Внести до
              </label>
              <input
                type="date"
                style={{
                  width: "100%",
                  padding: "4px",
                  fontSize: "14px",
                  border: "1px solid rgba(0, 0, 0, 0.23)",
                  borderRadius: "4px",
                }}
              />
            </div>
          </div>
        </div>
      </div>

      <div>
        <div
          className="d-flex flex-column"
          style={{ width: "100%", marginBottom: "20px" }}
        >
          <label htmlFor="" style={{ color: "rgba(0, 0, 0, 0.54)" }}>
            Комментарии
          </label>
          <textarea
            style={{ display: "block", width: "100%", height: "300px" }}
          ></textarea>
        </div>
      </div>

      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          padding: "8px",
          border: "1px solid var(--light, rgba(0, 0, 0, 0.1))",
        }}
      >
        <div>
          <button className="green__btn" style={{ padding: "8px 20px" }}>
            <svg
              width="15"
              height="14"
              viewBox="0 0 18 14"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M1 7.61111L5.92308 12.5L17 1.5"
                stroke="#fff"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
            Сохранить
          </button>
          <button
            style={{
              padding: "8px 16px",
              fontSize: "14px",
              fontStyle: "normal",
              fontWeight: 400,
              lineHeight: "20px",
              borderRadius: "4px",
              border: "1px solid rgba(0, 0, 0, 0.23)",
              background: "var(--background, #f5f5f5)",
            }}
          >
            Незаезд
          </button>
          <button className="green__btn" style={{ padding: "8px 20px" }}>
            Поселить
          </button>
          <button
            style={{
              padding: "8px 16px",
              fontSize: "14px",
              fontStyle: "normal",
              fontWeight: 400,
              lineHeight: "20px",
              borderRadius: "4px",
              border: "1px solid rgba(0, 0, 0, 0.23)",
              background: "var(--background, #f5f5f5)",
            }}
          >
            В лист ожидания
          </button>
          <button
            style={{
              padding: "8px 16px",
              fontSize: "14px",
              fontStyle: "normal",
              fontWeight: 400,
              lineHeight: "20px",
              borderRadius: "4px",
              border: "1px solid rgba(0, 0, 0, 0.23)",
              background: "var(--background, #f5f5f5)",
            }}
          >
            Аннулировать
          </button>
          <button
            style={{
              padding: "8px 16px",
              fontSize: "14px",
              fontStyle: "normal",
              fontWeight: 400,
              lineHeight: "20px",
              borderRadius: "4px",
              border: "1px solid rgba(0, 0, 0, 0.23)",
              background: "var(--background, #f5f5f5)",
            }}
          >
            Опоздание
          </button>
        </div>

        <div>
          <button
            style={{
              padding: "8px 16px",
              fontSize: "14px",
              fontStyle: "normal",
              fontWeight: 400,
              lineHeight: "20px",
              borderRadius: "4px",
              border: "1px solid rgba(0, 0, 0, 0.23)",
              background: "var(--background, #f5f5f5)",
            }}
          >
            Закрыть
          </button>
        </div>
      </div>
    </main>
  );
}

export default Bron;
