---
title: "Tired of re-explaining every new Claude chat, I built an AI brain on GitHub"
date: 2026-10-26
series: ai-orchestration
part: 1
summary: "To get the same result no matter which device or chat window I use, I moved my rules and progress into a GitHub repository outside Claude. After a week of attempts, a new window now picks up the work from a single phrase: “connect blog”."
cover: /images/20261026-github-brain/01-블로그-연결-시작판.webp
---

To get the same result no matter which device or chat window I give the order from, **I built an AI brain in a GitHub repository outside Claude.**

The more I used Claude, the more I found myself giving it work from my home PC one time, my laptop the next, and my phone after that.
Sometimes in this chat window, sometimes in that one. It got far too complicated.
And every new chat window meant loading the previous posts and explaining how far I'd gotten. That got really tiresome.

Let me say this first: this is one part of building an orchestration setup, and this post is the work log for it.
Honestly, I think it's a pretty inefficient way to do it. Plenty of people have probably built far more efficient systems already.
Still, I'm leaving this here to share the process I went through.

![The "blog connection start board" screen: a one-page guide so that three accounts and several PCs all start work in the same order](/images/20261026-github-brain/01-블로그-연결-시작판.webp)

## All I wanted was one thing

Keep the brain on the web, and whatever device I make a request from, have it go through that brain (GitHub) and follow fixed procedures (skills, md documents) to produce a consistent result.
From the outside it looks like "isn't that easy?", but it wasn't.
I spent almost a week building this system. Countless chat windows, countless tests, countless tokens burned.
And I'm still optimizing it.

This is my setup. The problem was that all of it worked separately.

| Item | What I use |
|---|---|
| Devices | Home PC, work PC, laptop, phone |
| Claude accounts | Two personal, one work. Three accounts |
| Chat windows | Desktop app chat, Code tab, cloud sessions, mobile app |
| Outputs | Kang PD Log, the multilingual site Cutroom Notes (5 languages), Naver blog |

Claude has memory too. But it builds up separately for each account.
One account's memory picked up work blog rules, another picked up personal blog rules. New windows ended up following the wrong rules.
So I decided to keep the memory outside Claude, not inside it.

## What I tried over the week

I didn't land on the current structure from the start. Most attempts failed.

| Date | Attempt | Result |
|---|---|---|
| 10/23 | Designed a structure where I write instructions in one document in the repository, and a watcher program checks it every 1–2 hours and sends the work to dedicated chat windows by field (blog, Naver, Premiere) | Only settled the direction |
| 10/24 | Moved the to-do queue to GitHub Issues. Wrote 11 labels (needs triage, waiting, in progress, blocked, per owner, per PC), an issue template and an operating rules document | The skeleton stood up |
| 10/24 | Ran a scheduled task, the "command session", every 2 hours from 09:00 to 23:00 to triage and assign new issues | Triage worked well. Launching the dedicated chat windows didn't |
| 10/24 | A GitHub Actions workflow that runs translation automatically through the Gemini API | Unstable with 429 and 503 errors, and it used more tokens, so I rolled it back |
| 10/24 | Dropped all of it and condensed everything into one skill that runs the fixed procedure to the end from one command: "let's write a blog post" | The starting point of the current approach |
| 10/25 | A shared structure for three accounts and several PCs. The original lives in one repository; accounts and PCs only hold an entrance | The start board above came out of this |
| 10/25 | Stopped saving to PC folders too. The only workspace is GitHub | The current structure |
| 10/26 | Cut the entrance skill down to three lines and moved every rule into the repository | Entrance v2 |

I had high hopes for the Gemini API. Handing it jobs like translation, separate from Claude's limits, seemed like a good idea.
But I had to persuade both Gemini and Claude. If either one slipped, the workload doubled.
So for now I decided to go with Claude only.

I also tried a scheduled task that checks Git at set intervals so that work starts on its own whenever a file changes.
The problem was that every time I edited the rulebook (the document with my writing rules), that counted as a change too and triggered a check. It just leaked tokens.
On top of that, a session started by a scheduled task had no way to open a new chat window. I ran it twice to confirm.
In the end I gave up on automatic watching. If I do it at all, I'll add it last, once the whole design is finished.

## The current structure: a thin entrance, the brain in the repository

![Diagram: whatever device the request comes from, it passes through the entrance and produces results according to the rules in the GitHub repository](/images/20261026-github-brain/02-저장소-뇌-구조도.webp)

I drew this diagram myself. The key is keeping almost nothing on the accounts and PCs.

| Layer | What's there | Where |
|---|---|---|
| Entrance | A short instruction: when I say "connect blog", read the repository first | One skill per account (blog-connect), and one block of global instructions on PCs that use Claude Code |
| Brain | Start instructions, work log, rulebook, writing procedure skill | Private repository blog-notes |
| Outputs | Posts, translations, photos | Two public repositories (Kang PD Log, Cutroom Notes) |

I don't write rules in the entrance. If I did, each account would end up with a different version, and every fix would mean editing three places.
All the entrance does is say "go to the repository and read in this order". I gave the entrance a version number (v1), and if it doesn't match the number in the repository's start instructions, the window says in one line "please update the entrance". It started as v1 and became v2 a day later, for the reasons below.

![The "first time on a new account" section of the start board, expanded to show how to register the blog-connect entrance skill by pasting its full text](/images/20261026-github-brain/03-새-계정-입구-스킬.webp)

When adding a new account, I just follow this section. If the window can't read the repository, I paste in the whole skill text and register it.

