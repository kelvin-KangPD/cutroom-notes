---
title: "Keyboard PCB self-repair guide: from a hot-swap key that won't register to soldering a ripped copper pad on an AULA"
date: 2026-11-03
summary: "When one key on a hot-swap keyboard stops working, here is where to look first for each symptom, in the order I actually checked while fixing my AULA F108."
cover: /images/20261102-aula-f108-keyboard-repair/12-뜯긴-패드-자리.webp
---

When one key on a hot-swap keyboard stops working, find your symptom below and jump straight to that number.

```
A key won't register
├ Works with another switch → done
└ Still dead → step 2
   ├ Socket is lifted → step 3
   │  └ Pad is brown → step 4
   ├ Two keys press together → step 5
   └ Pad is gone → step 6
```

| Where I am now | Jump to |
|---|---|
| Not sure what the symptom even is | [1. Sort by symptom first](#s1) |
| Swapping the switch didn't help | [2. Rule out the switch and open the case](#s2) |
| The socket on the back is lifted | [3. Resolder a lifted socket](#s3) |
| The socket spot is brown | [4. Check whether the copper pad is ripped](#s4) |
| Two keys press together | [5. Two keys at once means a line short](#s5) |
| The pad is gone and there's nowhere to attach the socket | [6. No pad? Reroute with a wire](#s6) |
| It's fixed but something is still off | [7. What's left after the fix](#s7) |

This is the actual path I took while fixing the X key on my AULA F108 Pro. It was my first time soldering, and I had no multimeter. How I got here is in the [self-repair log](/en/posts/aula-f108-keyboard-repair/).

| What you need | What I used |
|---|---|
| Soldering iron and solder | Bought at Daiso |
| Tool to open the case | Anything hard |
| Tool to find the short | A toothpick and a keyboard test site |
| Wire for the detour | One strand from a LAN cable |
| Spare socket | Taken from an unused key position |
| Multimeter | Not needed |

## 1. Sort by symptom first {#s1}

Each symptom has a different cause and a different place to fix. Based on what I actually saw, it breaks down like this.

| Symptom | Suspect | Go to |
|---|---|---|
| One key dead, works with a different switch | The switch | Done |
| One key dead, same with a different switch | The hot-swap socket on the board | 2 → 3 |
| One side of the socket sticks up from the board | Socket solder or copper pad | 3 → 4 |
| Since soldering, two unrelated keys press together | Line short | 5 |
| The pad at the socket spot is empty and brown | Ripped copper pad | 4 → 6 |

Let's settle the names first. The black part the switch plugs into is the hot-swap socket, and the silver plate its legs attach to is the copper pad. The diode is a separate small part next to the socket.

## 2. Rule out the switch and open the case {#s2}

The first thing to do is plug a different switch into the dead spot. I swapped all my switches to Peach switches because the keyboard was loud, and then X stopped working. It stayed dead with a different switch, so from there I treated it as a board problem.

The bottom case opens more easily than you'd think.

| Step | What to do |
|---|---|
| 1 | Pull only the keycaps around the bottom case's locking slots |
| 2 | Put a hard tool into the slot and pop it like a lever |
| 3 | Gently pry apart only where needed |
| 4 | Disconnect the battery as soon as it opens |

![Prying the bottom case open with a hard tool in the slot](/images/20261102-aula-f108-keyboard-repair/06-지렛대로-하판-열기.webp)
<small>The bottom case opened by levering a tool in the slot</small>

I learned that you must disconnect the battery from [an AULA F99 repair post](https://blog.naver.com/ststeel/224044004123). If it's a wireless keyboard, do this first.

![The inside of the keyboard on first opening, with foam, wiring and the battery cable visible](/images/20261102-aula-f108-keyboard-repair/07-첫-오픈-배터리.webp)
<small>The battery cable you see when you first open the bottom case</small>

## 3. Resolder a lifted socket {#s3}

If one side of the socket is sticking up a little on the back of the dead key, you're here. If the solder lifted and the leg came off the pad, you just need to resolder it.

![The X socket lifted slightly and sticking up from the board](/images/20261102-aula-f108-keyboard-repair/09-튀어나온-소켓.webp)
<small>The X hot-swap socket with one side lifted from the board</small>

I got the soldering method wrong at first. I just melted solder with the iron and dropped it onto the socket spot, but **the right way is to heat the board first and then press the solder onto it**. The clip below shows the wrong way.

![The first soldering attempt, melting solder wire and dropping it onto the socket spot](/images/20261102-aula-f108-keyboard-repair/움짤1-첫-납땜.webp)
<small>The wrong way: dropping melted solder without heating the board</small>

If the socket came off completely, take one from an unused key position. I took mine from F10, and in hindsight I should have used Pause. Pick a key you rarely use.

![A single black hot-swap socket that fell off, resting on a palm](/images/20261102-aula-f108-keyboard-repair/10-떨어진-소켓.webp)
<small>A hot-swap socket that came off the board</small>

Before you solder, always check step 4 first. If what lifted was the pad and not the solder, reattaching won't work and only makes things worse.

## 4. Check whether the copper pad is ripped {#s4}

Look at the color of the pad where you removed the socket. If every other key's pad is silver and only this spot is brown, the pad is ripped.

![The back of the X position: the left square pad area is empty and brown, with burn marks around it](/images/20261102-aula-f108-keyboard-repair/12-뜯긴-패드-자리.webp)
<small>The X position showing a brown base instead of a silver pad</small>

I scraped it lightly with a box cutter and nothing came up. That settled it.

| Check | Verdict |
|---|---|
| The pad is silver and only the solder came off | Go back to step 3 and resolder |
| The pad spot is brown and scraping shows no metal | Ripped pad. Step 6 |

A copper pad is copper printed onto the board, so you can't take one from somewhere else and stick it on. The socket is the only thing you can transplant; **a missing pad has to be replaced with a wire.**

## 5. Two keys at once means a line short {#s5}

If two unrelated keys started pressing together in pairs after you soldered, it's a line short. In my case it happened right after the first soldering.

![Pressing keys around X on the reassembled keyboard prints the wrong letters in Notepad](/images/20261102-aula-f108-keyboard-repair/움짤2-첫-결과-메모장.webp)
<small>Pressing keys in Notepad after the first soldering</small>

| Key pressed | Result |
|---|---|
| Ctrl or Shift | Both press together |
| Alt | Presses with Z |
| Space | Presses with B |
| . | Presses with Fn |
| ↑ | Presses with ↓ |
| A·S·D·F·G, C·V·N·M | Each works fine |

Every pair was one key from the Shift row and the key right below it on the Ctrl row. A keyboard sends a signal down one column at a time and reads the rows, so if two rows are joined, the upper and lower keys in the same column register together ([QMK docs](https://develop-docs.qmk.fm/how_a_matrix_works)). C·V·N·M were fine because the row below them is the space bar, so they had no partner.

![A full board photo with the key pairs that press together marked with orange circles and red lines](/images/20261102-aula-f108-keyboard-repair/13-같이-눌리는-짝.webp)
<small>A map of the key pairs that press together, marked on the board</small>

![A board photo with the Shift row trace and the Ctrl row trace drawn, joined at one point](/images/20261102-aula-f108-keyboard-repair/14-두-줄-쇼트-원리.webp)
<small>How a line short works: the Shift row and the Ctrl row touching at one point</small>

You can find the short without a multimeter.

| Step | What to do |
|---|---|
| 1 | Connect the keyboard and open a keyboard test site |
| 2 | Hold down one key from a pair (I used Ctrl). Its partner (Shift) lights up on screen too |
| 3 | Press around the area you worked on, here and there, with a toothpick |
| 4 | The point where the partner key turns off is the short |

A toothpick doesn't conduct electricity, so it won't muddy the result. While pressing, something went "tick," and Shift started behaving on its own. It looks like the end of a lifted copper trace had been touching the row trace below and then came apart.

![A close-up of the torn area with the zone to press with a toothpick circled in orange](/images/20261102-aula-f108-keyboard-repair/15-이쑤시개로-쇼트-찾기.webp)
<small>The zone to press with a toothpick</small>

Here is what I tried before catching the short that didn't help. If your symptoms match, you can skip these.

| What I tried | Result |
|---|---|
| Removing metal debris on the board with tweezers | No change |
| Wiping burnt flux marks | No change |
| Cleaning up a solder blob | It wasn't touching nearby traces, so irrelevant |
| Pulling the dead key's switch and testing | No change |

## 6. No pad? Reroute with a wire {#s6}

Connect the socket leg on the ripped side directly to the line it's supposed to reach, using a wire. Find where to connect it by touching the wire by hand before soldering. This method comes from a [KeebTalk repair case](https://www.keebtalk.com/t/need-help-fixing-lifted-pads-hotswap-socket/20075).

**The most important thing is to plug in the switch and hold it down while touching the wire.** The two legs of the socket only connect when the switch is pressed. At first I touched without a switch and spent ages confused because only X wouldn't register.

| Step | What to do |
|---|---|
| 1 | Solder the socket leg on the side that still has a pad |
| 2 | Solder one end of a wire to the leg on the ripped side |
| 3 | Plug in the switch, hold that key down, and touch the other end of the wire to each candidate pad |
| 4 | Find the pad where that key shows up on the test screen |
| 5 | Solder the wire to that pad |

![A photo around X with the fixed point and candidates ①–⑦ circled](/images/20261102-aula-f108-keyboard-repair/16-X-연결-후보.webp)
<small>Seven candidate pads to touch the wire to</small>

For the wire, I pulled one strand out of a LAN cable and stripped both ends. It's thin, so it was easy to fit between pads.

![A thin wire pulled from a LAN cable with the insulation stripped](/images/20261102-aula-f108-keyboard-repair/17-랜선-전선.webp)
<small>One strand from a LAN cable with both ends stripped</small>

Once you touch, the result shows up right away. In my case, touching the D49 and D48 pads above printed D. That meant the leg on the ripped side was already connected to the same line as D. Touching the D63 pad right next to it brought up X. It wasn't S, which I'd expected, or D, the next candidate. So **rather than guessing, it's faster to touch every candidate.**

![Soldering a wire from the X socket's left leg onto a neighboring pad](/images/20261102-aula-f108-keyboard-repair/움짤3-전선-납땜.webp)
<small>Soldering the wire from the socket leg onto the neighboring pad</small>

![The path connecting the D63 pad and the X socket leg drawn as a blue line](/images/20261102-aula-f108-keyboard-repair/18-D63-연결.webp)
<small>The final path from the X socket leg to the D63 pad</small>

After connecting it, check that it stays quiet when not pressed and registers once when pressed.

![A keyboard test site showing the X key registered](/images/20261102-aula-f108-keyboard-repair/움짤4-X-테스트-완료.webp)
<small>X input after the repair, confirmed on a keyboard test site</small>

## 7. What's left after the fix {#s7}

A key saved with a wire detour isn't exactly like the original. In my case, this is what's left.

| What's left | Status |
|---|---|
| X and C at the same time | Doesn't work, because X borrows C's diode. Can be fixed by moving the wire to X's own diode leg |
| The key I took the socket from (F10) | Empty. Move an unused key's socket (Pause, etc.) or remap the key |
| The rerouted socket | Weak, with one pad missing. Support the socket from behind when pulling the switch |

It's fine for everyday typing, so I reassembled it as is.

Sources

| Source | What it covers |
|---|---|
| [AULA F99 key input failure (Korean)](https://blog.naver.com/ststeel/224044004123) | Opening the bottom case, disconnecting the battery |
| [QMK: How a Keyboard Matrix Works](https://develop-docs.qmk.fm/how_a_matrix_works) | Row/column matrix and how diodes work |
| [KeebTalk: Need help fixing lifted pads Hotswap socket](https://www.keebtalk.com/t/need-help-fixing-lifted-pads-hotswap-socket/20075) | Rerouting a ripped pad with a wire |
