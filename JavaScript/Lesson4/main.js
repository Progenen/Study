// 25. (д) Еще раз про аргументы функций

const usdCurr = 28;
const eurCurr = 32;

function convert (amount, curr) {
    console.log(curr * amount);
}

convert(500, usdCurr);
convert(500, eurCurr);