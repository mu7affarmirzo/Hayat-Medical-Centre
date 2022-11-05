import React from 'react';
import styles from "../views/main/index.module.scss";
import {NavBarDropdowns} from "../consts/main";
import parse from 'html-react-parser';
import { useLocation } from 'react-router';

const SideBar = () => {
    const location = useLocation()
    return (
        <div className={styles.sideBar}>
            {NavBarDropdowns[0]?.dropdown?.map(item => (
                <div className={`${styles.sideBar_item} ${item.path === location.pathname ? styles.active : ""}`}>
                    {item.img}
                    <span>{parse(item.sideBarText || item.text)}</span>
                </div>
            ))}
        </div>
    );
};

export default SideBar;