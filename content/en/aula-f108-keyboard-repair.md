---
title: "AULA F108 keyboard X key not working: a self-repair where Claude and I ruled out guesses one by one and saved a ripped pad"
date: 2026-11-02
summary: "The X key on my AULA F108 Pro stopped working, so I picked up a soldering iron, ran into a short and a ripped pad, and fixed it by testing Claude's guesses one at a time and running a wire to the next key's pad."
cover: /images/20261102-aula-f108-keyboard-repair/01-분해-전-독거미-F108.webp
---

The X key on my AULA F108 Pro stopped working, so I picked up a soldering iron, ran into a short and a ripped pad, and fixed it by testing Claude's guesses one at a time and running a wire to the next key's pad.

🙋🏻‍♂️ Keyboard soldering? I heard you just touch it with the iron and you're done. 🙋🏻‍♀️ So did I, haha.

![The AULA F108 keyboard before disassembly, with grey keycaps and a knob in the top right](/images/20261102-aula-f108-keyboard-repair/01-분해-전-독거미-F108.webp)
<small>The F108 Pro before I opened it, back when I thought fixing one X key would be the end of it</small>

One weekend I was tinkering with keyboards and playing around with Claude. Then my wife said something from the side: "Aren't you typing a bit too hard?" 🤔

I said I would type more quietly. But the comment stayed with me. Then I saw a pretty keyboard selling cheap on Coupang's overseas direct shipping, and I bought it right away. Up to here it was an ordinary shopping story. 😛

This post is a repair log that started with that keyboard's X key. It was my first time soldering, and I didn't have a multimeter either. **So why didn't I give up halfway?**

> **Goal** Bring the dead X key back<br>
> **Obstacles** A pad ripped off during soldering, a short that made two rows press together, no measuring tools<br>
> **Result** Short removed, X key restored with a wire detour to the neighboring key's pad

## Box one📦 A noisy keyboard and an X that won't press

![A Coupang review screen with a five-star review on the AULA F108 Pro 104-key Caramel Latte switch model](/images/20261102-aula-f108-keyboard-repair/02-쿠팡-리뷰.webp)
<small>The AULA F108 Pro Caramel Latte I bought through Coupang, and the purchase review written with my Claude automation</small>

The model I bought was the AULA F108 Pro, 104 keys, Caramel Latte switches. I even wrote the review with my Claude automation. I throw in a few keywords and Claude writes the review and clicks the submit button. But once it arrived and I typed a few words, it was louder than I expected. 😫

I happened to have some Peach switches lying around at home. This keyboard is hot-swappable, so you can pull the switches out and replace them, and I swapped every one. 👀**<mark>I bought the keyboard to be quieter, and the real problem started the moment I changed the switches.</mark>**

![A keyboard with the keycaps removed and pink Peach switches plugged in here and there](/images/20261102-aula-f108-keyboard-repair/03-피치축-교체.webp)
<small>The F108 Pro mid-swap, with the stock switches coming out and my spare Peach switches going in</small>

When I tested it, X didn't register. I tried a different switch and a few other things, but nothing changed. I searched on Naver and found a post saying you just open the back board and touch it lightly with a soldering iron. I followed [a repair post on AULA F99 key input failure](https://blog.naver.com/ststeel/224044004123), and that post is also where I learned you must disconnect the battery when you open the bottom case. 🤩

![A Daiso soldering iron and solder wire, still in the packaging](/images/20261102-aula-f108-keyboard-repair/04-다이소-인두기와-납.webp)
<small>The soldering iron and solder wire I picked up at Daiso on the way home</small>

I went straight to Daiso, bought an iron and solder, and headed home. It was my first time soldering.

![The keyboard with only a few keycaps around X pulled out](/images/20261102-aula-f108-keyboard-repair/05-홈-주위-키캡-뽑기.webp)
<small>Only the keycaps around the bottom case's locking slots pulled out</small>

