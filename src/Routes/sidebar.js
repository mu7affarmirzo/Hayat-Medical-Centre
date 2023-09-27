import { PiAirplane } from "react-icons/pi";
import { LiaUserLockSolid } from "react-icons/lia";
import { PiSuitcase } from "react-icons/pi";
import { LiaMoneyCheckAltSolid } from "react-icons/lia";
import { FiSearch } from "react-icons/fi";
import { FaUserPen } from "react-icons/fa6";
// import GridSearch from "../assets/icons/grid-search.svg";
import { gridSearch } from "../assets/icons/grid-search";

export const routes = [
  {
    path: "/",
    icon: <PiAirplane />,
    name: "Ожидаемый заезд",
  },
  {
    path: "/residents",
    icon: <LiaUserLockSolid />,
    name: "Проживающие",
  },
  {
    path: "/expected_departure",
    icon: <PiSuitcase />,
    name: "Ожидаемый выезд",
  },
  {
    path: "/unpaid",
    icon: <LiaMoneyCheckAltSolid />,
    name: "Неоплаченные",
  },
  {
    path: "/search",
    icon: <FiSearch />,
    name: "Поиск",
  },
  {
    path: "/availability_of_rooms",
    icon: gridSearch,
    name: "Наличие комнат",
  },
];

export const extraRoutes = [
  {
    path: "/booking_wizard",
    icon: <FaUserPen />,
    name: "Мастер бронирования",
  },
];
