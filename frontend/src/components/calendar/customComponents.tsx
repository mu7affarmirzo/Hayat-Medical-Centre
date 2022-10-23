import React, {useCallback, useEffect, useState} from "react";
import styles from "./calendar.module.scss"
import moment from "moment";
import 'moment/locale/ru'
import {observer, useLocalObservable} from "mobx-react-lite";
import DoctorStateKeeper from "../../store/DoctorStateKeeper";
import {CalendarEventStateKeeper} from "../../store";

const ToolBarView = (data) => {
    const calendarEventsStateKeeper = useLocalObservable(() => CalendarEventStateKeeper.instance);
    const {addViewAction} = calendarEventsStateKeeper;

    const changeActiveTime = useCallback(() => {
        let activeTime: any = document.querySelector(".calendar_block .week_time_block.active_time");
        if (activeTime?.dataset?.timehour !== String(new Date().getHours())) {
            activeTime.classList.remove("active_time")
            activeTime.parentElement.nextElementSibling.querySelector(".week_time_block ").classList.add("active_time");
        }
    }, [])

    useEffect(() => {
        let timeOut, timeInterval;
        const activeDataElem: HTMLElement | null = document.querySelector(".rbc-day-slot.rbc-time-column.rbc-now.rbc-today");
        const activeButton = document.querySelector(".month_buttons_block .month_buttons.month_button_active");

        if(activeButton && activeButton.getAttribute("data-type") !== data.view){
            data.onView(activeButton.getAttribute("data-type"));
        }

        if(activeButton?.getAttribute("data-type") === "day"){
            document.querySelectorAll(".calendar_block .rbc-time-view .rbc-time-content .rbc-day-slot.rbc-today").forEach((item: any) => item.style.backgroundColor = "#fff")
            document.querySelectorAll(".calendar_block .rbc-time-view .rbc-time-header").forEach((item: any) => item.style.display = "none")
        }

        addViewAction(data.onView)

        // if (data.view !== active) {
        //     setActive(data.view)
        // }

        if (data.view === "day") {
            activeDataElem?.classList?.add("day_view_mode")
        } else {
            activeDataElem?.classList?.remove("day_view_mode")
        }

        if (data.view !== "month") {
            let timeArray = document.querySelectorAll(".calendar_block .week_time_block");

            timeArray.forEach((item: any) => {
                if (item?.dataset?.timehour === String(new Date().getHours())) {
                    item.classList.add("active_time")
                }
            });
            timeOut = setTimeout(() => {
                changeActiveTime();
                timeInterval = setInterval(changeActiveTime, 1000 * 60 * 60);
            }, (1000 * 60) * (60 - (new Date().getMinutes())))
        } else {
            clearTimeout(timeOut);
            clearInterval(timeInterval);
        }


        return () => {
            clearTimeout(timeOut);
            clearInterval(timeInterval);
        }
    }, [data.view])

    return (
        <></>
    );
}

const MonthHeaderView = (data) => {
    console.log(data, "MonthHeaderView")
    return (
        <>
            <div
                className={`month_name_block ${styles.month_name}`}>{new Date(data.date).toLocaleDateString("ru", {weekday: 'short'})}</div>
        </>
    )
};

const MonthNumberView = (data) => (
    <>
        <div className={`month_number ${styles.month_number}`}>{new Date(data.date).getDate()}</div>
    </>
);

const WeekHeaderView = (data) => {
    const converDate = () => {
        let _date = new Date(data.date);
        let [month, weekDay] = _date.toLocaleDateString("ru", {month: 'short', weekday: 'short'}).split(" ");
        return `${weekDay} | ${_date.getDate()} ${month}`
    }

    useEffect(() => {
        let a: any = document.querySelectorAll(".calendar_block .rbc-time-header .rbc-time-header-content .rbc-allday-cell");
        a.length && a.forEach(item => item.style.display = "none");
    }, [])

    return (
        <>
            <div className={`week_name_block ${styles.weeks_name}`}>{converDate()}</div>
        </>
    )
};

const TimeSlotView = (data) => {
    let date = new Date(data.value);

    if (data.children?.props?.children?.props?.children) {
        return (
            <div className={`week_time_block ${styles.week_time_wrapper}`} data-timehour={String(date.getHours())}>
                <div className={styles.hour}>{date.getHours()}</div>
                <div className={`calendar_minutes ${styles.minutes_block}`}>
                    <div className={styles.minutes_item}>00</div>
                    <div className={styles.minutes_item}>30</div>
                </div>
            </div>
        )
    } else {
        return (
            <div className={`week_days_box ${styles.week_days_box}`}></div>
        )
    }
}

