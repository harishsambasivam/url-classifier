console.log("Background script is up and running");
chrome.tabs.onUpdated.addListener(pageLoaded);

let tabUpdated = false;

function pageLoaded(tabID, changeInfo, tab) {
  chrome.tabs.query({ active: true, lastFocusedWindow: true }, async function (
    tabs
  ) {
    // if (changeInfo.status == 'complete' && tab.status == 'complete' && tab.url != undefined) {
    //     if (!tabUpdated) {
    //         tabUpdated = true;
    //     }
    // }
    if (tab.url !== undefined && changeInfo.status == "complete") {
      console.log("made fetch");
      let response = await fetch(
        `http://e15fc3610191.ngrok.io/parseurl?url=${tab.url}`
      );
      response.json().then((data) => {
        console.log(data);
        chrome.tabs.sendMessage(tabID, { data });
      });
    }
  });
}
