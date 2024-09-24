const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    result = "";
    for (let c of str){
        result += c.match(/[A-Z]/) !== null ? c.toLowerCase() : c.toUpperCase(); 
    }
    console.log(result);
});