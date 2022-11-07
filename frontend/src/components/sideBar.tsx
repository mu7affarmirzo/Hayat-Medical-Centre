import React from "react";
import styles from "../views/main/index.module.scss";
import { NavBarDropdowns } from "../consts/main";
import parse from "html-react-parser";
import { useLocation, useNavigate } from "react-router";
import Modal from "./Modal";
import GroupAppointment from "./GroupAppointment";

const SideBar = () => {
    const location = useLocation();
    const navigate = useNavigate();
    const [groupAppointment, setGroupAppointment] = React.useState(false);

    const clickHandler = (path: string) => {
        if (path === "/groupAppointment") {
            setGroupAppointment(true);
        } else {
            navigate(path);
        }
    };

    return (
        <div className={styles.sideBar}>
          {groupAppointment ? (
              <Modal
                  show={groupAppointment}
                  onClose={() => setGroupAppointment(false)}
              >
                  <GroupAppointment />
              </Modal>
          ) : null}
          {NavBarDropdowns[0]?.dropdown?.map((item) => (
              <div
                  onClick={() => clickHandler(item.path)}
                  className={`${styles.sideBar_item} ${item.path === location.pathname ? styles.active : ""
                      }`}
              >
                  {item.img}
                  <span>{parse(item.sideBarText || item.text)}</span>
              </div>
          ))}
      </div>
  );
};

export default SideBar;
