import React from 'react';

const Test = (...args: any) => {
    console.log("TEST", args)

    return (
        <div style={{color: "red", backgroundColor: "black"}}>
            some
        </div>
    );
};

export default Test;