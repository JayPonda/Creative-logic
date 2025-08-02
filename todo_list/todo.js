console.log("hello");

ids = 1;

function status() {
  n = document.querySelector("#bord").querySelector("div");
  if (n == null) {
    return false;
  }
  return true;
}

function disapear(btn) {
  let edit = document.querySelector(btn);
  edit.disabled = true;
  edit.style.background = "#004e53";
  edit.style.color = "white";
  edit.style.cursor = "default";
}

function apear(btn) {
  let edit = document.querySelector(btn);
  edit.disabled = false;
  edit.style.cursor = "pointer";
  edit.style.background = "white";
  edit.style.color = "black";
}

function regulation() {
  if (!status()) {
    disapear("#clean");
    disapear("#reindex");
    ids = 0;
  }
}

regulation();

function authenticate(msg) {
  if (message == "") {
    alert("we can not add empty task");
    return false;
  } else if (message) {
    let p = 0;
    for (let j = 0; j < message.length; j++) {
      if (message[j] == " ") p++;
      else break;
    }
    if (message.length == p) {
      alert("we can not add empty task");
      return false;
    }
  } else {
    alert("cancel task");
    return false;
  }
  return true;
}

function addtask() {
  div = document.getElementById("bord");

  message = prompt("enter your task");

  if (!authenticate(message)) return;
  ids++;

  newdiv = document.createElement("div");
  newdiv.id = "newtask";

  newele = document.createElement("span");
  newele.id = "taskDetails";
  newele1 = document.createElement("span");
  newele1.id = "taskIndex";

  // tast buttons - ma

  // delete
  newbtn1 = document.createElement("button");
  newbtn1.textContent = "delete";
  newbtn1.id = "danger";
  newbtn1.className = "btn";
  newbtn1.onclick = function () {
    if (confirm("do you want to delete this task?")) {
      this.parentNode.remove();
      regulation();
      alert("this task is secussfully deleted");
    }
  };

  // edit
  newbtn2 = document.createElement("button");
  newbtn2.textContent = "edit";
  newbtn2.id = "normal";
  newbtn2.className = "btn";
  newbtn2.onclick = function () {
    if (confirm("do you want to edit this task?")) {
      omsg = this.parentNode.querySelectorAll("span")[1];
      msg = prompt("edit here", omsg.textContent);
      if (msg == null || omsg.textContent == msg) {
        alert("no changes detected");
      } else {
        omsg.textContent = msg;
        alert("edited");
      }
    }
  };

  // mark as done
  newbtn3 = document.createElement("button");
  newbtn3.textContent = "mark as done";
  newbtn3.id = "balance";
  newbtn3.className = "btn";
  newbtn3.onclick = function () {
    let p = this.parentNode.querySelectorAll("span");
    let bt = this.parentNode.querySelector("#balance");
    if (bt.textContent == "mark as done") {
      p[1].style.textDecoration = "line-through";
      p[0].style.backgroundColor = "#f99fc9ff";
      bt.textContent = "pending";
    } else {
      p[1].style.textDecoration = "none";
      p[0].style.backgroundColor = "white";
      bt.textContent = "mark as done";
    }
    console.log();
  };

  newele1.textContent = String(ids);
  newele.textContent = message;

  newdiv.appendChild(newele1);
  newdiv.appendChild(newele);
  newdiv.appendChild(newbtn3);
  newdiv.appendChild(newbtn2);
  newdiv.appendChild(newbtn1);

  div.appendChild(newdiv);

  apear("#clean");
  apear("#reindex");
}

function activate() {
  let j = document.querySelector("#bord").querySelectorAll("div");
  for (let i = 0; i < j.length; i++) {
    let p = j[i].querySelector("input");
    if (p && p.type == "checkbox") {
      p.style.display = "block";
    }
  }
}

function editask() {
  activate();
}

function clean() {
  j = confirm("do you want to clear all tasks?");
  if (j) {
    const k = document.querySelector("#bord");
    while (k.firstChild) {
      k.removeChild(k.lastChild);
    }
  } else {
    alert("no tasks deleted");
  }

  regulation();
}

function reindex() {
  let newt = document.querySelector("#bord").querySelectorAll("div");
  for (let i = 0; i < newt.length; i++) {
    let t = newt[i].querySelectorAll("span")[0].textContent;
    let t1 = String(i + 1);
    newt[i].querySelector("span").textContent = t1;
  }
  ids = newt.length;
}
