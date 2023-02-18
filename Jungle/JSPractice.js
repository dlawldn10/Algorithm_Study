// 두 수의 합
function solution(num1, num2) {
    return num1 + num2;
}

// 두 수의 차
function solution(num1, num2) {
    return num1 - num2;
}

// 두 수의 곱
function solution(num1, num2) {
    return num1 * num2;
}

// 몫 구하기
function solution(num1, num2) {
    return parseInt(num1/num2);
}

// 두 수의 나눗셈
function solution(num1, num2) {
    return parseInt((num1 / num2)*1000);
}

// parseInt() : 
// - 문자열에서 숫자 추출하기. 
//   단, parseInt("50 100 150 200")은 50만 반환한다. 주어진 문자열의 첫번째 값만 추출하기 때문
//   또한 주어진 문자열이 숫자로 시작되지 않는 경우 NaN을 반환하므로 주의.
// - 실수를 정수로 만들기(소수점 뒤의 숫자들은 버린다.)
// - 10진수를 n진수로 바꾸기
//   ex) parseInt("50", 16) -> 80

// 숫자 비교하기
function solution(num1, num2) {
    return num1 === num2 ? 1 : -1
}

// == : 값이 같은지를 비교
// === : 값과 값의 타입이 모두 같은지를 비교


// 분수의 덧셈
function solution(numer1, denom1, numer2, denom2) {
    var answer = []
    
    // 통분, 덧셈
    var sum = numer1*denom2 + numer2*denom1
    var denom = denom1*denom2

    // 최대공약수 구하기
    var lcm = 0
    for(let i = 1 ; i <= sum ; i ++) {
        if(sum%i === 0 && denom%i === 0) {
            lcm = i
        }
    }

    // 약분하여 대입
    answer.push(sum/lcm)
    answer.push(denom/lcm)

    return answer;
}

// 참고) 유클리드 호제법
// num1 * num2 = gcd * lcm

// 최소공배수 구하기
let getLCM = (num1, num2) =>{
	let lcm = 1;
   
    while(true){
      if((lcm % num1 == 0) && (lcm % num2 == 0)){
        break;
      }
      lcm++;
    }
  	return lcm
}

// 재귀를 이용하여 최대공약수 구하기
// a % b == 0 이면 b 가 최대공약수
function getGCD(a, b){
    return (a % b) ? getGCD(b, a % b) : b;
}

// 배열 두배 만들기
function solution(numbers) {

    var answer = [];
    for (i=0; i < numbers.length ; i++){
        answer.push(numbers[i]*2)
    }
    return answer;

    // 또는
    return numbers.map( v => v*2 )
}


// 나머지 구하기
function solution(num1, num2) {
    return num1 % num2;
}


// 중앙값 구하기
function solution(array) {
    // 숫자 오름차순 정렬
    array.sort(function(a, b)  { return a - b; });
    return array[parseInt(array.length/2)];

    // 좀더 간략히 하면
    return array.sort( (a, b) =>  a - b )[parseInt(array.length/2)];
}


// 최빈값 구하기
function solution(array) {
    let map = new Map();
    for (let i of array){
        if (map.get(i)) map.set(i, map.get(i)+1)
        else map.set(i, 1)
    }
    
    var counts = [...map.values()]
    var max = Math.max(...counts)
    map = [...map].filter(it => it[1] == max)
    
    return map.length === 1 ? map[0][0] : -1
}


// 짝수는 싫어요
function solution(n) {
    var answer = [];
    for(let i = 1; i <= n; i++){
        if (i % 2 != 0){
            answer.push(i)
        }
    }

    // 또는
    for (let i=1; i <= n; i += 2) answer.push(i)

    return answer;
}

// 피자 나눠먹기(1)
function solution(n) {
    // 7로 나누고 올림
    return Math.ceil(n/7);
}

// 올림
// Math.ceil() 함수
// 내림
// Math.floor()
// 반올림
// Math.round()
// 소수점 반올림
// toFixed(), toPrecision()

// 피자 나눠먹기(2)
function solution(n) {
    let i = 1
    while (true){
        if ((i*6) % n == 0) return i
        i++
    }
}

// 피자 나눠먹기(3)
function solution(slice, n) {
    return  Math.ceil(n/slice);
}


// 배열의 평균값
function solution(numbers) {
    return numbers.reduce((acc, num) => acc + num) / numbers.length
}


