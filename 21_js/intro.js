/* Team Jam Juice (Jonathan Lee, Jeffrey Huang)
SoftDev
K21 - - Get Scripty
2021-04-09 */

function factI(n) { //returns factorial of n, computed iteratively.
    if (n < 0) return "error, negative input";
    else if (n == 0) return 1;
    for (var i = n - 1; i > 0; i--) {
      n = n * i;
    }
    return n;
  }

  function factR(n) { //returns factorial of n, computed recursively.
    if (n < 0) return "error, negative input";
    else if (n == 0) return 1;
    else if (n == 1) return 1;
    else return n * factR(n-1);
  }

  function fibI(n) { //returns the nth Fibonacci number, computed iteratively.
    var ans = 0;
    var pri = 0;
    var sec = 1;
    if (n < 0) return "error, negative input";
    else if (n == 0) return 0;
    else if (n == 1) return 1;
    for (var i = 1; i < n; i++) {
      ans = pri + sec;
      pri = sec;
      sec = ans;
    }
    return ans;
  }

  function fibR(n) { //returns the nth Fibonacci number, computed recursively.
    if (n < 0) return "error, negative input";
    else if (n == 0) return 0;
    else if (n == 1) return 1;
    else return fibR(n-1) + fibR(n-2);
  }

  console.log(factI(2)); //should be 2
  console.log(factR(2)); //should be 2
  console.log(fibI(2)); //should be 1
  console.log(fibR(2)); //should be 1
  console.log(fibI(4)); //should be 3
  console.log(fibR(4)); //should be 3
  console.log(fibI(5)); //should be 5
  console.log(fibR(5)); //should be 5
