import React from "react";
import { ReactComponent as CalendarEdit } from "../assets/img/header_icons/calendar-edit.svg";
import { ReactComponent as FolderAdd } from "../assets/img/header_icons/folder-add.svg";
import { ReactComponent as Note } from "../assets/img/header_icons/note.svg";
import { ReactComponent as ProfileUser } from "../assets/img/header_icons/profile-2user.svg";
import { ReactComponent as Moneys } from "../assets/img/header_icons/moneys.svg";
import { ReactComponent as ProfileMoney } from "../assets/img/header_icons/profile-money.svg";
import { ReactComponent as LockArrow } from "../assets/img/header_icons/lock.svg";
import { ReactComponent as ClipboardClose } from "../assets/img/header_icons/clipboard-close.svg";
import { ReactComponent as People } from "../assets/img/header_icons/people.svg";
import { ReactComponent as Clients } from "../assets/img/header_icons/clients.svg";
import { ReactComponent as UserSquare } from "../assets/img/header_icons/user-square.svg";
import { ReactComponent as ScanBarcode } from "../assets/img/header_icons/scan-barcode.svg";
import { ReactComponent as Exchange } from "../assets/img/exchange-card.svg";
import { ReactComponent as CreateNote } from "../assets/img/create-note.svg";
import { ReactComponent as Printer } from "../assets/img/printer.svg";
import { ReactComponent as Bookmark } from "../assets/img/bookmark.svg";
import { ReactComponent as Checklist } from "../assets/img/checklist.svg";
import { ReactComponent as Wallet } from "../assets/img/wallet.svg";

interface INav {
    button: string;
    title?: string;

    dropdown?: Array<{
        img: typeof CalendarEdit;
        text: string;
        sideBarText?: string;
        active?: boolean;
        path: string;
    }>;
}

export const NavBarDropdowns: Array<INav> = [
    {
        button: "Регистратура",
        title: "Регистратура",
        dropdown: [
            {
                img: <CalendarEdit />,
                text: "Расписания врачей",
                sideBarText: "Расписания <br> врачей",
                active: true,
                path: "/main",
            },
            {
                img: <FolderAdd />,
                text: "Добавить пакет",
                sideBarText: "Добавить <br> пакет",
                path: "",
            },
            {
                img: <Note />,
                text: "Добавить группу приемов",
                sideBarText: "Добавить <br> группу приемов",
                path: "/groupAppointment",
            },
            {
                img: <ProfileUser />,
                text: "Справочник пациентов",
                sideBarText: "Справочник <br> пациентов",
                path: "/patientsDirectory",
            },
        ],
    },
    {
        button: "Кассовые операции",
        title: "Касса",
        dropdown: [
            {
                img: <Moneys />,
                text: "Касса",
                sideBarText: 'Касса',
                path: "/cashbox",
            },
            {
                img: <ProfileMoney />,
                text: "Оплаты по пациентам",
                sideBarText: "Оплаты по пациентам",
                path: "/patientPayments",
            },
            {
                img: <LockArrow />,
                text: "История закрытий",
                sideBarText: "История закрытий",
                path: "/historyPayments",
            },
            {
                img: <ClipboardClose />,
                text: "Быстрая запись",
                path: "/quickAppointment",
                sideBarText: "Быстрая запись"
            },
        ],
    },
    // {
    //     button: "Стационар",
    // },
    {
        button: "Справочники",
        title: "Справочники",
        dropdown: [
            {
                img: <Clients />,
                text: "Клиенты",
                path: "",
            },
            {
                img: <UserSquare />,
                text: "Группа клиентов",
                path: "",
            },
            {
                img: <ScanBarcode />,
                text: "Промокоды",
                path: "",
            },
        ],
    },
    {
        button: "Утилиты",
        title: "Утилиты",
        dropdown: [
            {
                img: <People />,
                text: "Слияние пациентов",
                path: "/merge-patients",
            },
        ],
    },
    {
        button: "Настройки",
    },
        // {
        //     button: "Телефония",
        // },
];
export const CashBoxDropdowns: Array<INav> = [
    {
        button: "Регистратура",
        title: "Регистратура",
        dropdown: [
            {
                img: <CalendarEdit />,
                text: "Расписания врачей",
                sideBarText: "Расписания <br> врачей",
                active: true,
                path: "/main",
            },
            {
                img: <Checklist />,
                text: "Реестр посещений  ",
                sideBarText: "Реестр <br/>посещений  ",
                path: "/registeryVisits",
            },
            {
                img: <Wallet />,
                text: "Реестр счетов ",
                sideBarText: "Реестр счетов ",
                path: "/registeryAccounts",
            },
        ],
    },
    {
        button: "Кассовые операции",
        title: "Касса",
        dropdown: [
            {
                img: <Moneys />,
                text: "Касса",
                path: "/cashbox",
                sideBarText: 'Касса'
            },
            {
                img: <ProfileMoney />,
                text: "Оплаты по пациентам",
                sideBarText: "Оплаты по пациентам",
                path: "/patientPayments",
            },
            {
                img: <LockArrow />,
                text: "История закрытий",
                sideBarText: "История закрытий",
                path: "/historyPayments",
            },
            {
                img: <ClipboardClose />,
                text: "Быстрая запись",
                sideBarText: "Быстрая запись",
                path: "",
            },
        ],
    },
    {
        button: "Отчёты",
        title: "Отчёты",
        dropdown: [
            {
                img: <Note />,
                text: "По кассовым операциям",
                sideBarText: "По кассовым операциям",
                path: "/reports",
            },
            {
                img: <Note />,
                text: "По клиентским скидкам",
                sideBarText: "По клиентским скидкам",
                path: "/patientSale",
            },
            {
                img: <Note />,
                text: "По перенаправленным приёмам",
                path: "/patientSale",
            },
            {
                img: <Note />,
                text: "По пациенту возврата",
                path: "/patientSale",
            },
        ],
    },
];

export const CASHIER_ACTIONS = [
    {
        title: "Взаимарасчёт",
        img: <Exchange />,
    },
    {
        title: "Редактировать прием",
        img: <CreateNote />,
    },
    {
        title: "Печать бланка",
        img: <Printer />,
    },
    {
        title: "Печать счёта",
        img: <Bookmark />,
    },
];
