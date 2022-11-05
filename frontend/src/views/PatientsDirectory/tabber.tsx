import * as React from "react";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import classes from "./createPatient.module.scss";
import {
    FormControl,
    FormLabel,
    InputLabel,
    MenuItem,
    Select,
    TextField,
} from "@mui/material";
import Grid from "@mui/material/Unstable_Grid2";

interface TabPanelProps {
    children?: React.ReactNode;
    index: number;
    value: number;
}

function TabPanel(props: TabPanelProps) {
    const { children, value, index, ...other } = props;

    return (
        <div
            role="tabpanel"
            hidden={value !== index}
            id={`simple-tabpanel-${index}`}
            aria-labelledby={`simple-tab-${index}`}
            {...other}
        >
            {value === index && (
                <Box sx={{ p: 3 }}>
                    <Typography>{children}</Typography>
                </Box>
            )}
        </div>
    );
}

function a11yProps(index: number) {
    return {
        id: `simple-tab-${index}`,
        "aria-controls": `simple-tabpanel-${index}`,
    };
}

export default function Tabber() {
    const [value, setValue] = React.useState(0);

    const handleChange = (event: React.SyntheticEvent, newValue: number) => {
        setValue(newValue);
    };

    return (
        <Box sx={{ width: "100%" }} className={classes.tabber}>
            <Box sx={{ borderBottom: 1, borderColor: "divider" }}>
                <Tabs
                    value={value}
                    onChange={handleChange}
                    aria-label="basic tabs example"
                >
                    <Tab label="CRM" {...a11yProps(0)} />
                    <Tab label="Учётные данные" {...a11yProps(1)} />
                    <Tab label="Документы" {...a11yProps(2)} />
                    <Tab label="Накопит система" {...a11yProps(3)} />
                </Tabs>
            </Box>
            <TabPanel value={value} index={0}>
                <FormLabel>Источник информации</FormLabel>
                <FormControl style={{ marginBottom: 10 }} fullWidth>
                    <Select labelId="demo-simple-select-label" id="demo-simple-select">
                        <MenuItem value={10}>Ten</MenuItem>
                    </Select>
                </FormControl>
                <FormLabel>Группа</FormLabel>
                <FormControl style={{ marginBottom: 10 }} fullWidth>
                    <Select labelId="demo-simple-select-label" id="demo-simple-select">
                        <MenuItem value={30}>Thirty</MenuItem>
                    </Select>
                </FormControl>
            </TabPanel>
            <TabPanel value={value} index={1}>
                <FormLabel>Лечащий врач</FormLabel>
                <FormControl style={{ marginBottom: 10 }} fullWidth>
                    <Select labelId="demo-simple-select-label" id="demo-simple-select">
                        <MenuItem value={10}>Ten</MenuItem>
                    </Select>
                </FormControl>
                <FormLabel>Дата постановки на учет</FormLabel>
                <FormControl style={{ marginBottom: 10 }} fullWidth>
                    <Select labelId="demo-simple-select-label" id="demo-simple-select">
                        <MenuItem value={10}>Ten</MenuItem>
                    </Select>
                </FormControl>
            </TabPanel>
            <TabPanel value={value} index={2}>
                <Grid spacing={2} container>
                    <Grid md={4}>
                        <FormLabel>Тип документа</FormLabel>
                        <FormControl style={{ marginBottom: 10 }} fullWidth>
                            <Select
                                labelId="demo-simple-select-label"
                                id="demo-simple-select"
                            >
                                <MenuItem value={"passport"}>Passport</MenuItem>
                                <MenuItem value={"id"}>ID card</MenuItem>
                            </Select>
                        </FormControl>
                    </Grid>
                    <Grid md={4}>
                        <FormControl fullWidth>
                            <FormLabel>Номер документа</FormLabel>
                            <TextField type="number" />
                        </FormControl>
                    </Grid>
                    <Grid md={4}>
                        <FormControl fullWidth>
                            <FormLabel>Выдан (дата)</FormLabel>
                            <TextField type="text" />
                        </FormControl>
                    </Grid>
                    <Grid md={6}>
                        <FormControl fullWidth>
                            <FormLabel>Номер ИНН</FormLabel>
                            <TextField type="number" />
                        </FormControl>
                    </Grid>
                    <Grid md={6}>
                        <FormControl fullWidth>
                            <FormLabel>Гражданство</FormLabel>
                            <TextField type="text" />
                        </FormControl>
                    </Grid>
                </Grid>
            </TabPanel>
            <TabPanel value={value} index={3}>
                <Grid container>
                    <Grid md={6}>
                        <FormControl fullWidth>
                            <FormLabel>Общая сумма заказов</FormLabel>
                            <TextField type="number" />
                        </FormControl>
                    </Grid>
                    <Grid md={6}>
                        <FormLabel>Категория НС</FormLabel>
                        <FormControl style={{ marginBottom: 10 }} fullWidth>
                            <Select
                                labelId="demo-simple-select-label"
                                id="demo-simple-select"
                            >
                                <MenuItem value={"Основная"}>Основная</MenuItem>
                                <MenuItem value={"id"}>ID card</MenuItem>
                            </Select>
                        </FormControl>
                    </Grid>
                </Grid>
            </TabPanel>
        </Box>
    );
}
