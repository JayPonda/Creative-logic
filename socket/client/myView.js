let socket = null;
let url = null;
let state = false;

let statusSpan = document.getElementById("status");
let board = document.getElementById("board");
let tile = document.getElementById("tile");

document.getElementById("send").addEventListener("click", () => sendMsg(true));

document
    .getElementById("getAll")
    .addEventListener("click", () => sendMsg(false));
document
    .getElementById("disconnect")
    .addEventListener("click", () => disconnectSkt());

document
    .getElementById("clearFile")
    .addEventListener("click", () => sendMsg(true, true));

fetch("../config.json")
    .then((res) => res.json())
    .then((json) => {
        url = `ws://${json.URL}:${json.PORT}`;
        statusSpan.textContent = "ready";
    });

function getVal() {
    return {
        query: "writeAndEcho",
        title: document.getElementById("title").value,
        content: document.getElementById("content").value,
    };
}

function getAll() {
    return {
        query: "getAll",
    };
}

function clearAll() {
    let table = document.getElementById("board");
    table.innerHTML = "";
    let header = table.createTHead();
    let row = header.insertRow(0);
    row.innerHTML = `
    <th>id</th>
    <th>title</th>
    <th>content</th>
    `;
    return {
        query: "clear",
    };
}

function sendMsg(justOne = true, clear = false) {
    if (!(socket != null && socket.readyState == WebSocket.OPEN)) {
        ns = document.getElementById("newStatus");
        ns.style.display = "block";
        ns.textContent = "trying to connect";
        statusSpan.textContent = "create socket";

        socket = new WebSocket(url);

        socket.addEventListener("open", function (event) {
            console.log("connection Established");
            ns.textContent = "connect sucessfully";
        });

        socket.addEventListener("message", function (event) {
            data = JSON.parse(event.data);
            statusSpan.textContent = "receive";
            console.log(data, data["query"] == "getAll");

            if (data["query"] == "getAll") {
                if (data["unique"] == 1) showAllPrevious(data["data"]);
            } else if (data["query"] == "writeAndEcho") {
                document.getElementById("resTitle").textContent = data["title"];
                document.getElementById("resContent").textContent =
                    data["content"];
            } else {
                table = document.getElementById("board");
                table.innerHTML = "";
                document.getElementById("resTitle").textContent = "";
                document.getElementById("resContent").textContent = "";
            }

            console.log(data, socket.readyState);
        });
    }

    if (justOne) {
        tile.style.display = "block";
        board.style.display = "none";
    } else {
        tile.style.display = "none";
        board.style.display = "table";
    }

    statusSpan.textContent = "sending";
    const t = setInterval(() => {
        if (socket != null && socket.readyState == WebSocket.OPEN) {
            console.log(JSON.stringify(getVal()));
            if (clear) socket.send(JSON.stringify(clearAll()));
            else
                justOne
                    ? socket.send(JSON.stringify(getVal()))
                    : socket.send(JSON.stringify(getAll()));
            clearInterval(t);
            statusSpan.textContent = "send";
        }
    }, 500);
}

function disconnectSkt() {
    console.log("disconnect");
    if (socket != null) socket.close(1000, "demanded disconnection");
    socket = null;
    statusSpan.textContent = "disconnect";
    ns = document.getElementById("newStatus");
    ns.textContent = "disconnect";
    setTimeout(() => {
        ns.style.display = "none";
    }, 3000);
}

function writting() {
    statusSpan.textContent = "writting";
}

function unWritting() {
    statusSpan.textContent = socket == null ? "disconnect" : "connect";
}

function showNote(msg) {
    const s = document.getElementById("newStatus");
    s.textContent = msg;

    const t = setTimeout(() => {}, 3000);
}

function showAllPrevious(pData) {
    table = document.getElementsByTagName("table")[0];
    clearAll();
    console.log(table);
    pData.forEach((element, index) => {
        obj = JSON.parse(element);
        row = table.insertRow();
        newId = row.insertCell(0);
        newId.textContent = index + 1;
        newTitle = row.insertCell(1);
        newTitle.textContent = obj["title"];
        newContent = row.insertCell(2);
        newContent.textContent = obj["content"];
    });
}
