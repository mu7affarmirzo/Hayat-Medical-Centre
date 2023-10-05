import React from "react";

function FormatDate({ date }) {
  const parsedDate = new Date(date);

  // Format the date as "dd.mm.yyyy" with leading zeros
  const day = parsedDate.getDate().toString().padStart(2, "0");
  const month = (parsedDate.getMonth() + 1).toString().padStart(2, "0");
  const year = parsedDate.getFullYear();

  const formattedDate = `${day}.${month}.${year}`;
  return <>{formattedDate}</>;
}

export default FormatDate;
