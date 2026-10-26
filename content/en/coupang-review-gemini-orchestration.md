---
title: "Want to join Coupang's reviewer program but stuck with dozens of overdue reviews? Try this"
date: 2026-10-26
summary: "I gave only keywords for 20 Coupang reviews: Claude directed the work, Gemini wrote the text, and Claude posted it. Here are the failures and the order that finally worked."
series: ai-orchestration
part: 2
cover: /images/20261026-coupang-gemini-reviews/01-제미나이-작성-화면.webp
---

I gave only keywords for 20 Coupang reviews, **Gemini wrote the text, and Claude posted it.**

I wanted to try Coupang's reviewer program, but my account had a pile of reviews I had never written. Coupang has no draft saving, so once you open a review you have to finish it on the spot. I kept putting it off.

One thing first: there is no place to apply for Coupang's reviewer program. As far as I found, Coupang invites people who write reviews steadily, and no apply button shows up. So I decided to build up a review history first.

![Gemini writing reviews by number, with a title, three summary lines, purchase reason, usage review and verdict](</images/20261026-coupang-gemini-reviews/01-제미나이-작성-화면.webp>)

## I split the roles

Gemini is good at writing reviews, and Claude clicks through web pages to post them. I split it this way to save tokens.

| Role | Job |
|---|---|
| Me | Throw keywords for each product: why I bought it and how it felt |
| Claude | Organize the keywords, send them to Gemini, then post and edit the result on Coupang |
| Gemini | Expand the keywords into a full review |

I used the normal Gemini chat with a Flash model, not AI Studio. If you link a Google account in the Whale browser, Claude can operate that window directly.

## At first it was too short and had no line breaks

The first reviews I posted were one block of text, with no paragraphs and not much length. Opened on my phone, it looked like a wall.

![An early review opened on a phone, one block of text with no paragraph breaks](</images/20261026-coupang-gemini-reviews/02-처음-줄바꿈-없는-후기.webp>)

Well-written reviews by other people had something in common: sections for why they bought it, how it felt, and a verdict, with summary lines on top. I told Gemini to use exactly that format.

| Section | Content |
|---|---|
| Title | One line for the whole review |
| 3 summary lines | Short sentences starting with a check mark |
| Purchase reason | Why I bought it |
| Usage review | Two paragraphs |
| Verdict | Who I would recommend it to |

## What went wrong with Gemini

It did not work in one go. Here they are in the order I hit them.

| Problem | Fix |
|---|---|
| Asking for JSON broke it midway and lost line breaks | Switched to plain text with numbered separators |
| Asking for 500 characters gave about 380 to 430 | Gemini counts short. Asking for 580 to 750 landed near 500 |
| Sometimes it refused with "I can't help with that" | Sent the same request again, worded differently |
| It slipped in frequencies like "every day" that I never said | Searched for those words and removed them before posting |

The last row mattered most. I asked it to expand things so they read well, but it must not invent experiences I never described. So it could only use the facts I gave, and for a product I had not used yet it wrote "not used yet" as is.

## Coupang quietly blocked the save

When Claude pressed save on the Coupang edit page, it often failed without any error. The cause was that the Coupang tab was not in front. After going to the Gemini tab and coming back, Coupang stayed behind, and saving silently failed in that state. I made it bring the tab forward before every save and check the list page afterward to see whether the text had changed. An error message is always hidden in the page, so it could not be trusted as a failure sign.

A body that was too short, around 60 characters, also failed to save.

## Result

I fixed 20 reviews into the new format and posted them. All I wrote was keywords.

![Coupang's list of written reviews, each with a title, three check-mark summary lines, purchase reason, usage review and verdict](</images/20261026-coupang-gemini-reviews/03-최종-후기-쿠팡.webp>)

Some things remain. I will upload photos myself later, and I will edit the reviews of products I have not used yet once I have. I also looked into Coupang Partners, but signing up needs identity verification and a disclosure of compensation is required, so I have to apply myself.

I plan to keep this process as a "Coupang review writing" skill, so next time keywords alone run the same steps.
