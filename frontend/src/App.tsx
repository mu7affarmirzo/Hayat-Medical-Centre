import React from 'react';
import {BrowserRouter} from "react-router-dom";
import AppRouting from "./routes/AppRouting";
import { AdapterMoment } from '@mui/x-date-pickers/AdapterMoment';
import {LocalizationProvider} from "@mui/x-date-pickers";
import AuthVerify from './components/AuthVerify';

function App() {
    return (
        <BrowserRouter>
            <AuthVerify />
            <LocalizationProvider dateAdapter={AdapterMoment}>
                <AppRouting />
            </LocalizationProvider>
        </BrowserRouter>
    );
}

export default App;
