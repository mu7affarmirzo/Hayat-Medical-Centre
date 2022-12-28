import { observer, useLocalObservable } from "mobx-react-lite";
import React from "react";
import { IPatient } from "../../consts/types";
import { PatientStateKeeper } from "../../store";
import PatientsDirectory from "../../views/PatientsDirectory";

const DirectoryContainer = observer(() => {
    const patientStateKeeper = useLocalObservable(
        () => PatientStateKeeper.instance
    );

    const [patients, setPatients] = React.useState<IPatient[]>([]);
    const { filteredPatients } = patientStateKeeper

    React.useEffect(() => {
        patientStateKeeper.findAllPatients().then();
    }, []);

    React.useEffect(() => {
        setPatients([...patientStateKeeper.patients]);
    }, [patientStateKeeper.patients]);

    return <PatientsDirectory patients={patients} filteredPatients={filteredPatients} />;
});

export default DirectoryContainer;
