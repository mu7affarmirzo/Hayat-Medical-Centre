import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { BASE_URL } from '../../../constants/constants';
import PlacementScheme from '../../containers/PlacementScheme/PlacementScheme';

const formatDateWithWeekday = (dateString) => {
    const date = new Date(dateString);

    const optionsDate = {
        day: 'numeric',
        month: 'long',
        localeMatcher: 'best fit',
        timeZone: 'UTC',
    };

    const optionsWeekday = {
        weekday: 'short',
        localeMatcher: 'best fit',
        timeZone: 'UTC',
    };

    const formattedDate = date.toLocaleDateString('ru', optionsDate);
    const formattedWeekday = date.toLocaleDateString('ru', optionsWeekday);

    return (
        <div style={{ color: formattedWeekday == "сб" || formattedWeekday == "вс" ? "red" : "black" }}>
            {formattedDate}
            <br />
            {formattedWeekday}
        </div>
    );
}
function PlacementSchemeFetch({ startDate, leaveDate, setStartDate, setLeaveDate }) {
    const [roomData, setRoomData] = useState({});
    const [dates, setDates] = useState([]);
    const [today, setToday] = useState(null);
    const [futureDate, setFutureDate] = useState(null);

    useEffect(() => {
        const currentDate = new Date();
        setToday(formatDate(currentDate));

        const futureDate = new Date(currentDate);
        futureDate.setDate(currentDate.getDate() + 16);
        setFutureDate(formatDate(futureDate));
    }, []);

    const formatDate = (date) => {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        return `${year}-${month}-${day}`;
    };

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.post(`${BASE_URL}/api/v1/logus/free-rooms/`, {
                    start_date: today,
                    end_date: futureDate,
                }, {
                    headers: {
                        "Authorization": `Bearer ${localStorage.getItem("access-token")}`
                    }
                });
                const data = response.data;
                setRoomData(data);
                setDates(Object.keys(data));
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };
        fetchData();
    }, [today, futureDate]);

    // Transform the data ===
    const transformedData = {};

    Object.keys(roomData).forEach((date) => {
        Object.keys(roomData[date]).forEach((roomType) => {
            if (!transformedData[roomType]) {
                transformedData[roomType] = {};
            }
            transformedData[roomType][date] = roomData[date][roomType];
        });
    });
    console.log(roomData)

    // OVERALL DATE NUMBERS ======= >>
    const [overallNumbers, setOverallNumbers] = useState({});

    useEffect(() => {
        // Calculate the overall numbers when the component mounts
        const calculateOverallNumbers = () => {
            const newOverallNumbers = {};

            // Iterate through the data and calculate overall numbers
            for (const date in roomData) {
                const materials = roomData[date];
                const total = Object.values(materials).reduce((acc, value) => acc + value, 0);
                newOverallNumbers[date] = total;
            }

            setOverallNumbers(newOverallNumbers);
        };

        calculateOverallNumbers();
    }, [roomData]);



    useEffect(() => {
        const currentDate = new Date();
        setStartDate(formatDate(currentDate));

        const futureDate = new Date(currentDate);
        futureDate.setDate(currentDate.getDate() + 6);
        setLeaveDate(formatDate(futureDate));
    }, []);
    const startDateNum = new Date(startDate);
    const leaveDateNum = new Date(leaveDate);

    const daysDifference = (leaveDateNum - startDateNum) / (1000 * 60 * 60 * 24) + 1;
    console.log(daysDifference)
    return (
        dates && <PlacementScheme dates={dates} formatDateWithWeekday={formatDateWithWeekday} setStartDate={setStartDate} setLeaveDate={setLeaveDate} transformedData={transformedData} overallNumbers={overallNumbers} startDate={startDate} leaveDate={leaveDate} daysDifference={daysDifference} />
    )
}

export default PlacementSchemeFetch