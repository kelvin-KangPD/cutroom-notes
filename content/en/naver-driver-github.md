---
title: "How my Naver blog input tool stopped needing a PC folder and local server and started reading from GitHub"
date: 2026-10-28
series: ai-orchestration
part: 3
summary: "When I handed Claude a Naver migration, it rewrote the input tool that needed a PC folder and a local server so that it reads drafts and photos straight from GitHub. Now all the PC has to provide is one logged-in Whale browser window."
cover: /images/20261028-naver-driver-github/01-입력기-커밋-여섯-판.webp
---

When I handed Claude a Naver migration, it rewrote the input tool that needed a PC folder and a local server so that it reads drafts and photos straight from GitHub. Now all the PC has to provide is one logged-in Whale browser window.

In the early hours of October 28, I asked Claude to move parts 1 to 4 of my wedding film series to Naver. While saving the four drafts, Claude rewrote the input tool, and once the work was done it mentioned this in one line at the end of its report.

![GitHub commit history screen: six commits starting with "Naver input tool, GitHub version" stacked one above the other](/images/20261028-naver-driver-github/01-입력기-커밋-여섯-판.webp)
<small>Commit history of the new input tool. The bottom one is the first version; each one above fixes one more place that got stuck</small>

The input tool is a script that drives the Whale browser through Playwright and puts a post into the Naver editor. If Playwright is the hand, the input tool is the work order you put in that hand. It reads the draft and decides in what order to enter the title, quote-style headings, tables and photos. What changed this time was not the hand but the work order.

## The rule said GitHub only, but the tool was tied to the PC

On October 25, I made GitHub the only workspace for the blog. The idea was that whichever account, PC or phone I open it from, the work continues from the same state. So I added a rule to the start instructions: nothing is saved to or pulled into PC folders.

![GitHub commit diff screen: in the start instructions, the "PC detection and permissions" line is deleted in red and "the workspace is GitHub only" is added in green](/images/20261028-naver-driver-github/02-작업공간-규칙-변경.webp)
<small>The start instructions change on October 25. The PC detection line came out and "the workspace is GitHub only" went in</small>

The Naver input tool, though, still worked the old way. To run the old tool (`naver_driver.js`), the PC needed this preparation.

| Prep | Old input tool |
|---|---|
| Draft | Read through a local server started with `python -m http.server 8125` in the blog-notes folder on the PC |
| Photos | Copied into a PC folder Playwright allows, named `up0.webp`, `up1.webp` |
| Settings | Tool copied into the same folder as `drv.js`, draft name and start position written in `naver_params.json` |
| Photo insert | When it stopped at a photo, upload with `browser_file_upload` and run again |

Under the rule, none of the steps that use a PC folder were allowed. Two days earlier, for the Coupang review post, a cloud window worked around this by hand. It drew the thumbnail on a canvas inside the PC browser and pasted the photos one by one from their public addresses on Kang PD Log.

## It tested with two addresses first

Claude first pushed the four drafts and thumbnails to the private repository on GitHub. The materials had to live in the repository, not on the PC, to match the rule.

Then, instead of building the tool right away, it ran a test. Whale is logged into my GitHub account. So could Whale also fetch files from a private repository? It requested two addresses from Whale, one thumbnail and one draft, and both came back.

**That one test removed the need for a PC folder.** Drafts and thumbnails come from the private repository, and body photos come from Kang PD Log addresses that are already published. The draft's front matter just needs one line with the photo folder name (`imgdir`).

| Material | Where the new tool gets it |
|---|---|
| Draft | blog-notes private repository, `네이버/*.md` |
| Thumbnail | Same repository, `네이버/썸네일/<slug>.webp` |
| Body photos | Kang PD Log public address `images/<imgdir>/` |
| The tool itself | Same repository, `tools/naver_driver_gh.js`, pinned by commit |

The tool itself is read from GitHub too. It works by telling Whale, "fetch the input tool at this commit and run it." With the commit pinned, every fix just means pushing a new commit and calling it again with the new number.

