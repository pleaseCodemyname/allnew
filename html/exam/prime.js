onmessage = function (e) {
    let num = parseint(e.data.from);
    let isPrime = true;
    for(let i=2; i<num; i++)
      if(num%i ==0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime == true) {
    postMessage(`${num} is a Prime Number`);
  } else {
    postMessage(`${num} is not a Prime Number`);
}