const EventWrapperView = observer((data: any) => {
    const [offsetTop, setOffsetTop] = useState<number>(0);
    const [viewMode, setViewMode] = useState<any>("");


    useEffect(() => {
        let hourBlock = document.querySelector(`.rbc-timeslot-group .week_time_block[data-timehour="${data.event.start.getHours()}"]`);
        let activeButton = document.querySelector(".month_buttons_block .month_buttons.month_button_active");
        setViewMode(activeButton?.getAttribute("data-type"))

        if (viewMode === "day") {
            let EventsList = Array.from(document.querySelectorAll(".calendar_block .rbc-time-view .rbc-time-content .rbc-day-slot .rbc-events-container .event_wrapper_block"))
                .map(item => ({
                    [item?.getAttribute("data-test") || ""]: item
                }));
            let store: Array<any> = [];

            EventsList.forEach((item, i, array) => {
                let key = Object.keys(item)[0];

                let sameElems = array.filter(item2 => Object.keys(item2)[0] === key)

                if (sameElems.length > 1) {
                    store.push(sameElems)
                }

            });
            store.forEach(item => {
                if (item.length > 4) {
                    document.querySelectorAll(".rbc-time-content .rbc-day-slot.rbc-time-column .rbc-timeslot-group")
                        .forEach((_item: any) => _item.style.width = (280 * item.length) + "px");
                }

                item.forEach((item2, i, arr) => {
                    let eventElem: any = Object.values(item2)[0];
                    if (eventElem && eventElem?.style) {
                        eventElem.style.width = `calc(${100 / (arr.length > 4 ? 4 : arr.length)}% - ${(i === 0 || i === (arr.length - 1)) ? "5px" : "10px"})`;
                        eventElem.style.left = `calc(${(i * (100 / (arr.length > 4 ? 4 : arr.length)))}% + ${i === 0 ? "0" : "5px"})`;
                    }
                })
            })
        } else if (viewMode === "month") {
            let eventsList: Array<Element> = Array.from(document.querySelectorAll(".rbc-row-content .rbc-row")).filter(item => Boolean(item.querySelector(".rbc-row-segment")));
            const getNumber = (str: string | null): string => {
                if (str) {
                    const regExp: RegExp = /\d/g;
                    let matchedSymbols = str.match(regExp);
                    if (matchedSymbols && matchedSymbols.length >= 1) {
                        return matchedSymbols.join("");
                    }
                }

                return "0";
            }

            eventsList.forEach(item => {
                let segmentButton: any = item.querySelector(".rbc-row-segment button.rbc-button-link.rbc-show-more");
                if (segmentButton) {
                    let rowSegment = segmentButton.parentElement;
                    let date = rowSegment?.parentElement?.previousElementSibling?.querySelector(".event_wrapper_block")?.getAttribute("data-date");
                    segmentButton.parentElement.innerHTML = `<div  data-date=${date} class="event_wrapper_block  event_block_couter ${styles.event_wrapper}">
                                                                <span id="events_number">${getNumber(segmentButton?.textContent)}</span>+ записей
                                                            </div>`
                }
            })
        } else if (viewMode === "week") {
            let EventsList = Array.from(document.querySelectorAll(".calendar_block .rbc-time-view .rbc-time-content .rbc-day-slot .rbc-events-container .event_wrapper_block"))
                .map(item => ({
                    [item?.getAttribute("data-test") || ""]: item
                }));
            let store: Array<any> = [];
            let _EventsList = EventsList.concat();

            for (let i = 0; i < _EventsList.length; i++) {
                let key = Object.keys(_EventsList[i])[0];
                let sameDate = {};

                let sameElems = _EventsList.filter(item2 => Object.keys(item2)[0] === key);

                if (sameElems.length > 1) {
                    _EventsList = _EventsList.filter(item => Object.keys(item)[0] !== Object.keys(sameElems[0])[0]);
                    sameElems.forEach((item: any) => {
                        let elem: any = Object.values(item)[0];
                        let dateNumber = elem.getAttribute("data-date");
                        if (dateNumber in sameDate) {
                            sameDate[dateNumber].push(elem);
                        } else {
                            sameDate[dateNumber] = [elem];
                        }
                    })
                    store.push(sameDate);
                }
            }

            // console.log(store, "store")

            store.forEach(item => {
                Object.entries(item).forEach((data, i) => {
                    const elems: any = data[1];
                    const date: any = data[0];

                    if (elems.length > 1) {
                        elems.forEach((elem, index) => {
                            if (index === 0) {
                                let pHTML = elem.querySelector("p").outerHTML
                                elem.innerHTML = `
                                    ${pHTML}
                                    <div style="margin-left: 6px;">+${elems.length - 1}</div>
                                `;
                            } else {
                                elem.style.display = "none";
                            }
                        })
                    }
                })
            })
        }

        let block: any = hourBlock?.querySelector(".calendar_minutes")?.children[data.event.start.getMinutes() >= 30 ? 1 : 0];
        setOffsetTop(block?.offsetTop);
    }, [data, viewMode]);

    return (
        <div
            data-test={`${new Date(data.event.start).getHours()}:${new Date(data.event.start).getMinutes()}`}
            data-date={new Date(data.event.start).getDate()}
            className={`event_wrapper_block ${styles.event_wrapper} ${viewMode === "day" ? styles.day : ""}`}
            style={viewMode !== "month" ? {top: offsetTop + "px", position: "absolute"} : undefined}
            data-eventid={data.event.id}
        >
            <p className={styles.event_text}>{data.event.title}</p>
        </div>
    );
})


export const calendarComponent = {
    eventWrapper: EventWrapperView,
    timeSlotWrapper: TimeSlotView,
    toolbar: ToolBarView,
    month: {
        header: MonthHeaderView,
        dateHeader: MonthNumberView,
    },

    week: {
        header: WeekHeaderView,
    }
}