import Login from "../views/registaration/Login";
import Test2 from "../views/registaration/test2";
import Test from "../views/registaration/test";
import React, {ReactElement} from "react";
import MainIndex from "../views/main";
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

type IRouting = {
    path: string;
    component: ReactElement,
    global?: boolean
}

type MyGroupType = {
    [key:string]: Array<IRouting>;
}

interface INav {
    button: string;
    title?: string;

    dropdown?: Array<{
        img: typeof CalendarEdit;
        text: string;
        sideBarText?: string;
    }>
}

export const RoutingData: MyGroupType = {
    "NoAuth": [
        {
            "path": "/login",
            "component": <Login />,
            "global": true,
        },
        {
            "path": "/test2",
            "component": <Test2 />,
        }
    ],
    "test": [
        {
            "path": "/test",
            "component": <MainIndex />,
            "global": true,
        },
        {
            "path": "/test2",
            "component": <Test2 />,
        }
    ]
};

export const NavBarDropdowns:Array<INav> = [
    {
        button: "Регистратура",
        title: "Регистратура",
        dropdown: [
            {
                img: <CalendarEdit />,
                text: "Расписания врачей",
                sideBarText: "Расписания <br> врачей"
            },
            {
                img: <FolderAdd />,
                text: "Добавить пакет",
                sideBarText: "Добавить <br> пакет"
            },
            {
                img: <Note />,
                text: "Добавить группу приемов",
                sideBarText: "Добавить <br> группу приемов"
            },
            {
                img: <ProfileUser />,
                text: "Справочник пациентов",
                sideBarText: "Справочник <br> пациентов"
            },
        ]
    },
    {
        button: "Кассовые операции",
        title: "Касса",
        dropdown: [
            {
                img: <Moneys />,
                text: "Касса"
            },
            {
                img: <ProfileMoney />,
                text: "Оплаты по пациентам"
            },
            {
                img: <LockArrow />,
                text: "История закрытий"
            },
            {
                img: <Bill />,
                text: "Мемордера"
            },
            {
                img: <MoneyTime />,
                text: "Должники"
            },
            {
                img: <ClipboardClose />,
                text: "Быстрая запись"
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
                img: <Clients />,
                text: "Клиенты"
            },
            {
                img: <UserSquare />,
                text: "Группа клиентов"
            },
            {
                img: <ScanBarcode />,
                text: "Промокоды"
            }
        ]
    },
    {
        button: "Утилиты",
        title: "Утилиты",
        dropdown: [
            {
                img: <People />,
                text: "Слияние пациентов"
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