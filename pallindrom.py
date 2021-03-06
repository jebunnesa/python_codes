class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def is_palindromic_linked_list(head):
  if head is None or head.next is None:
    return True

  slow, fast = head, head

  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next

  second_half = reverse(slow)
  copy_second_half = second_half
  while head is not None and second_half is not None:
    if head.value != second_half.value:
      break
    head = head.next
    second_half = second_half.next
  reverse(copy_second_half)
  if head is None or second_half is None:
    return True
  return False




def reverse(head):
  prev = None
  while head is not None:
    next = head.next
    head.next = prev
    prev = head
    head = next
  return prev


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))
  head.print_list()
  head.next.next.next.next.next = Node(6)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
