
import singly_linked_list

def reverseLinkedList(myLinkedList):
    previous = None
    current = myLinkedList.head
    while(current != None):
        temp = current.next
        current.next = previous
        previous = current
        current = temp
    myLinkedList.head = previous


if __name__ == '__main__':
    myLinkedList = singly_linked_list.LinkedList()
    for i in range(10, 0, -1):
        myLinkedList.insertAtStart(i)

    print('Original', end=": ")
    myLinkedList.printLinkedList()
    print()
    print('Reversed', end=": ")
    reverseLinkedList(myLinkedList)
    myLinkedList.printLinkedList()