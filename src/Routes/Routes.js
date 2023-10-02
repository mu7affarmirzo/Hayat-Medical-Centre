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
const MyTasks = lazy(() => import("../pages/MyTask/MyTasks"));
const CreateTasks = lazy(() => import("../pages/CreateTasks/CreateTasks"));
const TaskSearch = lazy(() => import("../pages/TaskSearch/TaskSearch"));

const NightAudit = lazy(() => import("../pages/NightAudit/NightAudit"));
const CreateNightAudit = lazy(() =>
  import("../pages/CreateNightAudit/CreateNightAudit")
);

const routes = [
  {
    path: "/404",
    component: InternalPage,
  },

  {
    path: "/reception",
    component: ExpectedArrival,
  },
  {
    path: "/reception/residents",
    component: Residents,
  },
  {
    path: "/reception/expected_departure",
    component: ExpectedDeparture,
  },
  {
    path: "/reception/unpaid",
    component: Unpaid,
  },
  {
    path: "/reception/search",
    component: Search,
  },
  {
    path: "/reception/availability_of_rooms",
    component: AvailabilityRooms,
  },
  {
    path: "/reception/booking_wizard",
    component: BookingWizard,
  },
  {
    path: "/tasks/",
    component: MyTasks,
  },
  {
    path: "/tasks/create_tasks",
    component: CreateTasks,
  },
  {
    path: "/tasks/task_search",
    component: TaskSearch,
  },
  {
    path: "/night_audit",
    component: NightAudit,
  },
  {
    path: "/night_audit/create_night_audit",
    component: CreateNightAudit,
  },
];
export default routes;
