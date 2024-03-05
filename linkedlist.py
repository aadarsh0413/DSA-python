class Node:

  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next


class LinkedList:

  def __init__(self):
    self.head = None

  def insert_at_begining(self, data):
    node = Node(data, self.head)
    self.head = node

  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data, None)
    else:
      itr = self.head
      while itr.next:
        itr = itr.next
      itr.next = Node(data, None)

  def find_length(self):
    count = 1
    itr = self.head
    while itr.next:
      count += 1
      itr = itr.next
    return count

  def insert_any(self, data, index):
    if index < 0 or index >= self.find_length():
      print("Invalid index")
      return
    else:
      count = 0
      itr = self.head
      while itr.next:
        if count == index - 1:
          node = Node(data, itr.next)
          itr.next = node

        itr = itr.next
        count += 1

  def delete_any(self, index):
    if index < 0 or index >= self.find_length():
      print("Invalid index")
      return
    else:
      count = 0
      itr = self.head
      while itr.next != None:
        if count == index - 1:

          itr.next = itr.next.next
          break

        itr = itr.next
        count += 1

  def delete_start(self):
    self.head = self.head.next

  def delete_end(self):
    length = self.find_length() - 1
    self.delete_any(length)

  def print(self):
    if self.head is None:
      print("Linked list is empty")
      return
    itr = self.head
    llstr = ''
    while itr:
      llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
      itr = itr.next
    print(llstr)


if __name__ == '__main__':
  ll = LinkedList()
  ll.insert_at_begining(5)
  ll.insert_at_begining(89)
  ll.insert_at_end(20)
  ll.insert_at_end(70)
  
  ll.insert_any(33, 1)
  ll.print()
  print(ll.find_length())
  # ll.delete_any(1)
  # ll.delete_start()
  ll.delete_end()
  ll.print()