// 옷가게 할인받기
function solution(price) {
    var answer = price;
    if (500000 <= price) answer *= 0.80
    else if(300000 <= price) answer *= 0.90
    else if(100000 <= price) answer *= 0.95
    return parseInt(answer);
}


// 아이스 아메리카노
function solution(money) {
    var answer = [];
    answer.push(parseInt(money/5500))
    answer.push(money%5500)
    return answer;
}


// 나이 출력
function solution(age) {
    return 2022 - age;
}


// 배열 뒤집기
function solution(num_list) {
    return num_list.reverse();
}


// 문자열 뒤집기
function solution(my_string) {
    let answer = [];
    for (let i = my_string.length-1; i >= 0; i--){
        answer.push(my_string[i])
    }
    return answer.join('');

    // 또는
    return [...my_string].reverse().join("")
}


// 직각 삼각형 출력하기
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    let n = Number(input[0])
    for (let i = 1; i <= n; i++){
        console.log('*'.repeat(i))
    }
});


// 짝수 홀수 갯수
function solution(num_list) {
    // 짝수, 홀수
    var answer = [0, 0];
    num_list.forEach( it => {
        if (it % 2 == 0) answer[0] += 1
        else answer[1] += 1
    })
    return answer;

    // 또는 reduce 사용
    return num_list.reduce((acc, cur) => (cur % 2 == 0 ? acc[0]++ : acc[1]++, acc), [0, 0])
}


// 문자 반복 출력하기
function solution(my_string, n) {
    var answer = '';
    answer = [...my_string].map( it => { it.repeat(n) })
    return answer;
}


// 특정 문자 제거하기
function solution(my_string, letter) {
    return [...my_string].filter( it => it != letter).join("");

    // 또는
    return my_string.split(letter).join("")

    // 또는
    return my_string.replaceAll(letter, "")
}


// 각도기
function solution(angle) {

    if (0 < angle && angle < 90) return 1
    else if(angle == 90) return 2
    else if(90 < angle && angle < 180) return 3
    else return 4

    // 또는 삼항연산자 사용
    return angle < 90 ? 1 : angle === 90 ? 2 : angle < 180 ? 3 : 4;
}


// 양꼬치
function solution(n, k) {
    return n * 12000 + (k - parseInt(n/10)) * 2000
}


// 짝수의 합
function solution(n) {
    var answer = 0;
    for (let i = 2; i <= n; i += 2){
        answer += i
    }
    return answer;
}


// 배열 자르기
function solution(numbers, num1, num2) {
    return numbers.slice(num1, num2+1);
}


// 외계행성의 나이
function solution(age) {
    var answer = '';
    let alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    answer = age.toString()
    return [...answer].map(it => alpha[it]).join("");

    // 또는
    // .split("") 을 이용해서 string 객체를 array로 바꿀 수 있다.
    return age
        .toString()
        .split("")
        .map((v) => "abcdefghij"[v])
        .join("");
}


// 진료 순서 정하기
function solution(emergency) {
    let list = [...emergency].sort((a, b) => b - a)
    return emergency.map((num, index) => list.indexOf(num)+1);
}


// 순서쌍의 갯수
function solution(n) {
    var answer = 0;
    let i = 0
    while (i < n){
        i++
        if (n % i == 0) answer++
    }
    return answer;
}


// 개미 군단
function solution(hp) {
    var answer = 0;
    answer = parseInt(hp / 5)
    answer = answer + parseInt((hp % 5) / 3)
    answer = answer + parseInt((hp % 5) % 3)
    return answer;
}


// 모스 부호
function solution(letter) {
    let morse = {
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }

    return letter.split(' ').map(it => morse[it]).join("");
}


// 가위 바위 보
function solution(rsp) {
    var answer = '';
    for (let r of rsp) {
        switch (r){
            case 2:
                answer += '2'
                break
            case 0:
                answer += '5'
                break
            case 5:
                answer += '2'
                break
        }
    }

    // 또는 객체를 사용하여
    let arr = {
        2: 0,
        0: 5,
        5: 2
    };
    var answer = [...rsp].map(v => arr[v]).join("");
    return answer;
}


// 구슬을 나누는 경우의 수
// 조합의 경우의 수를 구하는 문제이므로 팩토리얼을 이용해서 구할 수 있다.
// 팩토리얼
function solution(balls, share) {
    if (share === 0) return 1
    return  factorial(balls) / (factorial(balls - share) * factorial(share))
}

