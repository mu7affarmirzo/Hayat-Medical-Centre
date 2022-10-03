import {makeAutoObservable} from "mobx";

interface IEvent {
    end: Date;
    start: Date;
    title: string;
    id: number;
    allDay?: boolean;
    resource?: any;
}

class CalendarEvents {
    events: Array<IEvent> = [
        {
            id: 1,
            title: "Лебедев Сергей Васильевич",
            start: new Date(2022, 9, 3, 15),
            end: new Date(2022, 9, 3, 16),
        },
        {
            id: 2,
            title: "Мария Морозова",
            start: new Date(2022, 9, 3, 10, 30),
            end: new Date(2022, 9, 3, 12),
        },
        {
            id: 3,
            title: "Мария Морозова2",
            start: new Date(2022, 9, 3, 9),
            end: new Date(2022, 9, 3, 10),
        },
        {
            id: 4,
            title: "Мария Морозова3",
            start: new Date(2022, 9, 3, 8),
            end: new Date(2022, 9, 3, 9),
        },
        {
            id: 5,
            title: "Мария Морозова4",
            start: new Date(2022, 9, 3, 10),
            end: new Date(2022, 9, 3, 12),
        },
        {
            id: 6,
            title: "Мария Морозова5",
            start: new Date(2022, 9, 3, 10),
            end: new Date(2022, 9, 3, 12),
        },
        {
            id: 6,
            title: "Мария Морозова6",
            start: new Date(2022, 9, 3, 10),
            end: new Date(2022, 9, 3, 12),
        },
        {
            id: 6,
            title: "Мария Морозова7",
            start: new Date(2022, 9, 3, 10),
            end: new Date(2022, 9, 3, 12),
        },
        {
            id: 6,
            title: "Мария Морозова8",
            start: new Date(2022, 9, 3, 10),
            end: new Date(2022, 9, 3, 12),
        },
        {
            id: 7,
            title: "Some test ",
            start: new Date(2022, 8, 28, 10),
            end: new Date(2022, 8, 28, 12),
        }
    ];

    constructor() {
        makeAutoObservable(this);
    }

    addEvent (data: IEvent) {
        this.events.push(data)
    }

}

export default new CalendarEvents();