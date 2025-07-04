import React from "react"
import ReactDom from "react_dom/client"
const x=React.createElement("h1",{},"hello react!")
const root=ReactDOM.createRoot(document.getElementsByClassName("root")[0]);
root.render(x);