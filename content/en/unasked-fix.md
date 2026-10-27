---
title: "Claude built a new tool I never asked for, so I traced its reasoning through the logs"
date: 2026-10-28
draft: true
summary: "When I saw an improvement Claude made without being asked, I felt it had evolved on its own. Tracing the logs backward, I found I had set the direction, and Claude had filled the gap where that direction collided with an outdated tool."
cover: /images/20261028-unasked-fix/01-입력기-커밋-여섯-판.webp
---

When I saw an improvement Claude made without being asked, I felt it had evolved on its own. Tracing the logs backward, I found I had set the direction, and Claude had filled the gap where that direction collided with an outdated tool.

## All I said was "move it to Naver"

In the early hours of October 28, I asked Claude to move parts 1 to 4 of my wedding film series to my Naver blog. All I said was "do the Naver migration."

At the end of the report saying four drafts had been saved, there was one extra line. The old input tool needed a folder on my PC and a local server to run, so Claude had built a new one that reads the drafts and photos straight from GitHub.

![GitHub commit history screen: six commits starting with "Naver input tool, GitHub version" stacked one above the other](/images/20261028-unasked-fix/01-입력기-커밋-여섯-판.webp)
<small>Commit history of the new input tool. The bottom one is the first version; each one above fixes one more thing that got stuck</small>

![Naver blog list of saved drafts: parts 1 to 4 of the wedding film saved between 1:11 and 1:18 on October 28, with one October 27 post at the bottom](/images/20261028-unasked-fix/02-네이버-임시저장-네-편.webp)
<small>Between 1:11 and 1:18 a.m., the four posts went in one after another. The October 27 post at the bottom is the old short version</small>

**I never asked for that.** So I thought Claude had evolved it on its own. It looked as if it had noticed the old way was inconvenient and built a better one by itself.

What I wanted to know was the process. What did it see as lacking, and in what order did that judgment unfold? I asked Claude in the next chat window.

## I was the one who set the direction

The first thing Claude pointed out was that half of my premise was off. Matching the commits against my work log, the decision to take the PC out of the loop was one I had made three days earlier.

| Date | What changed | Who |
|---|---|---|
| Oct 25 | Workspace fixed to GitHub only; no saving or pulling in PC folders | My instruction |
| Oct 26 | Account skill reduced to a pointer; rules moved into the repository | My instruction |
| Oct 26 | A way to insert photos by pasting when file upload was blocked | Found by a window that got stuck |
| Oct 28 | A new Naver input tool that reads drafts and photos from GitHub | Claude, unasked |

![GitHub commit diff screen: in the rules document, the "PC detection and permissions" line is deleted in red and "the workspace is GitHub only" is added in green](/images/20261028-unasked-fix/03-10월25일-작업공간-규칙.webp)
<small>The rules document change on October 25. The PC detection line came out and "the workspace is GitHub only" went in</small>

The problem was that only the rules changed, and the tool stayed the same. The rules said not to open PC folders, yet the Naver input tool still needed photos in a PC folder and a local server (port 8125) running on the PC.

In the meantime, each window worked around it by hand. On October 26, one drew the thumbnail directly inside the PC browser and pasted the photos in one by one from their public addresses.

## The order of judgment Claude described

One thing to make clear first. The chat window that built the new tool is already closed, and it did not write down why it did what it did. The Claude in the current window cannot look into that judgment either. So it worked backward from the actions left in the conversation log and the order of the commits.

Claude described the starting point as a **conflict**, not a frustration. To do the migration it had to use the input tool, and using the input tool meant breaking the rules. It said there were three paths at that point.

| Path | Outcome |
|---|---|
| Stop and ask | Work stalls waiting for an answer in the middle of the night. The rules also say not to stop but to queue it |
| Old way | Breaks the rules |
| Find a new path | Whether it would work could be checked with a single test |

That was also why it took the third path. The guess that a browser logged into GitHub could fetch files from a private repository was confirmed right away by opening two addresses. If they had not loaded, it said, the rules would have meant queuing only the drafts.

The rest is all in the record.

| Step | Action left in the record | Claude's explanation |
|---|---|---|
| 1 | Pushed the 4 drafts and thumbnails to GitHub first | The materials had to live in the repository, not on the PC, to match the rules |
| 2 | Opened two files from the private repository in Whale | Cheapest test first |
| 3 | Read the photo-size tool and wrote the new input tool | Reuse what already works (Table 2 style, photo size, font) |
| 4 | Photo insertion failed twice → switched to pasting | Playwright intercepted the file picker. It used the method another window had written down two days earlier |
| 5 | Six commits between 1:03 and 1:12 a.m. | Run it, fix the one place that broke, run again |
| 6 | One line of usage in the skill | So the next window doesn't get lost in the same spot |

The commit list at the top is step 5. In nine minutes, it fixed the first version five more times.

## One gap was left behind

The window that built the new tool added a line of usage to the skill, but it did not remove the old procedure. Inside the skill, the old steps using a PC folder and a local server sat right next to the new tool. A next window reading only the skill could easily have gone back the old way.

The one that found it is the window writing this post. When I asked whether the skill had changed, it pointed out first that the start instructions and the skill were saying different things. I told it to clean that up, and it fixed it on the spot.

![GitHub commit diff screen: in the start instructions, the "local server" line telling you to start a server is deleted and replaced with "not needed"](/images/20261028-unasked-fix/04-오늘-정리한-시작-지침.webp)
<small>The start instructions fixed today. The line that said to start a local server now says "not needed"</small>

The gap one window filled, the next window finished filling.

## A better word than "evolved"

I also asked whether "evolved" was the right word. Claude said no. "Evolved" makes it sound as if Claude got smarter, but the model is the same, and once the window changes it does not even remember what happened.

What changed is the repository. The rules document, the new input tool, and the one line left in the skill piled up, and the next window starts by reading them.

So the words Claude chose were "an unasked improvement," or shorter, "it filled a gap." Claude summed it up like this. **I set the direction, Claude fills the places where that direction and reality don't line up, and what it fills stays in the repository.** It said the repository I called the [AI brain](/en/posts/github-brain-for-claude/) is what grew.
