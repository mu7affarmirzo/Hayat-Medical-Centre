import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { BASE_URL } from "../constants/constants";

const residentsApi = createApi({
  reducerPath: "residentsApi",
  baseQuery: fetchBaseQuery({
    baseUrl: `${BASE_URL}/api/v1/logus`,
    prepareHeaders: (headers) => {
      headers.set(
        "Authorization",
        `Bearer ${localStorage.getItem("access-token")}`
      );
      return headers;
    },
  }),
  tagTypes: ["residents"],
  endpoints: (builder) => ({
    residentsView: builder.query({
      query: () => ({
        url: "/residents-view/",
        method: "GET",
      }),
      providesTags: ["residents"],
    }),
  }),
});

export const { useResidentsViewQuery } = residentsApi;
export { residentsApi };
