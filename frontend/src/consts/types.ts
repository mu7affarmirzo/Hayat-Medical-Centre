import moment from "moment/moment";

export interface ILoginState {
    login: string;
    password: string;
    showPassword: boolean;
    isLoginValid: boolean | null;
    isPasswordValid: boolean | null;
    rememberMe: boolean;
}

export interface ISpeciality {
    id: string;
    name: string;
    color: string
}

export interface IDoctor {
  id: string;
  f_name: string;
  speciality: ISpeciality;
  phone_number: string;
  color: string;
  active: boolean;
  email?: string;
}

export interface IEvent {
  end: Date;
  start: Date;
  title: string;
  id: number;
  allDay?: boolean;
  resource?: any;
  doctorId?: string;
}

export interface IAppointment {
  id: number;
  title: string;
  doctorId: string;
  start: string;
  end: string;
}

interface IEMC {
  name: string;
  createdAt: string;
  modifiedAt: string;
}

export interface IPatient {
  id: number;
  firstName: string;
  middleName?: string;
  lastName: string;
  email: string;
  dob: string;
  homPhoneNumber: string;
  mobilePhoneNumber: string;
  address: string;
  inn: string;
  lastVisitAt: string;
  emc: IEMC;
}

export interface IMedicalService {
  id: number;
  name: string;
  cost: number;
  doctorId: number;
}

export interface IDateValue {
  from: moment.Moment | null;
  to: moment.Moment | null;
}
export interface IBranch {
  name: string;
  id: number;
  organization: number;
}