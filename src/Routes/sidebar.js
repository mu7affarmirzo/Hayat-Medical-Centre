import { PiAirplane } from "react-icons/pi";
import { LiaUserLockSolid } from "react-icons/lia";
import { PiSuitcase } from "react-icons/pi";
import { LiaMoneyCheckAltSolid } from "react-icons/lia";
import { FiSearch } from "react-icons/fi";
import { FaUserPen } from "react-icons/fa6";
// import GridSearch from "../assets/icons/grid-search.svg";
import { gridSearch } from "../assets/icons/grid-search";
import { LuCalendarCheck } from "react-icons/lu";
import { BsMoonStars } from "react-icons/bs";

export const routes = {
  reception: [
    {
      path: "/reception",
      icon: <PiAirplane />,
      name: "Ожидаемый заезд",
    },
    {
      path: "/reception/residents",
      icon: <LiaUserLockSolid />,
      name: "Проживающие",
    },
    {
      path: "/reception/expected_departure",
      icon: <PiSuitcase />,
      name: "Ожидаемый выезд",
    },
    {
      path: "/reception/unpaid",
      icon: <LiaMoneyCheckAltSolid />,
      name: "Неоплаченные",
    },
    {
      path: "/reception/search",
      icon: <FiSearch />,
      name: "Поиск",
    },
    {
      path: "/reception/availability_of_rooms",
      icon: gridSearch,
      name: "Наличие комнат",
    },
  ],

  tasks: [
    {
      path: "/tasks",
      icon: <LuCalendarCheck />,
      name: "Мои задачи",
    },
    {
      path: "/tasks/task_search",
      icon: <FiSearch />,
      name: "Поиск",
    },
  ],

  night_audit: [
    {
      path: "/night_audit",
      icon: <BsMoonStars />,
      name: "Ночной аудит",
    },
  ],
};

export const extraRoutes = {
  reception: [
    {
      path: "/reception/booking_wizard",
      icon: <FaUserPen />,
      name: "Мастер бронирования",
      title: "Создать бронь",
    },
  ],
  tasks: [
    {
      path: "/tasks/create_task",
      icon: <FaUserPen />,
      name: "Мастер бронирования",
      title: "Создать задачу",
    },
  ],
  night_audit: [
    {
      path: "/night_audit/create_nigh_audit",
      icon: <FaUserPen />,
      name: "Мастер бронирования",
      title: "Ночной аудит",
    },
  ],
};
