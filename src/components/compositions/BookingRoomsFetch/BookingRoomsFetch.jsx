import React from 'react'
import { useRoomsQuery } from '../../../services/roomsApi'
import BookingRooms from '../../containers/BookingRooms/BookingRooms'

function BookingRoomsFetch({ selectedRoom, setSelectedRoom, selectedPrice }) {
    const { data: rooms, isSuccess } = useRoomsQuery(Number(selectedPrice?.id))
    return (
        isSuccess && <BookingRooms rooms={rooms} selectedRoom={selectedRoom} setSelectedRoom={setSelectedRoom} selectedPrice={selectedPrice} />
    )
}

export default BookingRoomsFetch