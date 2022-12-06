import React, { ChangeEvent, useEffect, useState } from "react";
import { FlexSpaceBetween } from "../../themes/customItems";
import { Link, useNavigate } from "react-router-dom";
import { Backdrop, Box, Button, TextField, Typography } from "@mui/material";
import styles from "./index.module.scss";
import { ReactComponent as NoteAdd } from "../../assets/img/note-add.svg";
import { ReactComponent as CloseCircle } from "../../assets/img/close-circle.svg";
import { ReactComponent as UserAdd } from "../../assets/img/user-add.svg";
import Edit from "../../assets/img/edit.svg";
import ArrowDropDownIcon from "@mui/icons-material/ArrowDropDown";
import ArrowCircle from "../../assets/img/arrow-circle-left.svg";
import PatientsTable from "./patientsTable";
import { observer, useLocalObservable } from "mobx-react-lite";
import {
    AuthorizationStateKeeper,
    CalendarEventStateKeeper,
    DoctorStateKeeper,
    MedicalServiceStateKeeper,
    PatientStateKeeper,
} from "../../store";
import { IDateValue, IMedicalService, IPatient } from "../../consts/types";
import moment from "moment";
import ErrorNotification from "../../store/ErrorNotification";
import axios from "axios";
import { ReactComponent as EkmLogo } from "../../assets/ekm.svg";

interface IAppointment {
    patient: any;
    name: any;
    exemtion: string;
    start_time: any;
    end_time: any;
    price: string;
    debt: string;
    referring_doctor: string;
    information_source: string;
    referring_doctor_notes: string;
    addition_info: string;
    branch: string;
    services: any;
}

