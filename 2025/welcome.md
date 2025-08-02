Hi all!

If you're getting this email, I think you're an incoming UCSD CSE transfer
student this fall. Welcome!

👋🏻 **CSE Summer Series**

[My name is Joe](https://jpolitz.github.io/), I'm a professor in the CSE department. I teach several lower
division courses (you may end up taking CSE29 with me in the fall!).

As part of [CSE Summer
Series](https://cse.ucsd.edu/undergraduate/cse-summer-series), a free online
summer program run by the department, I'll be reaching out with weekly emails
until fall quarter starts, will be providing bunch of different resources:

- A Discord chat server for saying hi and asking me (and each other) questions
- A weekly activity (usually programming) for reviewing content useful for the
  upcoming year
- Videos, readings, and websites related to (and in some cases straight from)
our courses to help you prepare for the year
- Reminders about summer events and opportunities

✅ **Do Now! (Do one, some, or all!)**

- Watch [the welcome video](https://youtu.be/99TD24cJ5Uw), which has some information about how to complete the steps below:

  https://youtu.be/99TD24cJ5Uw
  
- Fill out the [welcome form](https://docs.google.com/forms/d/1wymRYUsQMA4gWiz7-WIsBGSEFOJXBZIsnp39gKfBnQs/preview)

- Join the [Discord server](https://discord.gg/4zexzTVv6Z) and say hi:
  
  [https://discord.gg/4zexzTVv6Z](https://discord.gg/4zexzTVv6Z)

- Make a free LeetCode account: https://leetcode.com (let me know if you can't!
You can email me directly or ask on Discord.) Follow along with what I did in
the startup video! Typing in the code like I did is great practice and will
build towards more sophisticated examples.

- Do your best to complete the [Length of Last Word](https://leetcode.com/problems/length-of-last-word/) problem in a programming language of your choice:

  https://leetcode.com/problems/length-of-last-word/

  Then, share your solution with me by replying to this email or putting the
  code in a direct message on Discord. I'll share some answers that I see on
  Discord next week. Also feel free to ask programming questions on Discord to
  each other or to me if you get stuck, are curious about something in the
  video, etc!

🔗 **Links and Resources**

- CSE courses and enrollment: [https://cse.ucsd.edu/undergraduate/tentative-course-offerings](https://cse.ucsd.edu/undergraduate/tentative-course-offerings)
- CSE advising: [https://cse.ucsd.edu/undergraduate/undergraduate-advising](https://cse.ucsd.edu/undergraduate/undergraduate-advising)
- Check out [Dive Into Systems](https://diveintosystems.org/book/introduction.html), the textbook used in CSE29, one of the first courses you'll likely take:
  
  [https://diveintosystems.org/book/introduction.html](https://diveintosystems.org/book/introduction.html)

  It also has lots of C programming resources!
- Check out the [course web page](https://ucsd-cse29.github.io/ss1-25/) for CSE 29 from summer session if that's a course you plan to take this fall.
- I plan to hold **Remote Office Hours** on Tuesdays at 11am pacific time for the rest of the summer. You can find the link through [my contact page](https://jpolitz.github.io/contact/) which has a calendar of many advising office hours!
- The website [https://cse-summer-series.github.io/2025/](https://cse-summer-series.github.io/2025/) has all of these messages

The code from the welcome video is also copied here for your reference:

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)): #note j and i are never equal
                if nums[i] + nums[j] == target:
                    return [i, j]
```

```
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* result = calloc(sizeof(int), 2); // create an array with 2 elements of size int
    for(int i = 0; i < numsSize; i += 1) {
        for(int j = i + 1; j < numsSize; j += 1) {
            //printf("%d %d %d %d\n", i, j, nums[i], nums[j]);
            if(nums[i] + nums[j] == target) {
                result[0] = i;
                result[1] = j;
                *returnSize = 2;

                //printf("%d %d\n", result[0], result[1]);
                return result;
            }
        }
    }
    return NULL;
}
```

```
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i = 0; i < nums.length; i += 1) {
            for(int j = i + 1; j < nums.length; j += 1) {
                if(nums[i] + nums[j] == target) {
                    int[] toReturn = { i, j };
                    return toReturn;
                }
            }
        }
        return null;
    }
}
```

