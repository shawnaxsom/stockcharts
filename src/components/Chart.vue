<template>
  <div>
    <svg width='500' height='270'>
      <g style='transform: translate(0, 10px)'>
        <path :d='line' />
      </g>
    </svg>
    <button v-on:click='chartQuotes'>Get Quote</button>
  </div>
</template>


<script>
  import * as d3 from 'd3';
import flatten from 'lodash/flatten';

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
  mounted: function() {
    this.chartQuotes();
  },
  methods: {
    chartQuotes: async function() {
      const quotes = [
        await getQuote("AAPL"),
        await getQuote("MSFT"),
      ]

      this.quote = quotes[0];

      this.draw(quotes);
    },
    draw(quotes) {
      console.warn("ZZZZ Chart.vue", "quotes", quotes)
      var svg = d3.select('svg'),
        margin = {top: 20, right: 20, bottom: 30, left: 50},
        width = +svg.attr('width') - margin.left - margin.right,
        height = +svg.attr('height') - margin.top - margin.bottom,
        g = svg.append('g').attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');

      var parseTime = d3.timeParse('%Y-%m-%d');

      var x = d3.scaleTime()
        .rangeRound([0, width]);

      var y = d3.scaleLinear()
        .rangeRound([height, 0]);

      console.warn("ZZZZ Chart.vue", `parseTime("2018-01-01")`, parseTime("2018-01-01"))

      const allQuoteData = flatten(quotes.map(q => q.data));
      x.domain(d3.extent(allQuoteData, function(d) {
        console.warn("ZZZZ Chart.vue", "d.date", d.date)
        return parseTime(d.date);
      }))
      y.domain(d3.extent(allQuoteData, function(d) {
        console.warn("ZZZZ Chart.vue", "d.close", d.close)
        return d.close; }))

      g.append('g')
        .attr('transform', 'translate(0,' + height + ')')
        .call(d3.axisBottom(x))
        .select('.domain')
        .remove()

      g.append('g')
        .call(d3.axisLeft(y))
        .append('text')
        .attr('fill', '#000')
        .attr('transform', 'rotate(-90)')
        .attr('y', 6)
        .attr('dy', '0.71em')
        .attr('text-anchor', 'end')
        .text('Price ($)')

      var line = d3.line()
        .x(function(d) {
          console.warn("ZZZZ Chart.vue", 'parseTime("2018-01-01")', d.date, parseTime(x(d.date)))
          return x(parseTime(d.date)); })
        .y(function(d) {
          console.warn("ZZZZ Chart.vue", "line d.close", d.close, y(d.close))
          return y(d.close); });

      g.append('path')
        .datum(quotes[0].data)
        .attr('fill', 'none')
        .attr('stroke', 'steelblue')
        .attr('stroke-linejoin', 'round')
        .attr('stroke-linecap', 'round')
        .attr('stroke-width', 1.5)
        .attr('d', line)
      g.append('path')
        .datum(quotes[1].data)
        .attr('fill', 'none')
        .attr('stroke', 'steelblue')
        .attr('stroke-linejoin', 'round')
        .attr('stroke-linecap', 'round')
        .attr('stroke-width', 1.5)
        .attr('d', line)
      console.warn("ZZZZ Chart.vue", "lineee", line(quotes[0].data))
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
