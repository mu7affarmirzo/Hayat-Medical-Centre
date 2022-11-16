import { Alert, Snackbar } from '@mui/material'
import React from 'react'

const Notification = ({ handleClose, open, }) => {
    return (
        <Snackbar open={open} autoHideDuration={6000} onClose={handleClose}>
            <Alert onClose={handleClose} severity="success" sx={{ width: '100%' }}>
                This is a success message!
            </Alert>
        </Snackbar>
    )
}

export default Notification