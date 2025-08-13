Hi all!

Here with summer series updates!

✅ **Do Now! (Do one, some, or all!)**

- Watch [the video of me solving a Leetcode problem about a cool number representation](https://youtu.be/F-5cax98m7w):

    https://youtu.be/F-5cax98m7w

    This one is a step up in complexity from last week! The problem was the deceptively simple-sounding “Add two numbers”:

    https://leetcode.com/problems/add-two-numbers/

- Fill out the [welcome form](https://docs.google.com/forms/d/1wymRYUsQMA4gWiz7-WIsBGSEFOJXBZIsnp39gKfBnQs/preview) if you haven't – if you have, you should have gotten an email from me by now saying hi and replying to your questions.

- Join the [Discord server](https://discord.gg/4zexzTVv6Z) and say hi:
  
  [https://discord.gg/4zexzTVv6Z](https://discord.gg/4zexzTVv6Z)

  I will also be posting assignment solutions given by students with some discussion to Discord.

- Make a free LeetCode account: https://leetcode.com (let me know if you can't!
You can email me directly or ask on Discord.) Follow along with what I did in
the video! Typing in the code like I did is great practice and will
build towards more sophisticated examples.

- Do your best to complete the [add-binary](https://leetcode.com/problems/add-binary/description/) problem in a programming language of your choice:

  https://leetcode.com/problems/add-binary/description/

  Then, share your solution with me by replying to this email or putting the
  code in a direct message on Discord. I'll share some answers that I see on
  Discord next week. Also feel free to ask programming questions on Discord to
  each other or to me if you get stuck, are curious about something in the
  video, etc!

🔗 **Links and Resources**

- Looking to get involved in the department? Check out our [student organizations](https://cse.ucsd.edu/student-organization) which have free events from hackathons to socials to project opportunities throughout the year.
- I continue to hold **Remote Office Hours** on Tuesdays at 11am pacific time for the rest of the summer. You can find the link through [my contact page](https://jpolitz.github.io/contact/) which has a calendar of many advising office hours!
- The website [https://cse-summer-series.github.io/2025/](https://cse-summer-series.github.io/2025/) has all of these messages

The code from today's video is also copied here for your reference:

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode currentEnd = new ListNode();
        ListNode start = currentEnd;
        while (l1 != null || l2 != null) {
            int val1 = l1 == null ? 0 : l1.val;
            int val2 = l2 == null ? 0 : l2.val;
            int digitResult = val1 + val2 + carry;

            boolean isCarry = digitResult >= 10;
            int newDigit = isCarry ? digitResult - 10 : digitResult;
            carry = isCarry ? 1 : 0;

            ListNode resultNode = new ListNode(newDigit, null);
            currentEnd.next = resultNode;
            currentEnd = resultNode;

            if (l1 != null) { l1 = l1.next; }
            if (l2 != null) { l2 = l2.next; }
        }
        if (carry == 1) {
            currentEnd.next = new ListNode(1);
        }
        return start.next;
    }
}
```


```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode ListNode;
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int carry = 0;
    ListNode* currentEnd = malloc(sizeof(ListNode));
    ListNode* start = currentEnd;
    while(l1 != NULL || l2 != NULL) {
        int val1 = l1 == NULL ? 0 : l1->val;
        int val2 = l2 == NULL ? 0 : l2->val;
        int digitResult = val1 + val2 + carry;

        int isCarry = digitResult >= 10;
        int newDigit = isCarry ? digitResult - 10 : digitResult;
        carry = isCarry ? 1 : 0;

        ListNode* newNode = malloc(sizeof(ListNode));
        newNode->val = newDigit;
        newNode->next = NULL;
        currentEnd->next = newNode;
        currentEnd = newNode;

        if(l1 != NULL) { l1 = l1->next; }
        if(l2 != NULL) { l2 = l2->next; }
    }
    if(carry == 1) { 
        ListNode* newNode = malloc(sizeof(ListNode));
        newNode->val = 1;
        newNode->next = NULL;
        currentEnd->next = newNode;
    }
    return start->next;
}
```

