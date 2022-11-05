import React from "react";
import {ReactComponent as CalendarEdit} from "../assets/img/header_icons/calendar-edit.svg";
import {ReactComponent as FolderAdd} from "../assets/img/header_icons/folder-add.svg";
import {ReactComponent as Note} from "../assets/img/header_icons/note.svg";
import {ReactComponent as ProfileUser} from "../assets/img/header_icons/profile-2user.svg";
import {ReactComponent as Moneys} from "../assets/img/header_icons/moneys.svg";
import {ReactComponent as ProfileMoney} from "../assets/img/header_icons/profile-money.svg";
import {ReactComponent as LockArrow} from "../assets/img/header_icons/lock.svg";
import {ReactComponent as Bill} from "../assets/img/header_icons/bill.svg";
import {ReactComponent as MoneyTime} from "../assets/img/header_icons/money-time.svg";
import {ReactComponent as ClipboardClose} from "../assets/img/header_icons/clipboard-close.svg";
import {ReactComponent as People} from "../assets/img/header_icons/people.svg";
import {ReactComponent as Clients} from "../assets/img/header_icons/clients.svg";
import {ReactComponent as UserSquare} from "../assets/img/header_icons/user-square.svg";
import {ReactComponent as ScanBarcode} from "../assets/img/header_icons/scan-barcode.svg";

interface INav {
    button: string;
    title?: string;

    dropdown?: Array<{
        img: typeof CalendarEdit;
        text: string;
        sideBarText?: string;
        active?: boolean,
        path: string
    }>
}

export const NavBarDropdowns: Array<INav> = [
    {
        button: "Регистратура",
        title: "Регистратура",
        dropdown: [
            {
                img: <CalendarEdit/>,
                text: "Расписания врачей",
                sideBarText: "Расписания <br> врачей",
                active: true,
                path: "/main"
            },
            {
                img: <FolderAdd/>,
                text: "Добавить пакет",
                sideBarText: "Добавить <br> пакет",
                path: ""
            },
            {
                img: <Note/>,
                text: "Добавить группу приемов",
                sideBarText: "Добавить <br> группу приемов",
                path: " "
            },
            {
                img: <ProfileUser/>,
                text: "Справочник пациентов",
                sideBarText: "Справочник <br> пациентов",
                path: "/patientsDirectory"
            },
        ]
    },
    {
        button: "Кассовые операции",
        title: "Касса",
        dropdown: [
            {
                img: <Moneys/>,
                text: "Касса",
                path: ""
            },
            {
                img: <ProfileMoney/>,
                text: "Оплаты по пациентам",
                path: ""
            },
            {
                img: <LockArrow/>,
                text: "История закрытий",
                path: ""
            },
            {
                img: <Bill/>,
                text: "Мемордера",
                path: ""
            },
            {
                img: <MoneyTime/>,
                text: "Должники",
                path: ""
            },
            {
                img: <ClipboardClose/>,
                text: "Быстрая запись",
                path: ""
            },
        ]
    },
    {
        button: "Стационар"
    },
    {
        button: "Справочники",
        title: "Справочники",
        dropdown: [
            {
                img: <Clients/>,
                text: "Клиенты",
                path: ""
            },
            {
                img: <UserSquare/>,
                text: "Группа клиентов",
                path: ""
            },
            {
                img: <ScanBarcode/>,
                text: "Промокоды",
                path: ""
            }
        ]
    },
    {
        button: "Утилиты",
        title: "Утилиты",
        dropdown: [
            {
                img: <People/>,
                text: "Слияние пациентов",
                path: ""
            }
        ]
    },
    {
        button: "Телефония"
    },
    {
        button: "Телефония"
    },

]