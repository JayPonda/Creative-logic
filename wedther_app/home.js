tab = 1;

// onload functions
function tostring(ostring) {
  let str = "";
  for (let i = 0; i < ostring.length; i++) {
    str = str + ostring[i];
  }
  return str;
}

function avalibility() {
  var statusForInternat = window.navigator.onLine;
  if (statusForInternat) return true;
  else return false;
}

//functions wich is interecting with apis
("use strict");

const API_KEY = "YOUR_KEY";

const request = async (url) => {
  try {
    const response = await fetch(url);
    return response.ok ? response.json() : Promise.reject({ error: 500 });
  } catch (err) {
    console.log(err);
    return Promise.reject({ error: 400 });
  }
};

const getInfo = async (x) => {
  try {
    if (x == 1) {
      let c = document.getElementById("city");
      const url = `https://api.openweathermap.org/data/2.5/weather?q=${c.value}&appid=${API_KEY}`;
      const response = await request(url);
      console.log(response.weather[0].main);
      document.getElementById("lon").value = response.coord.lon;
      document.getElementById("lat").value = response.coord.lat;
      setElements(response);
    } else if (x == 2) {
      let lat = document.getElementById("lat");
      let lon = document.getElementById("lon");
      let c = document.getElementById("city");
      const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat.value}&lon=${lon.value}&appid=${API_KEY}`;
      const response = await request(url);
      c.value = response.name;
      console.log(response.name, response);
      setElements(response);
    } else {
      console.log(x);
    }
  } catch (err) {
    console.log(err.error);
    if (err.error == 500) {
      setElements(1);
    } else if (err.error == 400) {
      setElements(0);
    } else {
      setElements(-1);
    }
  }
};

function setElements(data) {
  let notify = document.querySelector("#header");
  let e1 = document.querySelector("#short1");
  let e2 = document.querySelector("#disc1");
  let e3 = document.querySelector("#icne1");
  let e4 = document.querySelector("#tem");
  let e5 = document.querySelector("#min-tem");
  let e6 = document.querySelector("#max-tem");
  let e7 = document.querySelector("#location");
  let e8 = document.querySelector("#short2");
  let e9 = document.querySelector("#disc2");
  let e10 = document.querySelector("#icne2");

  if (data != null && data != 1 && data != -1 && data != 0) {
    const url = `http://openweathermap.org/img/wn/${data["weather"][0]["icon"]}.png`;

    e1.innerText = data["weather"][0]["main"];
    e2.innerText = data["weather"][0]["description"];
    e3.src = url;

    e8.innerText = data["weather"][0]["main"];
    e9.innerText = data["weather"][0]["description"];
    e10.src = url;

    e4.innerText =
      "temperature: " + parseInt((data.main.temp - 273) * 100) / 100 + " \xB0C";
    e5.innerText = "pressure: " + data["main"]["pressure"];
    e6.innerText = "humidity: " + data.main.humidity + " %";

    e7.textContent = data["name"];

    notify.style.display = "none";
  } else if (data == 1) {
    notify.textContent = "This location is unknown";
    notify.style.display = "block";
    notify.style.backgroundColor = "#931bd8";
  } else if (data == 0) {
    notify.textContent = "you are not in active connection";
    notify.style.display = "block";
    notify.style.backgroundColor = "#fffb0b";
  } else {
    notify.textContent = "unknown error";
    notify.style.display = "block";
    notify.style.backgroundColor = "#002586";

    makeoffline();
  }
}

// event handling functions

function searchcity(x) {
  document.getElementById("current_date").innerHTML = getDate();
  //console.clear();
  if (!avalibility()) makeoffline();
  else {
    console.log(x);
    getInfo(x);
  }
}

function makeoffline() {
  let notify = document.querySelector("#header");
  notify.textContent = "You are not connected with internet";
  notify.style.display = "block";
  notify.style.backgroundColor = "#e40a0a";
  console.log(notify);

  document.querySelectorAll("#form")[0].style.display = "none";
  document.querySelectorAll("#form")[1].style.display = "none";
}

function makedefault() {
  document.querySelector("#short1").textContent = "wedther";
  document.querySelector("#disc1").textContent = "disc";
  document.querySelector("#icne1").src = "test2.jpg";
  document.querySelector("#tem").textContent = "--";
  document.querySelector("#min-tem").textContent = " -- ";
  document.querySelector("#max-tem").textContent = " -- ";
  document.querySelector("#location").textContent = "location";
  document.querySelector("#short2").textContent = "wedther";
  document.querySelector("#disc2").textContent = "disc";
  document.querySelector("#icne2").src = "test2.jpg";
}

function previous() {
  document.getElementById("current_date").innerHTML = getDate();
  if (!avalibility()) {
    makeoffline();
  } else {
    document.querySelectorAll("#form")[0].style.display = "block";
    document.querySelectorAll("#form")[1].style.display = "block";
    document.querySelector("#header").style.display = "none";
  }
  if (tab == 1) {
    document.getElementById("tab3").style.display = "inline";
    document.getElementById("tab2").style.display = "none";
    document.getElementById("tab1").style.display = "none";
    tab = 3;
  } else if (tab == 2) {
    document.getElementById("tab1").style.display = "inline";
    document.getElementById("tab2").style.display = "none";
    document.getElementById("tab3").style.display = "none";
    tab--;
  } else {
    document.getElementById("tab2").style.display = "inline";
    document.getElementById("tab1").style.display = "none";
    document.getElementById("tab3").style.display = "none";
    tab--;
  }
}

function next() {
  document.getElementById("current_date").innerHTML = getDate();
  if (!avalibility()) {
    makeoffline();
  } else {
    document.querySelectorAll("#form")[0].style.display = "block";
    document.querySelectorAll("#form")[1].style.display = "block";
    document.querySelector("#header").style.display = "none";
  }
  if (tab == 1) {
    document.getElementById("tab2").style.display = "inline";
    document.getElementById("tab1").style.display = "none";
    document.getElementById("tab3").style.display = "none";
    tab++;
  } else if (tab == 2) {
    document.getElementById("tab3").style.display = "inline";
    document.getElementById("tab2").style.display = "none";
    document.getElementById("tab1").style.display = "none";
    tab++;
  } else {
    document.getElementById("tab1").style.display = "inline";
    document.getElementById("tab2").style.display = "none";
    document.getElementById("tab3").style.display = "none";
    tab = 1;
  }
}

function getDate() {
  let mon = [
    "jan",
    "fab",
    "mar",
    "apr",
    "may",
    "jun",
    "jul",
    "aug",
    "sep",
    "oct",
    "Nov",
    "dec",
  ];
  let today = new Date();
  let month = mon[today.getMonth()];
  let year = today.getFullYear();
  let date = today.getDate();

  let hour = today.getHours();
  hour = hour > 12 ? hour - 12 : hour;
  hour = hour < 10 ? "0" + hour : hour;
  let minute = today.getMinutes();
  minute = minute < 10 ? "0" + minute : minute;
  let second = today.getSeconds();
  second = second < 10 ? "0" + second : second;

  return `${date}, ${month} ${year}  ${hour}:${minute}:${second}`;
}

//initial active call

document.getElementById("current_date").innerHTML = getDate();
document.getElementById("tab1").style.display = "inline";
searchcity(1);
