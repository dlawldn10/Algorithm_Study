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


// 컨트롤 제트
function solution(s) {
    var stack = [];

    s.split(' ').forEach(it => {
        if (it != 'Z') stack.push(it)
        else stack.pop()
    })

    return stack.map(Number).reduce((acc, val) => acc + val, 0);
}


// 삼육구 게임
function solution(order) {
    var answer = 0;
    order.toString().split('').forEach(it => {
        if (it == '3' || it == '6' || it == '9') answer++
    })
    return answer;

    // 또는 matchAll() 사용
    return [...order.toString().matchAll(/[3|6|9]/g)].length

}


// 암호 해독
function solution(cipher, code) {
    var answer = '';
    for (let i = code-1 ; i < cipher.length; i += code) {
        answer += cipher[i]
    }
    return answer;
}


// 대문자와 소문자
function solution(my_string) {
    let answer = '';
    [...my_string].forEach(it => {
        if (it.match(/[a-z]/g)) answer += it.toUpperCase()
        else answer += it.toLowerCase()
    });
    return answer;

    // 또는
    return [...my_string].map(it => {
        if (it.match(/[a-z]/g)) it = it.toUpperCase()
        else it = it.toLowerCase()
        return it
    }).join("");

}


// 인덱스 바꾸기
function solution(my_string, num1, num2) {
    let copy = [...my_string];
    let tmp = my_string[num1];
    copy[num1] = copy[num2]
    copy[num2] = tmp
    return copy.join('');

    // 또는
    my_string = my_string.split('');
    [my_string[num1], my_string[num2]] = [my_string[num2], my_string[num1]];
    return my_string.join('');
}


// 한번만 등장한 문자
function solution(s) {
    var answer = new Set();

    for (let i = 0; i < s.length; i++) {
        if (s.split('').filter( it => s[i] === it).length === 1){
            answer.add(s[i])
        }
    }

    return [...answer].sort().join('');


    // 또는 lastIndexOf() 함수를 이용
    let res = [];
    for (let c of s) if (s.indexOf(c) === s.lastIndexOf(c)) res.push(c);
    return res.sort().join('');
}



// 약수 구하기
function solution(n) {
    var answer = [];
    let i = 1;
    while (i <= n){
        if (n % i == 0) answer.push(i)
        i++
    }
    return answer;
}



// 영어가 싫어요
function solution(numbers) {
    let array = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ];
    for (let i=0; i < array.length; i++) {
        numbers = numbers.split(array[i]).join(i.toString())
    }
    return parseInt(numbers);

    // 또는 객체 + 정규 표현식 + replace() 콜백 이용
    const obj = {
        zero: 0, one: 1, two: 2, three: 3, four: 4,
        five: 5, six: 6, seven: 7, eight: 8, nine: 9
    };

    const num = numbers.replace(/zero|one|two|three|four|five|six|seven|eight|nine/g, v => obj[v]);

    return Number(num);
}


// 잘라서 배열로 저장하기
function solution(my_str, n) {
    var answer = [];
    for (let i = 0; i < my_str.length; i += n) {
        answer.push(my_str.split('').slice(i, i+n).join(''))
    }
    return answer;
}



// 문자열 계산하기
function solution(my_string) {
    return eval(my_string);

    // 또는
    const stack = [];

    let sign = 1;
    for (const ch of my_string.split(" ")) {
        if (ch === "+") {
            sign = 1;
        } else if (ch === "-") {
            sign = -1;
        } else {
            stack.push(ch * sign);
        }
    }

    return stack.reduce((a,b) => a + b, 0);
}



// 외계어 사전
// dfs 순열 사용
let result = Array(10).fill(0)
let checklist = Array(10).fill(0)
let permutations = []
function solution(spell, dic) {
    dfs(0, spell)
    console.log(permutations)

    for (let word of dic) {
        for (let permutation of permutations) {
            if (word == permutation){
                return 1
            }
        }
    }

    return 2;
}

