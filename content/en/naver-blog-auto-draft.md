---
title: "Writing on a Naver blog with AI: fully automated up to saving the draft"
date: 2026-10-19
series: naver-blog-automation
part: 1
summary: "Uploading to a Naver blog used to take me over 30 minutes by hand each time. Now AI drives the browser directly, puts in the text, photos, captions and title, and saves it as a draft."
---

Uploading one post a day to a Naver blog used to take me over 30 minutes by hand every time.
**Now I've automated it to the point where AI drives the browser directly, puts in the text, photos, captions and title, and saves it as a draft.**

Yesterday it worked end to end for the first time.
All I do is open the saved draft, skim it once, and press publish.
What matters most about this work is that it's good enough to use in my job right away.

## How it used to be

Part of my job is moving articles from our company blog, written by an outside agency on inblog, over to Naver blog. Naver is Korea's main search portal. I don't copy the articles as they are. I rework the style and structure to suit Naver search. About one article a day. I was already doing the rewriting with AI. But each time there was still work left: putting it into the Naver editor with lots of clicking, uploading photos, and touching it up again in my own style.

Naver blog has no official API for publishing posts. So whatever the AI wrote, a person ultimately had to carry over by hand.
To cut that down, I had made bookmark buttons (bookmarklets) and PowerShell commands.

| Order | Who | Task |
|---|---|---|
| 1 | AI | Make a work sheet with the body text, title options, list of photos, and captions |
| 2 | Person | Copy the "fetch photos" command from the work sheet and paste it into PowerShell |
| 3 | Person | Click "copy body" and paste it into the Naver editor |
| 4 | Person | Click the "convert format" bookmark (changes the shape of quotes and dividers) |
| 5 | Person | Click the "insert photo" bookmark once per photo, choosing the photo in the file picker each time |
| 6 | Person | Click each photo's caption field and paste the caption |
| 7 | Person | Type the title, check the link card, publish |

The buttons did cut it down a lot. Still, with more than ten photos it meant dozens of clicks.
Automatic captions had failed, so they were only copied to the clipboard and a person pasted them in.
**One post took 30 minutes at the very least.**

## The new way: AI drives the browser with code

The key is Playwright MCP.
Playwright is a tool for controlling a browser with code, and once it's connected through MCP, AI can use it directly.
It doesn't take a screenshot and click coordinates. It reads the structure of the page, picks elements, and operates on them. So it's fast, and it rarely misses.

This is how I connected it.

