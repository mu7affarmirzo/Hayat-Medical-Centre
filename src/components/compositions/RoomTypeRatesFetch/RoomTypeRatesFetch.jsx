import React, { useState } from 'react'
import { useRoomTypeTariffQuery } from '../../../services/roomType&TariffApi'
import RoomTypeRates from '../../containers/RoomTypeRates/RoomTypeRates'

function RoomTypeRatesFetch({ selectedPrice, setSelectedPrice }) {
    const { data: roomTypeTariff, isSuccess } = useRoomTypeTariffQuery()
    return (
        isSuccess && <RoomTypeRates roomTypeTariff={roomTypeTariff} selectedPrice={selectedPrice} setSelectedPrice={setSelectedPrice} />
    )
}

export default RoomTypeRatesFetch