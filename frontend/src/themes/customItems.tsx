import {styled} from "@mui/material/styles";
import {Box, TextField} from "@mui/material";

export const Item = styled(Box)(({theme}) => ({
    display: "flex",
    alignItems: "center",
    justifyContent: "center"
}));

export const FlexSpaceBetween = styled(Box)(({ theme }) => ({
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between"
}));