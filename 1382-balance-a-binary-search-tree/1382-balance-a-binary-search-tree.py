# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        def func(arr,left,right):
            if(left<=right):
                mid=(left+right)/2;
                root=TreeNode(arr[mid]);
                root.left=func(arr,left,mid-1);
                root.right=func(arr,mid+1,right);
                return root;
            else:
                return None;
        arr=[];
        def func1(root):
            if(root!=None):
                func1(root.left);
                arr.append(root.val);
                func1(root.right);
        func1(root);
        return func(arr,0,len(arr)-1);
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """