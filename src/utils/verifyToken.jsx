import axios from "axios";
import { BASE_URL } from "../constants/constants";
import { useNavigate } from "react-router";

function verifyAccessToken(accessToken) {

    const requestBody = {
        token: accessToken,
    };

    axios.post(`${BASE_URL}/api/v1/token/verify/`, requestBody)
        .then((response) => {
            // Access token is valid
            console.log("Access token is valid:", response.data);
        })
        .catch((error) => {
            // Access token is invalid or an error occurred
            console.error("Error verifying access token:", error);

            // Navigate the user to the login page
            window.location.href = '/login'; // Change the URL as needed
            localStorage.removeItem("access-token")
            localStorage.removeItem("refresh-token")
        });
}
export default verifyAccessToken