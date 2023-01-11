import {makeAutoObservable, runInAction} from "mobx";
import {PatientApiStub} from "../repositories";
import {IPatient} from "../consts/types";

class PatientStateKeeper {
  static _instance: PatientStateKeeper;
  private readonly patientApiStub: PatientApiStub;

  patients: IPatient[] = [];
  selectedPatient: IPatient | null = null;
  filteredPatients: IPatient[] = [];

  static get instance() {
    if (!PatientStateKeeper._instance) {
      PatientStateKeeper._instance = new PatientStateKeeper();
    }
    return PatientStateKeeper._instance;
  }

  constructor(patientApiStub: PatientApiStub = PatientApiStub.instance) {
    this.patientApiStub = patientApiStub;
    makeAutoObservable(this, {}, { autoBind: true });
  }

  async findAllPatients(): Promise<IPatient[]> {
    const patients = await this.patientApiStub.findAllPatients();
    runInAction(() => {
      this.patients = patients;
    });
    return patients;
  }

  async mergePatients(data) {
    return await this.patientApiStub.mergePatient(data);
  }

  async searchPatients(patient: string): Promise<IPatient[]> {
    const filteredPatients = await this.patientApiStub.searchPatients(patient);
    runInAction(() => {
      this.filteredPatients = filteredPatients;
    });
    return filteredPatients;
  }

  setSelectedPatient(patient: IPatient | null) {
    this.selectedPatient = patient;
  }
}

export default PatientStateKeeper;

