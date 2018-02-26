# stockcharts

> A Vue.js project

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```


## GraphQL API

``` bash
# virtualenv of fish shell
vf new stockcharts
vf activate stockcharts

# start django, with GraphQL module
manage.py runserver

# Endpoint with GraphiQL running on it
open http://127.0.0.1:8000/graphql

{
  peers(symbol: "msft")
}
```



### 3rd party APIs

* https://iextrading.com/developer/docs/#chart
* https://iextrading.com/developer/docs/#key-stats
* https://www.alphavantage.co/
* https://blog.quandl.com/api-for-stock-data

