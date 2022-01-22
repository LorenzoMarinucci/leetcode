def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        last = first = ListNode()
        ext = 0
        
        while (l1 or l2):
            
            a = b = 0
            
            if (l1):
                a = l1.val
                l1 = l1.next
                
            if (l2):
                b = l2.val
                l2 = l2.next
                
            result = a + b + ext
            ext = result // 10
            
            last.next = ListNode(result % 10)
            last = last.next
                
        if (ext):
            last.next = ListNode(1)
        
        return first.next