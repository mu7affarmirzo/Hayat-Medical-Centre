import React, { useEffect, useState } from "react";
import "./BookingWizard.css";
import { useLocation, useNavigate } from "react-router-dom";
import { CiMoneyBill } from "react-icons/ci";
import { FiCalendar } from "react-icons/fi";
import RoomTypeRates from "../../components/containers/RoomTypeRates/RoomTypeRates";
import BookingRooms from "../../components/containers/BookingRooms/BookingRooms";
import SearchPatient from "./SearchPatient";
import PlacementSchemeFetch from "../../components/compositions/PlacementSchemeFetch/PlacementSchemeFetch";
import RoomTypeRatesFetch from "../../components/compositions/RoomTypeRatesFetch/RoomTypeRatesFetch";
import BookingRoomsFetch from "../../components/compositions/BookingRoomsFetch/BookingRoomsFetch";

const formatDate = (date) => {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
};

function BookingWizard({ activeRoutes, setActiveRoutes }) {
  const location = useLocation();
  const navigate = useNavigate();

  const handleCloseRoute = () => {
    const updateActiveRoutes = activeRoutes.filter(
      (route) => route !== location.pathname
    );
    setActiveRoutes(updateActiveRoutes);
    navigate("/reception");
  };

  // BOOKING DATA ============= = = = > > > >

  const [startDate, setStartDate] = useState('');
  const [leaveDate, setLeaveDate] = useState('');
  const [selectedPrice, setSelectedPrice] = useState({})
  const [selectedRoom, setSelectedRoom] = useState({})


  return (
    <main className="expectation__main">
      <h4 className="mb-3" style={{ fontSize: "20px", fontWeight: "500" }}>
        Мастер бронирования
      </h4>

      <div className="booking__detail-box py-2">
        <SearchPatient />
      </div>
      <nav className="p-0 ">
        <div className="nav nav-tabs gap-1" id="nav-tab" role="tablist">
          <button
            className="nav-link active text-align-start"
            id="nav-home-tab"
            data-bs-toggle="tab"
            data-bs-target="#nav-home"
            type="button"
            role="tab"
            aria-controls="nav-home"
            aria-selected="true"
            style={{ textAlign: "start" }}
          >
            <div className="d-flex justify-content-between gap-2 text-align-baseline">
              <FiCalendar style={{ fontSize: "24px" }} />
              <div>
                <p
                  className=""
                  style={{
                    fontFamily: "Roboto",
                    fontSize: "14px",
                    fontWeight: 500,
                    lineHeight: "14px",
                    marginBottom: "2px",
                  }}
                >
                  Схема размещения и сроки
                </p>
                <p
                  className="m-0"
                  style={{
                    fontFamily: "Roboto",
                    fontSize: "13px",
                    fontStyle: "normal",
                    fontWeight: 500,
                  }}
                >
                  24-29 апр 2023, заезд с 00:00, выезд до 23:59 1 взр. 1 комната
                </p>
              </div>
            </div>
          </button>
          <button
            className="nav-link"
            id="nav-profile-tab"
            data-bs-toggle="tab"
            data-bs-target="#nav-profile"
            type="button"
            role="tab"
            aria-controls="nav-profile"
            aria-selected="false"
          >
            <div
              className="d-flex justify-content-between gap-2 text-align-baseline"
              style={{
                fontFamily: "Roboto",
                fontSize: "14px",
                fontWeight: 500,
                margin: "0",
              }}
            >
              <CiMoneyBill style={{ fontSize: "24px" }} />
              <div style={{ textAlign: "start" }}>
                <p className="m-0">Тип комнаты и тарифы</p>
                <span className="m-0" style={{ fontSize: "11px" }}>
                  ПЛЮКС ЛЮКСБ 5 350 000 so’m
                </span>
              </div>
            </div>
          </button>
          {selectedPrice?.id && (

            <button
              className="nav-link"
              id="nav-contact-tab"
              data-bs-toggle="tab"
              data-bs-target="#nav-contact"
              type="button"
              role="tab"
              aria-controls="nav-contact"
              aria-selected="false"
            >
              <div
                className="d-flex justify-content-between gap-2 text-align-baseline"
                style={{
                  fontFamily: "Roboto",
                  fontSize: "14px",
                  fontWeight: 500,
                  margin: "0",
                }}
              >
                <svg
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M12.3212 10.6852L4 19L6 21M7 16L9 18M20 7.5C20 9.98528 17.9853 12 15.5 12C13.0147 12 11 9.98528 11 7.5C11 5.01472 13.0147 3 15.5 3C17.9853 3 20 5.01472 20 7.5Z"
                    stroke="black"
                    strokeOpacity="0.87"
                    strokeWidth="1.5"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  />
                </svg>
                {/* <div style={{ textAlign: "start" }}> */}
                <p className="m-0">Комната</p>
                {/* </div> */}
              </div>
            </button>
          )}

        </div>
      </nav>
      <div className="tab-content" id="nav-tabContent" role="tablist">
        <div
          className="tab-pane fade show active"
          id="nav-home"
          role="tabpanel"
          aria-labelledby="nav-home-tab"
          tabIndex="0"
        >
          <PlacementSchemeFetch startDate={startDate} setStartDate={setStartDate} setLeaveDate={setLeaveDate} leaveDate={leaveDate} />
        </div>
        <div
          className="tab-pane fade"
          id="nav-profile"
          role="tabpanel"
          aria-labelledby="nav-profile-tab"
          tabIndex="0"
        >
          <RoomTypeRatesFetch selectedPrice={selectedPrice} setSelectedPrice={setSelectedPrice} />
        </div>
        <div
          className="tab-pane fade"
          id="nav-contact"
          role="tabpanel"
          aria-labelledby="nav-contact-tab"
          tabIndex="0"
        >
          <BookingRoomsFetch selectedRoom={selectedRoom} setSelectedRoom={setSelectedRoom} />
        </div>
      </div>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          padding: "8px",
          border: "1px solid var(--light, rgba(0,0, 0, 0.1))",
          marginTop: "24px",
        }}
      >
        <div>
          {selectedRoom.id ? (

            <button className=" green__btn" style={{ padding: "8px 20px" }}>
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
          ) : (
            <button
              style={{
                padding: "8px 16px",
                fontSize: "14px",
                fontStyle: "normal",
                fontWeight: "400",
                lineHeight: "20px",
                borderRadius: "4px",
                border: "1px solid rgba(0, 0, 0, 0.23)",
                background: "var(--background, #f5f5f5)",
              }}
            >
              <svg
                width="15"
                height="14"
                viewBox="0 0 18 14"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M1 7.61111L5.92308 12.5L17 1.5"
                  stroke="black"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              </svg>
              Сохранить
            </button>
          )}
        </div>

        <div>
          <button
            onClick={handleCloseRoute}
            style={{
              padding: "8px 16px",
              fontSize: "14px",
              fontStyle: "normal",
              fontWeight: "400",
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
    </main >
  );
}

export default BookingWizard;
