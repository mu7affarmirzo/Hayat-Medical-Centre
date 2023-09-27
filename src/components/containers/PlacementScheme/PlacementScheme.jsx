import React from "react";
import "./PlacementScheme.css";
function PlacementScheme() {
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
              <th style={{ fontSize: "20px" }}>Тип комнаты</th>
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
