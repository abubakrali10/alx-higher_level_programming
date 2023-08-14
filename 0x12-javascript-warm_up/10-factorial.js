#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (isNaN(x) || x < 0) {
  console.log(1);
} else {
  console.log(factorial(x));
}

function factorial (n) {
  if (n === 1) {
    return n;
  } else {
    return n * factorial(n - 1);
  }
}
