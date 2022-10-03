import React, {useState} from 'react';
import { MainView } from "../../views";

const MainContainer = () => {
    const [selectData, setSelectData] = useState<string>('');

    return (
        <>
            <MainView
                selectData={selectData}
                setSelectData={setSelectData}
            />
        </>
    );
};

export default MainContainer;