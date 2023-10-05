import React from "react";
import "./RoomTypeRates.css";
function RoomTypeRates() {
  const thStyle = {
    textAlign: "start",
  };

  const colorBoxStyle = {
    display: "inline-block",
    width: "8px",
    height: "20px",
    marginRight: "10px",
    borderRadius: "2px",
  };

  const headerTextStyle = {
    fontSize: "12px",
  };

  const greenTextStyle = {
    fontSize: "12px",
    color: "#4CAF50",
  };

  const orangeTextStyle = {
    fontSize: "12px",
    color: "#FF9800",
  };

  const tableHeaders = [
    {
      bgColor: "#BD6E30",
      text: "ЛЮКСА",
      greenText: "3",
      orangeText: "+0",
    },
    {
      bgColor: "#E99A56",
      text: "ЛЮКСА.К",
      greenText: "7",
      orangeText: "+0",
    },
    {
      bgColor: "#3E7D96",
      text: "ЛЮКСБ",
      greenText: "4",
      orangeText: "+0",
    },
    {
      bgColor: "#5DA1BA",
      text: "ЛЮКСБ.К",
      greenText: "9",
      orangeText: "+0",
    },
    {
      bgColor: "#A08AC3",
      text: "VIPA",
      greenText: "0",
      orangeText: "+0",
    },
    {
      bgColor: "#C6B0E9",
      text: "VIPA.K",
      greenText: "1",
      orangeText: "+0",
    },
    {
      bgColor: "#D67B75",
      text: "VIPБ",
      greenText: "1",
      orangeText: "+0",
    },
    {
      bgColor: "#F1A09B",
      text: "VIPБ.K",
      greenText: "2",
      orangeText: "+0",
    },
    {
      bgColor: "#EA3323",
      text: "РЕАНИМ",
      greenText: "4",
      orangeText: "+0",
    },
    {
      bgColor: "#EA3323",
      text: "РЕАНИМ.К",
      greenText: "10",
      orangeText: "+0",
    },
  ];

  const data = [
    {
      label: "СТД",
      description: "Стандарт",
      color: "#98B15D",
      prices: [
        { basePrice: "700 000 so`m", discountedPrice: "4 150 000 so`m" },
        // Add more prices here as needed
      ],
    },
    {
      label: "СОПР",
      description: "Сопровождение",
      color: "#A4CBFA",
      prices: [
        { basePrice: "700 000 so`m", discountedPrice: "4 150 000 so`m" },
        // Add more prices here as needed
      ],
    },
  ];

  return (
    <div className="d-flex justify-content-between gap-2 mb-4">
      <div className="expectation__table m-0" style={{ width: "70%" }}>
        <table className="type_room_table">
          <thead>
            <tr>
              <th style={{ textAlign: "start" }}>Тариф</th>
              <th style={{ textAlign: "start" }}>
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
              ))}
            </tr>
          </thead>

          <tbody>
            {data.map((item, index) => (
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
            ))}
          </tbody>
        </table>
      </div>

      <div
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          width: "30%",
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
