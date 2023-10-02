import React, { lazy } from "react";
import "./ExpectedArrival.css";

const ExpectedArrivalFetch = lazy(() =>
  import("../../components/compositions/ExpectedArrival/ExpectedArrivalFetch")
);

function ExpectedArrival() {
  return (
    <main className="expectation__main">
      <ExpectedArrivalFetch />
    </main>
  );
}

export default ExpectedArrival;
