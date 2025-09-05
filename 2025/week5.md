Hi all!

Here with summer series updates!

🔗 **Links and Resources**

- CSE-PACE ([https://pace.ucsd.edu](https://pace.ucsd.edu)), also listed as the
course CSE89, is a space to come hang out, talk about CS, get advice from more
experienced student mentors, and eat free lunch. It's open to drop by or sign up
for anyone in their first year (this includes all of you) as a CSE student at
UCSD. I'll be there on most Tuesdays this fall!

The website
[https://cse-summer-series.github.io/2025/](https://cse-summer-series.github.io/2025/)
has all of the summer series messages.


✅ **Do Now! (Do one, some, or all!)**

- Watch [the video about stacks with a min operation](https://youtu.be/uA9b39blpLg):

    https://youtu.be/uA9b39blpLg 

    This one looks at a clever extra method on a `Stack` interface.


- Fill out the [welcome form](https://docs.google.com/forms/d/1wymRYUsQMA4gWiz7-WIsBGSEFOJXBZIsnp39gKfBnQs/preview) if you haven't – if you have, you should have gotten an email from me by now saying hi and replying to your questions.

- Join the [Discord server](https://discord.gg/4zexzTVv6Z) and say hi:
  
  [https://discord.gg/4zexzTVv6Z](https://discord.gg/4zexzTVv6Z)

  I will also be posting assignment solutions given by students with some discussion to Discord.

- Do your best to complete the [Implement Stack with Queues](https://leetcode.com/problems/implement-stack-using-queues/description/)
  problem in a programming language of your choice:

  https://leetcode.com/problems/implement-stack-using-queues/description/
  
- For either or both of those tasks, share your solution with me by replying to
  this email or putting the code in a direct message on Discord. I'll share some
  answers that I see on Discord next week.

The code from today's video is copied here for your reference:

```java
import java.util.LinkedList;
class MinStack {
    // <-- top
    // empty
    // 50           push 50     min 50  top 50
    // 100 50       push 100    min 50  top 100
    // 25 100 50    push 25     min 25  top 25
    // 90 25 100 50 push 90     min 25  top 90
    // 25 100 50    pop         min 25  top 25
    // 100 50       pop         min 50  top 100
    LinkedList<Integer> stack = new LinkedList<Integer>();
    LinkedList<Integer> mins = new LinkedList<Integer>();
    public MinStack() {}
    
    public void push(int val) {
        stack.addFirst(val);
        if(mins.size() == 0) { mins.addFirst(val); }
        else if(val <= mins.getFirst()) { mins.addFirst(val); }
    }
    
    public void pop() {
        // new Integer(5) == new Integer(5) actually false!
        if(stack.getFirst().equals(mins.getFirst())) {
            mins.removeFirst();
        }
        stack.removeFirst();
    }
    
    public int top() {
        return stack.getFirst();
    }
    
    public int getMin() {
        return mins.getFirst();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
```