Disassembly was easier than I thought. Pull only the keycaps around the slots that lock the bottom case, put anything hard into the slot, and pop it open like a lever. If you gently pry only where you need to, it comes apart easily. The first thing I did after opening it was disconnect the battery. 👍

| Step | What I did |
|---|---|
| 1 | Pulled only the keycaps around the bottom case's locking slots |
| 2 | Put a hard tool into the slot and popped it like a lever |
| 3 | Gently pried apart only where needed |
| 4 | Disconnected the battery as soon as it opened |

![Prying the bottom case open with a hard tool in the slot](/images/20261102-aula-f108-keyboard-repair/06-지렛대로-하판-열기.webp)
<small>Opening the bottom case by levering a hard tool in the slot</small>

![The inside of the keyboard on first opening, with foam, wiring and the battery cable visible](/images/20261102-aula-f108-keyboard-repair/07-첫-오픈-배터리.webp)
<small>The inside of the keyboard on first opening, and the battery cable to disconnect first</small>

## Box two📦 Ruling out guesses one by one with Claude

![The soldering iron plugged in and heating up, with solder wire and the keyboard next to it](/images/20261102-aula-f108-keyboard-repair/08-인두기-달구기.webp)
<small>Heating up the Daiso soldering iron for the first time</small>

I heated the iron and looked at the back of the X position. One side of the socket was sticking up a little. At the time I thought the solder had just lifted. 💥**In fact it wasn't the solder: the copper pad on the board had been torn off entirely.** 🤯

![The X socket lifted slightly and sticking up from the board](/images/20261102-aula-f108-keyboard-repair/09-튀어나온-소켓.webp)
<small>The X hot-swap socket sticking up, back when I didn't know the pad was torn</small>

![A single black hot-swap socket that fell off, resting on a palm](/images/20261102-aula-f108-keyboard-repair/10-떨어진-소켓.webp)
<small>The X socket I was about to reattach without knowing anything</small>

Without knowing any of this, I soldered the socket back on. I took the socket from the unused F10 position. When the first repair was done, I thought I had nailed it. 😎

![The first soldering attempt, melting solder wire and dropping it onto the socket spot](/images/20261102-aula-f108-keyboard-repair/움짤1-첫-납땜.webp)
<small>The wrong way: just dropping melted solder without heating the board</small>

![The back of the board after the first soldering](/images/20261102-aula-f108-keyboard-repair/11-1차-수리.webp)
<small>The first repair, which I thought went well at the time</small>

The result got worse. X still didn't press, and unrelated keys started pressing together in pairs. I pressed them one by one on a keyboard test screen and in Notepad, and here is what I found.

![Pressing keys around X on the reassembled keyboard prints the wrong letters in Notepad](/images/20261102-aula-f108-keyboard-repair/움짤2-첫-결과-메모장.webp)
<small>Notepad right after the first repair, when I pressed keys expecting it to just work</small>

| Key pressed | Result |
|---|---|
| Ctrl or Shift | Both press together |
| Alt | Presses with Z |
| Space | Presses with B |
| . | Presses with Fn |
| ↑ | Presses with ↓ |
| A·S·D·F·G | Each works fine |
| C·V·N·M | Each works fine |

This is where Claude and I really got going. Claude's very first diagnosis was a **line short** where two rows had stuck together. Every pair was one key from the Shift row and the key right below it on the Ctrl row. 🤔

![A full board photo with the key pairs that press together marked with orange circles and red lines](/images/20261102-aula-f108-keyboard-repair/13-같이-눌리는-짝.webp)
<small>A map of the key pairs that press together on the back of the board: every pair is a socket right above or below the other</small>

Of course it didn't look this clean from the start. When I uploaded a photo of the torn spot, the pad area on the left of X was brown, not silver. Scraping it with a box cutter showed nothing. Every other key's pad was silver, so the pad had clearly been ripped off. 😮

