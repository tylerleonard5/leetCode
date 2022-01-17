
 struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
  };


#include <iostream>
#include <string>
#include <vector>





class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        std::vector<int> vec;
        int level = height(root);
        addCurrentLevel(root, level, vec);
        return vec.at(0);
    }

    void addCurrentLevel(TreeNode* root, int level, std::vector<int> &vec)
    {
        
        if (root == NULL)
            return;
        if (level == 1)
            vec.push_back(root->val);
        else if (level > 1) {
            addCurrentLevel(root->left, level - 1, vec);
            addCurrentLevel(root->right, level - 1, vec);
        }
    }   

    int height(TreeNode* root){
        if (root == nullptr){
            return 0;
        }
        else{
            int lheight = height(root->left);
            int rheight = height(root->right);

            if(lheight > rheight){
                return lheight + 1;
            }else{
                return rheight + 1;
            }
        }
    }
};