import React, { useEffect, useState } from "react";
import "./PlacementScheme.css";
import axios from "axios";
import { BASE_URL } from "../../../constants/constants";



function PlacementScheme({ dates, formatDateWithWeekday, transformedData, overallNumbers, startDate, leaveDate, setStartDate, setLeaveDate, daysDifference }) {
  const filteredDates = dates.filter((date) => date >= startDate && date <= leaveDate);

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
          <input type="date" defaultValue={startDate} onChange={(e) => setStartDate(e.target)} style={{
            width: "100%",
            padding: "7px",
            border: "1px solid rgba(0, 0, 0, 0.23)",
          }} />
        </div>

        <div className="d-flex flex-column" style={{ width: "80px" }}>
          <input
            value={daysDifference}
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
          <label style={{ whiteSpace: "nowrap" }} className="" htmlFor="days">
            дней по
          </label>
          <input type="date" defaultValue={leaveDate} onChange={(e) => setLeaveDate(e.target.value)} style={{
            width: "100%",
            padding: "7px",
            border: "1px solid rgba(0, 0, 0, 0.23)",
          }} />
        </div>
      </div>
      <div className="expectation__table m-0" style={{ width: "100%" }}>
        <table className="type_room_table">
          <thead>
            <tr>
              <th rowSpan={2} style={{ fontSize: "20px", position: "sticky", top: "0", left: "0" }}>
                Тип комнаты
              </th>
              {dates?.map((date, index) => (
                <th className="free__rooms_dates" key={index}>{formatDateWithWeekday(date)}</th>
              ))}
            </tr>
            <tr>
              {Object.keys(overallNumbers).map((date) => (
                <th key={date} className="all__free__rooms">
                  {overallNumbers[date]}
                </th>
              ))}
            </tr>
          </thead>

          <tbody>
            {Object.keys(transformedData).map((roomType, rowIndex) => (
              <tr key={rowIndex}>
                <td className="position-sticky start-0 bg-white">{roomType}</td>
                {dates?.map((date, colIndex) => (
                  <td className={`${filteredDates.includes(date) ? "freeRoom__selected" : "freeRoomTable"}`} style={{ textAlign: "center" }} key={colIndex}>{transformedData[roomType][date] || 0}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}

export default PlacementScheme;
