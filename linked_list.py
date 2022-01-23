class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next
        print()


def find_cycle_start(head):
    slow, fast = head, head
    cycle_len = 0
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            cycle_len = calculate_cycle_length(fast)
            break
    return cycle_first_node(cycle_len, head)


def cycle_first_node(cycle_len, head):
    pointer1 = head
    pointer2 = head
    while cycle_len > 0:
        pointer2 = pointer2.next
        cycle_len -= 1
    while pointer2 != pointer1:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


def calculate_cycle_length(fast):
    current = fast
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == fast:
            break
    return cycle_length



def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))
    

main()