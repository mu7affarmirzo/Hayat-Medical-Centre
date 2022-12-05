import React from "react";
import styles from "../views/main/index.module.scss";
import { CashBoxDropdowns, NavBarDropdowns } from "../consts/main";
import parse from "html-react-parser";
import { useLocation, useNavigate } from "react-router";
import Modal from "./Modal";
import GroupAppointment from "./GroupAppointment";

const SideBar = () => {
    const location = useLocation();
    const [navbar, setNavbar] = React.useState(NavBarDropdowns);
    const navigate = useNavigate();
    const [groupAppointment, setGroupAppointment] = React.useState(false);
    const [index, setIndex] = React.useState<number>(0);
    const clickHandler = (path: string) => {
        if (path === "/groupAppointment") {
            setGroupAppointment(true);
        } else {
            navigate(path);
        }
    };

    const cashbox_use_cases = [
        "/cashbox",
        "/patientPayments",
        "/historyPayments",
    ];
    const info_use_cases = ["/reports", "/patientSale"];
    const info_use_cases_for_registry = [
        "/registeryVisits",
        "/registeryAccounts",
    ];
    React.useEffect(() => {
        if (cashbox_use_cases.includes(location.pathname)) {
            setIndex(1);
        } else if (info_use_cases.includes(location.pathname)) {
            setNavbar(CashBoxDropdowns);
            setIndex(2);
        } else if (info_use_cases_for_registry.includes(location.pathname)) {
            setNavbar(CashBoxDropdowns);
            setIndex(0);
        } else {
            setNavbar(NavBarDropdowns);
            setIndex(0);
        }
    }, [location.pathname]);

    return (
        <div className={styles.sideBar}>
            {groupAppointment && (
                <Modal
                    onClose={() => setGroupAppointment(false)}
                    show={groupAppointment}
                >
                    <GroupAppointment />
                </Modal>
            )}
            {navbar[index]?.dropdown?.map(
                (item, index) =>
                    item.sideBarText && (
                        <div
                            key={index}
                            onClick={() => clickHandler(item.path)}
                            className={`${styles.sideBar_item} ${item.path === location.pathname ? styles.active : ""
                                }`}
                        >
                            {item.img}
                            <span>{parse(item.sideBarText || item.text)}</span>
                        </div>
                    )
            )}
      </div>
  );
};

export default SideBar;
