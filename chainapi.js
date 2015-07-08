var Chain = require('chain-node');
var chain = new Chain({
  keyId: 'af95284ac8d016f948c642572103a2d1',
  keySecret: 'e0828f64620f7cb019721e1584ee5bae',
  blockChain: 'bitcoin'
});

chain.getAddress('1NdoPDBFH6fGBKoCZwAMTWuqEdfFiwz1Qa ', function(err, resp) {
  console.log('balance=' + resp.total.balance);
});