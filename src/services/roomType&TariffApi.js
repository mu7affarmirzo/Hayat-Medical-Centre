import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { BASE_URL } from "../constants/constants";

const roomTypeTariffApi = createApi({
  reducerPath: "roomType&Tariff",
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
  tagTypes: ["roomType"],
  endpoints: (builder) => ({
    roomTypeTariff: builder.query({
      query: () => ({
        url: "/tariff-type-price/",
        method: "GET",
      }),
      providesTags: ["roomType"],
    }),
  }),
});

export const { useRoomTypeTariffQuery } = roomTypeTariffApi;
export { roomTypeTariffApi };
