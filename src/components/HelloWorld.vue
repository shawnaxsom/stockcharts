<template>
  <div class='hello'>
    <h1>{{ msg }}</h1>
    <button v-on:click='chartQuotes'>Get Quote</button>
    <div id='chart'></div>
    <div>
      {{ quote }}
    </div>
  </div>
</template>

<script>
import Chart from "frappe-charts/dist/frappe-charts.min.esm"

function drawChart(quotes) {
  console.warn("ZZZZ HelloWorld.vue", "quotes", quotes)
  if (!quotes || quotes.length === 0) {
    return;
  }

  const data = {
    labels: quotes[0].data.map(day => day.date.substr(5, day.date.length)),
    datasets: quotes.map(quote => ({
      title: quote.symbol,
      values: quote.data.map(day => day.close),
    })),
  };
  console.warn("ZZZZ HelloWorld.vue", "data", data)

  let chart = new Chart({
    parent: '#chart', // or a DOM element
    title: 'My Awesome Chart',
    data: data,
    type: 'line', // or 'bar', 'line', 'scatter', 'pie', 'percentage'
    height: 250,

    colors: ['#7cd6fd', 'violet', 'blue'],

    format_tooltip_x: d => (d + '').toUpperCase(),
    format_tooltip_y: d => d + ' pts'
  });
};

async function getQuote(symbol) {
  const response = await fetch(`https://api.iextrading.com/1.0/stock/${symbol.toLowerCase()}/chart`);
  const data = await response.json();
  return {
    symbol: symbol,
    data,
  };
};

export default {
  name: 'HelloWorld',
  data: () => {
    return {
      msg: 'Welcome to Your Vue.js App',
      quote: 'before',
    }
  },
  methods: {
    chartQuotes: async function() {
      const quotes = [
        await getQuote("AAPL"),
        await getQuote("MSFT"),
      ]

      this.quote = quotes[0];

      drawChart(quotes);
    }
  }
}
</script>

<!-- Add 'scoped' attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