function dfs(L, spell) {
    if (L == spell.length) {
        permutations.push(result.filter(it => it != 0).join(''));
    }
    else {
        for (let i = 0; i < spell.length; i++){
            if (checklist[i] == 0){
                result[L] = spell[i];
                checklist[i] = 1
                dfs(L+1, spell)
                checklist[i] = 0
            }
        }
    }

}


// 또는
// 그냥 정렬해서 내용 같으면 1 return
function solution(spell, dic) {
    spell = spell.sort().join("")
    dic = dic.filter((el)=>el.split("").sort().join("") == spell)
    return dic[0] ? 1 : 2
}



// 문자열 밀기
// 2:37
// 2:44
function solution(A, B) {
    let Aarray = A.split('');
    for (let i = 0; i < A.length; i++) {
        if (Aarray.join('') == B) return i
        Aarray.unshift(Aarray.pop())
    }
    return -1;

    // 또는
    // B 2개를 이어붙여서 A가 시작되는 인덱스를 리턴한다. = 몇번 밀면 되는지 나온다.
    return (B+B).indexOf(A)
}



// 폰켓몬
// 2:49
// 3:02
function solution(nums) {
    var answer = 0;
    nums.sort((a, b) => a - b)
    let map = new Map()
    let pre = 0
    for (let num of nums) {
        if (num != pre){
            pre = num
            map.set(num, 1)
        }else{
            map.set(num, map.get(num) + 1)
        }
    }
    console.log(map)
    if (map.size >= nums.length/2) answer = parseInt(nums.length/2)
    else answer = map.size
    return answer;

    // 또는
    // 여기서는 종류 수만 세면 되니까 세트 사용했어도 됨.
    const max = nums.length / 2;
    const arr = [...new Set(nums)];
    return arr.length > max ? max : arr.length
}



// 완주하지 못한 선수
// 3:06
// 3:14
function solution(participant, completion) {
    // let partiMap = new Map()
    // for (let p of participant) {
    //     if (!partiMap.has(p)){
    //         partiMap.set(p, 1)
    //     }else{
    //         partiMap.set(p, partiMap.get(p) + 1)
    //     }
    // }
    //
    // for (let c of completion) {
    //     if (partiMap.has(c)){
    //         partiMap.set(c, partiMap.get(c) - 1)
    //     }
    // }
    //
    // for (let pair of partiMap) {
    //     if (pair[1] != 0) return pair[0]
    // }

    // 위 코드를 좀더 간단하게 하면
    let partiMap = new Map()
    for (let i = 0; i < participant.length; i++) {
        let a = participant[i], b = completion[i];

        partiMap.set(a, (partiMap.get(a) || 0) + 1);
        partiMap.set(b, (partiMap.get(b) || 0) - 1);
    }

    for (let [name, count] of partiMap) {
        if (count != 0) return name
    }
}


// 위장
// 3:21
// 3:38
function solution(clothes) {
    // let map = new Map()
    // for (let [name, kind] of clothes) {
    //
    //     if (map.has(kind)) {
    //         let tmp = map.get(kind);
    //         tmp.push(name);
    //         map.set(kind, tmp)
    //     }
    //     else map.set(kind, [ name ])
    //
    // }
    // return [...map].reduce((acc, val) => acc * (val[1].length + 1), 1) -1;

    // 여기도 마찬가지로 갯수만 있어도 답을 구할 수 있기 때문에
    // 이렇게 바꿀 수 있다.
    let map = new Map()
    for (let [name, kind] of clothes) {
        map.set(kind, (map.get(kind) || 1) + 1);
    }
    return [...map].reduce((acc, val) => acc * val[1], 1) -1;
}


