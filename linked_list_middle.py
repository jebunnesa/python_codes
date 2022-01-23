class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_middle_of_linked_list(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    return slow

def find_mid_brute_force(head):
    length = 0
    temp = head
    while temp is not None:
        length += 1
        temp = temp.next
    if length%2 == 0:
        length //= 2
        length +=1
    else:
        length = (length+1)//2
    current = head
    for i in range(length-1):
        print(current.value)
        current = current.next



def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Middle Node: " + str(find_middle_of_linked_list(head).value))

    head.next.next.next.next.next = Node(6)
    print("Middle Node: " + str(find_middle_of_linked_list(head).value))

    head.next.next.next.next.next.next = Node(7)
    print("Middle Node: " + str(find_middle_of_linked_list(head).value))
    print(find_mid_brute_force(head))


main()