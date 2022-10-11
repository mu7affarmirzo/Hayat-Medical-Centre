import {makeAutoObservable} from "mobx";

interface IEvent {
    end: Date;
    start: Date;
    title: string;
    id: number;
    allDay?: boolean;
    resource?: any;
    doctorsId?: string;
}

class CalendarEvents {
    events: Array<IEvent> = [
        {
            id: 1,
            title: "Лебедев Сергей Васильевич",
            start: new Date(2022, 9, new Date().getDate(), 15),
            end: new Date(2022, 9, new Date().getDate(), 16),
        },
        {
            id: 2,
            title: "Мария Морозова",
            start: new Date(2022, 9, new Date().getDate(), 10, 30),
            end: new Date(2022, 9, new Date().getDate(), 12),
        },
        {
            id: 3,
            title: "Мария Морозова2",
            start: new Date(2022, 9, new Date().getDate(), 9),
            end: new Date(2022, 9, new Date().getDate(), 10),
        },
        {
            id: 4,
            title: "Мария Морозова3",
            start: new Date(2022, 9, new Date().getDate(), 8),
            end: new Date(2022, 9, new Date().getDate(), 9),
        },
        {
            id: 5,
            title: "Мария asdsadsa",
            start: new Date(2022, 9, new Date().getDate(), 10),
            end: new Date(2022, 9, new Date().getDate(), 12),
        },
        {
            id: 6,
            title: "Мария Морозова5",
            doctorsId: "113",
            start: new Date(2022, 9, new Date().getDate(), 10),
            end: new Date(2022, 9, new Date().getDate(), 12),
        },
        {
            id: 6,
            title: "Мария Морозова6",
            start: new Date(2022, 9, new Date().getDate(), 10),
            end: new Date(2022, 9, new Date().getDate(), 12),
        },
        {
            id: 6,
            title: "Мария Морозова7",
            doctorsId: "112",
            start: new Date(2022, 9, new Date().getDate(), 10),
            end: new Date(2022, 9, new Date().getDate(), 12),
        },
        {
            id: 6,
            title: "Мария Морозова8",
            start: new Date(2022, 9, new Date().getDate(), 10),
            end: new Date(2022, 9, new Date().getDate(), 12),
        },
        {
            id: 7,
            title: "Some test ",
            start: new Date(2022, 8, 28, 10),
            end: new Date(2022, 8, 28, 12),
        },
        {
            id: 7,
            title: "Some test ",
            doctorsId: "112",
            start: new Date(2022, 8, 28, 10),
            end: new Date(2022, 8, 28, 12),
        },
        {
            id: 7,
            title: "Some test 2",
            start: new Date(2022, 9, 7, 10),
            end: new Date(2022, 9, 7, 12),
        }
    ];

    eventsCopy: Array<IEvent> = this.events.concat();

    constructor() {
        makeAutoObservable(this);
    }

    addEvent (data: IEvent) {
        this.events.push(data)
    }

    filterEventById (id: string) {
        this.eventsCopy = this.events.filter(item => item.doctorsId === id);
    }

}

export default new CalendarEvents();