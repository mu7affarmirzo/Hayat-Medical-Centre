import React from "react";
import "./RoomTypeRates.css";
import { HiOutlineBan } from "react-icons/hi"
function RoomTypeRates({ roomTypeTariff, selectedPrice, setSelectedPrice }) {

  const tariffNames = [...new Set(roomTypeTariff.map(item => item.tariff.name))];
  const roomTypeNames = [...new Set(roomTypeTariff.map(item => item.room_type.name))];

  // SELECTING PRICE = = = = = >> > >
  const toggleSelectedPrice = (item) => {
    setSelectedPrice(item.id === selectedPrice?.id ? null : item);
  };

  console.log(selectedPrice)


  return (
    <div className="d-flex justify-content-between gap-2 mb-4">
      <div className="expectation__table m-0" style={{ width: "78%" }}>
        <table className="type_room_table">
          <thead>
            <tr>
              {tariffNames.map(tariffName => (
                <th key={tariffName}>{tariffName}</th>
              ))}
            </tr>
          </thead>

          <tbody>
            {roomTypeNames.map((roomTypeName) => (
              <tr key={roomTypeName}>
                <td>{roomTypeName}</td>
                {tariffNames.map((tariffName) => {
                  const item = roomTypeTariff.find(
                    (item) =>
                      item.room_type?.name === roomTypeName &&
                      item.tariff?.name === tariffName
                  );

                  const isPriceSelected = item && selectedPrice && selectedPrice.id === item.id;

                  return (
                    <td
                      key={tariffName}
                      className={isPriceSelected ? 'room__selected__rice' : ''}
                      onClick={item?.price ? () => toggleSelectedPrice(item) : null}                    >
                      {item?.price ? (
                        `${item.price} so'm`
                      ) : (
                        <HiOutlineBan style={{ color: "gray" }} />
                      )}
                    </td>
                  );
                })}

              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          width: "22%",
          padding: "10px",
          border: "1px solid var(--Light, rgba(0, 0, 0, 0.10))",
        }}
      >
        <div className="mb-3">
          <p
            className="mb-2"
            style={{
              fontFamily: "Roboto",
              fontSize: "14px",
              fontStyle: "normal",
              fontWeight: 400,
              lineHeight: "20px",
              letterSpacing: "0.15px",
            }}
          >
            Скидка
          </p>

          <select
            className="mb-2"
            name=""
            id=""
            style={{
              width: "100%",
              padding: "8px",
              fontSize: "14px",
              color: "rgba(0, 0, 0, 0.38)",
              border: "1px solid rgba(0, 0, 0, 0.23)",
              borderRadius: "4px",
            }}
          >
            <option value="">не предоставляется</option>
          </select>

          <table>
            <thead>
              <tr>
                <th style={{ fontWeight: 400, background: "#f5f5f5" }}>Дата</th>
                <th style={{ fontWeight: 400, background: "#f5f5f5" }}>
                  Прожив.
                </th>
                <th style={{ fontWeight: 400, background: "#f5f5f5" }}>
                  Пакет
                </th>
                <th style={{ fontWeight: 400, background: "#f5f5f5" }}></th>
              </tr>
            </thead>

            <tbody>
              <tr>
                <td>24.04</td>
                <td>900 000 so'm</td>
                <td>0,00</td>
                <td></td>
              </tr>
              <tr>
                <td>24.04</td>
                <td>900 000 so'm</td>
                <td>0,00</td>
                <td></td>
              </tr>
              <tr>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
              </tr>
            </tbody>
          </table>
        </div>

        <div className="d-flex justify-content-between gap-1">
          <input
            type="text"
            style={{
              width: "47%",
              padding: "5px",
              border: "1px solid rgba(0, 0, 0, 0.23)",
            }}
          />
          <input
            type="text"
            style={{
              width: "47%",
              padding: "5px",
              border: "1px solid rgba(0, 0, 0, 0.23)",
            }}
          />
        </div>
      </div>
    </div>
  );
}

export default RoomTypeRates;
