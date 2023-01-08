export const generate_date = (e) => {
  // const month = String(
  //   e.toLocaleString("default", { month: "short" })
  // );
  const month = ["01","02","03","04","05","06","07","08","09","10","11","12"];
  const day = String(e.getDate()).padStart(2, "0");
  const year = String(e.getFullYear());
  const formattedDate = `${day}.${month[e.getMonth()]}.${year}`;
  return formattedDate;
};