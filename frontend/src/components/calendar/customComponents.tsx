import React, {useEffect, useState} from "react";
import styles from "./calendar.module.scss"
import Test from "./test";
import moment from "moment";
import 'moment/locale/ru'

const ToolBarView = (data) => {
    console.log(data)
    const changeButtons: Array<{text: string, type: string}> = [
        {
            text: "месяц",
            type: "month"
        },
        {
            text: "неделя",
            type: "week"
        },
        {
            text: "день",
            type: "day"
        },

    ];
    const [active, setActive] = useState<string>("month");

    useEffect(() => {
        if(data.view !== active){
            setActive(data.view)
        }
    }, [data.view])

    const changeView = (type: string) => {
        setActive(type);
        data.onView(type);
    }

    const convertDate = () => {
        const momentRu = moment().locale("ru")
        if(active === "month"){
            return momentRu.format("MMMM YYYY")
        }else if(active === "week") {
            let startWeek = momentRu.startOf("week").format("DD MMMM YYYY");
            let endWeek = momentRu.endOf("week").format("DD MMMM YYYY");
            return `${startWeek} - ${endWeek}`;
        }else if(active === "day") {
            return momentRu.format("dddd | DD MMMM")
        }
    }

    return (
        <div className={styles.toolbar}>
            <div className={styles.button_now}>Сегодня</div>
            <p className={styles.now_day}> {convertDate()}</p>

            <div className={styles.buttons_change}>
                {changeButtons.map((item, i) => (
                    <div onClick={(e) => changeView(item.type)} className={`${styles.button_item} ${item.type === active ? styles.active : ""}`}>{item.text}</div>
                ))}
            </div>
        </div>
    );
}

const MonthHeaderView = (data) => (
    <>
        <div className={`month_name_block ${styles.month_name}`}>{new Date(data.date).toLocaleDateString("ru", {weekday: 'long'})}</div>
    </>
);

const MonthNumberView = (data) => (
    <>
        <div className={`month_number ${styles.month_number}`}>{new Date(data.date).getDate()}</div>
    </>
);

const WeekHeaderView = (data) => {
    const converDate = () => {
        let _date = new Date(data.date);
        let [month, weekDay] = _date.toLocaleDateString("ru", {month: 'short', weekday: 'long'}).split(" ");
        return `${weekDay} | ${_date.getDate()} ${month}`
    }

    return (
        <>
            <div className={`week_name_block ${styles.weeks_name}`}>{converDate()}</div>
        </>
    )
};

const TimeSlotView = (data) => {
    let date = new Date(data.value);

    if(data.children?.props?.children?.props?.children){
        return (
            <div className={`week_time_block ${styles.week_time_wrapper}`}>
                <div className={styles.hour}>{date.getHours()}</div>
                <div className={styles.minutes_block}>
                    <div className={styles.minutes_item}>00</div>
                    <div className={styles.minutes_item}>30</div>
                </div>
            </div>
        )
    }else{
        return (
            <div className={`week_days_box ${styles.week_days_box}`}></div>
        )
    }
}



export const calendarComponent = {
    // timeGutterHeader: Test,
    timeSlotWrapper: TimeSlotView,
    toolbar: ToolBarView,
    month: {
        header: MonthHeaderView,
        dateHeader: MonthNumberView,
    },

    week: {
        header: WeekHeaderView,
    },
}