instr = [0, "", 0];
//buffer_values  = [acc, sign, digit]
index = 0;
flag = false; // initialize the acc
count = false; // can count with acc
negflag = false; // panding negative
flotflag = false; // is float ?

function calculat(par = null) { 
  switch (par ? par : instr[1]) {
    case "c":
      instr = [0, "", 0];
      index = 0;
      flag = false;
      count = false;
      negflag = false;
      break
    case 'n':
      instr[index] *= -1
      break
    case "+":
      instr[0] += instr[2];
      break;
    case "-":
      instr[0] -= instr[2];
      break;
    case "*":
      instr[0] *= instr[2];
      break;
    case "/":
      instr[0] /= instr[2];
      break;
  }
}

function digitCalculation(val){
  if (!Number.isInteger(instr[index])) {
    return parseFloat(String(instr[index]) + String(val))
  }
  else if (instr[index] >= 0)
  {          
    return instr[index] * 10 + val;
  }
  else{
    return instr[index] * 10 - val;
  }
}

function calcdriver(val) {
  if(val == 'n'){
    if(index != 1){
      calculat(val)
    }
    else{
      negflag = true
    }
  }
  else if(val == '%'){
    if (index != 1) {
      instr[index] /= 100
    } else {
      instr[2] /= 100
    }
  }
  else if (!flag) {
    if (!isNaN(val)){
      instr[index] = digitCalculation(val)
    }
    else if(val == '%'){
      instr[index] /= 100
    }
    else{
      flag = true
      index += 1
      if(['+', '-', '*', '/'].includes(val)){
        instr[index] = val;
      }
      else{
        console.log('errer')
      }
    } 
  }
  else{
    if (!isNaN(val)) {
      if (count) {
        calculat("c");
      }

      if (index == 1) {
        index += 1;
        instr[index] = 0;
      }

      instr[index] = digitCalculation(val);
      if (negflag) {
        calculat("n");
        negflag = false;
      }
    } else if (val == "=") {
      if (index == 2) {
        calculat();
      }
      count = true;
      console.log("ans", instr[0]);
    } else {
      if (index == 2) {
        !count ? calculat() : "";
        index -= 1;
      }
      instr[index] = val;
      count = false;
    }
  }
  console.log(val, instr,index, flag, negflag, count);
}

calcdriver(8)
calcdriver(9);
calcdriver(3);
calcdriver('-');
calcdriver(5);
calcdriver(2);
calcdriver(6);
calcdriver('+');
calcdriver(4);
calcdriver(5);
calcdriver(0);
calcdriver('*');
calcdriver(2);
calcdriver(5);
calcdriver('=');
