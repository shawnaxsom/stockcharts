export default interface ChartVue {
  quotes: Quote[];
  draw: (quotes: Quote[]) => {};
}

