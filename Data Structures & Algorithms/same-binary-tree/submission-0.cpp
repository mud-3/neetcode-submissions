/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
bool same = true;
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p and !q) {
            return true;
        }
        
        if ((!p and q) or (!q and p) or p->val != q->val) {
            same = false;
            return false;
        }

        isSameTree(p->left, q->left);
        isSameTree(p->right, q->right);

        return same;
    }
};
