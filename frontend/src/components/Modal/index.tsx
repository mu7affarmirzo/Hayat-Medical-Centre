import styles from "./modal.module.scss";
import React from "react";
import ReactDOM from "react-dom";
import { createPortal } from "react-dom";
import { useEffect, useState } from "react";

function Modal({ children, show, onClose }) {
    const [isBrowser, setIsBrowser] = useState(true);
    const root = document.querySelector('#portal') as Element;

    useEffect(() => {
        setIsBrowser(true);
        document.body.style.overflow = 'hidden'
        return () => {
            setIsBrowser(false)
            document.body.style.overflow = 'initial'
        }
    }, []);

    const modal = show ? (
        <>
            <div onClick={onClose} className={styles.overlay}></div>
            <div className={styles.modal_wrapper}>{children}</div>
        </>
    ) : null;

    return isBrowser && typeof document != 'undefined'
        ? createPortal(
            <>
                {modal}
            </>,
            root)
        : null
}

export default Modal;