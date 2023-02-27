class Node {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor() {
        this.root = null;
    }

    /* 정렬되어 있는 배열 array 를 BST로 만든다. */
    makeTree(array){
        this.root = this.makeTreeRecur(array, 0, array.length-1);
    }

    makeTreeRecur(array, start, end){
        if(start > end) return null;

        let mid = parseInt((start + end) / 2);
        

        let node = new Node(array[mid]);
        node.left = this.makeTreeRecur(array, start, mid - 1);
        node.right = this.makeTreeRecur(array, mid + 1, end);
        return node;
    }

    /* find 값을 갖는 노드를 탐색한다. */
    search(curNode, find){

        // 트리 말단에 도달한 경우 리턴
        if(curNode == null) return curNode

        if(find < curNode.data){
            console.log("data is smaller than " + curNode.data);
            this.search(curNode.left, find);
        }else if(find > curNode.data){
            console.log("data is bigger than " + curNode.data);
            this.search(curNode.right, find);
        }else if(find == curNode.data){
            console.log("data found!");
            return curNode;
        }
    }

    /* 트리 말단에 노드를 하나 추가한다. */
    insert(newData){
        // root가 변경되었을 수 있기 때문에 결과를 받아 root 갱신해준다.
        this.root = this.insertRecur(this.root, newData);
    }

    /* 노드를 insert 할 위치를 찾아 들어간 후 노드를 추가. */
    insertRecur(root, newData){
        // 트리가 비어있거나, 말단에 도달해 노드 추가하는 경우
        if(root == null) {
            root = new Node(newData);
            return root;
        }

        // 아직 자리를 찾지 못한경우, 추가 재귀
        // 추가하고자 하는 값이 현재 노드의 값보다 작은 경우 -> 왼쪽 서브트리로 이동
        if(newData < root.data){
            root.left = this.insertRecur(root.left, newData);
        }
        // 추가하고자 하는 값이 현재 노드의 값보다 큰 경우 -> 오른쪽 서브트리로 이동
        else if(newData > root.data){
            root.right = this.insertRecur(root.right, newData);
        }

        return root;

    }



    /* 노드 하나를 삭제한다. */
    delete(data){
        // root가 삭제되었을 수 있기 때문에 결과를 받아 root 갱신해준다.
        this.root = this.deleteRecur(this.root, data);
    }

    /* 삭제할 노드를 찾아 들어간 후 해당 노드를 삭제 */
    deleteRecur(root, data){
        // 트리가 비어있거나, 말단에 도달한 경우, 대체될 노드에 도달한 경우.
        if(root == null) return root;

        // 아직 노드를 찾지 못한경우, 추가 재귀
        // 삭제하고자 하는 값이 현재 노드의 값보다 작은 경우 -> 왼쪽 서브트리로 이동
        if(data < root.data){
            root.left = this.deleteRecur(root.left, data);
        }
        // 삭제하고자 하는 값이 현재 노드의 값보다 큰 경우 -> 오른쪽 서브트리로 이동
        else if(data > root.data){
            root.right = this.deleteRecur(root.right, data);
        }
        // 삭제할 데이터를 찾은 경우
        else{
            // 말단 노드를 삭제하는 경우.
            if(root.left == null && root.right == null) return null;
            // 자식이 하나인 노드를 삭제하는 경우.
            else if(root.left == null) return root.right;
            else if(root.right == null) return root.left;
            // 자식이 두개인 노드를 삭제하는 경우.

            // 오른쪽 서브트리에서 제일 작은 값(또는 왼쪽 서브트리에서 제일 큰값)을 가져와 
            // 삭제된 노드의 자리에 끼워넣는다.
            // 원래 있던 자리의 링크를 끊는다.
            root.data = this.findMin(root.right);
            root.right = this.deleteRecur(root.right, root.data);

        }
        return root;

    }

    /* 주어진 root부터 왼쪽 자식들을 타고 내려가 서브트리의 최소값을 알아낸다. */
    findMin(root){
        let min = root.data;
        while(root.left != null){
            min = root.left.data;
            root = root.left;
        }
        return min;
    }

    /* 트리를 전위순회하며 노드들의 값을 출력한다. */
    printInorder(){
        this.inorderRecur(this.root);
        console.log("");
    }

    inorderRecur(root){
        if(root != null){
            this.inorderRecur(root.left);
            console.log(root.data);
            this.inorderRecur(root.right);
        }
    }

}

let array = [4,2,1,3,6,5,7]
let bstree = new BinarySearchTree();
bstree.makeTree(array);
// bstree.insert(4);
// bstree.insert(2);
// bstree.insert(1);
// bstree.insert(3);
// bstree.insert(6);
// bstree.insert(5);
// bstree.insert(7);
bstree.printInorder();

bstree.insert(10);
bstree.insert(8);
bstree.printInorder();

bstree.delete(5);
bstree.printInorder();