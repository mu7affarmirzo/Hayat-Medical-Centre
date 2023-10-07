import React, { lazy } from 'react'
import { useResidentsViewQuery } from '../../../services/residentsApi'
const Residents = lazy(() => import("../../containers/ResidentsTable/Residents"))
function ResidentsFetch() {
    const { data: residents, isSuccess } = useResidentsViewQuery()
    return (
        isSuccess && <Residents residents={residents} />
    )
}

export default ResidentsFetch