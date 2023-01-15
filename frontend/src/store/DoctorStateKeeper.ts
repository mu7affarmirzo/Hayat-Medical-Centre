import {makeAutoObservable, runInAction} from "mobx";
import {DoctorApiStub} from "../repositories";
import { IDoc, IInformationSource, IReferring } from "../consts/types";

class DoctorStateKeeper {
  static _instance: DoctorStateKeeper;
  private readonly doctorApiStub: DoctorApiStub;

  doctors: IDoc[] = [];
  doctorsCopy: IDoc[] = [];
  selectedDoctor: IDoc | null = null;
  selectedDoctors: IDoc[] = [];
  referring_doctors: IReferring[] = [];
  informationSources: IInformationSource[] = [];

  static get instance() {
    if (!DoctorStateKeeper._instance) {
      DoctorStateKeeper._instance = new DoctorStateKeeper();
    }
    return DoctorStateKeeper._instance;
  }

  constructor(doctorApiStub: DoctorApiStub = DoctorApiStub.instance) {
    this.doctorApiStub = doctorApiStub;
    makeAutoObservable(this, {}, { autoBind: true });
  }

  async findAllDoctors(): Promise<IDoc[]> {
    const doctors = await this.doctorApiStub.findAllDoctors();
    runInAction(() => {
      this.doctors = doctors;
      this.doctorsCopy = doctors;
    });
    return doctors;
  }

  async findAllReferrings(): Promise<IReferring[]> {
    const referring_doctors = await this.doctorApiStub.findAllReferrings();
    runInAction(() => {
      this.referring_doctors = referring_doctors;
    });
    return referring_doctors;
  }
  async findAllInformationSource(): Promise<IInformationSource[]> {
    const informationSources =
      await this.doctorApiStub.findAllInformationSource();
    runInAction(() => {
      this.informationSources = informationSources;
    });
    return informationSources;
  }

  setSelectedDoctor(doctor: IDoc) {
    this.selectedDoctor = doctor;
  }

  setSelectedDoctors(doctors: IDoc[]) {
    this.selectedDoctors = doctors;
  }

  searchDoctor(str: string) {
    if (str === "") {
      this.doctorsCopy = this.doctors;
      return false;
    }
    this.doctorsCopy = this.doctors.filter((item) => {
      if (item.doctor.f_name) {
        return (
          item.doctor.f_name.toLowerCase().includes(str.toLowerCase()) ||
          item.specialty_name.toLowerCase().includes(str.toLowerCase())
        );
        //   item.phone_number.toLowerCase().includes(str.toLowerCase())
      }
    });
  }
}

export default DoctorStateKeeper;

