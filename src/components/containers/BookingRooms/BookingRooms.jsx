import React from "react";
import "./BookingRooms.css";
import BookingRoomsTable from "./BookingRoomsTable";
function BookingRooms({ rooms, selectedRoom, setSelectedRoom }) {
  console.log(rooms)



  return (
    <>
      <div className="booking__detail-box py-2 gap-2 align-items-end">
        <div className="d-flex flex-column" style={{ width: "30%" }}>
          <label htmlFor="" style={{ color: "rgba(0, 0, 0, 0.54)" }}>
            Расположение
          </label>
          <select
            name=""
            id=""
            style={{
              width: "100%",
              padding: "5px",
              border: "1px solid rgba(0, 0, 0, 0.23)",
            }}
          >
            <option value=""></option>
            <option value=""></option>
          </select>
        </div>
        <div className="d-flex flex-column" style={{ width: "30%" }}>
          <label htmlFor="" style={{ color: "rgba(0, 0, 0, 0.54)" }}>
            Вид
          </label>
          <select
            name=""
            id=""
            style={{
              width: "100%",
              padding: "5px",
              border: "1px solid rgba(0, 0, 0, 0.23)",
            }}
          >
            <option value=""></option>
            <option value=""></option>
          </select>
        </div>
        <div className="d-flex flex-column" style={{ width: "30%" }}>
          <label htmlFor="" style={{ color: "rgba(0, 0, 0, 0.54)" }}>
            Теги
          </label>
          <input
            type="text"
            style={{
              width: "100%",
              padding: "5px",
              border: "1px solid rgba(0, 0, 0, 0.23)",
            }}
          />
        </div>

        <button
          style={{
            padding: "5px 12px",
            background: "#F5F5F5",
            borderRadius: "4px",
            border: "1px solid rgba(0, 0, 0, 0.23)",
          }}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="22"
            height="22"
            viewBox="0 0 22 22"
            fill="none"
          >
            <path
              d="M5.5 5.5L16.5 16.5M16.5 5.5L5.5 16.5"
              stroke="black"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          </svg>
        </button>
      </div>

      <div className="expectation__table">
        <table className="room__table">
          <thead>
            <tr>
              <th>Комната</th>
              <th>Дата выезда</th>
              <th>Дата заезда</th>
              <th>Пол</th>
              <th>Возраст</th>
              <th>Вид</th>
              <th>Корпус</th>
              <th>Этаж</th>
              <th>Статус уборки</th>
              <th>Вид уборки</th>
              <th>Занят?</th>
              <th>Комментарии</th>
              <th>K-во использований</th>
            </tr>
          </thead>

          <tbody>
            {rooms?.map((item, index) => <BookingRoomsTable key={index} {...item} item={item} selectedRoom={selectedRoom} setSelectedRoom={setSelectedRoom} />)}
          </tbody>
        </table>
      </div>
    </>
  );
}

export default BookingRooms;