![The back of the X position: the left square pad area is empty and brown, with burn marks around it](/images/20261102-aula-f108-keyboard-repair/12-뜯긴-패드-자리.webp)
<small>The X position with only a brown base left where the pad was torn off, and burnt flux marks around it</small>

What I had been calling "the little plate" was properly called a copper pad. It's a thin metal plate that holds the switch leg, and because it's copper printed onto the board, you can't take one from somewhere else and stick it on. ✔**<mark>The socket is the only thing you can transplant; a missing pad has to be replaced with a wire.</mark>**

Without a multimeter there was only one way left. Fix one suspicious spot, press the keys again, and cross it off if nothing changes. Claude would suggest a candidate, I would actually try it and report back. Here are the guesses we crossed off that way.

| Guess | What I actually tried | Result |
|---|---|---|
| Broke it by plugging in while hot | Asked Claude. The answer was that at 5V low voltage, heat is very unlikely to damage the chip | Ruled out |
| Metal debris on the board | Removed it with tweezers | No change |
| Burnt flux marks | Wiped them off | No change |
| Silver rings around the holes are solder | Claude saw them as solder, but when I looked they were switch legs | Claude was wrong, ruled out |
| Solder blob | It was only piled high on the pad, not touching nearby traces | Irrelevant |
| X switch leg touching inside the hole | Pulled the X switch and tested | No change |

Claude was wrong too. Seeing the silver rings as solder, and first explaining that "the two whole rows become one," were both wrong. When I asked back whether lots of keys in those rows didn't still work on their own, it corrected the explanation right away. Even with two rows shorted, only **columns that have keys in both the upper and lower row** get tied together. C·V·N·M were fine because the row below them is the space bar, so they had no partner. 😮

![A board photo with the Shift row trace and the Ctrl row trace drawn, joined at one point](/images/20261102-aula-f108-keyboard-repair/14-두-줄-쇼트-원리.webp)
<small>A drawing on the board of how the Shift row trace and the Ctrl row trace touch at one point</small>

