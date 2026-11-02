import ListNode

def twoNumber(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.vasl if l2 else 0

        number = x + y + carry
        carry = number // 10
        number = number % 10

        curr.next = ListNode(number)
        curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next