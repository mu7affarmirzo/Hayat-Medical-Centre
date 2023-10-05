import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { BASE_URL } from "../constants/constants";

const residentsApi = createApi({
  reducerPath: "residentsApi",
  baseQuery: fetchBaseQuery({
    baseUrl: `${BASE_URL}/api/v1/logus`,
    // Set the headers with the authorization token
    prepareHeaders: (headers) => {
      headers.set("Authorization","Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NjYwMDY4MSwiaWF0IjoxNjk2NTE0MjgxLCJqdGkiOiI1N2M1Y2Y2YTAyYTc0NzE5YjEwM2MxYjM3ODBjMDFjOSIsInVzZXJfaWQiOjF9.7rsJYwRg50p69mtmEivjEy5ll9MhGEaVWeTkxv2kbuQ"
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

export const { useExpectedDepartureQuery } = residentsApi;
export { residentsApi };
