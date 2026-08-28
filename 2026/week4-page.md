# Week 4

<style>
details[id] { border: 1px solid #d0d7de; border-radius: 6px; padding: .5em .75em; margin: .5em 0; }
details[id] > summary { cursor: pointer; font-weight: 600; }
details[id][open] { background: #f6f8fa; }
</style>

## 🧩 The lightning quiz — answers {#answers}

Three proposed strategies for [Symmetric
Tree](https://leetcode.com/problems/symmetric-tree):

1. Do an in-order traversal, check if the resulting list is the same forwards
   and backwards.
2. Check `isSameTree(root.left, root.right)`.
3. Create a mirrored copy of the tree and check if the mirrored copy is
   identical to the original.

Click below to open!

<details id="q-all" markdown="1">
<summary>I said: all of them are correct</summary>

Nope — only one of the three is right! Both 1 and 2 fail, and interestingly
they fail on *different* trees, so no single counterexample catches both. Read
the breakdown below.

</details>

<details id="q-just1" markdown="1">
<summary>I said: just 1 is correct</summary>

Strategy 1 feels so good! But it's wrong. Here's a tree that shows it is
incorrect:

```
        1
      /   \
     3     2
    /     /
   2     3
```

The in-order traversal reads `2, 3, 1, 3, 2` — a perfect palindrome! But the
tree isn't symmetric! The 3 vs 2 positioning is clearly different in the left
and right subtrees.

</details>

<details id="q-just2" markdown="1">
<summary>I said: just 2 is correct</summary>

Not correct! Here's a tree that breaks it:

```
        1
      /   \
     2     2
      \   /
       3 3
```

That tree *is* symmetric — fold it down the middle and it matches. But
`isSameTree(root.left, root.right)` compares `left.left` (null) against
`right.left` (3), says "these differ," and returns false.

The bug is that **equality isn't mirroring**. `isSameTree` pairs left with left
and right with right. Symmetry pairs left with *right*:

```
isMirror(a, b) = a.val == b.val
              && isMirror(a.left,  b.right)
              && isMirror(a.right, b.left)
```

That's an actual answer to this problem.

</details>

<details id="q-just3" markdown="1">
<summary>I said: just 3 is correct</summary>

✅ That's right. Build a mirrored copy, compare it to the original, done.

It does have the downside that it allocates a whole second tree to answer a
yes/no question! The better efficient solution is in the dropdown for #2.

</details>

<details id="q-two" markdown="1">
<summary>I said: two of them are right, one is wrong</summary>

Only **one** of the three actually works. Strategies 1 and 2 both fail, on two
different trees. Click on the other answers to see the explanations for why!

</details>

<details id="q-none" markdown="1">
<summary>I said: none of them are correct</summary>

There is **one** of the three that actually works! Strategies 1 and 2 both
fail, on two different trees, but the third works. Click on the other answers
to see the explanations for why!

</details>

This is a very representative data structures problem – it requires thinking
about tree shapes, what “correct” means, and what potential examples could
break your implementation. It does this without thinking about specific *code*,
but about *solution shapes*. This is the kind of thinking an engineer does
before picking an approach to a problem, and also is the kind of language you
could use to talk to colleagues (or an agent!) about code at a high level.

## 💬 From Last Time

Here are some implementations of symmetric tree (not directly from students,
representative of what we saw in the quiz question and in what folks sent to
me)

The direct version in C, the trick is the swap in the recursive calls:

```c
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static bool isMirror(struct TreeNode *a, struct TreeNode *b) {
    if (a == NULL && b == NULL) return true;
    if (a == NULL || b == NULL) return false;
    return a->val == b->val
        && isMirror(a->left,  b->right)        /* left against right */
        && isMirror(a->right, b->left);        /* and right against left */
}

bool isSymmetric(struct TreeNode *root) {
    return root == NULL || isMirror(root->left, root->right);
}
```

And strategy 3 — build the reflection as a brand-new tree, then ask whether
it's the same as the original — in Python:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mirrored(node):
    if node is None: return None
    # the swap happens here, at construction time
    return TreeNode(node.val, mirrored(node.right), mirrored(node.left))

def same_tree(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return (a.val == b.val
            and same_tree(a.left, b.left)
            and same_tree(a.right, b.right))

def isSymmetric(root):
    return same_tree(root, mirrored(root))
```

Both are correct. The first version swaps as it *compares*, so it returns
`false` the first time it finds a mismatch; it never allocates anything. The
second version swaps as it *builds*, so it constructs an entire second tree
before it starts checking. Same idea, and one of them does a lot more work to
get there. (This isn't a language comparison – you could implement the
mirroring one in C and the checking one in Python, I just like showing lots of
examples).


**Also from previous weeks:** If you're not sure about the `lastword.c` and
`tree.c` bugs, we had some discussion and posts about both on Discord – you can
just sign in and scroll around to see those.

## 🧠 Coding Activity — (AI off) {#coding}

This video works through the key properties of binary *search* trees, and a
mistake that's easy to make when checking one:

  [https://youtu.be/GBvzkgYFkiM](https://youtu.be/GBvzkgYFkiM)

Then try [**Recover Binary Search
Tree**](https://leetcode.com/problems/recover-binary-search-tree/description/),
which steps up from *checking* a BST to *repairing* one — exactly two nodes
have been swapped, and you have to find them:

  [https://leetcode.com/problems/recover-binary-search-tree/description/](https://leetcode.com/problems/recover-binary-search-tree/description/)

Send it in if you want to; this one is more of a challenge than past weeks!

## 📆 Ways to Connect {#connect}

Never too late to start, no deadline, no pressure — a month from now is fine.

- [CSE PACE](https://pace.ucsd.edu) – a place to come hang out, talk about
  computing topics, and get free lunch. Open to *anyone* in their first year at
  UCSD (that includes incoming transfer students!)
- Student orgs are where a lot of CSE community actually happens, and they know things I
  don't — to name just a few: [CSES](https://csesucsd.com/), [ACM at
  UCSD](https://acmucsd.com/), [TESC](https://tesc.ucsd.edu/),
  [WIC](https://wicucsd.vercel.app/),
  [ColorStack](https://colorstackucsd.org/), [Triton Quantitative
  Trading](https://tquantt.com/), [IEEE at UCSD](https://ieeeatucsd.org/), and
  [CS foreach](https://www.csforeach.org/).
- [CSE Summer Series Welcome Form](https://forms.gle/dtpHtyHwj8Kgmb2X8) — still
  a good way to ask me a question.
- [Appointment slots with me](https://calendar.app.google/6oig2m1mc4H4DKTY7)
- All of these messages live at
  [https://cse-summer-series.github.io/2026/](https://cse-summer-series.github.io/2026/).


Joe

The code from the video is copied here for your reference:

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



<script>
(function () {
  // Public exe.dev proxy for this box, port 8000. If this is wrong the page
  // still works perfectly -- the beacon just fails silently and no counts land.
  var ENDPOINT = "https://cse-summer-series.exe.xyz:8000/log";
  var picks = 0;

  function log(section, kind) {
    if (!ENDPOINT) return;
    try {
      navigator.sendBeacon(
        ENDPOINT,
        "week=4&section=" + encodeURIComponent(section) + "&kind=" + kind
      );
    } catch (e) { /* logging must never break the page */ }
  }

  // Attach first, so a programmatic open below still fires a toggle.
  document.querySelectorAll("details[id]").forEach(function (d) {
    d.addEventListener("toggle", function () {
      if (!d.open) return;
      log(d.id, picks++ === 0 ? "first" : "again");
    });
  });

  function openFromHash() {
    var el = document.getElementById(location.hash.slice(1));
    if (el && el.tagName === "DETAILS") {
      el.open = true;                       // fires toggle -> logs the pick
      el.scrollIntoView({ block: "center" });
    }
  }

  log("pageview", "view");                  // the denominator
  openFromHash();
  window.addEventListener("hashchange", openFromHash);
})();
</script>
