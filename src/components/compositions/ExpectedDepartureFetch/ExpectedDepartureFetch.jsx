import React, { lazy } from "react";
import { useExpectedDepartureQuery } from "../../../services/expectedDepartureApi";

const ExpectedDepartureTable = lazy(() =>
  import("../../containers/ExpectedDepartureTable/ExpectedDepartureTable")
);

function ExpectedDepartureFetch() {
  const { data: expectedDeparture, isSuccess } = useExpectedDepartureQuery();
  return (
    <>
      {isSuccess && (
        <ExpectedDepartureTable expectedDeparture={expectedDeparture} />
      )}
    </>
  );
}

export default ExpectedDepartureFetch;
