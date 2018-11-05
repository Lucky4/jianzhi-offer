class Solution:
    def Print(self, pRoot):
        if pRoot == None:
            return []
        
        stack1 = []
        stack2 = []
        
        stack1.append(pRoot)
        level = 1
        
        res = []
        tmp_res = []
        
        while len(stack1) > 0:
            tmp = stack1.pop()
            tmp_res.append(tmp.val)
            
            if level % 2 == 0:
                if tmp.right != None:
                    stack2.append(tmp.right)
                    
                if tmp.left != None:
                    stack2.append(tmp.left)
            else:
                if tmp.left != None:
                    stack2.append(tmp.left)

                if tmp.right != None:
                    stack2.append(tmp.right)
                    
            if len(stack1) == 0:
                level += 1
                stack1 = stack2
                stack2 = []
                res.append(tmp_res)
                tmp_res = []

        return res