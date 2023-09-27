import { lazy } from "react";

const ExpectedArrival = lazy(() =>
  import("../pages/ExpectedArrival/ExpectedArrival")
);
const ExpectedDeparture = lazy(() =>
  import("../pages/ExpectedDeparture/ExpectedDeparture")
);
const InternalPage = lazy(() => import("../pages/404/404"));
const Residents = lazy(() => import("../pages/Residents/Residents"));
const Unpaid = lazy(() => import("../pages/Unpaid/Unpaid"));
const Search = lazy(() => import("../pages/Search/Search"));
const AvailabilityRooms = lazy(() =>
  import("../pages/AvailabilityRooms/AvailabilityRooms")
);
const BookingWizard = lazy(() =>
  import("../pages/BookingWizard/BookingWizard")
);

const routes = [
  {
    path: "/404",
    component: InternalPage,
  },
  {
    path: "/",
    component: ExpectedArrival,
  },
  {
    path: "/residents",
    component: Residents,
  },
  {
    path: "/expected_departure",
    component: ExpectedDeparture,
  },
  {
    path: "/unpaid",
    component: Unpaid,
  },
  {
    path: "/search",
    component: Search,
  },
  {
    path: "/availability_of_rooms",
    component: AvailabilityRooms,
  },
  {
    path: "/booking_wizard",
    component: BookingWizard,
  },
];
export default routes;
