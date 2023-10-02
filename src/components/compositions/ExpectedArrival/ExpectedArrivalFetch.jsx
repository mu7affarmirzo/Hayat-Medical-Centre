import React, { lazy } from "react";
import { useExpectedArrivalQuery } from "../../../services/expectedArrivalApi";
const ExpectedArrivalTable = lazy(() =>
  import("../../containers/ExpectedArrivalTable/ExpectedArrivalTable")
);

function ExpectedArrivalFetch() {
  const { data: expectedArrival, isSuccess } = useExpectedArrivalQuery();
  return (
    <>
      {isSuccess && <ExpectedArrivalTable expectedArrival={expectedArrival} />}
    </>
  );
}

export default ExpectedArrivalFetch;
