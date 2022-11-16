import {
    Button,
    FormControl,
    InputLabel,
    MenuItem,
    Select,
    SelectChangeEvent,
    TextField,
} from "@mui/material";
import axios from "axios";
import { observer, useLocalObservable } from "mobx-react-lite";
import React from "react";
import { useNavigate } from "react-router";
import BpCheckbox from "../../components/BpCheckbox";
import {
    PatientsDirectoryActions,
    PatientsDirectoryNav,
} from "../../consts/patientsDirectory";
import { IPatient } from "../../consts/types";
import useDebounce from "../../hooks/useDebounce";
import { AuthorizationStateKeeper } from "../../store";
import classes from "./patientsDirectory.module.scss";

const PatientsDirectory = observer(
    ({ patients }: { patients: Array<IPatient> }) => {
        const [searchedValue, setSearchedValue] = React.useState<string>("");
        const [age, setAge] = React.useState(["", ""]);
        const [active, setactive] = React.useState<object[]>([]);
        const [selected, setSelected] = React.useState<string>("0");
        const navigate = useNavigate();
        const debouncedValue = useDebounce<string>(searchedValue, 500)
        const authorizationStateKeeper = useLocalObservable(
            () => AuthorizationStateKeeper.instance)
        const token = authorizationStateKeeper.token;

        React.useEffect(() => {
            if (searchedValue.length > 0) {
                searchHandler()
            }
        }, [debouncedValue])

        const searchHandler = () => {
            axios.get(`https://back.dev-hayat.uz/api/v1/organizations/patients-search/`, {
                headers: {
                    'Authorazition': 'Bearer ' + token
                },
                params: {
                    f_name: searchedValue
                }
            })
        }

        const handleChange = (event: SelectChangeEvent) => {
            setAge([...age, event.target.value]);
        };

        const handleSelectPatient = (event: React.MouseEvent<HTMLElement>) => {
            setSelected(event.currentTarget.dataset.id || "");
        };

        const handleSeachPatient = (event: React.ChangeEvent<HTMLInputElement>) => {
            setSearchedValue(event.target.value);
        };

        const handleClick = (event: React.MouseEvent<HTMLElement>) => {
            const type = event.currentTarget.dataset.type;
            switch (type) {
                case "add":
                    navigate("/patientsDirectory/create");
                    break;
                case "edit":
                    if (selected != "0") {
                        navigate(`/patientsDirectory/edit/${selected}`);
                    }
                    break;
                case "remove":
                    alert(JSON.stringify(active));
                    break;

                default:
                    break;
            }
        };

        const handlecheckboxchange = (e: React.ChangeEvent<HTMLInputElement>) => {
            const { checked, name } = e.currentTarget;
            if (checked) {
                setactive({ ...active, [name]: checked });
            } else {
                delete active[name];
                setactive(active);
            }
        };

        return (
            <div className={classes.main}>
                <nav className={classes.actionButtons}>
                    {PatientsDirectoryActions.map((button, index) => (
                        <Button
                            color={button.text === "Удалить" ? "error" : "primary"}
                            size="large"
                            className={classes.actionButton}
                            variant="contained"
                            key={index}
                            onClick={handleClick}
                            data-type={button.dataset}
                        >
                            {button.icon}
                            {button.text}
                        </Button>
                    ))}
                </nav>

                <nav className={classes.navbar}>
                    {PatientsDirectoryNav.map((item, index) =>
                        item.type === "select" ? (
                            <FormControl className={classes.navbarItem} fullWidth key={index}>
                                <InputLabel id="demo-select-small">{item.label}</InputLabel>
                                <Select
                                    labelId="demo-select-small"
                                    id="demo-select-small"
                                    value={age[index]}
                                    label={item.label}
                                    onChange={handleChange}
                                >
                                    {item.child?.map((child, i) => (
                                        <MenuItem key={i} value={child.value}>
                                            {child.name}
                                        </MenuItem>
                                    ))}
                                </Select>
                            </FormControl>
                        ) : (
                            <FormControl className={classes.navbarItem} fullWidth key={index}>
                                <TextField
                                    id="outlined-search"
                                    label={item.label}
                                    type={item.type}
                                        onChange={handleSeachPatient}
                                />
                            </FormControl>
                        )
                    )}
                </nav>

                <div className={classes.patientsList}>
                    {
                        !!patients !== true ? (
                            <table className={classes.table}>
                                <thead className={classes.tableHead}>
                                    {[
                                        "",
                                        "Фамилия",
                                        "Имя",
                                        "Отчество",
                                        "Пол",
                                        "Адрес",
                                        "Моб.телефон",
                                        "Дом.телефон",
                                        "Дата регис трации",
                                        "Регистратор",
                                        "Активный",
                                        "Дата последного посещение",
                                    ].map((item) => (
                                        <th key={item}>{item}</th>
                                    ))}
                                </thead>
                                {patients.slice(0, 7).map((item) => (
                                    <tr
                                        data-id={item.id}
                                        onClick={handleSelectPatient}
                                        className={
                                            item.id === parseInt(selected) ? classes.selectedDoctor : ""
                                        }
                                    >
                                        <td></td>
                                        <td>{item.lastName}</td>
                                        <td>{item.firstName}</td>
                                        <td>{item.middleName}</td>
                                        <td>{item.dob}</td>
                                        <td>{item.address}</td>
                                        <td>{item.mobilePhoneNumber}</td>
                                        <td>{item.homPhoneNumber}</td>
                                        <td>{item.dob}</td>
                                        <td>{item.email}</td>
                                        <td style={{ display: "flex", justifyContent: "center" }}>
                                            <BpCheckbox
                                                id={item.id}
                                                handlecheckboxchange={handlecheckboxchange}
                                                defaultChecked={false}
                                            />
                                        </td>
                                        <td>{item.lastVisitAt}</td>
                                    </tr>
                                ))}
                            </table>
                        ) : null
                    }
                </div>
            </div>
        );
    }
);

export default PatientsDirectory;