// 베스트 앨범
// 4:04
// 5:00
function solution(genres, plays) {
    var answer = [];
    let map = new Map();
    for (let i = 0; i < genres.length; i++) {
        let tmp = (map.get(genres[i]) || [])
        tmp.push([i, plays[i]])
        map.set(genres[i], tmp)
    }

    // 장르 내 정렬 -> map
    for (let [genre, play] of map) {
        play.sort((a, b) => b[1] - a[1])
    }

    // 장르별 정렬한 키 결과 -> newMap
    let newMap =[...map].sort((a, b) => {
        let tmpB = b[1].reduce((acc, val) => acc + val[1], 1)
        let tmpA = a[1].reduce((acc, val) => acc + val[1], 1)
        return tmpB - tmpA
    }).map(it => [it[0], []]);

    // 장르별 정렬한 키 결과대로 newMap 채우기
    for (let i=0; i < map.size; i++) {
        newMap[i][1] = map.get(newMap[i][0]);
    }

    // newMap 에서 2개씩 뽑기
    for (let [genre, play] of newMap) {
        for (let i = 0; i < play.length; i++) {
            if (i == 2) break
            answer.push(play[i][0])
        }
    }
    return answer;
}



// k 번째 수
function solution(array, commands) {
    var answer = [];
    for (let cmd of commands) {
        answer.push(array.slice(cmd[0]-1, cmd[1]).sort((a, b) => a-b)[cmd[2]-1])
    }
    return answer;
}


// 가장 큰 수
// 5:35
// --
// 시간 초과 및 런타임 에러
// let n = []
// let permutations = []
// let checklist = []
// let result = []
// let max = 0
// function solution(numbers) {
//     n = numbers.map(String);
//     checklist = Array(n.length).fill(0)
//     result = Array(n.length).fill("")
//     // dfs 순열 사용
//     dfs(0, n);
//     return max.toString();
// }
//
// function dfs(L, n) {
//     if (L == n.length) {
//         if (parseInt(result.join('')) >= max) max = parseInt(result.join(''))
//         else return
//     }
//     else {
//         for (let i = 0; i < n.length; i++){
//             if (checklist[i] == 0){
//                 result[L] = n[i];
//                 checklist[i] = 1
//                 dfs(L+1, n)
//                 checklist[i] = 0
//             }
//         }
//     }
//
// }

function solution(numbers) {
    numbers = numbers.map(String)
    numbers.sort((a, b) => parseInt(b+a) - parseInt(a+b))
    return numbers.join('').indexOf(0) == 0 ? '0' : numbers.join('');

    // 또는
    // ${}로 숫자 이어붙여서 정렬후 join
    let answer = numbers.sort((a, b) => `${b}${a}` - `${a}${b}`).join('');
    return answer[0] === '0' ? '0' : answer;
}



// H-Index
// 6:25
// 6:29
function solution(citations) {
    var answer = 0;
    let h = Math.max(...citations);
    while (true){
        let count = 0;
        citations.forEach(it => {
            if (it >= h) count++
        })
        if (count >= h) return h
        h--
    }
    return answer;

    // 또는
    // 정렬을 먼저 한 다음에 수행
    citations = citations.sort((a, b) => b - a);
    var i = 0;
    while(i + 1 <= citations[i]){
        i++;
    }
    return i;

}



// 최소 직사각형
// 7:21
// 7:30
function solution(sizes) {
    let xMax = 0;
    let yMax = 0;
    sizes.forEach(it => {
        it.sort((a, b) => a - b)
        xMax = Math.max(it[0], xMax);
        yMax = Math.max(it[1], yMax);
    })

    return xMax*yMax;
}



// 모의고사
// 7:31
// 8:03
function solution(answers) {
    let count = [0, 0, 0];
    let one = [1, 2, 3, 4, 5];
    let two = [2, 1, 2, 3, 2, 4, 2, 5];
    let three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

    let i = 0
    while (i < answers.length){
        if (one[i%5] == answers[i]) count[0] += 1
        if (two[i%8] == answers[i]) count[1] += 1
        if (three[i%10] == answers[i]) count[2] += 1
        i++
    }

    let max = Math.max(...count);
    let answer = []
    count.forEach((it, idx) => {
        if (it == max) answer.push(idx+1)
    })

    return answer.sort((a, b) => a - b)
}



