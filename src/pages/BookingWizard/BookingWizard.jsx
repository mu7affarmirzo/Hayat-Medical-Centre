import React from "react";
import "./BookingWizard.css";
import { useLocation, useNavigate } from "react-router-dom";
import { CiMoneyBill } from "react-icons/ci";
import { FiCalendar } from "react-icons/fi";
import PlacementScheme from "../../components/containers/PlacementScheme/PlacementScheme";
import RoomTypeRates from "../../components/containers/RoomTypeRates/RoomTypeRates";
import BookingRooms from "../../components/containers/BookingRooms/BookingRooms";
function BookingWizard({ activeRoutes, setActiveRoutes }) {
  const location = useLocation();
  const navigate = useNavigate();

  const handleCloseRoute = () => {
    const updateActiveRoutes = activeRoutes.filter(
      (route) => route !== location.pathname
    );
    setActiveRoutes(updateActiveRoutes);
    navigate("/");
  };

  return (
    <main className="expectation__main">
      <h4 className="mb-3" style={{ fontSize: "20px", fontWeight: "500" }}>
        Мастер бронирования
      </h4>

      <div className="booking__detail-box py-2">
        <div
          className="d-flex justify-content-between align-items-center"
          style={{ width: "100%" }}
        >
          <label htmlFor="" style={{ fontSize: "14px" }}>
            ФИО гостя
          </label>
          <input
            className="booking_input_bg"
            type="text"
            style={{
              width: "90%",
              padding: "4px 10px",
              background: "#fff",
              borderRadius: "4px",
              border: "1px solid rgba(0, 0, 0, 0.23)",
              backgroundPosition: "99% center !important",
            }}
          />
        </div>
      </div>
      <nav className="p-0 ">
        <div class="nav nav-tabs gap-1" id="nav-tab" role="tablist">
          <button
            class="nav-link active text-align-start"
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
            class="nav-link"
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
          <button
            class="nav-link"
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
              <CiMoneyBill style={{ fontSize: "24px" }} />
              <div style={{ textAlign: "start" }}>
                <p className="m-0">Тип комнаты и тарифы</p>
                <span className="m-0" style={{ fontSize: "11px" }}>
                  ПЛЮКС ЛЮКСБ 5 350 000 so’m
                </span>
              </div>
            </div>
          </button>
        </div>
      </nav>
      <div class="tab-content" id="nav-tabContent" role="tablist">
        <div
          class="tab-pane fade show active"
          id="nav-home"
          role="tabpanel"
          aria-labelledby="nav-home-tab"
          tabindex="0"
        >
          <PlacementScheme />
        </div>
        <div
          class="tab-pane fade"
          id="nav-profile"
          role="tabpanel"
          aria-labelledby="nav-profile-tab"
          tabindex="0"
        >
          <RoomTypeRates />
        </div>
        <div
          class="tab-pane fade"
          id="nav-contact"
          role="tabpanel"
          aria-labelledby="nav-contact-tab"
          tabindex="0"
        >
          <BookingRooms />
        </div>
      </div>
      <button onClick={handleCloseRoute}>close</button>
    </main>
  );
}

export default BookingWizard;
