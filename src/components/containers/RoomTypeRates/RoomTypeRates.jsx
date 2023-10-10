import React from "react";
import "./RoomTypeRates.css";
import { HiOutlineBan } from "react-icons/hi"
function RoomTypeRates({ roomTypeTariff, selectedPrice, setSelectedPrice }) {

  const tariffNames = [...new Set(roomTypeTariff.map(item => item.tariff.name))];
  const roomTypeNames = [...new Set(roomTypeTariff.map(item => item.room_type.name))];

  // SELECTING PRICE = = = = = >> > >
  const toggleSelectedPrice = (id) => {
    setSelectedPrice(id === selectedPrice?.id ? null : id);
  };

  console.log(selectedPrice)


  return (
    <div className="d-flex justify-content-between gap-2 mb-4">
      <div className="expectation__table m-0" style={{ width: "78%" }}>
        <table className="type_room_table">
          <thead>
            <tr>
              <th style={{ textAlign: "start" }}>Тариф</th>
              {/* <th style={{ textAlign: "start" }}>
                <div className="d-flex">
                  <span
                    style={{
                      display: "inline-block",
                      width: "8px",
                      height: "20px",
                      marginRight: "10px",
                      borderRadius: "2px",
                      background: "#2F538B",
                    }}
                  ></span>
                  <span style={{ fontSize: "12px" }}>СТД</span>
                </div>
                <div>
                  <span style={{ fontSize: "12px", color: "#4CAF50" }}>48</span>
                  <span style={{ fontSize: "12px", color: "#FF9800" }}>+0</span>
                </div>
              </th>
              <th style={{ textAlign: "start" }}>
                <div className="d-flex">
                  <span
                    style={{
                      display: "inline-block",
                      width: "8px",
                      height: "20px",
                      marginRight: "10px",
                      borderRadius: "2px",
                      background: "#A4CBFA",
                    }}
                  ></span>
                  <span style={{ fontSize: "12px" }}>СТД.К</span>
                </div>
                <div>
                  <span style={{ fontSize: "12px", color: "#4CAF50" }}>48</span>
                  <span style={{ fontSize: "12px", color: "#FF9800" }}>+0</span>
                </div>
              </th>
              {tableHeaders.map((header, index) => (
                <th key={index} style={thStyle}>
                  <div className="d-flex">
                    <span
                      style={{ ...colorBoxStyle, background: header.bgColor }}
                    ></span>
                    <span style={headerTextStyle}>{header.text}</span>
                  </div>
                  <div>
                    <span style={greenTextStyle}>{header.greenText}</span>
                    <span style={orangeTextStyle}>{header.orangeText}</span>
                  </div>
                </th>
              ))} */}
              {tariffNames.map(tariffName => (
                <th key={tariffName}>{tariffName}</th>
              ))}
            </tr>
          </thead>

          <tbody>
            {/* {data.map((item, index) => (
              <tr key={index}>
                <td>
                  <div className="d-flex">
                    <span
                      style={{
                        display: "inline-block",
                        width: "8px",
                        height: "20px",
                        marginRight: "10px",
                        borderRadius: "2px",
                        background: item.color,
                      }}
                    ></span>
                    <span style={{ fontSize: "12px" }}>{item.label}</span>
                  </div>
                  <div>
                    <span
                      style={{ fontSize: "12px", color: "rgba(0, 0, 0, 0.54)" }}
                    >
                      {item.description}
                    </span>
                  </div>
                </td>
                {item.prices.map((price, priceIndex) => (
                  <td key={priceIndex} style={{ fontSize: "12px" }}>
                    <p className="m-0">{price.basePrice}</p>
                    <p className="m-0" style={{ color: "rgba(0, 0, 0, 0.54)" }}>
                      {price.discountedPrice}
                    </p>
                  </td>
                ))}
              </tr>
            ))} */}
            {roomTypeNames.map((roomTypeName) => (
              <tr key={roomTypeName}>
                <td>{roomTypeName}</td>
                {tariffNames.map((tariffName) => {
                  const item = roomTypeTariff.find(
                    (item) =>
                      item.room_type.name === roomTypeName &&
                      item.tariff.name === tariffName
                  );
                  const isPriceSelected = selectedPrice?.id === item?.id;
                  console.log(item)

                  return (
                    <td
                      key={tariffName}
                      // className={isPriceSelected ? '' : ''}
                      onClick={() => toggleSelectedPrice(item?.id)}
                    >
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
