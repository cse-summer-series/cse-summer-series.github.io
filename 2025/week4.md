Hi all!

Here with summer series updates!

🔗 **Links and Resources**

- Through our _undergraduate committee_, faculty around the department have open
  office hours for students to come by and talk about a variety of topics. Check
  ouf the table and the calendar on [this
  page](https://cse.ucsd.edu/undergraduate/advising/undergraduate-committee-ugcom-advising-and-mentorship),
  which gets updated throughout the year.
- I continue to hold **Remote Office Hours** on Tuesdays at 11am pacific time
  for the rest of the summer. You can find the link through [my contact
  page](https://jpolitz.github.io/contact/) which has a calendar of many
  advising office hours!
- I got a few questions about _tutoring_, which is a role where undergraduates
  work for a course as an instructional assistant. Check out [the CSE tutoring
  page](https://cse.ucsd.edu/undergraduate/undergraduate-tutors) for more
  details.


The website
[https://cse-summer-series.github.io/2025/](https://cse-summer-series.github.io/2025/)
has all of the summer series messages.


✅ **Do Now! (Do one, some, or all!)**

- Watch [the video about search tree checking](https://youtu.be/GBvzkgYFkiM):

    https://youtu.be/GBvzkgYFkiM

    This one looks at the key properties of binary _search_ trees.

    https://leetcode.com/problems/validate-binary-search-tree/submissions/1752652924/

- Fill out the [welcome form](https://docs.google.com/forms/d/1wymRYUsQMA4gWiz7-WIsBGSEFOJXBZIsnp39gKfBnQs/preview) if you haven't – if you have, you should have gotten an email from me by now saying hi and replying to your questions.

- Join the [Discord server](https://discord.gg/4zexzTVv6Z) and say hi:
  
  [https://discord.gg/4zexzTVv6Z](https://discord.gg/4zexzTVv6Z)

  I will also be posting assignment solutions given by students with some discussion to Discord.

- Do your best to complete the [Recover Binary Search
  Tree](https://leetcode.com/problems/recover-binary-search-tree/description/)
  problem in a programming language of your choice:

  https://leetcode.com/problems/recover-binary-search-tree/description/
  
  
- As another kind of review (and preparation for CSE29!) try taking my Java
  solution (below/in video) and translate it to a C solution. Review past videos
  to see how I approached tree programming with C structs and pointers.
  
- For either or both of those tasks, share your solution with me by replying to
  this
  email or putting the code in a direct message on Discord. I'll share some
  answers that I see on Discord next week.


The code from today's video is copied here for your reference:

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
    public boolean isValidBST(TreeNode root) {
        if(root == null) { return true; }
        else {
            boolean leftIsBST = isValidBST(root.left);
            boolean rightIsBST = isValidBST(root.right);
            boolean leftAllSmaller = allSmaller(root.left, root.val);
            boolean rightAllLarger = allLarger(root.right, root.val);
            return leftIsBST && rightIsBST && leftAllSmaller && rightAllLarger;
        }
    }

    public boolean allLarger(TreeNode node, int val) {
        if(node == null) { return true; }
        else {
            if(node.val <= val) { return false; }
            return allLarger(node.left, val) && allLarger(node.right, val);
        }
    }

    public boolean allSmaller(TreeNode node, int val) {
        if(node == null) { return true; }
        else {
            if(node.val >= val) { return false; }
            return allSmaller(node.left, val) && allSmaller(node.right, val);
        }
    }
}
```