![File list of the private repository blog-notes: skill, plan, Naver and received-photos folders, plus CLAUDE.md and the work log](/images/20261026-github-brain/04-비공개-저장소-blog-notes.webp)

This is the private repository that acts as the brain. A new window reads only these, in this order.

| Order | File | What to read |
|---|---|---|
| 1 | CLAUDE.md | All of it. Short start instructions |
| 2 | 작업일지.md (work log) | Only "current status". No reading it end to end |
| 3 | 계획/준구블로그_법전.md (rulebook) | Only the chapters needed for the current task |
| 4 | .claude/skills/blog-write | Only the relevant section of the writing procedure |

I blocked full reading because of tokens. Reading the whole work log every time eats into the limit on its own.
When finishing, the window has to update "current status" in the work log and commit and push. **Work that isn't pushed doesn't show up on other devices.**

There was an actual accident along the way. Another window picked up the work blog's rulebook and worked from it.
At the top of the work folder there was a work document with "rulebook" in its name, so it showed up first in the search.
So I nailed it down in the start instructions: "the rulebook for these blogs is this one file". I also added a line telling it to look in the rulebook first before asking me about rules like photo sizes.

![The "when it doesn't work" section of the start board: symptoms I actually ran into, such as being asked which blog or working from the work rulebook, with causes and fixes](/images/20261026-github-brain/05-안-될-때.webp)

Symptoms I actually ran into piled up one by one in the start board's "when it doesn't work" section.

## Keeping the start board HTML too

The photo at the top is that start board. I kept getting confused every time I added a new account or a new PC, so I made it into a one-page HTML.
It has seven sections: opening a chat, finishing, first time on a new account, first time on a new PC, current progress, when it doesn't work, and where everything lives.
Originally each command only had a "copy" button. In the public version I removed the buttons and saved it again with every command and phrase fully expanded.

[Open the public version of the start board](https://kelvin-kangpd.github.io/files/ai-brain/start-board.html)

It reflects the state as of midday on October 25. After that it changed once more to "don't save to PC folders, use only GitHub", so I barely use the PC folder paths or the PowerShell push command on the board anymore. A few work-related mentions were replaced with general wording. The entrance skill also changed to v2 a day later, so the skill text inside the start board is still v1.

![File list of the public Kang PD Log repository, with kelvin-KangPD and claude both listed as commit authors](/images/20261026-github-brain/06-공개-저장소-강PD로그.webp)

This is the public repository where the outputs pile up. Both claude and I show up in the commit history. Whatever window did the work, the results end up here.

This post was written with that structure too. Today I just said "let's write a blog post" in a new chat window.
The window read the entrance skill, pulled the repository from GitHub, read the work log, and reported the next task in one line. It didn't ask which blog.
The first time it tried to pull the repository it got stuck once because there was no authentication, and it pulled it again by adding the repository to the session. Small snags like that are still left.

## Cutting the entrance down once more, a day later

On the evening I made the start board, I reworked the structure again. Accidents kept happening.

One window, while running on my home PC, told me "this is a cloud window, so you'll have to continue the Naver work on your home PC."
The PC connection had dropped and come back in the middle of the chat, and it decided without checking.
When I pointed that out, it built a procedure to tell my home PC from my work PC and took access to my D drive.
That was the opposite of what I wanted. **Nothing should be saved on any PC, so the work can continue from another PC or my phone.**

So I nailed down three things.

| Principle | What it means |
|---|---|
| Workspace | GitHub only. The window pulls the repository, works in it and pushes from there. It never opens or writes to a PC folder |
| Naver | If the window can't touch Naver, it doesn't stop. It adds one line to a queue md file, and a window with Playwright attached clears the queue in one go |
| Other accounts | As long as GitHub is connected, any account does the same job |

Applying that meant editing the entrance skill three times in one day. Each time I had to press "save skill" again in the account.
I had said no rules go in the entrance, yet the actual v1 skill held the order for opening the repository, the reading order, even what to do at the end.
So whenever a rule changed, I'd have had to go round all three accounts. When I asked why it wasn't built this way from the start, it said it had copied the skill made in an earlier window as it was and didn't see rules written in two places as a problem.

Entrance v2 asks for only three things.

| Step | Entrance v2 |
|---|---|
| 1 | Pull blog-notes from GitHub. Don't open PC folders |
| 2 | Read the repository's CLAUDE.md and follow it. If it differs from the skill or memory, the repository wins |
| 3 | If there's no way to pull it, say so in one line and stop. Don't work from memory or guesses |

Every other rule moved into CLAUDE.md. Now changing a rule doesn't touch the accounts at all.

There was one more accident. A new window asked to redo three Naver posts I had already cleaned up and published.
I'd published them but never updated the status value in the draft files or the queue. I added a line: when you publish on Naver, fix both on the spot.

Then I tested again in a new window. What I sent was two lines: "let's write a new blog post, this chat starts on the home PC."

![In a new chat window, after "let's write a new blog post", it pulls the repository, finishes preparing, and reports the received-photos folder, the Naver queue and next post candidates in a table](/images/20261026-github-brain/07-새-창-시험.webp)

The window pulled the repository, finished preparing, and told me the received-photos folder was empty and no Naver drafts were waiting.
It showed the "posts to write next" candidates from the work log in a table, and said it would handle the leftover translation fix along the way.
It didn't ask which blog, and it didn't ask me to open a PC folder.

What's left is automatic watching. Right now I still have to open a window and say one line.
Once the design is fully done, I plan to add it at the very end.
