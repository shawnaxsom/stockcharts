import ApiData from "./ApiData";

export default interface QuoteData extends ApiData {
  baseline:
    | {
        close: number;
        closeAtStartDate: number;
      }
    | undefined
    | null;
  closeAtStartDate: number;
}

