import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { BASE_URL } from '../../constants/constants';

function SearchPatient() {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);
    const [selectedResult, setSelectedResult] = useState(null);
    const apiUrl = `${BASE_URL}/api/v1/logus/search-patient/`;

    const accessToken = localStorage.getItem("access-token")
    const fetchSearchResults = async (searchQuery) => {
        try {
            const response = await axios.post(
                apiUrl,
                { word: searchQuery },
                {
                    headers: {
                        Authorization: `Bearer ${accessToken}`,
                    },
                }
            );
            if (response.status === 200) {
                setResults(response.data);
            }
        } catch (error) {
            console.error('There was a problem with the API request:', error);
        }
    };

    useEffect(() => {
        if (query.trim() !== '') {
            fetchSearchResults(query);
        } else {
            setResults([]);
        }
    }, [query]); // This effect will re-run whenever the 'query' state changes

    const handleResultSelection = (result) => {
        setSelectedResult(result);
        setQuery(`${result.f_name} ${result.l_name}`)
    };
    // Handler function to update 'query' state when the input changes
    const handleInputChange = (e) => {
        setQuery(e.target.value);
        setSelectedResult(null);
    };
    console.log(results)

    if (!query || selectedResult) {

        return (
            <div className="d-flex flex-column w-100 align-items-end">
                <div
                    className="d-flex justify-content-between align-items-center"
                    style={{ width: "100%" }}
                >
                    <label htmlFor="" style={{ fontSize: "14px" }}>
                        ФИО гостя
                    </label>
                    <input
                        className="booking_input_bg"
                        type="text"
                        style={{
                            width: "90%",
                            padding: "4px 10px",
                            background: "#fff",
                            borderRadius: "4px",
                            border: "1px solid rgba(0, 0, 0, 0.23)",
                            backgroundPosition: "99% center !important",
                        }}
                        value={query}
                        onChange={handleInputChange}
                    />
                </div>
            </div>
        )
    }
    return (
        <div className="d-flex flex-column w-100 align-items-end">
            <div
                className="d-flex justify-content-between align-items-center"
                style={{ width: "100%" }}
            >
                <label htmlFor="" style={{ fontSize: "14px" }}>
                    ФИО гостя
                </label>
                <input
                    className="booking_input_bg"
                    type="text"
                    style={{
                        width: "90%",
                        padding: "4px 10px",
                        background: "#fff",
                        borderRadius: "4px",
                        border: "1px solid rgba(0, 0, 0, 0.23)",
                        backgroundPosition: "99% center !important",
                    }}
                    value={query}
                    onChange={handleInputChange}
                />
            </div>

            <div className="patient__search-result cursor-pointer" style={{width:"90%"}}>
                {results.length > 0 ? (
                    <ul style={{ width: "90%" }}>
                        {results.map((result) => (
                            <li key={result.id} onClick={() => handleResultSelection(result)}>{result.f_name} {result.l_name}</li>
                        ))}
                    </ul>
                ) : (
                    <p>no result</p>
                )
                }
            </div>
        </div>
    )
}

export default SearchPatient