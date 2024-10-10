function solution(array) {
    array.sort(function(a,b) {
        return a - b;
    })
    
    var answer = array[Math.floor(array.length /2)];
    return answer;
}