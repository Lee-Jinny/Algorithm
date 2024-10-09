function solution(numer1, denom1, numer2, denom2) {
    let den = denom1 * denom2; 
    let num = numer1 * denom2 + numer2 * denom1; 
    let gda;
    
    // 분모와 분자의 최대공약수 구하기
    for (let i = 1; i <= Math.min(den, num); i++) {
        if ((den % i == 0) && (num % i == 0)) {
            gda = i; 
        } 
    }
    
    // 분자와 분모의 최대공약수로 나눈 분수 출력
    answer = [num/gda, den/gda]
    
    return answer;
}