const CreateNote = observer(() => {
    const navigator = useNavigate();
    const [openPatientsPopup, setOpenPatients] = useState<boolean | string>(
        false
    );
    const authorizationStateKeeper = useLocalObservable(
        () => AuthorizationStateKeeper.instance
    );
    const token = authorizationStateKeeper.token;
    const headers = {
        headers: {
            Authorization: "Bearer " + JSON.parse(token).access,
        },
    };
    const patientStateKeeper = useLocalObservable(
        () => PatientStateKeeper.instance
    );
    const doctorStateKeeper = useLocalObservable(
        () => DoctorStateKeeper.instance
    );

    const [dateValue, setDateValue] = React.useState<moment.Moment | null>(
        moment()
    );
    const [patients, setPatients] = useState<IPatient[]>([]);


    // { patiend: '', name: '',  exemtion: '', start_time: '', end_time: '', price: '', debt: '', referring_doctor: '', information_source: '', referring_doctor_notes: '', addition_info: '', branch: '', services: [], }

    useEffect(() => {
        patientStateKeeper.findAllPatients().then();
    }, []);

    useEffect(() => {
        setPatients([...patientStateKeeper.patients]);
    }, [patientStateKeeper.patients]);

    const [searchFields, setSearchFields] = useState<{
        fullName: string;
        inn: string;
        emcNumber: string;
        dob: string;
        phoneNumber: string;
        patientID: string;
        lastVisitAt: string;
    }>({
        fullName: "",
        inn: "",
        emcNumber: "",
        dob: "",
        phoneNumber: "",
        patientID: "",
        lastVisitAt: "",
    });

    const handleSearchOnChange = (event: ChangeEvent<HTMLInputElement>) => {
        const { name, value } = event.target;
        setSearchFields((prevSearchFields) => {
            return { ...prevSearchFields, [name]: value };
        });
    };

    useEffect(() => {
        setPatients(
            patientStateKeeper.patients
                .filter((patient) => {
                    return searchFields.fullName.length
                        ? searchFields.fullName
                            .toLowerCase()
                            .includes(patient.l_name.toLowerCase()) ||
                        patient.l_name
                            .toLowerCase()
                            .includes(searchFields.fullName.toLowerCase()) ||
                        searchFields.fullName
                            .toLowerCase()
                            .includes(patient.f_name.toLowerCase()) ||
                        patient.f_name
                            .toLowerCase()
                            .includes(searchFields.fullName.toLowerCase()) ||
                        searchFields.fullName
                            .toLowerCase()
                            .includes(
                                patient.mid_name ? patient.mid_name.toLowerCase() : ""
                            )
                        : true;
                })
                .filter((patient) => {
                    return searchFields.inn.length
                        ? searchFields.inn
                            .toLowerCase()
                            .includes(patient.inn.toLowerCase()) ||
                        patient.inn
                            .toLowerCase()
                            .includes(searchFields.inn.toLowerCase())
                        : true;
                })
                .filter((patient) => {
                    return searchFields.emcNumber.length
                        ? searchFields.emcNumber
                            .toLowerCase()
                            .includes(patient.emc.name.toLowerCase()) ||
                        patient.emc.name
                            .toLowerCase()
                            .includes(searchFields.emcNumber.toLowerCase())
                        : true;
                })
                .filter((patient) => {
                    return searchFields.phoneNumber.length
                        ? searchFields.phoneNumber
                            .toLowerCase()
                            .includes(patient.homPhoneNumber.toLowerCase()) ||
                        patient.homPhoneNumber
                            .toLowerCase()
                            .includes(searchFields.phoneNumber.toLowerCase()) ||
                        searchFields.phoneNumber
                            .toLowerCase()
                            .includes(patient.mobile_phone_number.toLowerCase()) ||
                        patient.mobile_phone_number
                            .toLowerCase()
                            .includes(searchFields.phoneNumber.toLowerCase())
                        : true;
                })
                .filter((patient) => {
                    return searchFields.patientID.length
                        ? searchFields.patientID
                            .toLowerCase()
                            .includes(patient.id.toString()) ||
                        patient.id.toString().includes(searchFields.patientID)
                        : true;
                })
                .filter((patient) => {
                    return searchFields.lastVisitAt.length
                        ? searchFields.lastVisitAt
                            .toLowerCase()
                            .includes(patient.last_visit_at.toLowerCase()) ||
                        patient.last_visit_at
                            .toLowerCase()
                            .includes(searchFields.lastVisitAt.toLowerCase())
                        : true;
                })
        );
    }, [searchFields]);

    const [discount, setDiscount] = useState<number>(0);
    const { changeVisibilityNotification } = useLocalObservable(
        () => ErrorNotification.instance
    );

    const [timeValue, setTimeValue] = React.useState<IDateValue>({
        from: moment(),
        to: moment().add(5, "minutes"),
    });
    const [formData, setFormData] = useState<IAppointment>({
        patient: "",
        name: "",
        exemtion: "",
        end_time: timeValue.from!.toDate(),
        start_time: timeValue.to!.toDate(),
        price: "",
        debt: "",
        referring_doctor: "",
        information_source: "",
        referring_doctor_notes: "",
        addition_info: "",
        branch: "",
        services: [],
    });

    const timeChangeHandler = (time, type) => {
        setTimeValue({ ...timeValue, [type]: time });
    };

    const medicalServiceStateKeeper = useLocalObservable(
        () => MedicalServiceStateKeeper.instance
    );
    const [services, setServices] = useState<IMedicalService[]>([]);
    const [appointedServices, setAppointedServices] = useState<
        {
            quantity: number;
            service: IMedicalService;
        }[]
    >([]);
    useEffect(() => {
        medicalServiceStateKeeper.findAllServices().then();
    }, []);

    useEffect(() => {
        if (doctorStateKeeper.selectedDoctors.length) {
            setServices([
                ...medicalServiceStateKeeper.services.filter(
                    (service) =>
                        service.id === doctorStateKeeper.selectedDoctors.at(0)?.doctor.id
                ),
            ]);
        }
    }, [
        medicalServiceStateKeeper.services,
        doctorStateKeeper.selectedDoctors.at(0),
    ]);

    const calendarEventStateKeeper = useLocalObservable(
        () => CalendarEventStateKeeper.instance
    );

    const handleCreateAppointmentClick = () => {
        if (doctorStateKeeper.selectedDoctors.length) {
            const values = {
                end: timeValue.from!.toDate(),
                start: timeValue.to!.toDate(),
                title: `${patientStateKeeper.selectedPatient?.l_name} ${patientStateKeeper.selectedPatient?.f_name}`,
                id: Math.max(
                    ...calendarEventStateKeeper.events.map((event) => event.id)
                ),
                doctor: String(doctorStateKeeper.selectedDoctors.at(0)!.id),
            };
            const selectedServices = appointedServices.map((item) => {
                const data: object = {
                    service: item.service.id,
                    quantity: item.quantity,
                    doctor: item.service.doctor[0].id,
                };
                return data;
            });
            calendarEventStateKeeper.addEvent(values);
            setFormData({
                ...formData,
                end_time: values.end,
                start_time: values.start,
                services: selectedServices,
                patient: patientStateKeeper.selectedPatient?.id,
                name: patientStateKeeper.selectedPatient?.f_name,
            });

            doctorStateKeeper.setSelectedDoctors([
                ...doctorStateKeeper.selectedDoctors,
            ]);
            setTimeout(() => {
                create_appointment(formData);

            }, 0);
        }
    };
    const create_appointment = (data) => {
        axios
            .post("https://back.dev-hayat.uz/api/v1/appointments/", data, headers)
            .then((res) => {
                if (res.status === 201) {
                    doctorStateKeeper.selectedDoctors.shift();
                    setServices([]);
                    setAppointedServices([]);
                    setDiscount(0);
                    clear_values()
                }
            })
            .catch((err) => {
                if (err.response.status == 400) {

                }
            });
    };
    const clear_values = () => [
        setFormData({ patient: '', name: '', exemtion: '', start_time: '', end_time: '', price: '', debt: '', referring_doctor: '', information_source: '', referring_doctor_notes: '', addition_info: '', branch: '', services: [] })
    ]
    useEffect(() => {
        if (doctorStateKeeper.selectedDoctors.length === 0) {
            navigator(-1);
            if (!patientStateKeeper.selectedPatient) {
                changeVisibilityNotification(true);
            } else if (Object.keys(patientStateKeeper.selectedPatient).length > 0) {
                patientStateKeeper.setSelectedPatient(null);
            }
        }
    }, [doctorStateKeeper.selectedDoctors]);

    return (
        <div className={styles.create_note}>
            <FlexSpaceBetween className={styles.top_block}>
                <Link to="/main" className={styles.return_back}>
                    <img src={ArrowCircle} alt="ArrowCircle" />
                    <p>
                        Запись на прием -{" "}
                        {doctorStateKeeper.selectedDoctors.at(0)?.doctor.f_name}
                    </p>
                </Link>

                <div className={styles.buttons}>
                    <Button
                        sx={{ backgroundColor: "#64B6F7" }}
                        variant="contained"
                        className={styles.create_btn}
                        startIcon={<NoteAdd />}
                        onClick={handleCreateAppointmentClick}
                    >
                        Создать
                    </Button>

                    <Link to="/main">
                        <Button
                            sx={{ backgroundColor: "#BDBDBD", marginLeft: "10px" }}
                            variant="contained"
                            className={styles.create_btn}
                            startIcon={<CloseCircle />}
                        >
                            Отмена
                        </Button>
                    </Link>
                </div>
            </FlexSpaceBetween>

            <FlexSpaceBetween mt="17px">
                <Box
                    className={styles.choose_block}
                    onClick={() => setOpenPatients(true)}
                >
                    <p className={styles.title}>Выберите пациента</p>
                    <FlexSpaceBetween>
                        <p className={styles.text}>
                            {patientStateKeeper.selectedPatient
                                ? `${patientStateKeeper.selectedPatient.l_name} ${patientStateKeeper.selectedPatient.f_name} ${patientStateKeeper.selectedPatient.mid_name}`.trim()
                                : "ФИО пациента"}
                        </p>
                        <ArrowDropDownIcon />
                    </FlexSpaceBetween>
                </Box>

                <Backdrop
                    open={Boolean(openPatientsPopup)}
                    onClick={(e: any) => {
                        if (!e.target.closest(`.${styles.patients_popup}`))
                            setOpenPatients(false);
                    }}
                    sx={{ zIndex: "999" }}
                >
                    <Box className={styles.patients_popup}>
                        <Typography variant="h5" className={styles.title}>
                            Пациенты
                        </Typography>

                        <div className={styles.patients_wrapper}>
                            <TextField
                                name="fullName"
                                id="outlined-basic"
                                label="ФИО пациента"
                                variant="outlined"
                                className={styles.patients_item}
                                value={searchFields.fullName}
                                onChange={handleSearchOnChange}
                            />
                            <TextField
                                name="inn"
                                id="outlined-basic"
                                label="ИНН"
                                variant="outlined"
                                className={styles.patients_item}
                                value={searchFields.inn}
                                onChange={handleSearchOnChange}
                            />
                            <TextField
                                name="emcNumber"
                                id="outlined-basic"
                                label="№ мед карты"
                                variant="outlined"
                                className={styles.patients_item}
                                value={searchFields.emcNumber}
                                onChange={handleSearchOnChange}
                            />
                            <TextField
                                name="dob"
                                id="outlined-basic"
                                label="Дата рождения"
                                variant="outlined"
                                className={styles.patients_item}
                                value={searchFields.dob}
                                onChange={handleSearchOnChange}
                            />
                            <TextField
                                name="phoneNumber"
                                id="outlined-basic"
                                label="Телефон"
                                variant="outlined"
                                className={styles.patients_item}
                                value={searchFields.phoneNumber}
                                onChange={handleSearchOnChange}
                            />
                            <TextField
                                name="patientID"
                                id="outlined-basic"
                                label="ID пациента"
                                variant="outlined"
                                className={styles.patients_item}
                                value={searchFields.patientID}
                                onChange={handleSearchOnChange}
                            />
                            <TextField
                                name="lastVisitedAt"
                                id="outlined-basic"
                                label="Дата приёма"
                                variant="outlined"
                                className={styles.patients_item}
                                value={searchFields.lastVisitAt}
                                onChange={handleSearchOnChange}
                            />
                            <Button
                                variant="contained"
                                onClick={() => navigator("/patientsDirectory/create")}
                                className={styles.create_btn}
                                startIcon={<UserAdd className="svg_stroke_white" />}
                                sx={{
                                    backgroundColor: "#64B6F7",
                                    height: "56px",
                                    width: "244px",
                                    marginBottom: "10px",
                                }}
                            >
                                Добавить Пациента
                            </Button>
                        </div>

                        <div className={styles.table_block}>
                            <div className={styles.table_top}>
                                <div className={styles.top_title}>Фамилия</div>
                                <div className={styles.top_title}>Имя</div>
                                <div className={styles.top_title}>Отчества</div>
                                <div className={styles.top_title}>Дата рождения</div>
                                <div className={styles.top_title}>Мобильный телефон</div>
                                <div className={styles.top_title}>ID номер</div>
                                <div className={styles.top_title}>
                                    Дата последнего посещения
                                </div>
                                <div className={styles.top_title}></div>
                            </div>

                            <div className={styles.table}>
                                <table>
                                    <tbody>
                                        {patients.map((patient, index) => (
                                            <tr key={index}>
                                                <td
                                                    onClick={() => {
                                                        patientStateKeeper.setSelectedPatient(patient);
                                                        setOpenPatients(false);
                                                    }}
                                                >
                                                    {patient?.l_name}
                                                </td>
                                                <td
                                                    onClick={() => {
                                                        patientStateKeeper.setSelectedPatient(patient);
                                                        setOpenPatients(false);
                                                    }}
                                                >
                                                    {patient?.f_name}
                                                </td>
                                                <td
                                                    onClick={() => {
                                                        patientStateKeeper.setSelectedPatient(patient);
                                                        setOpenPatients(false);
                                                    }}
                                                >
                                                    {patient.mid_name}
                                                </td>
                                                <td
                                                    onClick={() => {
                                                        patientStateKeeper.setSelectedPatient(patient);
                                                        setOpenPatients(false);
                                                    }}
                                                >
                                                    {new Date(patient.date_of_birth).toLocaleDateString()}
                                                </td>
                                                <td
                                                    onClick={() => {
                                                        patientStateKeeper.setSelectedPatient(patient);
                                                        setOpenPatients(false);
                                                    }}
                                                >
                                                    {patient.mobile_phone_number}
                                                </td>
                                                <td
                                                    onClick={() => {
                                                        patientStateKeeper.setSelectedPatient(patient);
                                                        setOpenPatients(false);
                                                    }}
                                                >
                                                    {patient.id}
                                                </td>
                                                <td
                                                    onClick={() => {
                                                        patientStateKeeper.setSelectedPatient(patient);
                                                        setOpenPatients(false);
                                                    }}
                                                >
                                                    {patient.last_visit_at}
                                                </td>
                                                <td>
                                                    <img src={Edit} alt="edit" />
                                                </td>
                                            </tr>
                                        ))}
                                    </tbody>
                                </table>
                            </div>
                        </div>

                        <div className={styles.patients_bottom}>
                            {/*<div className={`${styles.btn} ${styles.show}`}>Показать</div>*/}
                            <div
                                className={`${styles.btn} ${styles.cancel}`}
                                onClick={() => setOpenPatients(false)}
                            >
                                Отмена
                            </div>
                        </div>
                    </Box>
                </Backdrop>
                <Box>
                    <Button
                        sx={{ backgroundColor: "#007DFF", height: "42px", marginRight: 1 }}
                        variant="contained"
                        className={styles.create_btn}
                        startIcon={<EkmLogo className="svg_stroke_white" />}
                    >
                        ЭМК
                    </Button>
                    <Button
                        sx={{ backgroundColor: "#007DFF", height: "42px" }}
                        variant="contained"
                        onClick={() => setOpenPatients(true)}
                        className={styles.create_btn}
                        startIcon={<UserAdd className="svg_stroke_white" />}
                    >
                        Добавить Пациента
                    </Button>
                </Box>
            </FlexSpaceBetween>

            {patientStateKeeper.selectedPatient && (
                <PatientsTable
                    setFormData={setFormData}
                    formData={formData}
                    discount={discount}
                    setDiscount={setDiscount}
                    dateValue={dateValue}
                    setDateValue={setDateValue}
                    timeValue={timeValue}
                    timeChangeHandler={timeChangeHandler}
                    services={services}
                    appointedServices={appointedServices}
                    setAppointedServices={setAppointedServices}
                />
            )}
        </div>
    );
});

export default CreateNote;
