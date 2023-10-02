import React from "react";

function ExpectedDepartureTable({ expectedDeparture }) {
  console.log(expectedDeparture);
  return (
    <>
      <div className="expect__top">
        <div className="d-flex gap-5 align-items-center">
          <strong>Ожидаемый заезд</strong>
          <div className="d-flex gap-2">
            <button>
              <svg
                width="18"
                height="18"
                viewBox="0 0 18 18"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M3.75 9H14.25M3.75 9L8.25 4.5M3.75 9L8.25 13.5"
                  stroke="black"
                  strokeOpacity="0.87"
                  strokeWidth="1.5"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              </svg>
            </button>
            <input type="date" name="" id="" />
            <button>
              <svg
                width="18"
                height="18"
                viewBox="0 0 18 18"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M3.75 9H14.25M14.25 9L9.75 4.5M14.25 9L9.75 13.5"
                  stroke="black"
                  strokeOpacity="0.87"
                  strokeWidth="1.5"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              </svg>
            </button>
          </div>
        </div>
        <div className="d-flex align-items-center gap-2">
          <button>
            <svg
              width="18"
              height="18"
              viewBox="0 0 18 18"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M11.6248 4.12551L13.7461 6.24683M9.75 15.75H15.75M2.25 15.7503L2.28559 15.5012C2.41152 14.6197 2.47449 14.1789 2.61772 13.7674C2.74481 13.4023 2.91843 13.055 3.13429 12.7342C3.37756 12.3728 3.69239 12.0579 4.32206 11.4283L13.0581 2.69227C13.6438 2.10648 14.5936 2.10648 15.1794 2.69227C15.7652 3.27806 15.7652 4.2278 15.1794 4.81359L6.28308 13.7099C5.71185 14.2811 5.42623 14.5667 5.1009 14.7939C4.81213 14.9955 4.50069 15.1625 4.17298 15.2915C3.80378 15.4368 3.40782 15.5167 2.61595 15.6765L2.25 15.7503Z"
                stroke="black"
                strokeOpacity="0.87"
                strokeWidth="1.5"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
          </button>
          <button>
            <svg
              width="18"
              height="18"
              viewBox="0 0 18 18"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M2.25 3.75V14.25M2.25 12H15.75M15.75 14.25V9.9C15.75 9.05992 15.75 8.63988 15.5865 8.31901C15.4427 8.03677 15.2132 7.8073 14.931 7.66349C14.6101 7.5 14.1901 7.5 13.35 7.5H8.25V11.7955M5.25 9H5.2575M6 9C6 9.41421 5.66421 9.75 5.25 9.75C4.83579 9.75 4.5 9.41421 4.5 9C4.5 8.58579 4.83579 8.25 5.25 8.25C5.66421 8.25 6 8.58579 6 9Z"
                stroke="black"
                strokeOpacity="0.87"
                strokeWidth="1.5"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
          </button>
        </div>
      </div>

      <div className="expect__search">
        <div className="d-flex align-items-center gap-4">
          <div className="d-flex gap-2 align-items-center">
            <label htmlFor="">Поиск по тексту</label>
            <input type="text" />
          </div>
          <div className="d-flex gap-2 align-items-center">
            <label htmlFor="">Теги</label>
            <input type="text" />
          </div>
        </div>
        <div className="d-flex align-items-center gap-2">
          <button>
            <svg
              width="18"
              height="18"
              viewBox="0 0 18 18"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M8.625 15.75C12.56 15.75 15.75 12.56 15.75 8.625C15.75 4.68997 12.56 1.5 8.625 1.5C4.68997 1.5 1.5 4.68997 1.5 8.625C1.5 12.56 4.68997 15.75 8.625 15.75Z"
                stroke="white"
                strokeWidth="1.5"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
              <path
                d="M16.5 16.5L15 15"
                stroke="white"
                strokeWidth="1.5"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
            Найти
          </button>
          <button>
            <svg
              width="18"
              height="18"
              viewBox="0 0 18 18"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M4.5 4.5L13.5 13.5M13.5 4.5L4.5 13.5"
                stroke="black"
                strokeOpacity="0.87"
                strokeWidth="1.5"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
          </button>
        </div>
      </div>
      <div className="expectation__table">
        <div className="table__container">
          <table>
            <thead>
              <tr>
                <th>
                  <input type="checkbox" name="" id="" />
                </th>
                <th>№</th>
                <th>Имя гостя</th>
                <th>Группа/Квота</th>
                <th>Дата выезда</th>
                <th>Тип комнаты</th>
                <th>Комната</th>
                <th>Кол-во гостей</th>
                <th>Баланс</th>
                <th>Время заезда</th>
                <th>Оплачено</th>
                <th>Длительность</th>
                <th>Тариф</th>
                <th>Скидка</th>
                <th>Статус комнаты</th>
                <th>Скидка (код)</th>
                <th>Статуc</th>
                <th>Примечания</th>
                <th>Гарантия</th>
                <th>Дата создании</th>
                <th>Дата изменения</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div className="expect__footer">
        <span>Броней:0</span>
        <span>К-во гостей:</span>
      </div>
    </>
  );
}

export default ExpectedDepartureTable;
