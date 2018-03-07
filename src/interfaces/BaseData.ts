import Quote from "./Quote";

export default interface BaseData {
  baselineText: string;
  baseline: Quote | null | undefined;
  endDate: Object; // TODO: Moment.js bindings?
  lastD3Event: Object | null;
  quotes: Quote[];
  startDate: Object;
  symbols: Array<string>;
  symbolsText: string;
}

