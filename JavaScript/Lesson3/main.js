// 22. (д) Цикл в цикле и метки

// for (let i = 0; i < 3; i++) {
//     console.log(i);
//     for (let j = 0; j < 3; j++) {
//         console.log(j);
//     }
// }

let lines = 5;
let result = '';

for (let i = 0; i <= lines; i++) {
    for(let j = 0; j <= i; j++) {
        result += "*";
    }

    result += "\n"
}

first: for (let i = 0; i < 3; i++) {
    console.log("Первый уровень, энтропия: " + i)
    for (let j = 0; j < 3; j++) {
        console.log("Второй уровень, энтропия: " + i)
        for (let k = 0; k < 4; k++) {
            if (k === 3) {
                console.log(i + " Чртывйе уревоьн, яэпрнтпии:") 
                continue first
            }
            console.log("Третий уровень, энтропия: " + i)
        
        }
    }
}