// 소수 찾기
// 8:03
// 8:49
let result = []
let checklist = []
let permutations = new Set()
function solution(numbers) {
    var answer = 0;
    numbers = numbers.split('');
    let sets = new Set();
    // 조합 찾기
    for (let i = 1; i <= numbers.length; i++) {
        for (let j of getCombinations(numbers, i)){
            sets.add(j)
        }
    }

    // 찾은 조합에 대해 순열 구하기
    for (let set of sets) {
        result = Array(set.length).fill('');
        checklist = Array(set.length).fill(0);
        getPermutations(0, set)
    }


    // 찾은 순열에 대해 소수 판별
    for (let permutation of permutations) {
        if (isPrime(permutation)) {
            answer++
        }
    }

    return answer;
}

function getCombinations(arr, N) {
    const results = [];
    if (N === 1) return arr.map((value) => [value]);

    arr.forEach((fixed, index, origin) => {
        const rest = origin.slice(index + 1);
        const combinations = getCombinations(rest, N - 1);
        const attached = combinations.map((combination) => [fixed, ...combination]);
        results.push(...attached);
    });

    return results;
}

function getPermutations(L, arr) {
    if (L == arr.length) {
        permutations.add(parseInt(result.join('')));
    }
    else {
        for (let i = 0; i < arr.length; i++){
            if (checklist[i] == 0){
                result[L] = arr[i];
                checklist[i] = 1
                getPermutations(L+1, arr)
                checklist[i] = 0
            }
        }
    }

}

function isPrime(n){
    if (n == 0 || n == 1) return false

    let i = 2;
    while (i < Math.sqrt(n)){
        if (n % i == 0) return false
        i++
    }
    return true;
}


// 좀더 개선된 풀이
// 정리:
// - DFS 사용하여 순열 구하기
// - 효율적으로 소수 찾기
// - 중복제거를 위한 set 사용
// - (내부 함수 사용)
function solution(numbers) {
    let check = Array(numbers.length).fill(0);
    let result = new Set();

    function DFS(acc, level, check){
        if (level == numbers.length){
            result.add(Number(acc))
        }else{
            for (let i = 0; i < numbers.length; i++){
                if (!check[i]){
                    check[i] = 1
                    DFS(acc+numbers[i], level+1, check)
                    DFS(acc, level+1, check)
                    check[i] = 0
                }
            }
        }
    }

    function isPrime(n){
        if (n <= 1) return false
        for (let i = 2; i <= Math.sqrt(n); i++){
            if (n % i == 0) return false
        }
        return true
    }

    DFS('', 0, check);
    return [...result].filter(it => isPrime(it)).length
}



// 카펫
// 10:00
// 10:17
function solution(brown, yellow) {
    let i = 1;
    while (i <= yellow){
        if (yellow % i == 0){
            let yellow_w = i;
            let yellow_y = yellow/i;
            if ((yellow_w+2) * (yellow_y+2) - yellow == brown) {
                return [yellow_w+2, yellow_y+2].sort((a, b) => b - a)
            }
        }
        i++
    }
    return []

}



// 피로도
// 10:18
// 11:18
// 방향을 잘못 잡았었다...순열 처럼 구현하면 안되고 그냥 단순하게 구현하면 되는 문제였음.
// 꼭 루트를 다 구하려고 하지 말고 갯수를 셀것!
function solution(k, dungeons) {
    let route = [];
    let count = 1;
    let check = Array(dungeons.length).fill(0);

    function DFS(count, k){
        for (let i = 0; i < dungeons.length; i++) {
            if (!check[i] && dungeons[i][0] <= k){
                check[i] = 1;
                route.push(count)
                DFS(count+1, k-dungeons[i][1]);
                check[i] = 0;
            }
        }
    }

    DFS(count, k)

    return Math.max(...route);
}




















