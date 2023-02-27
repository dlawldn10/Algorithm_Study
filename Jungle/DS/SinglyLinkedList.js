class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    /* data를 갖는 노드를 찾는다. */
    find(data) {
        let thisList = this;

        // 빈 리스트에 대해 탐색 시도 시 즉시 반환
        if (thisList.head == null){
            console.log("빈 리스트입니다.");
            return null
        }

        // 앞에서부터 옆으로 한칸씩 가며 탐색.
        let curNode = thisList.head;
        while(curNode != null){
            // 일치하는 data를 찾은 경우 해당 노드 반환
            if(curNode.data == data) return curNode;

            curNode = curNode.next;
        }

        console.log("해당 노드를 찾을 수 없습니다.");   // 못찾고 끝에 다다른 경우 즉시 반환
        return null
    }

    /* 리스트 맨 마지막에 추가하기 */
    append(data) {
        let newNode = new Node(data);
        let thisList = this;
        
        if (thisList.head == null){
            thisList.head = newNode;    // 이 리스트가 빈 리스트였다면 새로운 노드를 head, tail로 설정한다.
            thisList.tail = newNode;
        }else{
            thisList.tail.next = newNode;   // 빈리스트가 아니었다면 tail 옆에 추가한다.
            thisList.tail = newNode;    // 추가된 노드를 리스트의 tail로 설정해준다.
        }
        
        thisList.size++;    // 리스트의 사이즈 업데이트

    }

    /* preNode 다음에 data 값을 갖는 노드를 삽입한다. */
    insert(preNode, data) {
        // 이전 노드가 null 이면 즉시 반환
        if (preNode == null) return

        let thisList = this;
        let newNode = new Node(data);
        // 이전 노드가 이 리스트의 tail 이었다면
        // 새로 추가된 노드를 tail로 업데이트
        if(preNode == thisList.tail) thisList.tail = newNode;
        newNode.next = preNode.next;
        preNode.next = newNode;
        thisList.size++
        
        return 
    }


    /* 인자로 받은 data를 갖는 노드를 삭제 */
    remove(data) {
        let thisList = this;
        // 삭제하고자 하는 데이터가 head인 경우
        if(thisList.head.data == data) {
            // 삭제 진행
            thisList.size--;

            // head와 tail 업데이트
            if(thisList.size > 1) {
                thisList.head = thisList.head.next;
            }else if(thisList.size == 1){
                thisList.head = thisList.head.next;
                thisList.tail = thisList.head;
            }else if(thisList.size == 0){
                thisList.head = null;
                thisList.tail = null;
            }

            return
        }

        // 앞에서부터 탐색하면서 삭제하고자 하는 노드의 바로 앞 노드를 찾음.
        let preNode = thisList.head;
        while(preNode.next != null){
            // 바로 앞 노드를 찾은 경우
            if(preNode.next.data == data){
                // 삭제 진행
                preNode.next = preNode.next.next
                thisList.size--;
                
                if(preNode.next == null) thisList.tail = preNode;   // 삭제한 노드가 tail 이었다면 preNode를 새로운 tail으로 업데이트.
                return
            }
            preNode = preNode.next;
        }
        
        // 못찾고 끝에 다다른 경우 즉시 반환
        console.log("해당 노드를 찾을 수 없습니다.");   
        return null
    }

    /* 리스트 처음부터 끝까지 노드들을 출력 */
    retrieve(){

        if(this.size == 0) {
            console.log("[ ] head: null tail: null");
            return
        }

        let node = this.head;
        let str = "";
        str += '[ '
        while(node != null){
            str += node.data;
            str += ' ';
            node = node.next;
        }
        str += ']';
        console.log(str + ' head: ' + this.head.data + ' tail: ' + this.tail.data );

    }
}


const linkedList = new SinglyLinkedList();
linkedList.append(1);
linkedList.append(6);
linkedList.append(2);
linkedList.append(8);
linkedList.retrieve();
linkedList.insert(linkedList.find(6), 21);
linkedList.retrieve();
linkedList.remove(2);
linkedList.retrieve();
linkedList.insert(linkedList.find(8), 30);
linkedList.remove(1);
linkedList.retrieve();

const linkedList2 = new SinglyLinkedList();
linkedList2.append(1);
linkedList2.append(6);
linkedList2.retrieve();
linkedList2.remove(1);
linkedList2.retrieve();
linkedList2.remove(6);
linkedList2.retrieve();
linkedList.insert(linkedList.find(0), 21);
linkedList2.append(7);
linkedList2.retrieve();