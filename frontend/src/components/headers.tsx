import React from 'react';
import { Button, Menu, MenuItem, Typography } from "@mui/material";
import styles from "../views/main/index.module.scss"
import logoImg from "../assets/img/logo.svg";
import { CashBoxDropdowns, NavBarDropdowns } from "../consts/main";
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';
import { useLocalObservable } from "mobx-react-lite";
import AuthorizationStateKeeper from "../store/AuthorizationStateKeeper";
import LogoutTwoToneIcon from '@mui/icons-material/LogoutTwoTone';
import { Link, useLocation } from 'react-router-dom';
import Modal from './Modal';
import GroupAppointment from './GroupAppointment';

const Headers = () => {
    const location = useLocation()
    const [anchorEl, setAnchorEl] = React.useState<{ index: string, elem: null | HTMLElement }>({
        index: "",
        elem: null
    });
    const [profileOpen, setProfileOpen] = React.useState<null | HTMLElement>(null);
    const [groupAppointment, setGroupAppointment] = React.useState(false)
    const localAuthorizationStateKeeper = useLocalObservable(() => AuthorizationStateKeeper.instance);
    const { setRole, removeToken } = localAuthorizationStateKeeper;
    const [navbar, setNavbar] = React.useState(NavBarDropdowns)
    const handleClick = (index: string, event: React.MouseEvent<HTMLButtonElement>) => {
        setAnchorEl({ index, elem: event.currentTarget });
    };

    const handleClose = () => {
        setAnchorEl({ index: "", elem: null });
    };

    const handleLogOut = () => {
        setRole("NoAuth");
        removeToken()
    }

    const handleModalOpener = () => {
        setGroupAppointment(true)
        handleClose()
    }
    const use_cases = ['/cashbox', '/patientPayments', '/historyPayments', '/reports', '/patientSale', "/registeryVisits", "/registeryAccounts",]
    React.useEffect(() => {
        if (use_cases.includes(location.pathname)) {
            setNavbar(CashBoxDropdowns)
        } else {
            setNavbar(NavBarDropdowns)
        }
    }, [location.pathname])

    return (
        <div className={styles.header}>
            {
                groupAppointment ? (
                    <Modal show={groupAppointment} onClose={() => setGroupAppointment(false)}>
                        <GroupAppointment />
                    </Modal>
                ) : null
            }
            <div className={styles.left}>
                <img src={logoImg} alt="logoImg" className={styles.logo} />

                <nav className={styles.nav}>

                    {navbar.map((item, i) => {
                        if (!item.dropdown) {
                            return (
                                <div key={i} className={styles.nav_item}>
                                    {item.button}
                                </div>
                            );
                        }

                        return (
                            <>
                                <Button
                                    id="basic-button"
                                    aria-controls={anchorEl.index === String(i) ? 'basic-menu' : undefined}
                                    aria-haspopup="true"
                                    aria-expanded={anchorEl.index === String(i) ? 'true' : undefined}
                                    onClick={(e) => handleClick(String(i), e)}
                                    className={styles.nav_item}
                                // key={item.id}
                                >
                                    {item.button}
                                </Button>

                                <Menu
                                    id="basic-menu"
                                    anchorEl={anchorEl.elem}
                                    open={anchorEl.index === String(i)}
                                    onClose={handleClose}
                                    MenuListProps={{
                                        'aria-labelledby': 'basic-button',
                                    }}
                                    className="header_dropdown_hidden"
                                >

                                    <Typography className="title">
                                        {item.title}
                                    </Typography>

                                    {
                                        item.dropdown.map((dropdownItem, index) => {
                                            return (
                                                dropdownItem.text === 'Добавить группу приемов' ? (
                                                    <MenuItem className={styles.dropdown_menu} key={index} onClick={handleModalOpener}>
                                                        {dropdownItem.img}
                                                        {dropdownItem.text}
                                                    </MenuItem>
                                                ) : (
                                                        <Link
                                                            to={dropdownItem.path}
                                                            key={index}
                                                        >
                                                        <MenuItem
                                                                className={styles.dropdown_menu}
                                                                onClick={handleClose}>
                                                                {dropdownItem.img}
                                                                {dropdownItem.text}
                                                        </MenuItem>
                                                        </Link>
                                                    )
                                            );
                                        })
                                    }

                                </Menu>
                            </>
                        );
                    })}
                </nav>
            </div>
            <div className={styles.right}>
                <>
                    <Button
                        id="fade-button"
                        aria-controls={Boolean(profileOpen) ? 'fade-menu' : undefined}
                        aria-haspopup="true"
                        aria-expanded={Boolean(profileOpen) ? 'true' : undefined}
                        onClick={(e) => setProfileOpen(e.currentTarget)}
                    >
                        <Typography variant="h6" className={styles.profile_text}>
                            Вадим Александров
                        </Typography>
                        <ArrowDropDownIcon sx={{ fill: "rgba(0, 0, 0, 0.54)" }} />
                    </Button>
                    <Menu
                        id="fade-menu"
                        anchorEl={profileOpen}
                        open={Boolean(profileOpen)}
                        onClose={() => setProfileOpen(null)}
                        className="hidden_profile_block"
                    >
                        {/*<MenuItem onClick={() => setProfileOpen(null)}>Profile</MenuItem>*/}
                        {/*<MenuItem onClick={() => setProfileOpen(null)}>My account</MenuItem>*/}
                        <MenuItem onClick={handleLogOut}>
                            <LogoutTwoToneIcon sx={{ mr: "12px" }} />
                            Logout
                        </MenuItem>
                    </Menu>
                </>
            </div>
        </div>
    );
};

export default Headers;