I also confirmed this explanation by searching. A keyboard sends a signal down one column at a time and reads the rows, so if two rows are joined, the keys above and below register together ([QMK docs](https://develop-docs.qmk.fm/how_a_matrix_works)). I also learned that you can't tell a board short from a dead controller chip by the symptoms alone. But since the spot I had worked on sat exactly between the two tied rows, I bet on the board. 😎

## Box three📦 A toothpick and a detour to the next pad

I wondered if I had to go buy a multimeter. I asked Claude to think of a version where I don't buy one. The answer was to use the keyboard tester screen itself as the measuring tool. 🤩

![A close-up of the torn area with the zone to press with a toothpick circled in orange](/images/20261102-aula-f108-keyboard-repair/15-이쑤시개로-쇼트-찾기.webp)
<small>The zone to press firmly with a toothpick while holding Ctrl</small>

If you hold Ctrl, Shift lights up on the screen too. In that state, you press around the torn area here and there with a toothpick and look for the point where Shift turns off. A toothpick doesn't conduct electricity, so it won't muddy the result. I kept pressing until something went "tick," and Shift started behaving on its own. 🤯

It looks like the end of a lifted copper trace had been touching the row trace below and then came apart. 💥**<mark>A toothpick caught the short I couldn't find with my eyes.</mark>**

That left X. I didn't know where to connect the leg on the torn side. At first Claude thought the S key side was more likely, because most keyboards share columns diagonally like Z-A-Q and X-S-W. The method of touching a wire by hand to check before soldering came from a repair case in the keyboard community ([KeebTalk case](https://www.keebtalk.com/t/need-help-fixing-lifted-pads-hotswap-socket/20075)). 🤔

![A photo around X with the fixed point and candidates ①–⑦ circled](/images/20261102-aula-f108-keyboard-repair/16-X-연결-후보.webp)
<small>Seven candidate spots to touch the wire to, with X's right pad as the fixed point</small>

For the wire, I pulled one strand from a LAN cable and stripped both ends. When I first soldered it in, everything worked except X. It turned out that once the socket is attached, you have to plug in a switch and hold it down while touching the wire. The two legs of the socket only connect when the switch is pressed. 😫

![A thin wire pulled from a LAN cable with the insulation stripped](/images/20261102-aula-f108-keyboard-repair/17-랜선-전선.webp)
<small>A single strand pulled from a LAN cable with both ends stripped</small>

![Soldering a wire from the X socket's left leg onto a neighboring pad](/images/20261102-aula-f108-keyboard-repair/움짤3-전선-납땜.webp)
<small>Soldering the wire on the socket's left leg onto the neighboring pad</small>

With the switch plugged in, I touched again and got answers. Touching the D49 and D48 pads above printed D. That meant the leg on the torn side was already connected to the same line as D. Then I touched the D63 pad right next to it, and X appeared. It wasn't S, which Claude had called most likely, or D, the next candidate. 😮

![The path connecting the D63 pad and the X socket leg drawn as a blue line](/images/20261102-aula-f108-keyboard-repair/18-D63-연결.webp)
<small>The wire path connecting the X socket to the D63 pad right next to it</small>

In effect, the connection that used to run to the board above now runs to the pad next door. When not pressed it stays quiet, and when pressed X registers exactly once. ✔**<mark>I found the right spot not by guessing but by actually touching the wire.</mark>**

![A laptop Notepad screen checking that pressing X types](/images/20261102-aula-f108-keyboard-repair/19-메모장-테스트.webp)
<small>Checking X input in Notepad after the repair</small>

![A keyboard test site showing the X key registered](/images/20261102-aula-f108-keyboard-repair/움짤4-X-테스트-완료.webp)
<small>X input confirmed on a keyboard test site after the repair</small>

One limit remains. You can't press X and C at the same time. Each key should have its own diode, and X is now borrowing C's. It makes no difference in everyday chatting, so I left it and reassembled the keyboard. In hindsight, I should have taken the socket from Pause rather than F10. 😛

| What's left | Status |
|---|---|
| X and C at the same time | Doesn't work. Can be fixed by moving the wire to X's own diode leg |
| F10 | Empty, since I took its socket. Can move the Pause socket over or remap the key |
| X socket | Weak, with one pad missing. Support the socket from behind when pulling the switch |

## I could have given up

Honestly, I could have given up halfway. When the short happened, and when I had removed the metal debris, wiped the burn marks and even pulled the switch with no change. But every time Claude and I went back and forth, there was one more thing to try, and I kept feeling it would work. 🤔

What Claude did wasn't getting the answer right. It heard the symptoms, suggested candidates, crossed them off based on what I tried, and came up with another approach when we got stuck. When I uploaded a photo, it marked right on it where I should look. It made plenty of wrong guesses, but they were crossed off as soon as I checked. 💰**<mark>Even when nobody knows the answer, actually checking guesses one by one and crossing them off opens a path.</mark>**

Someone soldering for the first time saved a ripped pad without even a multimeter. It made me think this AI era, where things that wouldn't work get made to work, is a good one. Maybe whether you can fix something comes down less to skill and more to whether there's always a next thing to try? 😎

If you got stuck in a similar way fixing an AULA keyboard or a hot-swap board, feel free to leave a comment.

Sources

| Source | What it covers |
|---|---|
| [AULA F99 key input failure (Korean)](https://blog.naver.com/ststeel/224044004123) | Opening the bottom case, disconnecting the battery, reattaching with an iron |
| [QMK: How a Keyboard Matrix Works](https://develop-docs.qmk.fm/how_a_matrix_works) | Row/column matrix and how diodes work |
| [KeebTalk: Need help fixing lifted pads Hotswap socket](https://www.keebtalk.com/t/need-help-fixing-lifted-pads-hotswap-socket/20075) | Rerouting a ripped hot-swap pad with a wire, and how to find where to connect |
