---
title: "Backing up travel footage: I left it to AI overnight and got a verification report in the morning"
date: 2026-10-18
series: video-archive-ai
part: 1
summary: "Footage from a trip to Tanzania was scattered across several cameras and hard drives. I let AI consolidate it onto one drive overnight, and in the morning I had a report that checked every file against its source."
---

Footage from a trip to Tanzania was scattered across several cameras and hard drives. I let AI consolidate it onto one drive overnight,
**and in the morning I had a verification report that checked every file against its source.**

Doing it by hand would have eaten a few weekends.
I plugged in the drives, went to bed, and read the report in the morning.
The backup started on a Wednesday night, by the weekend I had Premiere sequences, and on Monday morning the subtitles were still running.
There was a lot to cover, so I split these work notes into four parts. This first one is about backing up and organizing the files.

## Starting point: scattered files and a full drive

When I got back from the trip, the footage was spread across every device.

| Location | What was on it |
|---|---|
| Osmo Nano SD card | Footage from the second half of the trip |
| Osmo Nano internal memory | Clips that never made it to the SD card |
| GoPro SD card | Footage from the second half of the trip |
| 1TB external drive | DAY 1–12, moved over during the trip. About 6GB free |
| 2TB external drive | Around 320GB of older material, like our wedding photos |
| Another laptop | DAY 4 and DAY 6, about 300GB |

There were five kinds of camera: Osmo Nano, GoPro, Canon 100D, Canon G7X (my wife's camera), and a phone.

The catch was that I had another shoot the next day, so the SD cards had to be cleared that night.
The original plan was simple. Gather everything from the trip on the 2TB drive, and move the old material on the 2TB drive over to the 1TB drive.

The AI flagged an ordering problem first.
With only 6GB left on the 1TB drive, 320GB wasn't going to fit. And if I also cleared the SD cards, the trip files would exist in only one place: the 2TB drive.
So I changed the plan like this.

| Files | Gather on | Second copy |
|---|---|---|
| DAY 1–12 on the 1TB drive | 2TB drive | Left on the 1TB drive for now |
| Osmo and GoPro SD cards, Osmo internal memory | 2TB drive | D drive on the PC |
| Old material on the 2TB drive | Moved to the PC's D drive | |

To avoid mixing them up, I also named the drives. The 2TB drive got my wife's name, the 1TB drive got mine.

I used the AI through the Claude desktop app connected to my home PC. The AI opens, copies and compares the files itself. I wrote up how that connection is set up separately in part 3.

## Copying and verifying overnight

Bulk copying from the command line was slow, so the AI drove the 7-Zip File Manager through screen control.

At first it waited for one job to finish before asking about the next, which was slow.
I asked whether there was any reason to do them one at a time. It said there wasn't. From then on it ran them in parallel.

This is where things stood just before I went to sleep.

| Job | Progress | Expected finish |
|---|---|---|
| Osmo internal memory → 2TB drive and D drive | Part of 43 files | 1:30 a.m. |
| Old material on 2TB drive → D drive | 32GB of 257GB | 3 a.m., delete source after verification |
| DAY 1–12 on 1TB drive → 2TB drive | 125GB of 908GB | 5–6 a.m. |

It also listed what I had to leave alone before bed: keep the Osmo connected, keep both external drives connected, don't close the Claude app or the 7-Zip windows.
It said it would leave a report around 6:20 a.m., and it did.

| Job | Morning report |
|---|---|
| Osmo SD (66 files, 103GB) | Copied to both the 2TB drive and the D drive, matches the source |
| GoPro SD (19 files, 12GB) | Same |
| Osmo internal memory (22 files) | Same |
| DAY 1–12 on 1TB drive → 2TB drive | All 2,511 files match by name and size. 299 of them, all the large files plus a random sample, also compared byte by byte |
| Old material on 2TB drive → D drive | 9,938 files confirmed, then deleted from the drive |
| 33 GoPro files (17.5GB) duplicated in DAY 8 and DAY 10-11 | Confirmed identical, deleted from DAY 10-11 |

**Only what had been verified was marked "safe to delete."**
It told me not to delete the two SD cards and the Osmo's internal memory from the computer, but to format them in the cameras. I did that and went to work.

After the cleanup, the 2TB drive became the trip drive. DAY 1–15 all fit, with 794GB left over.
I decided I didn't need a second backup, so in the end I cleared the trip copy off the 1TB drive and used it for other material.

![Travel folder list](/images/20261018-travel-footage-ai-backup/01-여행-폴더-목록.webp)
<small>The travel folder list after cleanup. The DAY folders and the temporary GoPro and Osmo folders are gathered in one place.</small>

In the next post I cover how I synced the capture times of these 905 clips camera by camera and built per-day sequences in Premiere.
