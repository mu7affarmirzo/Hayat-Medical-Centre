import React from "react";
import "./PlacementScheme.css";
function PlacementScheme() {
  const days = [
    { date: "24 апрель", week: "Пн" },
    { date: "25 апрель", week: "Вт" },
    { date: "26 апрель", week: "Ср" },
    { date: "27 апрель", week: "Чт" },
    { date: "28 апрель", week: "Пт" },
    { date: "29 апрель", week: "Сб" },
    { date: "30 апрель", week: "Вс" },
    { date: "01 май", week: "Вт" },
    { date: "02 май", week: "Ср" },
    { date: "03 май", week: "Пт" },
    { date: "04 май", week: "Сб" },
    { date: "05 май", week: "Вс" },
    { date: "06 май", week: "Пн" },
    { date: "07 май", week: "Вт" },
    { date: "08 май", week: "Ср" },
    { date: "09 май", week: "Чт" },
  ];
  return (
    <>
      <div
        className="d-flex justify-content-between gap-2 align-items-end mb-4"
        style={{ width: "60%" }}
      >
        <div className="" style={{ width: "80px" }}>
          <label className="mb-3" htmlFor="quantity">
            Кол-во
          </label>
          <input
            type="number"
            id="quantity"
            style={{
              width: "100%",
              padding: "5px",
              border: "1px solid rgba(0, 0, 0, 0.23)",
            }}
          />
        </div>

        <div>
          <label className="mb-3" htmlFor="guests-accommodation">
            Гости и размещение
          </label>
          <div
            className="d-flex justify-content-between gap-2 align-items-center"
            style={{ width: "160px" }}
          >
            <label htmlFor="version">Вэр.:</label>
            <input
              type="number"
              id="version"
              style={{
                width: "70%",
                padding: "5px",
                border: "1px solid rgba(0, 0, 0, 0.23)",
              }}
            />
          </div>
        </div>

        <div className="d-flex flex-column" style={{ width: "200px" }}>
          <label className="mb-3" htmlFor="stay-period">
            Период проживания
          </label>
          <select
            name="stay-period"
            id="stay-period"
            style={{
              width: "100%",
              padding: "7px",
              border: "1px solid rgba(0, 0, 0, 0.23)",
            }}
          >
            <option value="">24.04.2023 0:00</option>
            <option value=""></option>
          </select>
        </div>

        <div className="d-flex flex-column" style={{ width: "80px" }}>
          <input
            type="number"
            style={{
              width: "100%",
              padding: "5px",
              border: "1px solid rgba(0, 0, 0, 0.23)",
            }}
          />
        </div>

        <div
          className="d-flex justify-content-between gap-2 align-items-center"
          style={{ width: "250px" }}
        >
          <label className="" htmlFor="days">
            дней по
          </label>
          <select
            name="days"
            id="days"
            style={{
              width: "70%",
              padding: "7px",
              border: "1px solid rgba(0, 0, 0, 0.23)",
            }}
          >
            <option value="">24.04.2023 0:00</option>
            <option value=""></option>
          </select>
        </div>
      </div>
      <div className="expectation__table m-0" style={{ width: "100%" }}>
        <table className="type_room_table">
          <thead>
            <tr>
              <th rowSpan={2} style={{ fontSize: "20px" }}>
                Тип комнаты
              </th>
              {days.map((item, index) => (
                <th
                  key={index}
                  style={{
                    color: item.week === "Вс" ? "red" : "black",
                  }}
                >
                  {item.date} <br />
                  {item.week}
                </th>
              ))}
            </tr>
            <tr>
              <th>25</th>
              <th>25</th>
              <th>25</th>
              <th>25</th>
              <th>25</th>
              <th>25</th>
              <th>25</th>
              <th>25</th>
              <th>25</th>
              <th>25</th>
              <th>25</th>
              <th>25</th>
              <th>25</th>
              <th>25</th>
              <th>25</th>
              <th>25</th>
            </tr>
          </thead>

          <tbody>
            <tr></tr>
          </tbody>
        </table>
      </div>
    </>
  );
}

export default PlacementScheme;
