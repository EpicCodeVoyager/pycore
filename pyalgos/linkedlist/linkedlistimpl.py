class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def setNext(self, data):
        self.next = data


class LinkedList:
    def __init__(self, node):
        self.head = node

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def insertAfter(self, node, dataI):
        temp = self.head
        while (temp is not None):
            if temp == node:
                newNode = Node(dataI)
                newNode.next = temp.next
                temp.next = newNode
                return
            temp = temp.next


node1 = Node(1)
ll = LinkedList(node1)

node2 = Node(2)
node1.setNext(node2)

node3 = Node(3)
node2.setNext(node3)

node4 = Node(4)
node3.setNext(node4)


ll.insertAfter(node3, 15)
ll.insertAfter(node4, 15)
ll.printList()