```js
async (page) => {
  const SHA = '<커밋 번호>';
  const s = await (await page.request.get('https://github.com/kelvin-KangPD/blog-notes/raw/' + SHA + '/tools/naver_driver_gh.js')).text();
  return await eval(s)(page, { SHA, FILE: '<원고 파일>', PHASE: 'write', START: 0, CLEAR: true });
}
```

Each piece of Playwright code has to finish within 60 seconds. So after 40 seconds, the tool returns a number meaning "entered up to here" and stops. Calling it again from that number continues the entry. Once the body is in, a separate finishing step applies the "Table 2" style, photo sizes (lead photo 600 wide, stretched photos back to original width), the NanumSquare body font, and saves the draft.

## Photos got stuck twice

When the first version ran, photos were what got stuck. Six commits piled up in nine minutes.

| Time | What changed | Why |
|---|---|---|
| 1:03 | First version | Read drafts and photos from GitHub with no PC folder or local server |
| 1:04 | Photos via the file picker | Putting files straight into the file input didn't work |
| 1:06 | Photos via a paste event | Playwright intercepts the file picker, so it can't be used |
| 1:06 | Don't reopen if already on the write screen | A "leave this page?" dialog appeared every time it reopened |
| 1:09 | Grab the cursor before a photo, check position | Right after a table or photo the cursor wasn't caught, and the photo went to the top of the post |
| 1:12 | Fully clear the body, wait longer for photos | Prevent starting with a half-cleared post and moving on before a photo finished loading |

The paste method was one another chat window had found two days earlier and written into the skill. If you build the photo as a file object inside the editor and send it with a "a paste just happened" signal, the Naver editor accepts the photo as if a person pressed Ctrl+V. When it got stuck, Claude took that record and put it into the tool.

The cursor problem is still written in the tool's comments. Right after a table goes in, the editor can't move the cursor out of the table, so the photo landed at the top of the post. It now grabs the cursor by typing one character and deleting it, and after a photo goes in it checks that the last block is a photo, stopping if it isn't.

## Four posts went in within seven minutes

With the sixth version, parts 1 to 4 went in one after another. Part 1 was saved at 1:11 and part 4 at 1:18.

![Naver blog list of saved drafts: parts 1 to 4 of the wedding film saved between 1:11 and 1:18 on October 28, with one October 27 post at the bottom](/images/20261028-naver-driver-github/03-네이버-임시저장-네-편.webp)
<small>The saved drafts list. Parts 1 to 4 went in one after another within seven minutes. The October 27 post at the bottom is the old short version</small>

**No preparation was done on the PC.** No server started, no photos copied. As long as the Whale window is open and logged into Naver and GitHub, that's it.

After finishing, Claude wrote one line of usage for the new tool into the skill. The old procedure for the old tool was still there, though. A few hours later another window pointed out that the start instructions and the skill were saying different things, and when I told it to clean up, it cleared out the old procedure.

![GitHub commit diff screen: in the start instructions, the "local server" line telling you to start a server is deleted and replaced with "not needed"](/images/20261028-naver-driver-github/04-시작-지침-정리.webp)
<small>The cleaned-up start instructions. The line that said to start a local server now says "not needed"</small>

## The PC only lends one Whale window

In the current setup, all the PC handles is a logged-in browser. Work happens in a cloud window, and the PC's Whale is borrowed only when needed.

| Task | Where |
|---|---|
| Drafts, thumbnails, photo conversion, publishing Kang PD Log and the multilingual site | Cloud window (GitHub repositories) |
| Naver draft saving | PC Whale window (the new tool reads from GitHub and enters it) |
| Web screen captures | Taken in the PC Whale window and brought back to the cloud |
| When Whale is off | Only the draft is made and queued in `네이버/대기열.md` |

The captures in this post came the same way. Whale took screenshots of GitHub, returned the image data as text, and the cloud side turned it back into image files. The font used for thumbnails can't be downloaded from the cloud because the address is blocked, so Whale fetched it instead and handed it over in two pieces.

Where the rule and the tool didn't match, it neither stopped nor broke the rule, and checked first with a cheap test whether there was a way. Then it fixed one thing at a time and got all four posts in. On this one, Claude did good work.
