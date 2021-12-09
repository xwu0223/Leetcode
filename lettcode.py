class Solution:
    import numpy as np
    import collections
    def isPalindrome(self, x: int) -> bool:
        count = 0
        if (x<0) | x> (2**31 -1):
            return False
        elif ((x <100) & (x >=10)):
            if str(x)[0]==str(x)[1]:
                return True
            else:
                return False
        elif ((x<10) & (x>=0)):
                return True 
        elif len(str(x))%2 == 0:
            for i in range(int(len(str(x))/2)):
                if str(x)[i]!=str(x)[len(str(x))-i-1]:
                    count=count+1
                else:
                    count=count
        elif len(str(x))%2 == 1:
            for i in range(int((len(str(x))-1)/2)):
                if str(x)[i]!=str(x)[len(str(x))-i-1]:
                    count=count+1
                else:
                    count=count
        if count>0:
            return False
        else:
            return True
    

    def romanToInt(self, s: str) -> int:
        rom_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        for i in range(len(s)):
            if i>0 and rom_map[s[i]]>rom_map[s[i-1]]:
                result += rom_map[s[i]]-2*rom_map[s[i-1]]
            else:
                result += rom_map[s[i]]
        return result

    def longestCommonPrefix(self, strs: List[str]) -> str:
        arr_len = []
        ary=""
        count = []
        non_match = 0
        
        for i in range(len(strs)):
            arr_len.append(len(list(strs[i])))
        
        for i in range(min(arr_len)):
            for j in range(len(strs)-1):
                if list(strs[j])[i]!=list(strs[j+1])[i]:
                    non_match+=1
            count.append(non_match)
        for i in range(min(arr_len)):
            if count[i]==0:
                ary=ary+list(strs[0])[i]
        return ary
    
    def isValid(self, s: str) -> bool:
        par = {'[':']','(':')','{':'}'}
        stack = []
        for i in s:
            if i in par:
                stack.append(i)
            elif len(stack)==0 or par[stack.pop()] != i:
                return False
        return len(stack)== 0
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy_node = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1= l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        
        return dummy_node.next
    
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1
        return l

    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.insert(-1,target)
            nums.sort()
            return nums.index(target)

    def firstUniqChar(self, s: str) -> int:
        cnt = collections.Counter(s)
        count = 0
        for idx,ch in enumerate(s):
            if cnt[ch] != 1:
                return False
        return True
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_1 = list(s1)
        s2_1 = list(s2)
        for i in range(len(s2_1)-len(s1_1)+1):
            if sorted(s2_1[i:(i+len(s1_1))]) == sorted(s1_1):
                return True
        return False

    # dummy function
    def a(b):
        return b
    # read here
    
                
    
                

