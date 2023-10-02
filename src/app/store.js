import { configureStore } from "@reduxjs/toolkit";
import { expectedArrivalApi } from "../services/expectedArrivalApi";
import { expectedDepartureApi } from "../services/expectedDepartureApi";

export const store = configureStore({
  reducer: {
    [expectedArrivalApi.reducerPath]: expectedArrivalApi.reducer,
    [expectedDepartureApi.reducerPath]: expectedDepartureApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(
      expectedArrivalApi.middleware,
      expectedDepartureApi.middleware
    ),
});
