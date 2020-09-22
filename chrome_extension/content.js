console.log("content script is up and running");
chrome.runtime.onMessage.addListener(gotEventmsg);

function gotEventmsg(msg, sender, senderResponse) {
  // let data = msg.data;
  // if (message === "phish") {
  //   alert("<h1>Warning This is a phising page</h1>");
  // } else if (message === "legitimate") {
  //   alert(":)");
  // }
  loadModel(msg.data);
}

async function loadModel(msg) {
  const model = await tf.loadLayersModel(
    "https://raw.githubusercontent.com/harishsambasivam/tfjs-classifier/master/model.json"
  );
  model
    .predict([
      tf.tensor([msg.data[0]]),
      tf.tensor([msg.data[1]]),
      tf.tensor([msg.data[2]]),
      tf.tensor([msg.data[3]]),
    ])
    .print();
}
