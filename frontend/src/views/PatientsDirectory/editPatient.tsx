import * as React from "react";
import classes from "./createPatient.module.scss";
import { SelectChangeEvent } from "@mui/material";
import { Dayjs } from "dayjs";
import axios from "axios";
import { useLocalObservable } from "mobx-react-lite";
import { AuthorizationStateKeeper } from "../../store";
import PatientForm from "../../containers/patientForm";
import { useParams } from "react-router";

const EditPatient = () => {
  type StateTypes = {
    date_of_birth?: string;
    f_name?: string;
    mid_name?: string;
    l_name?: string;
    email?: string;
    home_phone_number?: string;
    mobile_phone_number?: string;
    address?: string;
    additional_info?: object;
    is_active?: true;
    doc_type?: string;
    doc_number?: string;
    INN?: string;
    country?: string;
    information_source?: number;
    created_by?: number;
    modified_by?: number;
    organization?: number;
    patient_group?: [0];
  };

  const [state, setState] = React.useState<StateTypes>();
  const params = useParams();
  const authorizationStateKeeper = useLocalObservable(
    () => AuthorizationStateKeeper.instance
  );
  const token = authorizationStateKeeper.token;

  const handleTextFieldChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    const { name, value } = event.currentTarget;
    setState({ ...state, [name]: value });
  };

  const [value, setValue] = React.useState<Dayjs | null>();
  const [open, setOpen] = React.useState(false);
  const headers = {
    headers: {
      Authorization: "Bearer " + JSON.parse(token).access,
    },
  };
  const handleOpenNotification = () => {
    setOpen(true);
  };

  const handleCloseNotification = (
    event?: React.SyntheticEvent | Event,
    reason?: string
  ) => {
    if (reason === "clickaway") {
      return;
    }

    setOpen(false);
  };

  const handleChange = (newValue: Dayjs | null) => {
    setValue(newValue);
    setState({ ...state, date_of_birth: newValue?.toISOString() });
  };

  const [medcard, setMedCard] = React.useState("");

  const handleSelectChange = (event: SelectChangeEvent) => {
    setMedCard(event.target.value as string);
    setState({ ...state, [event.target.name]: event.target.value });
  };

  const post_patient = () => {
    axios
      .put(
        "https://back.dev-hayat.uz/api/v1/organizations/patients/",
        state,
        headers
      )
      .then((res) => {
        if (res.status === 201) {
          handleOpenNotification();
        }
      })
      .catch((err) => console.log(err));
  };

  React.useEffect(() => {
    axios
      .get(
        `https://back.dev-hayat.uz/api/v1/organizations/patients/${params.id}`,
        headers
      )
      .then((response) => {
        setState(response.data);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div className={classes.create}>
      <PatientForm
        title="Редактирование записи"
        medcard={medcard}
        state={state}
        setState={setState}
        value={value}
        open={open}
        handleTextFieldChange={handleTextFieldChange}
        handleChange={handleChange}
        handleCloseNotification={handleCloseNotification}
        handleSelectChange={handleSelectChange}
        post_patient={post_patient}
      />
    </div>
  );
};

export default EditPatient;
