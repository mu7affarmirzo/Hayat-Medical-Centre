import React from 'react'
import { useRoomsQuery } from '../../../services/roomsApi'
import BookingRooms from '../../containers/BookingRooms/BookingRooms'

function BookingRoomsFetch({ selectedRoom, setSelectedRoom }) {
    const { data: rooms, isSuccess } = useRoomsQuery()
    return (
        isSuccess && <BookingRooms rooms={rooms} selectedRoom={selectedRoom} setSelectedRoom={setSelectedRoom} />
    )
}

export default BookingRoomsFetch