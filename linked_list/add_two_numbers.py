class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def make_list(nums):
    dummy = ListNode(0)
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            current.next = ListNode(digit)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

# Test cases
sol = Solution()

# Test 1: [2,4,3] + [5,6,4] = [7,0,8] (342 + 465 = 807)
print_list(sol.addTwoNumbers(make_list([2,4,3]), make_list([5,6,4])))

# Test 2: [0] + [0] = [0]
print_list(sol.addTwoNumbers(make_list([0]), make_list([0])))

# Test 3: [9,9,9] + [1] = [0,0,0,1] (999 + 1 = 1000)
print_list(sol.addTwoNumbers(make_list([9,9,9]), make_list([1])))