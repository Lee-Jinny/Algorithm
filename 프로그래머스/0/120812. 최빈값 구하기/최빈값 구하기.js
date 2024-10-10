function solution(array) {
    const count = {};

    // 각 요소의 개수를 세기
    for (let i = 0; i < array.length; i++) {
        if (array[i] in count) {
            count[array[i]]++;
        } else {
            count[array[i]] = 1;
        }
    }

    // 최빈값을 찾기 위한 변수
    const maxCnt = Math.max(...Object.values(count)); // 최대 카운트
    const multipleMax = Object.values(count).filter(value => value === maxCnt).length > 1; // 중복 여부 확인

    // 중복된 최빈값이 있는 경우 -1 반환, 그렇지 않으면 최빈값 반환
    return multipleMax ? -1 : parseInt(Object.keys(count).find(key => count[key] === maxCnt));
}