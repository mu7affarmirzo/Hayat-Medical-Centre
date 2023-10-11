import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { BASE_URL } from "../constants/constants";

const roomsApi = createApi({
  reducerPath: "roomsApi",
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
  tagTypes: ["rooms"],
  endpoints: (builder) => ({
    rooms: builder.query({
      query: () => ({
        url: "/room/",
        method: "GET",
      }),
      providesTags: ["rooms"],
    }),
  }),
});

export const { useRoomsQuery } = roomsApi;
export { roomsApi };