| Step | Detail |
|---|---|
| 1 | Add `--remote-debugging-port=9222` to the end of the Whale (Naver's browser) shortcut target, and launch Whale from that shortcut |
| 2 | Register Playwright MCP in the Claude desktop app's config file, so it attaches to the Whale already running on port 9222 |
| 3 | Quit the app completely, then open it again |

This is what went into the config file. I was already using the Premiere MCP, so both are in there.

```json
{
  "mcpServers": {
    "playwright": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@playwright/mcp@latest", "--cdp-endpoint", "http://localhost:9222"]
    },
    "premiere-pro": { "...": "..." }
  }
}
```

What matters is that it doesn't open a separate new Whale, but attaches to the Whale I use every day.
I'm already logged in to Naver, so there's no need to hand the AI my username and password.

## Wrestling with the Naver editor

Naver's SmartEditor is stubborn to automate. Here's where I actually got stuck and how I got past it.

| Stuck on | Solution |
|---|---|
| Pasting the body | Skip the clipboard. Dispatch a fake paste event straight to the input area inside the editor. The HTML goes in as is, so tables, bold and line breaks survive |
| Paragraph spacing | Naver ignores paragraph margins. Blank lines have to go in as real empty paragraphs |
| Quote style | A quote pasted as HTML always comes in as the quotation-mark style. After pasting, click the quote and switch its shape with the style buttons |
| Photo positions | Put a placeholder line like <code>[📸 photo 01 &#124; caption: …]</code> in the body, then press the photo button where that line was deleted |
| Deleting a line | The editor intercepts selection keys like Shift+Home. Click at the end of the line and press Backspace as many times as there are characters |
| Uploading photos | Don't open the file picker; put the file in directly with Playwright's file upload. But it rejects files outside the working folder, so copies go in the working folder |
| Caption field | The caption field only appears after clicking the photo first. That's why automatic captions failed before |
| Checking the upload | Right after uploading, the photo address looks like an svg placeholder. That's normal. Wait a few seconds |
| Button won't click | It's covered by a side panel or mid-animation. Recalculate the button position every time and click it with the mouse |
| Hidden tab | If the tab is in the background, the page doesn't respond. Bring the tab to the front, then continue |

This is the code for pasting the body. Once this worked, the rest fell into place.

```js
async (page) => {
  const HTML = `...body HTML...`;
  const fr = page.frame({ name: 'mainFrame' }) || page.mainFrame();
  await fr.locator('.se-component.se-text .se-text-paragraph').first().click();
  await page.waitForTimeout(400);
  await fr.evaluate((h) => {
    const ib = [...document.querySelectorAll('iframe')]
      .map(i => { try { return i.contentDocument } catch (e) { return null } })
      .find(x => x && x.body && x.body.isContentEditable);
    const W = ib.defaultView, dt = new W.DataTransfer();
    dt.setData('text/html', h);
    dt.setData('text/plain', h.replace(/<[^>]+>/g, ''));
    ib.body.dispatchEvent(new W.ClipboardEvent('paste', { clipboardData: dt, bubbles: true, cancelable: true }));
  }, HTML);
  await page.waitForTimeout(4000);
}
```

Photos are handled one at a time in a loop. Each run does two things together: "add the caption to the previous photo" and "delete the next 📸 placeholder and press the photo button". When it reaches the file-picking state, the photo with that number is uploaded. It keeps going until no 📸 placeholders are left.

## Publish must never be pressed

The last step is saving the draft. What I was most careful about here was making sure the publish button never gets pressed, not even by accident.
The Naver editor's buttons are labeled in Korean: 저장 means "save" and 발행 means "publish". The code reads the button label first, and if it isn't 저장 or contains 발행, it stops without clicking.
Success is confirmed by the number next to the save button going up by 1.

```js
async (page) => {
  const fr = page.frame({ name: 'mainFrame' }) || page.mainFrame();
  const btn = fr.locator('button[class*="save_btn"]').first();
  const label = (await btn.textContent()).trim();
  if (!/저장/.test(label) || /발행/.test(label)) return { error: label };
  const cnt = () => fr.evaluate(() => document.querySelector('[class*="save_btn"]').parentElement.textContent);
  const before = await cnt();
  const b = await btn.boundingBox();
  await page.mouse.click(b.x + b.width / 2, b.y + b.height / 2);
  await page.waitForTimeout(2500);
  return { before, after: await cnt() };
}
```

Leaving publishing to a person is deliberate.
The post goes public under the company's name, so I do the final check myself.
**Apart from that check, there's nothing left for me to touch.**

| Stage | Before | Now |
|---|---|---|
| Writing | AI | AI |
| Preparing photos | Paste a command into PowerShell | AI |
| Entering the body | Copy and paste | AI |
| Tidying the format | Bookmark buttons | AI |
| Photos and captions | One click per photo, paste captions | AI |
| Title and link card | Person | AI |
| Saving the draft | Person | AI |
| Checking and publishing | Person | Person |

## I made one for my personal blog too

I packaged the same method as a separate skill so I can use it on my personal Naver blog as well.
The difference from the work version is the voice. I had the AI read a few of my old posts, pull my habits into a table (sentence endings, emoji, paragraph length, how I place photos), and write in that voice.
Give it a photo folder and some rough notes, and it writes the post and saves it as a draft.

| Item | Detail |
|---|---|
| Input | Photo folder path + notes |
| Voice | Once at the start, it reads the structure of my 5 most recent posts and saves a style profile |
| No making things up | Shop names, prices or dates not in the notes or photos aren't written; they're left as `[needs checking]` |
| Photos | HEIC to JPG, shrink anything too large, and a copy with location data removed if I want |
| End | Saved as a draft. I publish it myself |

I've made the skill files public (they're written in Korean). You can add them to Claude as a skill.

| File | Contents |
|---|---|
| [SKILL.md](https://kelvin-kangpd.github.io/files/naver-personal-draft/SKILL.md) | The full procedure and code |
| [my-blog.md](https://kelvin-kangpd.github.io/files/naver-personal-draft/my-blog.md) | Blank style profile template |

I was setting up the same connection on my home PC, but it's stalled halfway. I've put in the config file, but the Claude app still doesn't pick up Playwright. I'll start again by checking, in the developer tab of the app's settings, which config file it actually reads.

In the next post I write about what I thought after getting this done. Why, once this tool existed, I felt I had to hurry.
