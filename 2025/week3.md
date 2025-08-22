Hi all!

Here with summer series updates!

🔗 **Links and Resources**

Important enrollment deadlines are coming up! Check out these links for
information on the enrollment process:

https://cse.ucsd.edu/undergraduate/courses/enrolling-cse-courses

https://cse.ucsd.edu/undergraduate/fall-2025-undergraduate-course-updates

In particular: “CSE/EC26 Major Major Priority Deadline: **Tuesday, August 26th
11:59PM** - Current incoming CSE/EC26 majors who want enrollment priority must
waitlist their requested applicable courses by the stated date/time.”

So please reach out, make sure you've had a look at classes, reach out to
advising if needed, and understand that if you're a CSE major getting on
waitlists before Tuesday is important!

I continue to hold **Remote Office Hours** on Tuesdays at 11am pacific time for the rest of the summer. You can find the link through [my contact page](https://jpolitz.github.io/contact/) which has a calendar of many advising office hours!

The website [https://cse-summer-series.github.io/2025/](https://cse-summer-series.github.io/2025/) has all of these messages


✅ **Do Now! (Do one, some, or all!)**

- Watch [the video of solving a Leetcode problem about trees](https://youtu.be/Ay7ecVA0pco):

    https://youtu.be/Ay7ecVA0pco

    This one is about reviewing how to write recursive functions over (binary) trees.

    https://leetcode.com/problems/univalued-binary-tree/

- Fill out the [welcome form](https://docs.google.com/forms/d/1wymRYUsQMA4gWiz7-WIsBGSEFOJXBZIsnp39gKfBnQs/preview) if you haven't – if you have, you should have gotten an email from me by now saying hi and replying to your questions.

- Join the [Discord server](https://discord.gg/4zexzTVv6Z) and say hi:
  
  [https://discord.gg/4zexzTVv6Z](https://discord.gg/4zexzTVv6Z)

  I will also be posting assignment solutions given by students with some discussion to Discord.

- Do your best to complete the [Symmetric Tree](https://leetcode.com/problems/symmetric-tree) problem in a programming language of your choice:

  https://leetcode.com/problems/symmetric-tree

  Then, share your solution with me by replying to this email or putting the
  code in a direct message on Discord. I'll share some answers that I see on
  Discord next week.


The code from today's video is also copied here for your reference:

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isUnivalTree(TreeNode node) {
        // First check if this node has the same value as left/right children
        // Then, check that left/right children are unival trees
        if(node == null) { return true; }
        boolean leftValOK = (node.left == null) || (node.left.val == node.val);
        boolean rightValOK = (node.right == null) || (node.right.val == node.val);
        if(!leftValOK || !rightValOK) { return false; }

        boolean leftTreeOK = isUnivalTree(node.left);
        boolean rightTreeOK = isUnivalTree(node.right);

        return leftTreeOK && rightTreeOK;
    }

}
```


```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isUnivalTree(struct TreeNode* node) {
    if(node == NULL) { return 1; }
    int leftValOK = (node->left == NULL) || (node->left->val == node->val);
    int rightValOK = (node->right == NULL) || (node->right->val == node->val);
    if(!leftValOK || !rightValOK) { return 0; }

    int leftTreeOK = isUnivalTree(node->left);
    int rightTreeOK = isUnivalTree(node->right);
    return leftTreeOK && rightTreeOK;
}
```

