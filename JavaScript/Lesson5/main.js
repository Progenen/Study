'use strict';

const usdCurr = 490;
const discount = .9;

function convert(ammount, curr) {
    return curr * ammount;
}

function promotion(res) {
    console.log(res * discount);
}

const sum = convert(500, usdCurr);

// promotion(sum);

function test(a) {
    for (let i = 0; i < 5; i++) {
        console.log(i);
        if (i === a) return;
    }
    console.log("End test")
}

// test(3);

function getMathResult(a, b) {
    let res = '';
    
    if (b <= 0 || typeof b != "number") {
        return a;
    }
    
    for (let i = 1; i <= b; i++) {
        if (i == 1) {
            res += a + '';
        } else {
            res += '---' + a * i;
        }
    }

    return res;
}

console.log(getMathResult(5, 3));


