
// 힙은 배열을 이용하여 구현한다.
// 연결 리스트로도 구현할 수는 있지만 특정 노드를 검색, 이동하는 과정이 번거롭기 때문.
// 배열의 경우 랜덤 액세스가 가능하기 때문에 좀더 효율적이다.
// 배열로 구현하는 경우
// - 구현의 용이함을 위해 시작 인덱스(root)는 1부터 시작한다.
// - 각 노드와 대응되는 배열의 인덱스는 불변한다.
// - 왼쪽 자식 노드 인덱스 = 부모 노드 인덱스 * 2
// - 오른쪽 자식 노드 인덱스 = 부모 노드 인덱스 * 2 + 1
// - 부모 노드 인덱스 = 자식 노드 인덱스 / 2
class MinHeap {
    constructor() {
        this.heap = [0];
        this.size = 0;
    }

    isEmpty(){
        return this.size == 0;
    }

    getParent(i){
        return this.heap[i/2];
    }

    getLeft(i){
        return this.heap[i*2];
    }

    getRight(i){
        return this.heap[i*2 + 1];
    }

    swap(a, b) {
        [ this.heap[a], this.heap[b] ] = [ this.heap[b], this.heap[a] ];
    }


    heappush(value){
        // 새로운 value를 일단 push
        this.heap.push(value)
        this.size += 1;
        // 마지막 요소의 인덱스 부터 시작해서
        let curIdx = this.size;
        let parIdx = parseInt(curIdx / 2);

        // 부모 노드의 값이 현재 노드의 값보다 크면
        while(curIdx > 1 && this.heap[parIdx] > this.heap[curIdx]) {
            // 현재 노드의 값과 부모 노드의 값을 스왑
            this.swap(parIdx, curIdx);
            // 한단계 올라간다.
            curIdx = parIdx;
            parIdx = parseInt(curIdx / 2);
        }

        this.heap[curIdx] = value;
    }


    heappop(){
        // 빈 힙 예외 처리
        if(this.isEmpty()){
            console.log("empty heap");
            return;
        }

        // 루트 노드를 삭제하고
        let oldRoot = this.heap[1];
        // 배열의 맨 마지막 원소를 기준으로 정렬 시작.
        let last = this.heap.pop();
        this.size -= 1;

        let parentIdx = 1;
        let childIdx = 2;
        while(childIdx <= this.size){
            // 오른쪽 자식이 더 작으면 오른쪽으로 이동
            if(childIdx < this.heap.length && this.getLeft(parentIdx) > this.getRight(parentIdx)){
                childIdx += 1
            }

            // last 보다 큰 값을 만나면 더이상 내려가는게 의미가 없으므로 break;
            if(last <= this.heap[childIdx]) break;

            // sift-up 과정:
            // 값을 갱신하고
            this.heap[parentIdx] = this.heap[childIdx];
            // 다음 탐색을 위해 한단계 아래로 이동한다.
            parentIdx = childIdx;
            childIdx *= 2;
        }

        // 기준 노드를 최종 위치에 저장하고
        this.heap[parentIdx] = last;
        // 삭제된 루트 노드를 반환한다.
        return oldRoot;

    }

}

let minHeap = new MinHeap();
minHeap.heappush(10);
minHeap.heappush(5);
minHeap.heappush(30);
minHeap.heappush(8);
minHeap.heappush(9);
minHeap.heappush(3);
minHeap.heappush(7);
console.log(minHeap.heap);

for(let i = 1; i <= 7; i++){
    console.log(minHeap.heappop())
}

// 정리하기!


