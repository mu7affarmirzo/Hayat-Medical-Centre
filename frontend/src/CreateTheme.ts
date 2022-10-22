import {createTheme} from "@mui/material";

export const theme = createTheme({
    breakpoints: {
        values: {
            xs: 0,
            sm: 600,
            md: 900,
            lg: 1400,
            xl: 1920
        }
    },
    palette: {
        primary: {
            main: "#007DFF"
        },
        error: {
            main: "#F44336"
        }
    },
    typography: {

        interFont: {
            fontFamily: '"inter", "sans-serif"',

        }
    }
})