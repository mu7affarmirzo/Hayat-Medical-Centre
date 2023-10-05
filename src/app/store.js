import { configureStore } from "@reduxjs/toolkit";
import { expectedArrivalApi } from "../services/expectedArrivalApi";
import { expectedDepartureApi } from "../services/expectedDepartureApi";
import { residentsApi } from "../services/residentsApi";

export const store = configureStore({
  reducer: {
    [expectedArrivalApi.reducerPath]: expectedArrivalApi.reducer,
    [expectedDepartureApi.reducerPath]: expectedDepartureApi.reducer,
    [residentsApi.reducerPath]: residentsApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(
      expectedArrivalApi.middleware,
      expectedDepartureApi.middleware,
      residentsApi.middleware
    ),
});
