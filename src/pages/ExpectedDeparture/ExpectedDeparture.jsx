import React, { lazy } from "react";
import "./ExpectedDeparture.css";
const ExpectedArrivalFetch = lazy(() =>
  import(
    "../../components/compositions/ExpectedDepartureFetch/ExpectedDepartureFetch"
  )
);
function ExpectedDeparture() {
  return (
    <main className="expectation__main">
      <ExpectedArrivalFetch />
    </main>
  );
}

export default ExpectedDeparture;
