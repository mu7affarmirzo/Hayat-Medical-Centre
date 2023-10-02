import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { BASE_URL } from "../constants/constants";

const expectedDepartureApi = createApi({
  reducerPath: "expectedDepartureApi",
  baseQuery: fetchBaseQuery({ baseUrl: `${BASE_URL}/api/v1/logus` }),
  tagTypes: ["expectedDeparture"],
  endpoints: (builder) => ({
    expectedDeparture: builder.query({
      query: () => ({
        url: "/expected-departure/",
        method: "GET",
      }),
      providesTags: ["expectedDeparture"],
    }),
  }),
});

export const { useExpectedDepartureQuery } = expectedDepartureApi;
export { expectedDepartureApi };
