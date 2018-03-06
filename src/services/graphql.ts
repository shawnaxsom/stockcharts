import Quote from "../interfaces/Quote";

function postData(url: string, options: {body: string}) {
  return fetch(url, {
    body: options.body,
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "content-type": "application/json"
    },
    method: "POST",
    mode: "cors",
    redirect: "follow",
    referrer: "no-referrer",
  })
  .then(response => {
    return response.json()
  })
}

function query(query: string) {
  return postData("https://4v2cyqgx10.execute-api.us-east-1.amazonaws.com/dev/", {
    body: query,
  });
}

export async function getPeers(symbol: string) {
  const response = await query(`{ peers(symbol: "${symbol}") }`);
  const data = JSON.parse(response.peers.replace(/'/g, '"'));
  return {
    symbol: symbol,
    data,
  };
}

export async function getQuote(symbol: string): Promise<Quote> {
  const response = await query(`{ chart(symbol: "${symbol}", timespan: "5y") }`);
  const data = JSON.parse(response.chart.replace(/'/g, '"'));

  return {
    symbol: symbol,
    data,
  };
}
