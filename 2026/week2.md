Hi all!

Joe here with summer series week 2.

💬 **Discussion from Week 1**

First — thank you to everyone who sent in a solution to last week's *Length of
Last Word*. I'm posting a few of them below, anonymized and lightly edited to
aggregate ideas rather than putting specific people on the spot. The
**variety** was interesting, and there's a lot to learn from lining them
up side by side.

Let's look at two right here — one walks **forward** through the string, the other starts at the **end** and walks backward. Both are correct:

```python
# Idea 1 — walk forward, remembering the length of the word you're currently in,
#          and "saving" it every time you hit a space.
def lengthOfLastWord(s):
    current = 0
    last = 0
    for ch in s:
        if ch == ' ':
            if current > 0:
                last = current
                current = 0
        else:
            current += 1
    return current if current > 0 else last
```

```python
# Idea 2 — start at the end, skip any trailing spaces, then count backward
#          until you reach a space (or the very start of the string).
def lengthOfLastWord(s):
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    length = 0
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
    return length
```

I also ran a little experiment: I asked a bunch of AI assistants to solve the
same problem.

Many of them came up with the one line solution:

    return len(s.split()[-1])

This is very cute (and students showed me this solution as well!). It of course
practices little about writing careful loops, but it's definitely a solution! 🤷🏻

When I gave them fewer examples and less specific direction and told them it
was 'leetcode-like', they came up with similar solutions to you all (loops that
work backwards from the end).

If you want to see what they say, the two prompts I tried are here (the first
one almost always gives the one-liner solution, the second one gives a lot more
discussion and alternatives). Try them out!


**Prompt 1** — almost always gives the one-liner:

```
Solve this LeetCode problem in Python. Return just the function.
Given a string s consisting of words and spaces, return the length of the last
word. Examples: "Hello World" -> 5, "  fly me   to the moon  " -> 4.
def lengthOfLastWord(s: str) -> int:
```

**Prompt 2** — gives more discussion, and usually a backward-scanning loop:

```
Write a function/method in a language of your choice, leetcode-style, for the
following coding task: "Given a string s consisting of words and spaces, return
the length of the last word in the string."
```

What do you think makes the agents give such different answers to the two
prompts? Do you get the same results as me?


💻 **On the `PATH` exercise:** thanks for all the environment dumps! One neat
thing to notice: everybody's `PATH` is different, and it even *looks* different
depending on your operating system. Here's the computer I wrote this message
on, which runs Linux:

```
/home/exedev/.local/bin:/usr/local/bin:/usr/bin:/bin:/snap/bin
```

and here's a typical Windows one:

```
C:\Windows\System32;C:\Windows;C:\Program Files\Git\cmd;C:\Users\you\AppData\Local\Microsoft\WindowsApps
```

Notice the **separator** between entries — a colon `:` on Mac/Linux, but a
semicolon `;` on Windows — and that the folders themselves are completely
different. Even two people on the same operating system almost never match.
`PATH` is the list of places your computer looks for a program when you type
its name, and it gets built up differently on every machine. You'll run into it
again in the fall.

✅ **Do Now! (Do one, some, or all!)**

As usual, two small things — one with **AI off**, one with **AI on**.

🔌 **AI off — Programming Practice.** Keep practicing coding with your own typing skills and brain: you'll be tested in person this year. [Watch me solve *Add Two Numbers*](https://youtu.be/F-5cax98m7w), then try [Add Binary](https://leetcode.com/problems/add-binary/) yourself in a language of your choice:

  https://leetcode.com/problems/add-binary/


🤖 **AI on — Watch a C program lie to you.**

There was a mistake I saw in some `lengthOfLastWord` solutions (across
languages). Here it is in C:

```c
int lengthOfLastWord(char *s) {
    int i = strlen(s) - 1;

    while (s[i] == ' ') {      // skip trailing spaces
        i--;
    }
    int len = 0;
    while (s[i] != ' ') {      // count the last word
        len++;
        i--;
    }
    return len;
}
```



I'm not going to tell you the issue! You're going to use your own debugging
skills, plus AI to fill in any gaps, to understand what's going on.

  1. **Open our Codespace** — a full Linux terminal that runs in your browser, no setup, no payment method needed (the free tier is far more than enough for this):

     https://codespaces.new/cse-summer-series/summer-lab

     If you claimed the GitHub Student Pack after last week, nice — but you don't actually need it here.

  2. **Open the file `lastword.c`.** It's a C solution to last week's problem.
     Follow the numbered steps written at the top of the file. **If you're not
     sure how, ask an AI system to walk you through it**.

  3. **Report back** by replying to this email or posting on Discord:
     - the (probably wrong, maybe even different-each-time) number you got in
       step one
     - the one line AddressSanitizer blamed
     - the one-line fix (and your explanation of it).
     - Also tell me if you get stuck, and show me how AI helped you through the
       process. (Note that you don't _have_ to use AI to help here, the
       instructions in the file are pretty good! But I think an AI system will
       be able to give useful step-by-step instructions and explain some ideas
       here, and then we can check in about them.)

  This kind of debugging and tooling is something you'll see in CSE29. It's
  completely fine to feel lost in the terminal, use whatever resources you like
  to try and get through it, and reach out if you get stuck. The important
  thing is that *you* come out of the process understanding (a) the bug in the
  program (b) how to "see" the bug better by using built-in compiler tool.

🔗 **Links and Resources**

- Never used a terminal or `gcc` before? Ask the AI assistant inside the
  Codespace — it can explain every command as you go. Also check in on Discord
  and ask for places where you're stuck or the assistant gives an explanation
  that doesn't make sense to you.
- The GitHub Student Developer Pack
  ([education.github.com/pack](https://education.github.com/pack)) is still
  worth claiming for its other tools if you haven't yet.
- The website
  [https://cse-summer-series.github.io/2026/](https://cse-summer-series.github.io/2026/)
  has all of the summer series messages.
- I generally pay attention to DMs and messages on the Discord server through
  the summer, so reach out if you get stuck or just want to say hi.

See you on Discord,

Joe