function factorial(n) {
    let re = BigInt(1)

    for (let result = 2; result <= n; result++) {
        re *= BigInt(result)
    }
    return re
}


// 점의 위치 구하기
function solution(dot) {
    if (dot[0] > 0 && dot[1] > 0) return 1
    else if (dot[0] < 0 && dot[1] > 0) return 2
    else if (dot[0] < 0 && dot[1] < 0) return 3
    else return 4
}


// 2차원으로 만들기
function solution(num_list, n) {
    var answer = [];
    for (let i = 0; i < num_list.length; i += n) {
        answer.push(num_list.slice(i, i+n))
    }

    // 또는
    while(num_list.length) {
        answer.push(num_list.splice(0,n));
    }

    return answer;
}


// 공 던지기
function solution(numbers, k) {
    return numbers[(2 * (k -1)) % numbers.length];
}


// 배열 회전시키기
function solution(numbers, direction) {
    var answer = [];
    if (direction == "right") {
        numbers.unshift(numbers.pop())
    }else{
        numbers.push(numbers.shift())
    }
    return answer;
}


// 주사위의 개수
function solution(box, n) {
    return parseInt(box[0]/n) * parseInt(box[1]/n) * parseInt(box[2]/n);

    // 또는
    return box.reduce( (acc, val) => acc * parseInt(val/n), 1)
}


// 합성수 찾기
function solution(n) {
    var answer = 0;
    for (let i = 2; i <= n; i++) {
        let count = 1
        let j = 2
        while (j <= i){
            if (i % j == 0){
                count++
                if (count >= 3) {
                    answer++
                    break
                }
            }
            j++
        }
    }
    return answer;

    // DP 로도 풀 수 있다.
    let dp = new Array(n+1).fill(1)
    for(let i = 2 ; i <= n ; i++){
        if(dp[i]){
            for(let j = 2 ; i*j <= n ; j++){
                dp[i*j] = 0
            }
        }
    }

    return dp.filter(el => el === 0).length
}


// 최댓값 만들기
function solution(numbers) {
    let sorted = numbers.sort((a, b) => b - a)
    return sorted[0] * sorted[1];
}


// 팩토리얼
function solution(n) {
    if(n <= 1) return 1

    let re = 1
    for (let result = 2; true; result++) {
        re *= result
        if (re > n) return result-1
    }
}


// 모음 제거
// 정규표현식 - replace
function solution(my_string) {
    return my_string.replace(/[aeiou]/gi, "")
}


// g : 대소문자 구분
// gi : 대소문자 구분 없음


// 문자열 정렬하기
// 정규표현식 - match
function solution(my_string) {
    return my_string.match(/[0-9]/g).map(Number).sort((a,b) => a-b);
}


// 숨어있는 숫자의 덧셈
function solution(my_string) {
    return my_string.match(/[0-9]/g).map(Number).reduce((acc, cur) => acc + cur)
}


// 소인수 분해
function solution(n) {
    var answer = [];
    for (let i = 2; i <= n; i++) {
        if (n % i == 0) {
            answer.push(i)
            while (n % i == 0){
                n /= i
            }
        }
    }

    return answer;
}


// 배열 원소의 길이
function solution(strlist) {
    return strlist.map(it => it.length)
}


// 중복된 문자 제거
function solution(my_string) {
    let set = new Set(my_string);
    return [...set].join("");
}


// 삼각형의 완성 조건(1)
function solution(sides) {
    sides = sides.sort((a, b) => a - b)
    return sides[0] + sides[1] > sides[2] ? 1 : 2;
}


// 삼각형의 완성 조건(2)
function solution(sides) {
    var answer = 0;
    sides = sides.sort((a, b) => a - b)

    // sides[1]이 가장 긴 변
    // answer = sides[1] - (sides[1] - sides[0]) - 1

    // 새로운 변이 가장 긴 변
    // answer += sides[0] + sides[1] - sides[1]

    // 위의 식들을 정리하면
    answer = 2 * sides[0] - 1

    return answer;
}


// 가까운 수
// sort() 정렬조건 여러개
function solution(array, n) {
    // 먼저 두 수의 차이 작은 순서로 정렬 후
    // 두 수의 크기가 작은 순서로 정렬
    return array.map(e => [e, Math.abs(e-n)] ).sort( (a,b) => a[1] - b[1] || a[0] - b[0] )[0][0]
}






