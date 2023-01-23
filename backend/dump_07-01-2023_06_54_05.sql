--
-- PostgreSQL database cluster dump
--

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Drop databases (except postgres and template1)
--

DROP DATABASE hayat;




--
-- Drop roles
--

DROP ROLE hayat;


--
-- Roles
--

CREATE ROLE hayat;
ALTER ROLE hayat WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'SCRAM-SHA-256$4096:2R4pJNW4/WYqpMTJURu69Q==$sDD5k5kp4dlVMInrqsTYNUjgewFRLXnZWqhH/yoQCo0=:WH9qguxgdQfck1hR8Nrgj2ogbLeyxlPBjOSplfq2SrI=';






--
-- Databases
--

--
-- Database "template1" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 14.0 (Debian 14.0-1.pgdg110+1)
-- Dumped by pg_dump version 14.0 (Debian 14.0-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

UPDATE pg_catalog.pg_database SET datistemplate = false WHERE datname = 'template1';
DROP DATABASE template1;
--
-- Name: template1; Type: DATABASE; Schema: -; Owner: hayat
--

CREATE DATABASE template1 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE template1 OWNER TO hayat;

\connect template1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE template1; Type: COMMENT; Schema: -; Owner: hayat
--

COMMENT ON DATABASE template1 IS 'default template for new databases';


--
-- Name: template1; Type: DATABASE PROPERTIES; Schema: -; Owner: hayat
--

ALTER DATABASE template1 IS_TEMPLATE = true;


\connect template1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE template1; Type: ACL; Schema: -; Owner: hayat
--

REVOKE CONNECT,TEMPORARY ON DATABASE template1 FROM PUBLIC;
GRANT CONNECT ON DATABASE template1 TO PUBLIC;


--
-- PostgreSQL database dump complete
--

--
-- Database "hayat" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 14.0 (Debian 14.0-1.pgdg110+1)
-- Dumped by pg_dump version 14.0 (Debian 14.0-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: hayat; Type: DATABASE; Schema: -; Owner: hayat
--

CREATE DATABASE hayat WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE hayat OWNER TO hayat;

\connect hayat

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: account_account; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_account (
    id bigint NOT NULL,
    password character varying(128) NOT NULL,
    email character varying(60) NOT NULL,
    username character varying(30) NOT NULL,
    f_name character varying(50),
    l_name character varying(50),
    m_name character varying(50),
    phone_number character varying(30),
    sex boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    last_login timestamp with time zone NOT NULL,
    organization_id integer,
    branch_id integer,
    color character varying(255),
    is_admin boolean NOT NULL,
    is_active boolean NOT NULL,
    is_staff boolean NOT NULL,
    is_superuser boolean NOT NULL
);


ALTER TABLE public.account_account OWNER TO hayat;

--
-- Name: account_account_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_account_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_account_id_seq OWNER TO hayat;

--
-- Name: account_account_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_account_id_seq OWNED BY public.account_account.id;


--
-- Name: account_accountrolesmodel; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_accountrolesmodel (
    id bigint NOT NULL,
    date_created timestamp with time zone NOT NULL,
    role_id bigint NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.account_accountrolesmodel OWNER TO hayat;

--
-- Name: account_accountrolesmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_accountrolesmodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_accountrolesmodel_id_seq OWNER TO hayat;

--
-- Name: account_accountrolesmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_accountrolesmodel_id_seq OWNED BY public.account_accountrolesmodel.id;


--
-- Name: account_appointmentservicemodel; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_appointmentservicemodel (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL,
    appointment_id bigint,
    created_by_id bigint,
    modified_by_id bigint,
    service_id bigint NOT NULL,
    quantity integer NOT NULL,
    doctor_id bigint
);


ALTER TABLE public.account_appointmentservicemodel OWNER TO hayat;

--
-- Name: account_appointmentservicemodel_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_appointmentservicemodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_appointmentservicemodel_id_seq OWNER TO hayat;

--
-- Name: account_appointmentservicemodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_appointmentservicemodel_id_seq OWNED BY public.account_appointmentservicemodel.id;


--
-- Name: account_appointmentsmodel; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_appointmentsmodel (
    id bigint NOT NULL,
    name character varying(255),
    status character varying(50) NOT NULL,
    exemption integer,
    start_time timestamp with time zone NOT NULL,
    end_time timestamp with time zone,
    price bigint NOT NULL,
    debt bigint NOT NULL,
    referring_doc_notes text,
    addition_info text,
    is_contract boolean,
    is_priority boolean,
    send_sms boolean,
    created_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL,
    branch_id bigint,
    created_by_id bigint,
    information_source_id bigint,
    modified_by_id bigint,
    patient_id bigint NOT NULL,
    referring_doctor_id bigint
);


ALTER TABLE public.account_appointmentsmodel OWNER TO hayat;

--
-- Name: account_appointmentsmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_appointmentsmodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_appointmentsmodel_id_seq OWNER TO hayat;

--
-- Name: account_appointmentsmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_appointmentsmodel_id_seq OWNED BY public.account_appointmentsmodel.id;


--
-- Name: account_attendancemodel; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_attendancemodel (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    is_at_work boolean NOT NULL,
    staff_id bigint
);


ALTER TABLE public.account_attendancemodel OWNER TO hayat;

--
-- Name: account_attendancemodel_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_attendancemodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_attendancemodel_id_seq OWNER TO hayat;

--
-- Name: account_attendancemodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_attendancemodel_id_seq OWNED BY public.account_attendancemodel.id;


--
-- Name: account_branchmodel; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_branchmodel (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL,
    created_by_id bigint,
    modified_by_id bigint,
    organization_id bigint
);


ALTER TABLE public.account_branchmodel OWNER TO hayat;

--
-- Name: account_branchmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_branchmodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_branchmodel_id_seq OWNER TO hayat;

--
-- Name: account_branchmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_branchmodel_id_seq OWNED BY public.account_branchmodel.id;


--
-- Name: account_contractmodel; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_contractmodel (
    id bigint NOT NULL,
    contract_number character varying(255) NOT NULL,
    policy_number character varying(255),
    created_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL
);


ALTER TABLE public.account_contractmodel OWNER TO hayat;

--
-- Name: account_contractmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_contractmodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_contractmodel_id_seq OWNER TO hayat;

--
-- Name: account_contractmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_contractmodel_id_seq OWNED BY public.account_contractmodel.id;


--
-- Name: account_doctoraccountmodel; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_doctoraccountmodel (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL,
    doctor_id bigint NOT NULL
);


ALTER TABLE public.account_doctoraccountmodel OWNER TO hayat;

--
-- Name: account_doctoraccountmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_doctoraccountmodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_doctoraccountmodel_id_seq OWNER TO hayat;

--
-- Name: account_doctoraccountmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_doctoraccountmodel_id_seq OWNED BY public.account_doctoraccountmodel.id;


--
-- Name: account_doctorspecialitymodel; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_doctorspecialitymodel (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL,
    branch_id bigint,
    created_by_id bigint,
    doctor_id bigint,
    modified_by_id bigint,
    organization_id bigint,
    speciality_id bigint
);


ALTER TABLE public.account_doctorspecialitymodel OWNER TO hayat;

--
-- Name: account_doctorspecialitymodel_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_doctorspecialitymodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_doctorspecialitymodel_id_seq OWNER TO hayat;

--
-- Name: account_doctorspecialitymodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_doctorspecialitymodel_id_seq OWNED BY public.account_doctorspecialitymodel.id;


--
-- Name: account_emcdocumentmodel; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_emcdocumentmodel (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL,
    appointment_id bigint,
    created_by_id bigint,
    modified_by_id bigint,
    patient_id bigint,
    service_id bigint
);


ALTER TABLE public.account_emcdocumentmodel OWNER TO hayat;

--
-- Name: account_emcdocumentmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_emcdocumentmodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_emcdocumentmodel_id_seq OWNER TO hayat;

--
-- Name: account_emcdocumentmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_emcdocumentmodel_id_seq OWNED BY public.account_emcdocumentmodel.id;


--
-- Name: account_informationsourcemodel; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_informationsourcemodel (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL,
    created_by_id bigint,
    modified_by_id bigint,
    organization_id bigint
);


ALTER TABLE public.account_informationsourcemodel OWNER TO hayat;

--
-- Name: account_informationsourcemodel_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_informationsourcemodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_informationsourcemodel_id_seq OWNER TO hayat;

--
-- Name: account_informationsourcemodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_informationsourcemodel_id_seq OWNED BY public.account_informationsourcemodel.id;


--
-- Name: account_medicalservice; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_medicalservice (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    cost bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL,
    branch_id bigint,
    created_by_id bigint,
    modified_by_id bigint,
    speciality_id bigint
);


ALTER TABLE public.account_medicalservice OWNER TO hayat;

--
-- Name: account_medicalservice_doctor; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_medicalservice_doctor (
    id bigint NOT NULL,
    medicalservice_id bigint NOT NULL,
    doctoraccountmodel_id bigint NOT NULL
);


ALTER TABLE public.account_medicalservice_doctor OWNER TO hayat;

--
-- Name: account_medicalservice_doctor_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_medicalservice_doctor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_medicalservice_doctor_id_seq OWNER TO hayat;

--
-- Name: account_medicalservice_doctor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_medicalservice_doctor_id_seq OWNED BY public.account_medicalservice_doctor.id;


--
-- Name: account_medicalservice_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_medicalservice_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_medicalservice_id_seq OWNER TO hayat;

--
-- Name: account_medicalservice_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_medicalservice_id_seq OWNED BY public.account_medicalservice.id;


--
-- Name: account_organizationmodel; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_organizationmodel (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL,
    created_by_id bigint,
    modified_by_id bigint
);


ALTER TABLE public.account_organizationmodel OWNER TO hayat;

--
-- Name: account_organizationmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_organizationmodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_organizationmodel_id_seq OWNER TO hayat;

--
-- Name: account_organizationmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_organizationmodel_id_seq OWNED BY public.account_organizationmodel.id;


--
-- Name: account_patientgroupmodel; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_patientgroupmodel (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    color character varying(255) NOT NULL,
    exemption_percentage integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL,
    created_by_id bigint,
    modified_by_id bigint,
    organization_id bigint
);


ALTER TABLE public.account_patientgroupmodel OWNER TO hayat;

--
-- Name: account_patientgroupmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_patientgroupmodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_patientgroupmodel_id_seq OWNER TO hayat;

--
-- Name: account_patientgroupmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_patientgroupmodel_id_seq OWNED BY public.account_patientgroupmodel.id;


--
-- Name: account_patientmodel; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_patientmodel (
    id bigint NOT NULL,
    f_name character varying(255) NOT NULL,
    mid_name character varying(255),
    l_name character varying(255) NOT NULL,
    email character varying(254),
    date_of_birth timestamp with time zone NOT NULL,
    home_phone_number character varying(255),
    mobile_phone_number character varying(255),
    address text,
    additional_info jsonb,
    is_active boolean NOT NULL,
    doc_type character varying(255),
    doc_number character varying(255),
    issued_data date NOT NULL,
    "INN" character varying(255),
    country character varying(255),
    created_at timestamp with time zone NOT NULL,
    last_visit_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL,
    created_by_id bigint,
    information_source_id bigint NOT NULL,
    modified_by_id bigint,
    organization_id bigint
);


ALTER TABLE public.account_patientmodel OWNER TO hayat;

--
-- Name: account_patientmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_patientmodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_patientmodel_id_seq OWNER TO hayat;

--
-- Name: account_patientmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_patientmodel_id_seq OWNED BY public.account_patientmodel.id;


--
-- Name: account_patientmodel_patient_group; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_patientmodel_patient_group (
    id bigint NOT NULL,
    patientmodel_id bigint NOT NULL,
    patientgroupmodel_id bigint NOT NULL
);


ALTER TABLE public.account_patientmodel_patient_group OWNER TO hayat;

--
-- Name: account_patientmodel_patient_group_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_patientmodel_patient_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_patientmodel_patient_group_id_seq OWNER TO hayat;

--
-- Name: account_patientmodel_patient_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_patientmodel_patient_group_id_seq OWNED BY public.account_patientmodel_patient_group.id;


--
-- Name: account_permissionsmodel; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_permissionsmodel (
    id bigint NOT NULL,
    code integer NOT NULL,
    name character varying(255) NOT NULL,
    date_created timestamp with time zone NOT NULL
);


ALTER TABLE public.account_permissionsmodel OWNER TO hayat;

--
-- Name: account_permissionsmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_permissionsmodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_permissionsmodel_id_seq OWNER TO hayat;

--
-- Name: account_permissionsmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_permissionsmodel_id_seq OWNED BY public.account_permissionsmodel.id;


--
-- Name: account_referringdoctormodel; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_referringdoctormodel (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL,
    created_by_id bigint,
    modified_by_id bigint
);


ALTER TABLE public.account_referringdoctormodel OWNER TO hayat;

--
-- Name: account_referringdoctormodel_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_referringdoctormodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_referringdoctormodel_id_seq OWNER TO hayat;

--
-- Name: account_referringdoctormodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_referringdoctormodel_id_seq OWNED BY public.account_referringdoctormodel.id;


--
-- Name: account_rolepermissionmodel; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_rolepermissionmodel (
    id bigint NOT NULL,
    date_created timestamp with time zone NOT NULL,
    permission_id bigint NOT NULL,
    role_id bigint NOT NULL
);


ALTER TABLE public.account_rolepermissionmodel OWNER TO hayat;

--
-- Name: account_rolepermissionmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_rolepermissionmodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_rolepermissionmodel_id_seq OWNER TO hayat;

--
-- Name: account_rolepermissionmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_rolepermissionmodel_id_seq OWNED BY public.account_rolepermissionmodel.id;


--
-- Name: account_rolesmodel; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_rolesmodel (
    id bigint NOT NULL,
    code integer NOT NULL,
    name character varying(255) NOT NULL,
    date_created timestamp with time zone NOT NULL
);


ALTER TABLE public.account_rolesmodel OWNER TO hayat;

--
-- Name: account_rolesmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_rolesmodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_rolesmodel_id_seq OWNER TO hayat;

--
-- Name: account_rolesmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_rolesmodel_id_seq OWNED BY public.account_rolesmodel.id;


--
-- Name: account_specialitymodel; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.account_specialitymodel (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    modified_at timestamp with time zone NOT NULL,
    color character varying(255),
    branch_id bigint,
    created_by_id bigint,
    modified_by_id bigint,
    organization_id bigint
);


ALTER TABLE public.account_specialitymodel OWNER TO hayat;

--
-- Name: account_specialitymodel_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.account_specialitymodel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_specialitymodel_id_seq OWNER TO hayat;

--
-- Name: account_specialitymodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.account_specialitymodel_id_seq OWNED BY public.account_specialitymodel.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO hayat;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO hayat;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO hayat;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO hayat;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO hayat;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO hayat;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO hayat;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO hayat;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO hayat;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO hayat;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO hayat;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: hayat
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO hayat;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hayat
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: hayat
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO hayat;

--
-- Name: account_account id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_account ALTER COLUMN id SET DEFAULT nextval('public.account_account_id_seq'::regclass);


--
-- Name: account_accountrolesmodel id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_accountrolesmodel ALTER COLUMN id SET DEFAULT nextval('public.account_accountrolesmodel_id_seq'::regclass);


--
-- Name: account_appointmentservicemodel id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_appointmentservicemodel ALTER COLUMN id SET DEFAULT nextval('public.account_appointmentservicemodel_id_seq'::regclass);


--
-- Name: account_appointmentsmodel id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_appointmentsmodel ALTER COLUMN id SET DEFAULT nextval('public.account_appointmentsmodel_id_seq'::regclass);


--
-- Name: account_attendancemodel id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_attendancemodel ALTER COLUMN id SET DEFAULT nextval('public.account_attendancemodel_id_seq'::regclass);


--
-- Name: account_branchmodel id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_branchmodel ALTER COLUMN id SET DEFAULT nextval('public.account_branchmodel_id_seq'::regclass);


--
-- Name: account_contractmodel id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_contractmodel ALTER COLUMN id SET DEFAULT nextval('public.account_contractmodel_id_seq'::regclass);


--
-- Name: account_doctoraccountmodel id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_doctoraccountmodel ALTER COLUMN id SET DEFAULT nextval('public.account_doctoraccountmodel_id_seq'::regclass);


--
-- Name: account_doctorspecialitymodel id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_doctorspecialitymodel ALTER COLUMN id SET DEFAULT nextval('public.account_doctorspecialitymodel_id_seq'::regclass);


--
-- Name: account_emcdocumentmodel id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_emcdocumentmodel ALTER COLUMN id SET DEFAULT nextval('public.account_emcdocumentmodel_id_seq'::regclass);


--
-- Name: account_informationsourcemodel id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_informationsourcemodel ALTER COLUMN id SET DEFAULT nextval('public.account_informationsourcemodel_id_seq'::regclass);


--
-- Name: account_medicalservice id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_medicalservice ALTER COLUMN id SET DEFAULT nextval('public.account_medicalservice_id_seq'::regclass);


--
-- Name: account_medicalservice_doctor id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_medicalservice_doctor ALTER COLUMN id SET DEFAULT nextval('public.account_medicalservice_doctor_id_seq'::regclass);


--
-- Name: account_organizationmodel id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_organizationmodel ALTER COLUMN id SET DEFAULT nextval('public.account_organizationmodel_id_seq'::regclass);


--
-- Name: account_patientgroupmodel id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_patientgroupmodel ALTER COLUMN id SET DEFAULT nextval('public.account_patientgroupmodel_id_seq'::regclass);


--
-- Name: account_patientmodel id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_patientmodel ALTER COLUMN id SET DEFAULT nextval('public.account_patientmodel_id_seq'::regclass);


--
-- Name: account_patientmodel_patient_group id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_patientmodel_patient_group ALTER COLUMN id SET DEFAULT nextval('public.account_patientmodel_patient_group_id_seq'::regclass);


--
-- Name: account_permissionsmodel id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_permissionsmodel ALTER COLUMN id SET DEFAULT nextval('public.account_permissionsmodel_id_seq'::regclass);


--
-- Name: account_referringdoctormodel id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_referringdoctormodel ALTER COLUMN id SET DEFAULT nextval('public.account_referringdoctormodel_id_seq'::regclass);


--
-- Name: account_rolepermissionmodel id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_rolepermissionmodel ALTER COLUMN id SET DEFAULT nextval('public.account_rolepermissionmodel_id_seq'::regclass);


--
-- Name: account_rolesmodel id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_rolesmodel ALTER COLUMN id SET DEFAULT nextval('public.account_rolesmodel_id_seq'::regclass);


--
-- Name: account_specialitymodel id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_specialitymodel ALTER COLUMN id SET DEFAULT nextval('public.account_specialitymodel_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Data for Name: account_account; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_account (id, password, email, username, f_name, l_name, m_name, phone_number, sex, date_joined, last_login, organization_id, branch_id, color, is_admin, is_active, is_staff, is_superuser) FROM stdin;
4	pbkdf2_sha256$260000$p7joLnJDiN8rH3Vrum7FXH$uh8bJs0m3BH6rUAve2uexiV+zAIXOmM5Ej3GMvusbKE=	mac@gmail.com	Abdulla	Abdulla	Oripov	-	9989332772577	t	2022-12-03 08:39:31.555952+00	2022-12-03 11:04:10.004002+00	1	1	3	f	t	f	f
3	qwer1234	ulugbekr208@gmail.com	Ulug'bek	Ulug'bek	Rahmatullayev	Shavkat	998901287257	t	2022-12-03 08:35:25.4478+00	2022-12-03 11:05:25.878346+00	1	1	1	f	t	f	f
2	qwer1234	nazarmamatoc@gmail.com	Asrorxuja	Asrorxuja	Abdullayev	-	998933277257	t	2022-12-03 08:33:19.165324+00	2022-12-03 11:05:57.147195+00	1	1	white	f	t	f	f
1	pbkdf2_sha256$260000$5RdYof91JKOoky8UIEy8LA$bnM4KdWdwP9nTwySzwdHTqx64jDX1XY+AqB3V6T8rLI=	cmuzaffarmirzo@gmail.com	muzaffarmirzo	\N	\N	\N	\N	t	2022-12-02 18:48:11.47765+00	2023-01-01 16:20:45.291975+00	\N	\N	\N	t	t	t	t
\.


--
-- Data for Name: account_accountrolesmodel; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_accountrolesmodel (id, date_created, role_id, user_id) FROM stdin;
1	2022-12-03 11:03:16.791835+00	1	4
2	2022-12-03 11:06:35.275664+00	2	3
3	2022-12-03 11:07:15.135461+00	3	4
4	2022-12-03 11:07:36.759644+00	4	1
\.


--
-- Data for Name: account_appointmentservicemodel; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_appointmentservicemodel (id, created_at, modified_at, appointment_id, created_by_id, modified_by_id, service_id, quantity, doctor_id) FROM stdin;
1	2022-12-03 11:29:30.807222+00	2022-12-03 11:29:30.807265+00	1	2	2	1	1	\N
2	2022-12-03 21:13:28.682413+00	2022-12-03 21:13:28.682437+00	3	1	1	1	1	\N
3	2022-12-04 08:55:01.959195+00	2022-12-04 08:55:01.959219+00	4	1	1	2	1	\N
4	2022-12-04 08:58:38.34015+00	2022-12-04 08:58:38.340196+00	5	1	1	2	1	\N
5	2022-12-04 09:01:34.593097+00	2022-12-04 09:01:34.593117+00	6	1	1	1	1	\N
6	2022-12-04 09:02:57.595955+00	2022-12-04 09:02:57.595975+00	7	1	1	1	1	\N
7	2022-12-04 09:04:32.730465+00	2022-12-04 09:04:32.730496+00	7	1	1	3	1	\N
8	2022-12-05 09:17:57.382774+00	2022-12-05 09:17:57.382794+00	8	1	1	2	1	\N
9	2022-12-05 11:47:28.083155+00	2022-12-05 11:47:28.08318+00	9	1	1	2	1	\N
10	2022-12-05 15:00:04.882445+00	2022-12-05 15:00:04.88247+00	10	1	1	2	1	\N
11	2022-12-05 16:50:47.600452+00	2022-12-05 16:50:47.60049+00	11	1	1	2	1	\N
12	2022-12-05 16:55:57.278396+00	2022-12-05 16:55:57.278417+00	12	1	1	2	1	\N
13	2022-12-05 17:09:17.818131+00	2022-12-05 17:09:17.818152+00	13	1	1	2	1	\N
14	2022-12-06 14:43:19.901219+00	2022-12-06 14:43:19.90124+00	14	1	1	2	1	\N
15	2022-12-06 14:43:33.589115+00	2022-12-06 14:43:33.589134+00	15	1	1	2	1	\N
16	2022-12-06 14:54:23.204845+00	2022-12-06 14:54:23.204868+00	16	1	1	2	1	\N
17	2022-12-07 11:26:10.117391+00	2022-12-07 11:26:10.117643+00	17	1	1	2	1	\N
18	2022-12-07 13:42:36.43533+00	2022-12-07 13:42:36.435355+00	18	1	1	2	1	\N
19	2022-12-10 15:40:46.831865+00	2022-12-10 15:40:46.831892+00	19	1	1	1	1	\N
20	2022-12-12 15:25:21.443688+00	2022-12-12 15:25:21.443714+00	20	1	1	1	1	\N
21	2022-12-17 11:48:22.304977+00	2022-12-17 11:48:22.305018+00	21	1	1	2	1	\N
22	2022-12-18 19:03:33.476337+00	2022-12-18 19:03:33.476363+00	22	1	1	3	1	\N
23	2022-12-25 20:21:38.72109+00	2022-12-25 20:21:38.721122+00	23	1	1	2	1	\N
24	2022-12-26 13:02:19.645791+00	2022-12-26 13:02:19.645815+00	24	1	1	3	1	\N
25	2022-12-26 13:59:43.517213+00	2022-12-26 13:59:43.517236+00	25	1	1	1	1	\N
26	2022-12-26 14:01:41.976835+00	2022-12-26 14:01:41.976857+00	26	1	1	1	1	\N
27	2023-01-04 14:50:57.100991+00	2023-01-04 14:50:57.10104+00	27	1	1	3	1	\N
28	2023-01-04 20:37:13.71983+00	2023-01-04 20:37:13.719852+00	28	1	1	2	1	\N
\.


--
-- Data for Name: account_appointmentsmodel; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_appointmentsmodel (id, name, status, exemption, start_time, end_time, price, debt, referring_doc_notes, addition_info, is_contract, is_priority, send_sms, created_at, modified_at, branch_id, created_by_id, information_source_id, modified_by_id, patient_id, referring_doctor_id) FROM stdin;
1	ko'rik1	PAID	1	2022-12-03 11:17:24.261259+00	2022-12-01 11:16:40+00	100000	0			f	t	f	2022-12-03 11:17:24.261469+00	2022-12-03 11:17:24.261505+00	1	1	\N	1	1	\N
2	Rizvon	NOT PAID	25	2022-12-03 21:13:16.941017+00	2022-12-03 21:43:16.941017+00	1500000	1500000	Коммент нап врача	Доп. информация	f	f	f	2022-12-03 21:13:16.942332+00	2022-12-03 21:13:16.953304+00	\N	1	1	1	2	1
3	Rizvon	NOT PAID	25	2022-12-03 21:13:28.66737+00	2022-12-03 21:43:28.66737+00	1500000	1500000	Коммент нап врача	Доп. информация	f	f	f	2022-12-03 21:13:28.667473+00	2022-12-03 21:13:28.674549+00	\N	1	1	1	2	1
4	John	NOT PAID	30	2022-12-04 08:55:01.947474+00	2022-12-04 09:25:01.947474+00	2800000	2800000	Коммент нап врача	Доп. информация	f	f	f	2022-12-04 08:55:01.947585+00	2022-12-04 08:55:01.954492+00	\N	1	1	1	1	1
5	John	NOT PAID	35	2022-12-04 08:58:38.308846+00	2022-12-04 09:28:38.308846+00	1300000	1300000	Коммент нап врача	Доп. информация	f	f	f	2022-12-04 08:58:38.309075+00	2022-12-04 08:58:38.326996+00	\N	1	1	1	1	1
6	John	NOT PAID	70	2022-12-04 09:01:34.583986+00	2022-12-04 09:31:34.583986+00	300000	300000	Коммент нап врача	Доп. информация	f	f	f	2022-12-04 09:01:34.584112+00	2022-12-04 09:01:34.590456+00	\N	1	1	1	1	1
7	John	NOT PAID	50	2022-12-04 09:02:57.588872+00	2022-12-04 09:32:57.588872+00	3000000	3000000	Коммент нап врача234	ewrs	f	f	f	2022-12-04 09:02:57.58902+00	2022-12-04 09:02:57.592588+00	\N	1	1	1	1	1
8	Rizvon	NOT PAID	80	2022-12-05 09:17:57.356796+00	2022-12-05 09:47:57.356796+00	600000	500000	test	test	f	f	f	2022-12-05 09:17:57.356948+00	2022-12-05 09:17:57.379525+00	\N	1	1	1	2	1
9	John	NOT PAID	55	2022-12-05 11:47:28.069746+00	2022-12-05 12:17:28.069746+00	3000000	3000000	lorem	lorem	f	f	f	2022-12-05 11:47:28.069942+00	2022-12-05 11:47:28.07776+00	\N	1	1	1	1	1
10	John	NOT PAID	35	2022-12-05 15:00:04.759311+00	2022-12-05 15:30:04.759311+00	650000	650000	asd	asd	f	f	f	2022-12-05 15:00:04.762108+00	2022-12-05 15:00:04.877951+00	\N	1	1	1	1	1
11	John	NOT PAID	5	2022-12-05 16:50:47.580291+00	2022-12-05 10:15:21.722+00	1900000	1900000	asd	asd	f	f	f	2022-12-05 16:50:47.580498+00	2022-12-05 16:50:47.580527+00	\N	1	1	1	1	1
12	John	NOT PAID	5	2022-12-05 16:55:57.273311+00	2022-12-05 16:55:38.277+00	1900000	1900000	asdasdasd	asdasdasd	f	f	f	2022-12-05 16:55:57.273477+00	2022-12-05 16:55:57.273494+00	\N	1	1	1	1	1
13	John	NOT PAID	35	2022-12-05 17:09:17.813286+00	2022-12-05 17:08:47.877+00	1950000	1950000	test	test	f	f	f	2022-12-05 17:09:17.81342+00	2022-12-05 17:09:17.813438+00	\N	1	1	1	1	1
14	John	NOT PAID	\N	2022-12-06 14:43:19.880276+00	2022-12-06 15:13:19.880276+00	3000000	3000000	Коммент нап врача	Доп. информация	f	f	f	2022-12-06 14:43:19.881087+00	2022-12-06 14:43:19.897347+00	\N	1	1	1	1	1
15	John	NOT PAID	\N	2022-12-06 14:43:33.582927+00	2022-12-06 15:13:33.582927+00	3000000	3000000	Коммент нап врача	Доп. информация	f	f	f	2022-12-06 14:43:33.583031+00	2022-12-06 14:43:33.586267+00	\N	1	1	1	1	1
16	John	NOT PAID	45	2022-12-06 14:54:23.194869+00	2022-12-06 14:53:37.776+00	2000000	2000000	Коммент нап врача	Доп. информация	f	f	f	2022-12-06 14:54:23.195043+00	2022-12-06 14:54:23.195066+00	\N	1	1	1	1	1
17	Rizvon	NOT PAID	20	2022-12-07 11:26:10.097814+00	2022-12-07 11:25:44.013+00	800000	800000	Коммент нап врача	Доп. информация	f	f	f	2022-12-07 11:26:10.098873+00	2022-12-07 11:26:10.098894+00	\N	1	1	1	2	1
18	John	NOT PAID	100	2022-12-07 13:42:36.421189+00	2022-12-07 13:41:24.735+00	0	0	asd	asd	f	f	f	2022-12-07 13:42:36.421327+00	2022-12-07 13:42:36.421344+00	\N	1	1	1	1	1
19	John	NOT PAID	65	2022-12-10 15:40:46.816189+00	2022-12-10 15:38:53.154+00	850000	850000	asd	asd	f	f	f	2022-12-10 15:40:46.816535+00	2022-12-10 15:40:46.816556+00	\N	1	1	1	1	1
20	John	NOT PAID	40	2022-12-12 15:25:21.423827+00	2022-12-12 15:22:31.587+00	1500000	1500000	qedasad	asdasd	f	f	f	2022-12-12 15:25:21.425105+00	2022-12-12 15:25:21.425134+00	\N	1	1	1	1	1
21	John	NOT PAID	30	2022-12-17 11:48:22.281878+00	2022-12-17 09:11:50.044+00	3500000	3500000	Коммент нап врача		f	f	f	2022-12-17 11:48:22.283139+00	2022-12-17 11:48:22.283193+00	\N	1	1	1	1	1
22	ghjf	NOT PAID	5	2022-12-18 19:03:33.457185+00	2022-12-18 19:02:25.09+00	5700000	5700000	asdasd	asdasdasd	f	f	f	2022-12-18 19:03:33.457335+00	2022-12-18 19:03:33.457353+00	\N	1	1	1	3	\N
23	Sardor	NOT PAID	30	2022-12-25 20:21:38.709575+00	2022-12-25 21:10:34.02+00	2100000	2100000	Коммент нап врача	Доп. информация	f	f	f	2022-12-25 20:21:38.710064+00	2022-12-25 20:21:38.710091+00	\N	1	1	1	4	\N
24	Sardor	NOT PAID	5	2022-12-26 13:02:19.637313+00	2022-12-26 13:01:02.874+00	3000000	3000000	Коммент нап врача	Коммент нап врача	f	f	f	2022-12-26 13:02:19.637462+00	2022-12-26 13:02:19.637478+00	\N	1	1	1	4	\N
25	string	PAID	10	2022-12-26 13:59:43.508508+00	2022-12-26 13:57:18.615+00	100000	100000	string	string	f	f	f	2022-12-26 13:59:43.508663+00	2022-12-26 13:59:43.50868+00	1	1	1	1	1	1
26	string	PAID	10	2022-12-26 14:01:41.972197+00	2022-12-26 13:57:18.615+00	100000	100000	string	string	f	f	f	2022-12-26 14:01:41.972328+00	2022-12-26 14:01:41.972345+00	1	1	1	1	1	1
27	ghjf	NOT PAID	30	2023-01-04 14:50:57.082217+00	2023-01-04 09:11:49.153+00	3000000	3000000	1	1	f	f	f	2023-01-04 14:50:57.082662+00	2023-01-04 14:50:57.082709+00	\N	1	\N	1	3	\N
28	Sardor	NOT PAID	80	2023-01-04 20:37:13.711595+00	2023-01-04 23:21:13.253+00	200000	200000	123	123	f	f	f	2023-01-04 20:37:13.711728+00	2023-01-04 20:37:13.711745+00	\N	1	1	1	4	\N
\.


--
-- Data for Name: account_attendancemodel; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_attendancemodel (id, created_at, is_at_work, staff_id) FROM stdin;
\.


--
-- Data for Name: account_branchmodel; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_branchmodel (id, name, created_at, modified_at, created_by_id, modified_by_id, organization_id) FROM stdin;
1	Diagnostics	2022-12-02 18:51:34.478163+00	2022-12-02 18:51:34.478196+00	1	1	1
2	Kids	2022-12-02 18:51:44.5964+00	2022-12-02 18:51:44.596431+00	1	1	1
3	Hospital	2022-12-02 18:51:56.146595+00	2022-12-02 18:51:56.146628+00	1	1	1
\.


--
-- Data for Name: account_contractmodel; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_contractmodel (id, contract_number, policy_number, created_at, modified_at) FROM stdin;
\.


--
-- Data for Name: account_doctoraccountmodel; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_doctoraccountmodel (id, created_at, modified_at, doctor_id) FROM stdin;
1	2022-12-04 10:24:53.978539+00	2022-12-04 10:24:53.978569+00	1
2	2022-12-04 10:25:00.057308+00	2022-12-04 10:25:00.057369+00	4
3	2022-12-04 10:25:04.751393+00	2022-12-04 10:25:04.751425+00	3
4	2022-12-04 10:25:07.572746+00	2022-12-04 10:25:07.572779+00	2
\.


--
-- Data for Name: account_doctorspecialitymodel; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_doctorspecialitymodel (id, created_at, modified_at, branch_id, created_by_id, doctor_id, modified_by_id, organization_id, speciality_id) FROM stdin;
1	2022-12-03 11:32:28.899291+00	2022-12-03 11:32:28.899354+00	2	4	3	4	1	2
2	2022-12-03 11:37:17.696677+00	2022-12-03 11:37:17.696709+00	1	2	1	3	1	3
3	2022-12-03 11:38:53.482083+00	2022-12-03 11:38:53.482115+00	2	4	2	1	1	4
4	2022-12-10 06:59:19.234866+00	2022-12-10 06:59:19.234908+00	1	2	4	2	1	1
\.


--
-- Data for Name: account_emcdocumentmodel; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_emcdocumentmodel (id, name, created_at, modified_at, appointment_id, created_by_id, modified_by_id, patient_id, service_id) FROM stdin;
1	Emc doc	2022-12-03 11:42:31.68542+00	2022-12-03 11:42:31.685454+00	1	1	1	2	1
\.


--
-- Data for Name: account_informationsourcemodel; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_informationsourcemodel (id, name, created_at, modified_at, created_by_id, modified_by_id, organization_id) FROM stdin;
1	information1	2022-12-03 11:09:48.195344+00	2022-12-03 11:09:48.195413+00	1	1	1
\.


--
-- Data for Name: account_medicalservice; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_medicalservice (id, name, cost, created_at, modified_at, branch_id, created_by_id, modified_by_id, speciality_id) FROM stdin;
1	ko'rik	50000	2022-12-03 11:19:33.188436+00	2022-12-03 11:19:33.188467+00	1	1	1	1
2	Suyaklar ko'rigi	100000	2022-12-04 08:53:21.439686+00	2022-12-04 08:53:21.439743+00	1	1	1	4
3	Uzi	150000	2022-12-04 09:04:19.279704+00	2022-12-04 09:04:19.279734+00	1	1	1	4
\.


--
-- Data for Name: account_medicalservice_doctor; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_medicalservice_doctor (id, medicalservice_id, doctoraccountmodel_id) FROM stdin;
1	1	3
2	2	2
3	3	1
\.


--
-- Data for Name: account_organizationmodel; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_organizationmodel (id, name, created_at, modified_at, created_by_id, modified_by_id) FROM stdin;
1	Hayat	2022-12-02 18:51:19.647016+00	2022-12-02 18:51:19.64707+00	1	1
2	Hayat 2	2022-12-02 18:51:26.994527+00	2022-12-02 18:51:26.994558+00	1	1
\.


--
-- Data for Name: account_patientgroupmodel; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_patientgroupmodel (id, name, color, exemption_percentage, created_at, modified_at, created_by_id, modified_by_id, organization_id) FROM stdin;
1	Diabet	1	1	2022-12-03 11:10:14.24233+00	2022-12-03 11:10:14.242412+00	1	4	1
\.


--
-- Data for Name: account_patientmodel; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_patientmodel (id, f_name, mid_name, l_name, email, date_of_birth, home_phone_number, mobile_phone_number, address, additional_info, is_active, doc_type, doc_number, issued_data, "INN", country, created_at, last_visit_at, modified_at, created_by_id, information_source_id, modified_by_id, organization_id) FROM stdin;
1	John	Doe	James	John@doe.com	2022-11-03 11:08:40+00	321456789	987456654		\N	t	Oftalmolog	4	2022-12-03	234567876543	UZ	2022-12-03 11:10:43.070894+00	2022-12-03 11:10:43.070915+00	2022-12-03 11:10:43.070928+00	1	1	1	1
2	Rizvon	\N	Xon	\N	2000-12-03 11:41:28+00	837624512243654	123452		\N	t	\N	\N	2022-12-03	345654567	UZ	2022-12-03 11:42:19.435329+00	2022-12-03 11:42:19.435348+00	2022-12-03 11:42:19.435361+00	1	1	1	1
3	ghjf	jghf	ghjf	sardor@akbarov.uz	2022-12-20 21:31:43+00	123123123	12312312312	jhgf	"hf"	t	\N	\N	2022-12-08	1231	231231231	2022-12-07 21:33:34.251282+00	2022-12-07 21:33:34.251303+00	2022-12-07 21:33:34.251316+00	1	1	1	\N
4	Sardor		Akbarov	asrorjon5538@gmail.com	2001-08-12 13:29:14+00	735292432	+998990116000	Farg'ona	"developer"	t	\N	\N	2022-12-19	\N	\N	2022-12-19 13:31:22.536745+00	2022-12-19 13:31:22.536768+00	2022-12-19 13:31:22.536781+00	1	1	1	\N
\.


--
-- Data for Name: account_patientmodel_patient_group; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_patientmodel_patient_group (id, patientmodel_id, patientgroupmodel_id) FROM stdin;
1	1	1
2	2	1
3	3	1
4	4	1
\.


--
-- Data for Name: account_permissionsmodel; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_permissionsmodel (id, code, name, date_created) FROM stdin;
\.


--
-- Data for Name: account_referringdoctormodel; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_referringdoctormodel (id, name, created_at, modified_at, created_by_id, modified_by_id) FROM stdin;
1	Akbar Aliyev	2022-12-03 11:45:16.301398+00	2022-12-03 11:45:16.301429+00	3	3
\.


--
-- Data for Name: account_rolepermissionmodel; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_rolepermissionmodel (id, date_created, permission_id, role_id) FROM stdin;
\.


--
-- Data for Name: account_rolesmodel; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_rolesmodel (id, code, name, date_created) FROM stdin;
1	1	Doctor	2022-12-03 08:30:33.704632+00
2	2	Reseption	2022-12-03 11:06:29.019003+00
3	3	Sanitar	2022-12-03 11:07:05.895279+00
4	4	Director	2022-12-03 11:07:32.047077+00
\.


--
-- Data for Name: account_specialitymodel; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.account_specialitymodel (id, name, created_at, modified_at, color, branch_id, created_by_id, modified_by_id, organization_id) FROM stdin;
1	Okulist	2022-12-03 11:19:23.896544+00	2022-12-03 11:19:23.896576+00	black	1	1	4	1
2	Anesteziolog	2022-12-03 11:32:17.719006+00	2022-12-03 11:32:17.719037+00	green	1	1	4	1
3	Reanematolog	2022-12-03 11:37:07.151998+00	2022-12-03 11:37:07.152031+00	Black	1	1	1	1
4	Pediator	2022-12-03 11:38:43.265366+00	2022-12-03 11:38:43.265397+00	yellow	2	4	4	1
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add account	6	add_account
22	Can change account	6	change_account
23	Can delete account	6	delete_account
24	Can view account	6	view_account
25	Can add appointment service model	7	add_appointmentservicemodel
26	Can change appointment service model	7	change_appointmentservicemodel
27	Can delete appointment service model	7	delete_appointmentservicemodel
28	Can view appointment service model	7	view_appointmentservicemodel
29	Can add appointments model	8	add_appointmentsmodel
30	Can change appointments model	8	change_appointmentsmodel
31	Can delete appointments model	8	delete_appointmentsmodel
32	Can view appointments model	8	view_appointmentsmodel
33	Can add branch model	9	add_branchmodel
34	Can change branch model	9	change_branchmodel
35	Can delete branch model	9	delete_branchmodel
36	Can view branch model	9	view_branchmodel
37	Can add contract model	10	add_contractmodel
38	Can change contract model	10	change_contractmodel
39	Can delete contract model	10	delete_contractmodel
40	Can view contract model	10	view_contractmodel
41	Can add information source model	11	add_informationsourcemodel
42	Can change information source model	11	change_informationsourcemodel
43	Can delete information source model	11	delete_informationsourcemodel
44	Can view information source model	11	view_informationsourcemodel
45	Can add organization model	12	add_organizationmodel
46	Can change organization model	12	change_organizationmodel
47	Can delete organization model	12	delete_organizationmodel
48	Can view organization model	12	view_organizationmodel
49	Can add patient group model	13	add_patientgroupmodel
50	Can change patient group model	13	change_patientgroupmodel
51	Can delete patient group model	13	delete_patientgroupmodel
52	Can view patient group model	13	view_patientgroupmodel
53	Can add permissions model	14	add_permissionsmodel
54	Can change permissions model	14	change_permissionsmodel
55	Can delete permissions model	14	delete_permissionsmodel
56	Can view permissions model	14	view_permissionsmodel
57	Can add roles model	15	add_rolesmodel
58	Can change roles model	15	change_rolesmodel
59	Can delete roles model	15	delete_rolesmodel
60	Can view roles model	15	view_rolesmodel
61	Can add speciality model	16	add_specialitymodel
62	Can change speciality model	16	change_specialitymodel
63	Can delete speciality model	16	delete_specialitymodel
64	Can view speciality model	16	view_specialitymodel
65	Can add role permission model	17	add_rolepermissionmodel
66	Can change role permission model	17	change_rolepermissionmodel
67	Can delete role permission model	17	delete_rolepermissionmodel
68	Can view role permission model	17	view_rolepermissionmodel
69	Can add referring doctor model	18	add_referringdoctormodel
70	Can change referring doctor model	18	change_referringdoctormodel
71	Can delete referring doctor model	18	delete_referringdoctormodel
72	Can view referring doctor model	18	view_referringdoctormodel
73	Can add patient model	19	add_patientmodel
74	Can change patient model	19	change_patientmodel
75	Can delete patient model	19	delete_patientmodel
76	Can view patient model	19	view_patientmodel
77	Can add medical service	20	add_medicalservice
78	Can change medical service	20	change_medicalservice
79	Can delete medical service	20	delete_medicalservice
80	Can view medical service	20	view_medicalservice
81	Can add emc document model	21	add_emcdocumentmodel
82	Can change emc document model	21	change_emcdocumentmodel
83	Can delete emc document model	21	delete_emcdocumentmodel
84	Can view emc document model	21	view_emcdocumentmodel
85	Can add doctor speciality model	22	add_doctorspecialitymodel
86	Can change doctor speciality model	22	change_doctorspecialitymodel
87	Can delete doctor speciality model	22	delete_doctorspecialitymodel
88	Can view doctor speciality model	22	view_doctorspecialitymodel
89	Can add account roles model	23	add_accountrolesmodel
90	Can change account roles model	23	change_accountrolesmodel
91	Can delete account roles model	23	delete_accountrolesmodel
92	Can view account roles model	23	view_accountrolesmodel
93	Can add doctor account model	24	add_doctoraccountmodel
94	Can change doctor account model	24	change_doctoraccountmodel
95	Can delete doctor account model	24	delete_doctoraccountmodel
96	Can view doctor account model	24	view_doctoraccountmodel
97	Can add attendance model	25	add_attendancemodel
98	Can change attendance model	25	change_attendancemodel
99	Can delete attendance model	25	delete_attendancemodel
100	Can view attendance model	25	view_attendancemodel
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2022-12-02 18:51:19.65415+00	1	Hayat	1	[{"added": {}}]	12	1
2	2022-12-02 18:51:26.995973+00	2	Hayat 2	1	[{"added": {}}]	12	1
3	2022-12-02 18:51:34.480112+00	1	Diagnostics - Hayat	1	[{"added": {}}]	9	1
4	2022-12-02 18:51:44.597764+00	2	Kids - Hayat	1	[{"added": {}}]	9	1
5	2022-12-02 18:51:56.148378+00	3	Hospital - Hayat	1	[{"added": {}}]	9	1
6	2022-12-03 08:30:33.713819+00	1	Doctor	1	[{"added": {}}]	15	1
7	2022-12-03 08:33:19.179606+00	2	nazarmamatoc@gmail.com	1	[{"added": {}}]	6	1
8	2022-12-03 08:35:25.450028+00	3	ulugbekr2028@gmail.com	1	[{"added": {}}]	6	1
9	2022-12-03 08:39:31.557969+00	4	mac@gmail.com	1	[{"added": {}}]	6	1
10	2022-12-03 11:03:16.798798+00	1	Doctor-mac@gmail.com	1	[{"added": {}}]	23	1
11	2022-12-03 11:04:10.010947+00	4	mac@gmail.com	2	[{"changed": {"fields": ["Username", "F name", "L name", "M name"]}}]	6	1
12	2022-12-03 11:05:25.899028+00	3	ulugbekr208@gmail.com	2	[{"changed": {"fields": ["Email", "Username", "F name", "L name", "M name"]}}]	6	1
13	2022-12-03 11:05:57.150149+00	2	nazarmamatoc@gmail.com	2	[{"changed": {"fields": ["F name", "L name", "M name"]}}]	6	1
14	2022-12-03 11:06:29.022606+00	2	Reseption	1	[{"added": {}}]	15	1
15	2022-12-03 11:06:35.277418+00	2	Reseption-ulugbekr208@gmail.com	1	[{"added": {}}]	23	1
16	2022-12-03 11:07:05.8987+00	3	Sanitar	1	[{"added": {}}]	15	1
17	2022-12-03 11:07:15.138627+00	3	Sanitar-mac@gmail.com	1	[{"added": {}}]	23	1
18	2022-12-03 11:07:32.048103+00	4	Director	1	[{"added": {}}]	15	1
19	2022-12-03 11:07:36.761175+00	4	Director-cmuzaffarmirzo@gmail.com	1	[{"added": {}}]	23	1
20	2022-12-03 11:09:48.200219+00	1	information1	1	[{"added": {}}]	11	1
21	2022-12-03 11:10:14.246924+00	1	Diabet	1	[{"added": {}}]	13	1
22	2022-12-03 11:10:43.088191+00	1	John James Doe	1	[{"added": {}}]	19	1
23	2022-12-03 11:17:24.287087+00	1	John James Doe - ko'rik1	1	[{"added": {}}]	8	1
24	2022-12-03 11:19:23.899067+00	1	Okulist	1	[{"added": {}}]	16	1
25	2022-12-03 11:19:33.200341+00	1	ko'rik	1	[{"added": {}}]	20	1
26	2022-12-03 11:29:30.826606+00	1	ko'rik	1	[{"added": {}}]	7	1
27	2022-12-03 11:32:17.720843+00	2	Anesteziolog	1	[{"added": {}}]	16	1
28	2022-12-03 11:32:28.907022+00	1	ulugbekr208@gmail.com - Anesteziolog	1	[{"added": {}}]	22	1
29	2022-12-03 11:37:07.154653+00	3	Reanematolog	1	[{"added": {}}]	16	1
30	2022-12-03 11:37:17.702562+00	2	cmuzaffarmirzo@gmail.com - Reanematolog	1	[{"added": {}}]	22	1
31	2022-12-03 11:38:43.270568+00	4	Pediator	1	[{"added": {}}]	16	1
32	2022-12-03 11:38:53.484609+00	3	nazarmamatoc@gmail.com - Pediator	1	[{"added": {}}]	22	1
33	2022-12-03 11:42:19.447339+00	2	Rizvon Xon None	1	[{"added": {}}]	19	1
34	2022-12-03 11:42:31.689583+00	1	EMCDocumentModel object (1)	1	[{"added": {}}]	21	1
35	2022-12-03 11:45:16.303641+00	1	Akbar Aliyev	1	[{"added": {}}]	18	1
36	2022-12-04 08:53:21.462542+00	2	Suyaklar ko'rigi	1	[{"added": {}}]	20	1
37	2022-12-04 09:04:19.289071+00	3	Uzi	1	[{"added": {}}]	20	1
38	2022-12-04 09:04:32.731969+00	7	Uzi	1	[{"added": {}}]	7	1
39	2022-12-04 10:24:53.981288+00	1	<django.db.models.query_utils.DeferredAttribute object at 0x7f5e90230da0>	1	[{"added": {}}]	24	1
40	2022-12-04 10:25:00.063002+00	2	<django.db.models.query_utils.DeferredAttribute object at 0x7f5e90230da0>	1	[{"added": {}}]	24	1
41	2022-12-04 10:25:04.752428+00	3	<django.db.models.query_utils.DeferredAttribute object at 0x7f5e90230da0>	1	[{"added": {}}]	24	1
42	2022-12-04 10:25:07.573824+00	4	<django.db.models.query_utils.DeferredAttribute object at 0x7f5e90230da0>	1	[{"added": {}}]	24	1
43	2022-12-10 06:59:19.323485+00	4	nazarmamatoc@gmail.com - Okulist	1	[{"added": {}}]	22	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	account	account
7	account	appointmentservicemodel
8	account	appointmentsmodel
9	account	branchmodel
10	account	contractmodel
11	account	informationsourcemodel
12	account	organizationmodel
13	account	patientgroupmodel
14	account	permissionsmodel
15	account	rolesmodel
16	account	specialitymodel
17	account	rolepermissionmodel
18	account	referringdoctormodel
19	account	patientmodel
20	account	medicalservice
21	account	emcdocumentmodel
22	account	doctorspecialitymodel
23	account	accountrolesmodel
24	account	doctoraccountmodel
25	account	attendancemodel
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	account	0001_initial	2022-12-02 18:46:25.288091+00
2	contenttypes	0001_initial	2022-12-02 18:46:25.311286+00
3	admin	0001_initial	2022-12-02 18:46:25.397842+00
4	admin	0002_logentry_remove_auto_add	2022-12-02 18:46:26.445835+00
5	admin	0003_logentry_add_action_flag_choices	2022-12-02 18:46:26.523247+00
6	contenttypes	0002_remove_content_type_name	2022-12-02 18:46:26.627676+00
7	auth	0001_initial	2022-12-02 18:46:27.274751+00
8	auth	0002_alter_permission_name_max_length	2022-12-02 18:46:27.41533+00
9	auth	0003_alter_user_email_max_length	2022-12-02 18:46:27.800476+00
10	auth	0004_alter_user_username_opts	2022-12-02 18:46:27.888338+00
11	auth	0005_alter_user_last_login_null	2022-12-02 18:46:28.003305+00
12	auth	0006_require_contenttypes_0002	2022-12-02 18:46:28.007448+00
13	auth	0007_alter_validators_add_error_messages	2022-12-02 18:46:28.064255+00
14	auth	0008_alter_user_username_max_length	2022-12-02 18:46:28.103183+00
15	auth	0009_alter_user_last_name_max_length	2022-12-02 18:46:28.134382+00
16	auth	0010_alter_group_name_max_length	2022-12-02 18:46:28.222879+00
17	auth	0011_update_proxy_permissions	2022-12-02 18:46:28.391456+00
18	auth	0012_alter_user_first_name_max_length	2022-12-02 18:46:28.411854+00
19	sessions	0001_initial	2022-12-02 18:46:28.431079+00
20	account	0002_auto_20221204_1459	2022-12-04 10:00:04.104847+00
21	account	0003_auto_20221204_1526	2022-12-04 10:26:59.850406+00
22	account	0004_attendancemodel	2022-12-11 08:08:45.190617+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: hayat
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
38dwz9o5unklgm98b5g66uesg5hbrp7o	.eJxVjMsOwiAQRf-FtSHlMTxcuvcbyDCAVA0kpV0Z_12bdKHbe865LxZwW2vYRl7CnNiZCXb63SLSI7cdpDu2W-fU27rMke8KP-jg157y83K4fwcVR_3WPio05KQgocgqUFohQiw6gbQO0DsPtsjJGi_BTCUCIGKWhrT2ziF7fwDHXzce:1p1B6k:WuZNgZMLiYcq7kTWJBFRv_bJjhpGBLjKFj-ATypMZGk	2022-12-16 18:49:58.576516+00
ydz2bhly4pnpv7c1tcd877zl3viiytxy	.eJxVjMsOwiAQRf-FtSHlMTxcuvcbyDCAVA0kpV0Z_12bdKHbe865LxZwW2vYRl7CnNiZCXb63SLSI7cdpDu2W-fU27rMke8KP-jg157y83K4fwcVR_3WPio05KQgocgqUFohQiw6gbQO0DsPtsjJGi_BTCUCIGKWhrT2ziF7fwDHXzce:1p1NrT:RLf_hllr5A3JQxlw9OzRv2YqyENWyxAhKT1qAdXTCIE	2022-12-17 08:27:03.732176+00
rok1wj1xy9nn1qtevdx699spqxhlbjtq	.eJxVjMsOwiAQRf-FtSHlMTxcuvcbyDCAVA0kpV0Z_12bdKHbe865LxZwW2vYRl7CnNiZCXb63SLSI7cdpDu2W-fU27rMke8KP-jg157y83K4fwcVR_3WPio05KQgocgqUFohQiw6gbQO0DsPtsjJGi_BTCUCIGKWhrT2ziF7fwDHXzce:1p29zk:Pp72EG-Vd56kElk6k1zCUZ8ou5jW4w0nNlio1QojRdM	2022-12-19 11:50:48.794354+00
u447d5uf2mxmmu9lvjl3df0gmep83wbp	.eJxVjMsOwiAQRf-FtSHlMTxcuvcbyDCAVA0kpV0Z_12bdKHbe865LxZwW2vYRl7CnNiZCXb63SLSI7cdpDu2W-fU27rMke8KP-jg157y83K4fwcVR_3WPio05KQgocgqUFohQiw6gbQO0DsPtsjJGi_BTCUCIGKWhrT2ziF7fwDHXzce:1p3tjW:O1-xrNopKUQzgHs9FisgDReP5yA8sWr2T9i2SfziDB8	2022-12-24 06:53:14.223854+00
iswj4225q3faqwy2xjnbye3m00ldxa5y	.eJxVjMsOwiAQRf-FtSHlMTxcuvcbyDCAVA0kpV0Z_12bdKHbe865LxZwW2vYRl7CnNiZCXb63SLSI7cdpDu2W-fU27rMke8KP-jg157y83K4fwcVR_3WPio05KQgocgqUFohQiw6gbQO0DsPtsjJGi_BTCUCIGKWhrT2ziF7fwDHXzce:1p9pDU:rGSvAEJkXBY7AJSGgU9JRqkExYjg6SReET29uTzdyxI	2023-01-09 15:16:40.664597+00
bn6slp7me9kgsfh7r8yhi8by746gdgj8	.eJxVjMsOwiAQRf-FtSHlMTxcuvcbyDCAVA0kpV0Z_12bdKHbe865LxZwW2vYRl7CnNiZCXb63SLSI7cdpDu2W-fU27rMke8KP-jg157y83K4fwcVR_3WPio05KQgocgqUFohQiw6gbQO0DsPtsjJGi_BTCUCIGKWhrT2ziF7fwDHXzce:1pC14n:6WIMBHJkOOu5qdDKcCMFwhQjCIRt-QUe9KquugqKneQ	2023-01-15 16:20:45.296813+00
\.


--
-- Name: account_account_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_account_id_seq', 4, true);


--
-- Name: account_accountrolesmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_accountrolesmodel_id_seq', 4, true);


--
-- Name: account_appointmentservicemodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_appointmentservicemodel_id_seq', 28, true);


--
-- Name: account_appointmentsmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_appointmentsmodel_id_seq', 28, true);


--
-- Name: account_attendancemodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_attendancemodel_id_seq', 1, false);


--
-- Name: account_branchmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_branchmodel_id_seq', 3, true);


--
-- Name: account_contractmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_contractmodel_id_seq', 1, false);


--
-- Name: account_doctoraccountmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_doctoraccountmodel_id_seq', 4, true);


--
-- Name: account_doctorspecialitymodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_doctorspecialitymodel_id_seq', 4, true);


--
-- Name: account_emcdocumentmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_emcdocumentmodel_id_seq', 1, true);


--
-- Name: account_informationsourcemodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_informationsourcemodel_id_seq', 1, true);


--
-- Name: account_medicalservice_doctor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_medicalservice_doctor_id_seq', 3, true);


--
-- Name: account_medicalservice_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_medicalservice_id_seq', 3, true);


--
-- Name: account_organizationmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_organizationmodel_id_seq', 2, true);


--
-- Name: account_patientgroupmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_patientgroupmodel_id_seq', 1, true);


--
-- Name: account_patientmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_patientmodel_id_seq', 4, true);


--
-- Name: account_patientmodel_patient_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_patientmodel_patient_group_id_seq', 4, true);


--
-- Name: account_permissionsmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_permissionsmodel_id_seq', 1, false);


--
-- Name: account_referringdoctormodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_referringdoctormodel_id_seq', 1, true);


--
-- Name: account_rolepermissionmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_rolepermissionmodel_id_seq', 1, false);


--
-- Name: account_rolesmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_rolesmodel_id_seq', 4, true);


--
-- Name: account_specialitymodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.account_specialitymodel_id_seq', 4, true);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 100, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 43, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 25, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hayat
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 22, true);


--
-- Name: account_account account_account_email_key; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_account
    ADD CONSTRAINT account_account_email_key UNIQUE (email);


--
-- Name: account_account account_account_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_account
    ADD CONSTRAINT account_account_pkey PRIMARY KEY (id);


--
-- Name: account_account account_account_username_key; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_account
    ADD CONSTRAINT account_account_username_key UNIQUE (username);


--
-- Name: account_accountrolesmodel account_accountrolesmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_accountrolesmodel
    ADD CONSTRAINT account_accountrolesmodel_pkey PRIMARY KEY (id);


--
-- Name: account_appointmentservicemodel account_appointmentservicemodel_doctor_id_key; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_appointmentservicemodel
    ADD CONSTRAINT account_appointmentservicemodel_doctor_id_key UNIQUE (doctor_id);


--
-- Name: account_appointmentservicemodel account_appointmentservicemodel_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_appointmentservicemodel
    ADD CONSTRAINT account_appointmentservicemodel_pkey PRIMARY KEY (id);


--
-- Name: account_appointmentsmodel account_appointmentsmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_appointmentsmodel
    ADD CONSTRAINT account_appointmentsmodel_pkey PRIMARY KEY (id);


--
-- Name: account_attendancemodel account_attendancemodel_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_attendancemodel
    ADD CONSTRAINT account_attendancemodel_pkey PRIMARY KEY (id);


--
-- Name: account_branchmodel account_branchmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_branchmodel
    ADD CONSTRAINT account_branchmodel_pkey PRIMARY KEY (id);


--
-- Name: account_contractmodel account_contractmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_contractmodel
    ADD CONSTRAINT account_contractmodel_pkey PRIMARY KEY (id);


--
-- Name: account_doctoraccountmodel account_doctoraccountmodel_doctor_id_key; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_doctoraccountmodel
    ADD CONSTRAINT account_doctoraccountmodel_doctor_id_key UNIQUE (doctor_id);


--
-- Name: account_doctoraccountmodel account_doctoraccountmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_doctoraccountmodel
    ADD CONSTRAINT account_doctoraccountmodel_pkey PRIMARY KEY (id);


--
-- Name: account_doctorspecialitymodel account_doctorspecialitymodel_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_doctorspecialitymodel
    ADD CONSTRAINT account_doctorspecialitymodel_pkey PRIMARY KEY (id);


--
-- Name: account_emcdocumentmodel account_emcdocumentmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_emcdocumentmodel
    ADD CONSTRAINT account_emcdocumentmodel_pkey PRIMARY KEY (id);


--
-- Name: account_informationsourcemodel account_informationsourcemodel_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_informationsourcemodel
    ADD CONSTRAINT account_informationsourcemodel_pkey PRIMARY KEY (id);


--
-- Name: account_medicalservice_doctor account_medicalservice_d_medicalservice_id_accoun_0f9e5980_uniq; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_medicalservice_doctor
    ADD CONSTRAINT account_medicalservice_d_medicalservice_id_accoun_0f9e5980_uniq UNIQUE (medicalservice_id, doctoraccountmodel_id);


--
-- Name: account_medicalservice_doctor account_medicalservice_doctor_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_medicalservice_doctor
    ADD CONSTRAINT account_medicalservice_doctor_pkey PRIMARY KEY (id);


--
-- Name: account_medicalservice account_medicalservice_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_medicalservice
    ADD CONSTRAINT account_medicalservice_pkey PRIMARY KEY (id);


--
-- Name: account_organizationmodel account_organizationmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_organizationmodel
    ADD CONSTRAINT account_organizationmodel_pkey PRIMARY KEY (id);


--
-- Name: account_patientgroupmodel account_patientgroupmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_patientgroupmodel
    ADD CONSTRAINT account_patientgroupmodel_pkey PRIMARY KEY (id);


--
-- Name: account_patientmodel_patient_group account_patientmodel_pat_patientmodel_id_patientg_332fdf2c_uniq; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_patientmodel_patient_group
    ADD CONSTRAINT account_patientmodel_pat_patientmodel_id_patientg_332fdf2c_uniq UNIQUE (patientmodel_id, patientgroupmodel_id);


--
-- Name: account_patientmodel_patient_group account_patientmodel_patient_group_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_patientmodel_patient_group
    ADD CONSTRAINT account_patientmodel_patient_group_pkey PRIMARY KEY (id);


--
-- Name: account_patientmodel account_patientmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_patientmodel
    ADD CONSTRAINT account_patientmodel_pkey PRIMARY KEY (id);


--
-- Name: account_permissionsmodel account_permissionsmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_permissionsmodel
    ADD CONSTRAINT account_permissionsmodel_pkey PRIMARY KEY (id);


--
-- Name: account_referringdoctormodel account_referringdoctormodel_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_referringdoctormodel
    ADD CONSTRAINT account_referringdoctormodel_pkey PRIMARY KEY (id);


--
-- Name: account_rolepermissionmodel account_rolepermissionmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_rolepermissionmodel
    ADD CONSTRAINT account_rolepermissionmodel_pkey PRIMARY KEY (id);


--
-- Name: account_rolesmodel account_rolesmodel_code_key; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_rolesmodel
    ADD CONSTRAINT account_rolesmodel_code_key UNIQUE (code);


--
-- Name: account_rolesmodel account_rolesmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_rolesmodel
    ADD CONSTRAINT account_rolesmodel_pkey PRIMARY KEY (id);


--
-- Name: account_specialitymodel account_specialitymodel_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_specialitymodel
    ADD CONSTRAINT account_specialitymodel_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: account_account_email_3d3b3e7a_like; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_account_email_3d3b3e7a_like ON public.account_account USING btree (email varchar_pattern_ops);


--
-- Name: account_account_username_7d6d7da7_like; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_account_username_7d6d7da7_like ON public.account_account USING btree (username varchar_pattern_ops);


--
-- Name: account_accountrolesmodel_role_id_74bb8ecb; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_accountrolesmodel_role_id_74bb8ecb ON public.account_accountrolesmodel USING btree (role_id);


--
-- Name: account_accountrolesmodel_user_id_647559c8; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_accountrolesmodel_user_id_647559c8 ON public.account_accountrolesmodel USING btree (user_id);


--
-- Name: account_appointmentservicemodel_appointment_id_41f9cd48; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_appointmentservicemodel_appointment_id_41f9cd48 ON public.account_appointmentservicemodel USING btree (appointment_id);


--
-- Name: account_appointmentservicemodel_created_by_id_26a22fc8; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_appointmentservicemodel_created_by_id_26a22fc8 ON public.account_appointmentservicemodel USING btree (created_by_id);


--
-- Name: account_appointmentservicemodel_modified_by_id_f175fd02; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_appointmentservicemodel_modified_by_id_f175fd02 ON public.account_appointmentservicemodel USING btree (modified_by_id);


--
-- Name: account_appointmentservicemodel_service_id_dc575559; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_appointmentservicemodel_service_id_dc575559 ON public.account_appointmentservicemodel USING btree (service_id);


--
-- Name: account_appointmentsmodel_branch_id_242ab5ac; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_appointmentsmodel_branch_id_242ab5ac ON public.account_appointmentsmodel USING btree (branch_id);


--
-- Name: account_appointmentsmodel_created_by_id_0cee93f9; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_appointmentsmodel_created_by_id_0cee93f9 ON public.account_appointmentsmodel USING btree (created_by_id);


--
-- Name: account_appointmentsmodel_information_source_id_bf2ea644; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_appointmentsmodel_information_source_id_bf2ea644 ON public.account_appointmentsmodel USING btree (information_source_id);


--
-- Name: account_appointmentsmodel_modified_by_id_793521b5; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_appointmentsmodel_modified_by_id_793521b5 ON public.account_appointmentsmodel USING btree (modified_by_id);


--
-- Name: account_appointmentsmodel_patient_id_8072c842; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_appointmentsmodel_patient_id_8072c842 ON public.account_appointmentsmodel USING btree (patient_id);


--
-- Name: account_appointmentsmodel_referring_doctor_id_d4e4c12a; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_appointmentsmodel_referring_doctor_id_d4e4c12a ON public.account_appointmentsmodel USING btree (referring_doctor_id);


--
-- Name: account_attendancemodel_staff_id_f0a5937a; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_attendancemodel_staff_id_f0a5937a ON public.account_attendancemodel USING btree (staff_id);


--
-- Name: account_branchmodel_created_by_id_1405fc7c; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_branchmodel_created_by_id_1405fc7c ON public.account_branchmodel USING btree (created_by_id);


--
-- Name: account_branchmodel_modified_by_id_37e59bd1; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_branchmodel_modified_by_id_37e59bd1 ON public.account_branchmodel USING btree (modified_by_id);


--
-- Name: account_branchmodel_organization_id_b15d9044; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_branchmodel_organization_id_b15d9044 ON public.account_branchmodel USING btree (organization_id);


--
-- Name: account_doctorspecialitymodel_branch_id_da287079; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_doctorspecialitymodel_branch_id_da287079 ON public.account_doctorspecialitymodel USING btree (branch_id);


--
-- Name: account_doctorspecialitymodel_created_by_id_5a0144e6; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_doctorspecialitymodel_created_by_id_5a0144e6 ON public.account_doctorspecialitymodel USING btree (created_by_id);


--
-- Name: account_doctorspecialitymodel_doctor_id_f1cd2d2d; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_doctorspecialitymodel_doctor_id_f1cd2d2d ON public.account_doctorspecialitymodel USING btree (doctor_id);


--
-- Name: account_doctorspecialitymodel_modified_by_id_fcd7f6c2; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_doctorspecialitymodel_modified_by_id_fcd7f6c2 ON public.account_doctorspecialitymodel USING btree (modified_by_id);


--
-- Name: account_doctorspecialitymodel_organization_id_caf065e3; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_doctorspecialitymodel_organization_id_caf065e3 ON public.account_doctorspecialitymodel USING btree (organization_id);


--
-- Name: account_doctorspecialitymodel_speciality_id_457be40d; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_doctorspecialitymodel_speciality_id_457be40d ON public.account_doctorspecialitymodel USING btree (speciality_id);


--
-- Name: account_emcdocumentmodel_appointment_id_bd1d58be; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_emcdocumentmodel_appointment_id_bd1d58be ON public.account_emcdocumentmodel USING btree (appointment_id);


--
-- Name: account_emcdocumentmodel_created_by_id_e147f8ab; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_emcdocumentmodel_created_by_id_e147f8ab ON public.account_emcdocumentmodel USING btree (created_by_id);


--
-- Name: account_emcdocumentmodel_modified_by_id_e41e04f6; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_emcdocumentmodel_modified_by_id_e41e04f6 ON public.account_emcdocumentmodel USING btree (modified_by_id);


--
-- Name: account_emcdocumentmodel_patient_id_9be9fe01; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_emcdocumentmodel_patient_id_9be9fe01 ON public.account_emcdocumentmodel USING btree (patient_id);


--
-- Name: account_emcdocumentmodel_service_id_c81cfc36; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_emcdocumentmodel_service_id_c81cfc36 ON public.account_emcdocumentmodel USING btree (service_id);


--
-- Name: account_informationsourcemodel_created_by_id_c0a8b90f; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_informationsourcemodel_created_by_id_c0a8b90f ON public.account_informationsourcemodel USING btree (created_by_id);


--
-- Name: account_informationsourcemodel_modified_by_id_981deaec; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_informationsourcemodel_modified_by_id_981deaec ON public.account_informationsourcemodel USING btree (modified_by_id);


--
-- Name: account_informationsourcemodel_organization_id_55be1d2b; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_informationsourcemodel_organization_id_55be1d2b ON public.account_informationsourcemodel USING btree (organization_id);


--
-- Name: account_medicalservice_branch_id_5127a4ec; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_medicalservice_branch_id_5127a4ec ON public.account_medicalservice USING btree (branch_id);


--
-- Name: account_medicalservice_created_by_id_552434ac; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_medicalservice_created_by_id_552434ac ON public.account_medicalservice USING btree (created_by_id);


--
-- Name: account_medicalservice_doctor_account_id_d24bc787; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_medicalservice_doctor_account_id_d24bc787 ON public.account_medicalservice_doctor USING btree (doctoraccountmodel_id);


--
-- Name: account_medicalservice_doctor_medicalservice_id_558a5687; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_medicalservice_doctor_medicalservice_id_558a5687 ON public.account_medicalservice_doctor USING btree (medicalservice_id);


--
-- Name: account_medicalservice_modified_by_id_952287d5; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_medicalservice_modified_by_id_952287d5 ON public.account_medicalservice USING btree (modified_by_id);


--
-- Name: account_medicalservice_speciality_id_b51d5725; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_medicalservice_speciality_id_b51d5725 ON public.account_medicalservice USING btree (speciality_id);


--
-- Name: account_organizationmodel_created_by_id_8813ba33; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_organizationmodel_created_by_id_8813ba33 ON public.account_organizationmodel USING btree (created_by_id);


--
-- Name: account_organizationmodel_modified_by_id_3a70987c; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_organizationmodel_modified_by_id_3a70987c ON public.account_organizationmodel USING btree (modified_by_id);


--
-- Name: account_patientgroupmodel_created_by_id_654e1e76; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_patientgroupmodel_created_by_id_654e1e76 ON public.account_patientgroupmodel USING btree (created_by_id);


--
-- Name: account_patientgroupmodel_modified_by_id_509edc05; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_patientgroupmodel_modified_by_id_509edc05 ON public.account_patientgroupmodel USING btree (modified_by_id);


--
-- Name: account_patientgroupmodel_organization_id_078ae6c5; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_patientgroupmodel_organization_id_078ae6c5 ON public.account_patientgroupmodel USING btree (organization_id);


--
-- Name: account_patientmodel_created_by_id_1b0b2595; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_patientmodel_created_by_id_1b0b2595 ON public.account_patientmodel USING btree (created_by_id);


--
-- Name: account_patientmodel_information_source_id_a123e98f; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_patientmodel_information_source_id_a123e98f ON public.account_patientmodel USING btree (information_source_id);


--
-- Name: account_patientmodel_modified_by_id_20085674; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_patientmodel_modified_by_id_20085674 ON public.account_patientmodel USING btree (modified_by_id);


--
-- Name: account_patientmodel_organization_id_c4d750e6; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_patientmodel_organization_id_c4d750e6 ON public.account_patientmodel USING btree (organization_id);


--
-- Name: account_patientmodel_patie_patientgroupmodel_id_21677d95; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_patientmodel_patie_patientgroupmodel_id_21677d95 ON public.account_patientmodel_patient_group USING btree (patientgroupmodel_id);


--
-- Name: account_patientmodel_patient_group_patientmodel_id_e53c1730; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_patientmodel_patient_group_patientmodel_id_e53c1730 ON public.account_patientmodel_patient_group USING btree (patientmodel_id);


--
-- Name: account_referringdoctormodel_created_by_id_fe0a3ec4; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_referringdoctormodel_created_by_id_fe0a3ec4 ON public.account_referringdoctormodel USING btree (created_by_id);


--
-- Name: account_referringdoctormodel_modified_by_id_fda5f1d2; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_referringdoctormodel_modified_by_id_fda5f1d2 ON public.account_referringdoctormodel USING btree (modified_by_id);


--
-- Name: account_rolepermissionmodel_permission_id_57cada6c; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_rolepermissionmodel_permission_id_57cada6c ON public.account_rolepermissionmodel USING btree (permission_id);


--
-- Name: account_rolepermissionmodel_role_id_51569830; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_rolepermissionmodel_role_id_51569830 ON public.account_rolepermissionmodel USING btree (role_id);


--
-- Name: account_specialitymodel_branch_id_cac642b1; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_specialitymodel_branch_id_cac642b1 ON public.account_specialitymodel USING btree (branch_id);


--
-- Name: account_specialitymodel_created_by_id_f735d5d1; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_specialitymodel_created_by_id_f735d5d1 ON public.account_specialitymodel USING btree (created_by_id);


--
-- Name: account_specialitymodel_modified_by_id_91cb8351; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_specialitymodel_modified_by_id_91cb8351 ON public.account_specialitymodel USING btree (modified_by_id);


--
-- Name: account_specialitymodel_organization_id_9a98d939; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX account_specialitymodel_organization_id_9a98d939 ON public.account_specialitymodel USING btree (organization_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: hayat
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: account_accountrolesmodel account_accountroles_role_id_74bb8ecb_fk_account_r; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_accountrolesmodel
    ADD CONSTRAINT account_accountroles_role_id_74bb8ecb_fk_account_r FOREIGN KEY (role_id) REFERENCES public.account_rolesmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_accountrolesmodel account_accountroles_user_id_647559c8_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_accountrolesmodel
    ADD CONSTRAINT account_accountroles_user_id_647559c8_fk_account_a FOREIGN KEY (user_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_appointmentservicemodel account_appointments_appointment_id_41f9cd48_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_appointmentservicemodel
    ADD CONSTRAINT account_appointments_appointment_id_41f9cd48_fk_account_a FOREIGN KEY (appointment_id) REFERENCES public.account_appointmentsmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_appointmentsmodel account_appointments_branch_id_242ab5ac_fk_account_b; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_appointmentsmodel
    ADD CONSTRAINT account_appointments_branch_id_242ab5ac_fk_account_b FOREIGN KEY (branch_id) REFERENCES public.account_branchmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_appointmentsmodel account_appointments_created_by_id_0cee93f9_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_appointmentsmodel
    ADD CONSTRAINT account_appointments_created_by_id_0cee93f9_fk_account_a FOREIGN KEY (created_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_appointmentservicemodel account_appointments_created_by_id_26a22fc8_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_appointmentservicemodel
    ADD CONSTRAINT account_appointments_created_by_id_26a22fc8_fk_account_a FOREIGN KEY (created_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_appointmentservicemodel account_appointments_doctor_id_340f60bb_fk_account_d; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_appointmentservicemodel
    ADD CONSTRAINT account_appointments_doctor_id_340f60bb_fk_account_d FOREIGN KEY (doctor_id) REFERENCES public.account_doctoraccountmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_appointmentsmodel account_appointments_information_source_i_bf2ea644_fk_account_i; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_appointmentsmodel
    ADD CONSTRAINT account_appointments_information_source_i_bf2ea644_fk_account_i FOREIGN KEY (information_source_id) REFERENCES public.account_informationsourcemodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_appointmentsmodel account_appointments_modified_by_id_793521b5_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_appointmentsmodel
    ADD CONSTRAINT account_appointments_modified_by_id_793521b5_fk_account_a FOREIGN KEY (modified_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_appointmentservicemodel account_appointments_modified_by_id_f175fd02_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_appointmentservicemodel
    ADD CONSTRAINT account_appointments_modified_by_id_f175fd02_fk_account_a FOREIGN KEY (modified_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_appointmentsmodel account_appointments_patient_id_8072c842_fk_account_p; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_appointmentsmodel
    ADD CONSTRAINT account_appointments_patient_id_8072c842_fk_account_p FOREIGN KEY (patient_id) REFERENCES public.account_patientmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_appointmentsmodel account_appointments_referring_doctor_id_d4e4c12a_fk_account_r; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_appointmentsmodel
    ADD CONSTRAINT account_appointments_referring_doctor_id_d4e4c12a_fk_account_r FOREIGN KEY (referring_doctor_id) REFERENCES public.account_referringdoctormodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_appointmentservicemodel account_appointments_service_id_dc575559_fk_account_m; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_appointmentservicemodel
    ADD CONSTRAINT account_appointments_service_id_dc575559_fk_account_m FOREIGN KEY (service_id) REFERENCES public.account_medicalservice(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_attendancemodel account_attendancemodel_staff_id_f0a5937a_fk_account_account_id; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_attendancemodel
    ADD CONSTRAINT account_attendancemodel_staff_id_f0a5937a_fk_account_account_id FOREIGN KEY (staff_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_branchmodel account_branchmodel_created_by_id_1405fc7c_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_branchmodel
    ADD CONSTRAINT account_branchmodel_created_by_id_1405fc7c_fk_account_a FOREIGN KEY (created_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_branchmodel account_branchmodel_modified_by_id_37e59bd1_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_branchmodel
    ADD CONSTRAINT account_branchmodel_modified_by_id_37e59bd1_fk_account_a FOREIGN KEY (modified_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_branchmodel account_branchmodel_organization_id_b15d9044_fk_account_o; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_branchmodel
    ADD CONSTRAINT account_branchmodel_organization_id_b15d9044_fk_account_o FOREIGN KEY (organization_id) REFERENCES public.account_organizationmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_doctoraccountmodel account_doctoraccoun_doctor_id_936e4f7e_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_doctoraccountmodel
    ADD CONSTRAINT account_doctoraccoun_doctor_id_936e4f7e_fk_account_a FOREIGN KEY (doctor_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_doctorspecialitymodel account_doctorspecia_branch_id_da287079_fk_account_b; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_doctorspecialitymodel
    ADD CONSTRAINT account_doctorspecia_branch_id_da287079_fk_account_b FOREIGN KEY (branch_id) REFERENCES public.account_branchmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_doctorspecialitymodel account_doctorspecia_created_by_id_5a0144e6_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_doctorspecialitymodel
    ADD CONSTRAINT account_doctorspecia_created_by_id_5a0144e6_fk_account_a FOREIGN KEY (created_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_doctorspecialitymodel account_doctorspecia_doctor_id_f1cd2d2d_fk_account_d; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_doctorspecialitymodel
    ADD CONSTRAINT account_doctorspecia_doctor_id_f1cd2d2d_fk_account_d FOREIGN KEY (doctor_id) REFERENCES public.account_doctoraccountmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_doctorspecialitymodel account_doctorspecia_modified_by_id_fcd7f6c2_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_doctorspecialitymodel
    ADD CONSTRAINT account_doctorspecia_modified_by_id_fcd7f6c2_fk_account_a FOREIGN KEY (modified_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_doctorspecialitymodel account_doctorspecia_organization_id_caf065e3_fk_account_o; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_doctorspecialitymodel
    ADD CONSTRAINT account_doctorspecia_organization_id_caf065e3_fk_account_o FOREIGN KEY (organization_id) REFERENCES public.account_organizationmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_doctorspecialitymodel account_doctorspecia_speciality_id_457be40d_fk_account_s; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_doctorspecialitymodel
    ADD CONSTRAINT account_doctorspecia_speciality_id_457be40d_fk_account_s FOREIGN KEY (speciality_id) REFERENCES public.account_specialitymodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_emcdocumentmodel account_emcdocumentm_appointment_id_bd1d58be_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_emcdocumentmodel
    ADD CONSTRAINT account_emcdocumentm_appointment_id_bd1d58be_fk_account_a FOREIGN KEY (appointment_id) REFERENCES public.account_appointmentsmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_emcdocumentmodel account_emcdocumentm_created_by_id_e147f8ab_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_emcdocumentmodel
    ADD CONSTRAINT account_emcdocumentm_created_by_id_e147f8ab_fk_account_a FOREIGN KEY (created_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_emcdocumentmodel account_emcdocumentm_modified_by_id_e41e04f6_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_emcdocumentmodel
    ADD CONSTRAINT account_emcdocumentm_modified_by_id_e41e04f6_fk_account_a FOREIGN KEY (modified_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_emcdocumentmodel account_emcdocumentm_patient_id_9be9fe01_fk_account_p; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_emcdocumentmodel
    ADD CONSTRAINT account_emcdocumentm_patient_id_9be9fe01_fk_account_p FOREIGN KEY (patient_id) REFERENCES public.account_patientmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_emcdocumentmodel account_emcdocumentm_service_id_c81cfc36_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_emcdocumentmodel
    ADD CONSTRAINT account_emcdocumentm_service_id_c81cfc36_fk_account_a FOREIGN KEY (service_id) REFERENCES public.account_appointmentservicemodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_informationsourcemodel account_informations_created_by_id_c0a8b90f_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_informationsourcemodel
    ADD CONSTRAINT account_informations_created_by_id_c0a8b90f_fk_account_a FOREIGN KEY (created_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_informationsourcemodel account_informations_modified_by_id_981deaec_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_informationsourcemodel
    ADD CONSTRAINT account_informations_modified_by_id_981deaec_fk_account_a FOREIGN KEY (modified_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_informationsourcemodel account_informations_organization_id_55be1d2b_fk_account_o; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_informationsourcemodel
    ADD CONSTRAINT account_informations_organization_id_55be1d2b_fk_account_o FOREIGN KEY (organization_id) REFERENCES public.account_organizationmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_medicalservice account_medicalservi_branch_id_5127a4ec_fk_account_b; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_medicalservice
    ADD CONSTRAINT account_medicalservi_branch_id_5127a4ec_fk_account_b FOREIGN KEY (branch_id) REFERENCES public.account_branchmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_medicalservice account_medicalservi_created_by_id_552434ac_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_medicalservice
    ADD CONSTRAINT account_medicalservi_created_by_id_552434ac_fk_account_a FOREIGN KEY (created_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_medicalservice_doctor account_medicalservi_doctoraccountmodel_i_c1a7f3de_fk_account_d; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_medicalservice_doctor
    ADD CONSTRAINT account_medicalservi_doctoraccountmodel_i_c1a7f3de_fk_account_d FOREIGN KEY (doctoraccountmodel_id) REFERENCES public.account_doctoraccountmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_medicalservice_doctor account_medicalservi_medicalservice_id_558a5687_fk_account_m; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_medicalservice_doctor
    ADD CONSTRAINT account_medicalservi_medicalservice_id_558a5687_fk_account_m FOREIGN KEY (medicalservice_id) REFERENCES public.account_medicalservice(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_medicalservice account_medicalservi_modified_by_id_952287d5_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_medicalservice
    ADD CONSTRAINT account_medicalservi_modified_by_id_952287d5_fk_account_a FOREIGN KEY (modified_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_medicalservice account_medicalservi_speciality_id_b51d5725_fk_account_s; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_medicalservice
    ADD CONSTRAINT account_medicalservi_speciality_id_b51d5725_fk_account_s FOREIGN KEY (speciality_id) REFERENCES public.account_specialitymodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_organizationmodel account_organization_created_by_id_8813ba33_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_organizationmodel
    ADD CONSTRAINT account_organization_created_by_id_8813ba33_fk_account_a FOREIGN KEY (created_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_organizationmodel account_organization_modified_by_id_3a70987c_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_organizationmodel
    ADD CONSTRAINT account_organization_modified_by_id_3a70987c_fk_account_a FOREIGN KEY (modified_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_patientgroupmodel account_patientgroup_created_by_id_654e1e76_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_patientgroupmodel
    ADD CONSTRAINT account_patientgroup_created_by_id_654e1e76_fk_account_a FOREIGN KEY (created_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_patientgroupmodel account_patientgroup_modified_by_id_509edc05_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_patientgroupmodel
    ADD CONSTRAINT account_patientgroup_modified_by_id_509edc05_fk_account_a FOREIGN KEY (modified_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_patientgroupmodel account_patientgroup_organization_id_078ae6c5_fk_account_o; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_patientgroupmodel
    ADD CONSTRAINT account_patientgroup_organization_id_078ae6c5_fk_account_o FOREIGN KEY (organization_id) REFERENCES public.account_organizationmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_patientmodel account_patientmodel_created_by_id_1b0b2595_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_patientmodel
    ADD CONSTRAINT account_patientmodel_created_by_id_1b0b2595_fk_account_a FOREIGN KEY (created_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_patientmodel account_patientmodel_information_source_i_a123e98f_fk_account_i; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_patientmodel
    ADD CONSTRAINT account_patientmodel_information_source_i_a123e98f_fk_account_i FOREIGN KEY (information_source_id) REFERENCES public.account_informationsourcemodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_patientmodel account_patientmodel_modified_by_id_20085674_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_patientmodel
    ADD CONSTRAINT account_patientmodel_modified_by_id_20085674_fk_account_a FOREIGN KEY (modified_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_patientmodel account_patientmodel_organization_id_c4d750e6_fk_account_o; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_patientmodel
    ADD CONSTRAINT account_patientmodel_organization_id_c4d750e6_fk_account_o FOREIGN KEY (organization_id) REFERENCES public.account_organizationmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_patientmodel_patient_group account_patientmodel_patientgroupmodel_id_21677d95_fk_account_p; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_patientmodel_patient_group
    ADD CONSTRAINT account_patientmodel_patientgroupmodel_id_21677d95_fk_account_p FOREIGN KEY (patientgroupmodel_id) REFERENCES public.account_patientgroupmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_patientmodel_patient_group account_patientmodel_patientmodel_id_e53c1730_fk_account_p; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_patientmodel_patient_group
    ADD CONSTRAINT account_patientmodel_patientmodel_id_e53c1730_fk_account_p FOREIGN KEY (patientmodel_id) REFERENCES public.account_patientmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_referringdoctormodel account_referringdoc_created_by_id_fe0a3ec4_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_referringdoctormodel
    ADD CONSTRAINT account_referringdoc_created_by_id_fe0a3ec4_fk_account_a FOREIGN KEY (created_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_referringdoctormodel account_referringdoc_modified_by_id_fda5f1d2_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_referringdoctormodel
    ADD CONSTRAINT account_referringdoc_modified_by_id_fda5f1d2_fk_account_a FOREIGN KEY (modified_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_rolepermissionmodel account_rolepermissi_permission_id_57cada6c_fk_account_p; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_rolepermissionmodel
    ADD CONSTRAINT account_rolepermissi_permission_id_57cada6c_fk_account_p FOREIGN KEY (permission_id) REFERENCES public.account_permissionsmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_rolepermissionmodel account_rolepermissi_role_id_51569830_fk_account_r; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_rolepermissionmodel
    ADD CONSTRAINT account_rolepermissi_role_id_51569830_fk_account_r FOREIGN KEY (role_id) REFERENCES public.account_rolesmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_specialitymodel account_specialitymo_branch_id_cac642b1_fk_account_b; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_specialitymodel
    ADD CONSTRAINT account_specialitymo_branch_id_cac642b1_fk_account_b FOREIGN KEY (branch_id) REFERENCES public.account_branchmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_specialitymodel account_specialitymo_created_by_id_f735d5d1_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_specialitymodel
    ADD CONSTRAINT account_specialitymo_created_by_id_f735d5d1_fk_account_a FOREIGN KEY (created_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_specialitymodel account_specialitymo_modified_by_id_91cb8351_fk_account_a; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_specialitymodel
    ADD CONSTRAINT account_specialitymo_modified_by_id_91cb8351_fk_account_a FOREIGN KEY (modified_by_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_specialitymodel account_specialitymo_organization_id_9a98d939_fk_account_o; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.account_specialitymodel
    ADD CONSTRAINT account_specialitymo_organization_id_9a98d939_fk_account_o FOREIGN KEY (organization_id) REFERENCES public.account_organizationmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_account_account_id; Type: FK CONSTRAINT; Schema: public; Owner: hayat
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_account_account_id FOREIGN KEY (user_id) REFERENCES public.account_account(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

--
-- Database "postgres" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 14.0 (Debian 14.0-1.pgdg110+1)
-- Dumped by pg_dump version 14.0 (Debian 14.0-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE postgres;
--
-- Name: postgres; Type: DATABASE; Schema: -; Owner: hayat
--

CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE postgres OWNER TO hayat;

\connect postgres

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE postgres; Type: COMMENT; Schema: -; Owner: hayat
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database cluster dump complete
--

