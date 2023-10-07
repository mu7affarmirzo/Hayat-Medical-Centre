import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { BASE_URL } from "../constants/constants";
const expectedArrivalApi = createApi({
  reducerPath: "expectedArrivalApi",
  baseQuery: fetchBaseQuery({
    baseUrl: `${BASE_URL}/api/v1/logus`,
    prepareHeaders: (headers) => {
      headers.set("Authorization",`Bearer ${localStorage.getItem("access-token")}`
      );
      return headers;
    },
  }),
  tagTypes: ["expectedArrival"],

  endpoints: (builder) => ({
    expectedArrival: builder.query({
      query: () => ({
        url: "/expected-arrival/",
        method: "GET",
      }),
      providesTags: ["expectedArrival"],
    }),
  }),
});

export const { useExpectedArrivalQuery } = expectedArrivalApi;
export { expectedArrivalApi };
