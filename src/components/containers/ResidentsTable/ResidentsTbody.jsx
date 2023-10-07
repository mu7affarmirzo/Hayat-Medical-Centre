import React from 'react'
import FormatDate from '../../../utils/formatDate'

function ResidentsTbody({
    id,
    patients,
    room,
    guests_count,
    abs_price,
    room_price,
    discount,
    created_at,
}) {
    return (
        <tr>
            <td>
                <input type="checkbox" name="" id="" />
            </td>
            <td>{id}</td>
            <td>{patients.f_name}</td>
            <td>{patients.patient_group[0]}</td>
            <td>
                <FormatDate date={room.live_date.end_date} />
            </td>
            <td>{room.room_type}</td>
            <td>{room.room_number}</td>
            <td>{guests_count} взр.</td>
            <td>{abs_price} so’m</td>
            <td></td>
            <td>0 so'm</td>
            <td></td>
            <td>{room_price.tariff.name}</td>
            <td>{discount} МПЛ...</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>
                <FormatDate date={created_at} />
            </td>
            <td></td>
        </tr>
    )
}

export default ResidentsTbody