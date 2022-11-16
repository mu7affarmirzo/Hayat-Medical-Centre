import { useLocalObservable } from "mobx-react-lite";
import React from "react";
import { AuthorizationStateKeeper } from "../store";
import request from "../utils/request";

export const useFetch = (url: string) => {
  const authorizationStateKeeper = useLocalObservable(
    () => AuthorizationStateKeeper.instance
  );
  const token = authorizationStateKeeper.token;

  const [data, setData] = React.useState<object[]>([]);
  const [loading, setLoading] = React.useState(false);
  const [error, setError] = React.useState(null);
  const headers = {
    Authorization: "Bearer " + JSON.parse(token).access,
  };
  React.useEffect(() => {
    request
      .get(url, { headers })
      .then((response) => setData(response.data))
      .then(() => setLoading(false))
      .catch((error) => setError(error));
  }, [url]);

  return [loading, error, data];
};
