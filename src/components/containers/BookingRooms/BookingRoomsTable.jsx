import React from 'react'
import "./BookingRooms.css"
function BookingRoomsTable({ item, setSelectedRoom, selectedRoom, room_number, live_date }) {
    const toggleSelectRoom = (item) => {
        setSelectedRoom(item.id === selectedRoom?.id ? null : item);
    }

    const isRoomSelected = item.id === selectedRoom.id
    return (
        <tr className={`${isRoomSelected ? "rooms__list-active" : ""}`} onClick={() => toggleSelectRoom(item)}>
            <td className="d-flex justify-content-between gap-2 align-items-center">
                {/* <span>{room_number}</span> */}
                {/* <span style={{ color: "rgba(0, 0, 0, 0.38)" }}>202.1</span>
                <span
                    style={{
                        padding: "4px",
                        color: "rgba(0, 0, 0, 0.54)",
                        background: "#F8ED8D",
                    }}
                >
                    2
                </span> */}
            </td>
            {/* <td>{live_date.start_date}</td> */}
            {/* <td>{live_date.end_date}</td> */}
            <td>
                <span
                    style={{
                        padding: "4px",
                        color: "#fff",
                        backgroundColor: "#FF737F",
                    }}
                >
                    Ж
                </span>
            </td>
            <td>
                <span
                    style={{
                        padding: "4px",
                        color: "#000",
                        backgroundColor: "#E0E0E0",
                    }}
                >
                    85
                </span>
            </td>
            <td>ЖИЛ</td>
            <td>ГК</td>
            <td>ГК2</td>
            <td>Грязный</td>
            <td></td>
            <td></td>
            <td></td>
            <td className="text-end">202</td>
        </tr>
    )
}

export default BookingRoomsTable