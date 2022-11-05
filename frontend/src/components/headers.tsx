import React from 'react';
import { Button, Menu, MenuItem, Typography } from "@mui/material";
import styles from "../views/main/index.module.scss"
import logoImg from "../assets/img/logo.svg";
import { NavBarDropdowns } from "../consts/main";
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';
import { useLocalObservable } from "mobx-react-lite";
import AuthorizationStateKeeper from "../store/AuthorizationStateKeeper";
import LogoutTwoToneIcon from '@mui/icons-material/LogoutTwoTone';
import { Link } from 'react-router-dom';
import Modal from './Modal';
import GroupAppointment from './GroupAppointment';

const Headers = () => {
    const [anchorEl, setAnchorEl] = React.useState<{ index: string, elem: null | HTMLElement }>({
        index: "",
        elem: null
    });
    const [profileOpen, setProfileOpen] = React.useState<null | HTMLElement>(null);
    const [groupAppointment, setGroupAppointment] = React.useState(false)
    const localAuthorizationStateKeeper = useLocalObservable(() => AuthorizationStateKeeper.instance);
    const { setRole } = localAuthorizationStateKeeper;

    const handleClick = (index: string, event: React.MouseEvent<HTMLButtonElement>) => {
        setAnchorEl({ index, elem: event.currentTarget });
    };

    const handleClose = () => {
        setAnchorEl({ index: "", elem: null });
    };

    const handleModalOpener = () => {
        setGroupAppointment(true)
        handleClose()
    }

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

                    {NavBarDropdowns.map((item, i) => {
                        if (!item.dropdown) {
                            return (
                                <div className={styles.nav_item}>
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
                                                    <MenuItem onClick={handleModalOpener}>
                                                        {dropdownItem.img}
                                                        {dropdownItem.text}
                                                    </MenuItem>
                                                ) : (
                                                        <MenuItem onClick={handleClose}>
                                                            <Link to={dropdownItem.path}>
                                                                {dropdownItem.img}
                                                                {dropdownItem.text}
                                                            </Link>
                                                        </MenuItem>
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
                        <MenuItem onClick={() => setRole("NoAuth")}>
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