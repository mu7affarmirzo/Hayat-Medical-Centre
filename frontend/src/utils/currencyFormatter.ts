export const currencyFormatter = (sum: number, currency: string) => {
  return sum.toLocaleString("en-US", {
    style: "currency",
    currency,
    currencyDisplay: "code",
  });
};
