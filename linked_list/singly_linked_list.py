class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

class LinkedList(object):
    # ll의 헤드를 정의한다.
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data, end="=>")
            temp = temp.next

    def insertAtStart(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertBetween(self, previousNode, data):
        # 입력한 노드 위치 다음에 넣는다.
        # previousNode => Node(data) => previousNode.next
        if (previousNode.next is None):
            print("이전 노드의 다음 노드가 없습니다.")
        else:
            newNode = Node(data)
            newNode.next = previousNode.next
            previousNode.next = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode

    def delete(self, data):
        temp = self.head

        if temp.next is not None:
            # data가 head node의 data일 경우
            if(temp.data == data):
                self.head = temp.next
                temp = None
                return 
            else:
                # data를 찾는 while문
                while temp.next != None:
                    if temp.data == data:
                        break
                    prev = temp
                    temp = temp.next

                # data를 못 찾은 경우
                if temp == None:
                    return

                prev.next = temp.next
                return

    def search(self, node, data):
        if node == None:
            return False
        if node.data == data:
            return True
        return self.search(node.getNext(), data)

if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node("어, 다시 올라가네")
    node2 = Node("나비였네.")
    ll.head.setNext(node2)
    node3 = Node("그 사이에")
    node2.setNext(node3)
    ll.insertAtStart("꽃잎 하나가 떨어지네")
    ll.insertBetween(node2, "너와 나의 삶...")
    ll.insertAtEnd("벚꽃의 삶이 있다.")
    ll.printLinkedList()
    print()
    ll.delete("그 사이에")
    ll.printLinkedList()
    print()
    print(ll.search(ll.head, "어, 다시 올라가네"))
    
    
    
    