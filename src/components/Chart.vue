<template>
  <div>
    <input v-model='symbols' v-on:keyup.enter='chartQuotes' placeholder='AAPL,MSFT,SPY'>
    <button v-on:click='chartQuotes'>Get Quote</button>
    <svg width='700' height='500'>
    </svg>
  </div>
</template>


<script>
import * as d3 from 'd3';
import flatten from 'lodash/flatten';
import moment from 'moment';

async function getQuote(symbol) {
  const response = await fetch(`https://api.iextrading.com/1.0/stock/${symbol.toLowerCase()}/chart/1y`);
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
      startDate: new moment("1/20/2018"),
      symbols: 'AAPL,MSFT,SPY',
    }
  },
  mounted: function() {
    this.chartQuotes();
  },
  beforeMount () {
    // window.addEventListener('scroll', this.handleScroll);
  },
  beforeDestroy () {
    // window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    handleScroll: async function(event) {
      // console.warn("ZZZZ Chart.vue", "foo")
    },
    chartQuotes: async function() {
      // console.warn('ZZZZ Chart.vue', 'foo', this.symbols)
      const symbols = this.symbols.split(',');
      const quotes = [];
      for (var symbol of symbols) {
        const quote = await getQuote(symbol);
        quotes.push(quote);
      }

      this.quotes = quotes;

      this.draw(this.filterTime(quotes));
    },
    filterTime(quotes) {
      return quotes.map(quote => {
        return {
          ...quote,
          data: quote.data.filter(item => {
            return new moment(item.date) > this.startDate;
          })
        }
      })
    },
    draw(quotes) {
      var svg = d3.select('svg');
      var margin = {top: 20, right: 20, bottom: 30, left: 50};
      var width = +svg.attr('width') - margin.left - margin.right;
      var height = +svg.attr('height') - margin.top - margin.bottom;
      if (svg.nodes()[0].children.length) {
        // Redraw
        d3.select('g').remove();
      }

      const onZoom = (a, b, c, d, e, f, g) => {
        const minDate = new moment(this.quotes[0].data.reduce((min, next) => min && new moment(min.date) < new moment(next.date) ? min : next, null).date);
        const maxDate = new moment(this.quotes[0].data.reduce((max, next) => max && new moment(max.date) > new moment(next.date) ? max : next, null).date).add(-1, "day");

        if (d3.event.sourceEvent.deltaY > 0 && this.startDate < maxDate) {
          this.$set(this, "startDate", this.startDate.add(5, "day"))
          this.chartQuotes();
        } else if (d3.event.sourceEvent.deltaY < 0 && this.startDate > minDate) {
          this.$set(this, "startDate", this.startDate.add(-5, "day"))
          this.chartQuotes();
        }
      }

      var zoom = d3.zoom()
        .on("zoom", onZoom);

      svg.call(zoom);

      var g = svg.append('g').attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');

      var parseTime = d3.timeParse('%Y-%m-%d');

      var x = d3.scaleTime()
        .rangeRound([0, width]);

      var y = d3.scaleLinear()
        .rangeRound([height, 0]);

      const allQuoteData = flatten(quotes.map(q => q.data.map(d => ({
        close: d.close,
        date: d.date,
        start: q.data[0].close,
      }))));
      x.domain(d3.extent(allQuoteData, function(d) {
        return parseTime(d.date);
      }))
      y.domain(d3.extent(allQuoteData, function(d) {
        return d.close / d.start;
      }))

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

      const drawLine = data => {
        // const max = data.reduce((largest, next) => largest.close > next.close ? largest : next, 0).close;
        const start = data[0].close;

        var line = d3.line()
          .x(function(d) {
            return x(parseTime(d.date));
          })
          .y(function(d) {
            return y(d.close / start);
          });

        g.append('path')
          .datum(data)
          .attr('fill', 'none')
          .attr('stroke', 'steelblue')
          .attr('stroke-linejoin', 'round')
          .attr('stroke-linecap', 'round')
          .attr('stroke-width', 1.5)
          .attr('d', line);
      }

      quotes.forEach(quote => drawLine(quote.data))
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
