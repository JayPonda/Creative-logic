//data
const game = {
  win: 0,
  lose: 0,
  west: 0,
  score: [],
};

const records = {
  you: [],
  co: [],
  mainStack: [11, 12, 13, 21, 22, 23, 31, 32, 33],
  term: 0,
  toggel: true,
  iScore: false
};

// basics
function $(e) {
  return document.querySelector(e);
}

function $$(e) {
  return document.createElement(e);
}

function $$$(e) {
  return document.querySelectorAll(e);
}

function removeElm(e) {
  e = parseInt(e);
  for (let i = 0; i < records.mainStack.length; i++) {
    if (records.mainStack[i] == e) {
      records.mainStack.splice(i, 1);
      break;
    }
  }
}

// reset events

function scoreBord() {
  $("#my").textContent = game.win;
  $("#your").textContent = game.lose;
  $("#total").textContent = game.lose + game.win + game.west;
}

function resetgame() {
  game.win = 0;
  game.lose = 0;
  game.west = 0;
  game.score = [];

  console.log(game);
}

function resetBord(k) {
  console.log(game.score);
  for (let i = 1; i <= 3; i++) {
    c = ".col" + i;
    for (let j = 1; j <= 3; j++) {
      r = "#cell" + String(j) + String(i);
      $$$(c)[0].querySelector(r).innerHTML = "";
    }
  }
  records.you = [];
  records.co = [];
  records.mainStack = [11, 12, 13, 21, 22, 23, 31, 32, 33];
  records.term = 0;
  records.toggel = k ? true : !records.toggel;
  console.log(records);
}

function reset() {
  resetgame();
  resetBord(true);
  resetrows();
  scoreBord();
}

function newgame(y, x) {
  l = game.score.length + 1;

  if (y == 1) {
    game.win++;
    game.score.push(1);
  } else if (y == -1) {
    game.lose++;
    game.score.push(-1);
  } else {
    records.term != 0 ? (game.west++, game.score.push(0)) : 0;
    if (x != null && records.term != 0) addRow(true);
  }

  scoreBord();
  resetBord(false);
}

// main process

function rowCol(k) {
  const paper = {
    row: { 1: 0, 2: 0, 3: 0 },
    col: { 1: 0, 2: 0, 3: 0 },
    xdig: 0,
    ydig: 0,
  };

  myStack = k ? records.you : records.co;

  for (let i = 0; i < myStack.length; i++) {
    element = myStack[i];
    first_elm = parseInt(element / 10);
    second_elm = element % 10;

    if (paper.row[first_elm] < 3) {
      paper.row[first_elm]++;
    }

    if (paper.col[second_elm] < 3) {
      paper.col[second_elm]++;
    }

    if (first_elm == second_elm) {
      if (paper.xdig < 3) {
        paper.xdig++;
        if (first_elm == 2) paper.ydig++;
      }
    } else if (first_elm + second_elm == 4) {
      if (paper.ydig < 3) {
        paper.ydig++;
      }
    }

    if (
      paper.row[first_elm] == 3 ||
      paper.col[second_elm] == 3 ||
      paper.xdig == 3 ||
      paper.ydig == 3
    ) {
      return true;
    }
  }

  return false;
}

// event logic

function addMove(x, y) {
  if(records.toggel){
    if (records.mainStack.length % 2 == 0) {
      x = true;
    } else {
      x = false;
    }
  }
  else{
    if (records.mainStack.length % 2 != 0) {
      x = true;
    } else {
      x = false;
    }
  }
  

  if (y.childNodes.length == 0) {
    records.term++;
    x
      ? records.you.push(parseInt(y.id[4] + y.id[5]))
      : records.co.push(parseInt(y.id[4] + y.id[5]));

    removeElm(y.id[4] + y.id[5]);

    let k = $$("div");
    k.className = x ? "you" : "co";
    y.appendChild(k);
  } else {
    alert("this box is not empty");
  }

  setTimeout(() => {
    t = rowCol(x);
    console.log(t);
    if (t) {
      let b = x ? -1 : 1
      alert(b == 1? "i win" : "you win");
      scoreBord();
      newgame(b);
      addRow(false);
    } else if (records.term == 9) {
      alert("tia");
      newgame(0);
      addRow(false);
    }
  }, 500);
}


function addRow(y){
  
  var tbody = $('table').getElementsByTagName('tbody')[0];

  var newRow = tbody.insertRow();

  var i = newRow.insertCell();
  i.textContent = game.score.length; 
  let x = game.score[game.score.length - 1];
  
  var r1 = newRow.insertCell();
  var r2 = newRow.insertCell();
  var r3 = newRow.insertCell();
  if(x == 1){
    r1.textContent = '\u2713';
    y ? r1.style.color = 'red': 0;
    r2.textContent = "";
    r3.textContent = "";
  }
  else if(x == -1){
    r1.textContent = "";
    r2.textContent = "\u2713";
    y ? (r2.style.color = "red") : 0;
    r3.textContent = "";
  }
  else{
    r1.textContent = "";
    r2.textContent = "";
    r3.textContent = "\u2713";
    y ? (r3.style.color = "red") : 0;
  }
}

function active(){
  let b = $("#active");
  if (!records.iScore){
    b.textContent = 'show board';
    b.style.color = "white";
    b.style.backgroundColor = "rgb(96, 175, 96)";
    
    $(".col1").style.display = "none";
    $(".col2").style.display = "none";
    $(".col3").style.display = "none";
    $("table").style.display = "grid";
    records.iScore = !records.iScore;
  } 
  else{
    b.textContent = "show score";
    b.style.color = "black";
    b.style.backgroundColor = "white";
    $(".col1").style.display = "inline-flex";
    $(".col2").style.display = "inline-flex";
    $(".col3").style.display = "inline-flex";
    $("table").style.display = "none";
    records.iScore = !records.iScore;
  }
}

function resetrows(){
  let y = $("table").getElementsByTagName("tbody")[0];
  y.textContent = "";

  var newRow = y.insertRow();

  var i = newRow.insertCell();
  i.textContent = "round"
  var r1 = newRow.insertCell();
  r1.textContent = "i win";
  var r2 = newRow.insertCell();
  r2.textContent = "you win";
  var r3 = newRow.insertCell();
  r3.textContent = "no win";

  i.className = "th";
  r1.className = "th";
  r2.className = "th";
  r3.className = "th";
}
