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
  color: string;
  specialty_name: string;
}

// export interface IDoctor {
//   id: string;
//   f_name: string;
//   speciality: ISpeciality;
//   phone_number: string;
//   color: string;
//   active: boolean;
//   email?: string;
// }
export interface IDoc {
  branch: number;
  created_at: string;
  created_by: number;
  doctor: IDoctor;
  id: number;
  modified_at: string;
  modified_by: number;
  organization: number;
  specialty: ISpeciality[];
  specialty_name: string;
  is_at_work: boolean;
}
export interface IDoctor {
  branch_id: number;
  color: string;
  email: string;
  f_name: string;
  id: number;
  l_name: string;
  m_name: string;
  organization_id: number;
  phone_number: string;
  active?: boolean;
  sex: boolean;
  username: string;
  specialty?: any;
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
  addition_info: string;
  branch: number;
  debt: number;
  end_time: string;
  exemption: number;
  information_source: number;
  name: string;
  patient: number;
  price: number;
  referring_doc_notes: string;
  referring_doctor: number;
  services: [];
  start_time: string;
  status: string;
  id: number;
  doctorId?: string;
}

interface IEMC {
  name: string;
  createdAt: string;
  modifiedAt: string;
}

export interface IPatient {
  id: number;
  f_name: string;
  mid_name?: string;
  l_name: string;
  email: string;
  dob: string;
  homPhoneNumber: string;
  mobile_phone_number: string;
  address: string;
  inn: string;
  last_visit_at: string;
  emc: IEMC;
  date_of_birth: string;
  created_at: string;
  sex: string;
}

export interface IMedicalService {
  id: number;
  name: string;
  cost: number;
  doctorId: number;
  doctor: IDoc;
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

export interface ITransaction {
  payment_time: string;
  doctor: IDoctor;
  speacialty: ISpeciality;
  service: IMedicalService;
  payment_type: string;
  patient: IPatient;
  note: string;
  base_price: number;
  paid_amount: number;
  bank_name: string;
  type: string;
  payment_purpose: string;
  direction_of_payment: string;
  cheque: string;
  id: number;
}
export interface IPayment {
  receipt_id: number;
  patient: IPatient;
  doctor: IDoctor;
  sevice: IMedicalService;
  service_date: string;
  debt: number;
  price: number;
  discount: number;
  branch: IBranch;
  referring_doctor: any;
}
export interface IPaymentProcess {
  receipt_id: number;
  payment_type: string;
  is_manual: boolean;
  status: string;
  notes: string;
  referring_doctor_id: number;
  apointment_services: IMedicalService[];
}
export interface IReports {
  name: string;
}