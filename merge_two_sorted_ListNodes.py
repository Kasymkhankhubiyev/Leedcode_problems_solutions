def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) ->Optional[ListNode]:
        result = finish = ListNode()

        
        if not list1 and not list2:
            return list1
        elif not list1:
            return list2
        elif not list2:
            return list1
        else:
            while list1 or list2:
                if not list1:
                    result.next = list2
                    # result = list2
                    list2, result = list2.next, list2
                    
                elif not list2:
                    result.next = list1
                    # result = list1
                    list1, result = list1.next, list1
                    
                elif list1.val < list2.val:
                    result.next = list1
                    # result = list1
                    list1, result = list1.next, list1
                    
                else:
                    result.next = list2
                    # result = list2
                    list2, result = list2.next, list2
                    
            return finish.next
