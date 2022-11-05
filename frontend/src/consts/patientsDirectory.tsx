import React from "react";
import { ReactComponent as CalendarEdit } from "../assets/img/header_icons/calendar-edit.svg";
import { ReactComponent as CloseCircle } from "../assets/img/close-circle.svg";

interface IPatientDirectory {
    type: string;
    label: string;
    child?: Array<{
        name: string
        value: string
    }>
}
interface DirectoryActions {
    icon: typeof CalendarEdit;
    text: string;
    dataset: string
}

export const PatientsDirectoryNav: Array<IPatientDirectory> = [
    {
        type: "text",
        label: "ФИО",
    },
    {
        type: "number",
        label: "ИНН",
    },
    {
        type: "number",
        label: "№ медкарты",
    },
    {
        type: "number",
        label: "№ документа",
    },
    {
        type: "number",
        label: "Моб. телефон",
    },
    {
        type: "email",
        label: "Эл. почта",
    },
    {
        type: "select",
        label: "Дата рождения",
        child: [
            {
                name: '',
                value: ''
            }
        ]
    },
    {
        type: "select",
        label: "Дата регистрации",
        child: [
            {
                name: '',
                value: ''
            }
        ]
    },
    {
        type: "select",
        label: "Регистратор",
        child: [
            {
                name: 'Sardor Akbarov',
                value: 'Sardor-Akbarov'
            },
            {
                name: 'Sardor Akbarov',
                value: 'Sardor-Akbarov'
            },
        ]
    },
];
export const PatientsDirectoryActions: Array<DirectoryActions> = [
    {
        icon: <CalendarEdit />,
        text: "Добавить",
        dataset: 'add'
    },
    {
        icon: <CalendarEdit />,
        text: "Редактировать",
        dataset: 'edit'
    },
    {
        icon: <CloseCircle />,
        text: "Удалить",
        dataset: 'remove'
    },
];
export const PatientsDirectoryEditActions: Array<DirectoryActions> = [
    {
        icon: <CalendarEdit />,
        text: "Добавить",
        dataset: 'add'
    },

    {
        icon: <CloseCircle />,
        text: "Отмена",
        dataset: 'remove'
    },
];
