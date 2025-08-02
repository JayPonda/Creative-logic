console.log("hello");

tasks = [];
records = [];
const TASK_PER_PAGE = 10;

// functions for recordes
function $(x) {
  return document.createElement(x);
}

function addrecords(x, y, z) {
  records.push({ full_name: x, gender: y, dob: z });
}

function removerecords(x) {
  for (let k = 0; k < x; k++) {
    records.shift();
  }
}

function addTasks(x) {
  tasks.push(x);
}

function removeTasks() {
  tasks.shift();
}

function taskIn(x){
  for(let i=0; i< tasks.length ; i++){
    if (tasks[i] == x) return true;
  }
  return false;
}

// functions for requirments
function status() {
  return window.navigator.onLine;
}

// functions for creating cards
function makeCard(s, n, g, b) {
  let k = $("div");
  k.id = "cards";
  k.className = "card";

  let k1 = $("div");
  k1.id = "col";
  k1.className = "flex-col";

  let img = $("img");
  img.src = s;
  img.alt = "image not supported";

  k1.appendChild(img);

  let k2 = $("div");
  k2.id = "row";
  k2.className = "flex-row";

  let s1 = $("span");
  s1.textContent = n;

  let s2 = $("span");
  s2.textContent = g;

  let s3 = $("span");
  s3.textContent = b;

  k2.appendChild(s1);
  k2.appendChild(s2);
  k2.appendChild(s3);

  k.appendChild(k1);
  k.appendChild(k2);

  document.querySelector(".box").appendChild(k);
}

// functions for check whether scroll is at bottom or not
function checkbottom(elm) {
  if (
    elm.scrollHeight - elm.scrollTop ===
    elm.clientHeight /* elm.offsetHeight + elm.scrollTop >= elm.scrollHeight*/
  )
  {
    main();
  } 
    
}

const request = async (url) => {
  try {
    const response = await fetch(url);
    return response.ok ? response.json() : Promise.reject({ error: 401 });
  } catch (err) {
    console.log(err);
    return Promise.reject({ error: 402 });
  }
};

// functions for receiving data
async function receiveData(page) {
  try {
    if (!status()) {
      addTasks(page);
      return Promise.reject({ error: 403 });
    } else {
      const res = await request(
        `https://randomuser.me/api/?inc=name,gender,dob&page=${page}&results=${TASK_PER_PAGE}&seed=127`
      );
      return res;
    }
  } catch (err) {
    addTasks(page);
    return Promise.reject({ error: 405 });
  }
}

function setrecords(data) {
  for (let i = 0; i < data.results.length; i++) {
    addrecords(
      data.results[i].name.first + " " + data.results[i].name.last,
      data.results[i].gender,
      data.results[i].dob.date.split("T")[0]
    );
    let url =
      data.results[i].gender == "female"
        ? `https://spng.pngfind.com/pngs/s/114-1146521_girl-avatar-png-picture-female-avatar-no-face.png`
        : `https://spng.pngfind.com/pngs/s/5-52097_avatar-png-pic-vector-avatar-icon-png-transparent.png`;

    makeCard(
      url,
      data.results[i].name.first + " " + data.results[i].name.last,
      data.results[i].gender,
      data.results[i].dob.date.split("T")[0]
    );
  }
}

// main function
async function main() {
  
  if(status()){
    document.querySelector('#btn').style.display = "none";
    if (tasks.length !== 0) {
      for (let i = 0; i <= tasks.length; i++) {
        let data = await receiveData(tasks[i]);
        setrecords(await data);
        removeTasks();
      }
    } else {
      let page = records.length / TASK_PER_PAGE;
      let data = await receiveData(page + 1);
      setrecords(await data);
    }
  }
  else{
    document.querySelector('#btn').style.display = "block";
    if (!taskIn(records.length / TASK_PER_PAGE + 1)) {
      addTasks(records.length / TASK_PER_PAGE + 1);
    }
  }
}

main();
