# Represents the node of list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    # Declaring head and tail pointer as null.
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    # This function will add the new node at the end of the list.
    def add(self, data):
        newNode = Node(data)
        # Checks if the list is empty.
        if self.head.data is None:
            # If list is empty, both head and tail would point to new node.
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            # tail will point to new node.
            self.tail.next = newNode
            # New node will become new tail.
            self.tail = newNode
            # Since, it is circular linked list tail will point to head.
            self.tail.next = self.head

    # Displays all the nodes in the list
    def display(self):
        current = self.head
        if self.head is None:
            print("리스트가 비었습니다.")
            return
        else:
            print("원형 링크드 리스트의 노드들: ")
            # Prints each node by incrementing pointer.
            print(current.data),
            while(current.next != self.head):
                current = current.next
                print(current.data),


if __name__=="__main__":
    cl = CircularLinkedList()
    # Adds data to the list
    cl.add("코드 실행")
    cl.add("생각")
    cl.add("구글링")
    cl.add("복사 붙여넣기")
    # Displays all the nodes present in the list
    cl.display()
