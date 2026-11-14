---
title: "I Made Shorts from Public-Domain Folk Songs (Military Band Recordings Only, No AI Music)"
date: 2026-11-14
summary: "One song everyone in a country knows, plus the story of how it came to be, in 60 seconds. Only songs out of copyright, only real recorded performances. Notes from making three episodes in two days."
cover: /images/20261114-song-stories-shorts/01-세-편-첫-화면.webp
---

I'm making 60-second shorts about one famous song per country and the story behind it. I only use songs whose copyright has expired, and the sound is always a real recorded performance, never AI-generated. Over two days I made three episodes.

![First frames of three vertical videos. Left: a landscape painting with "WALTZING MATILDA · AUSTRALIA · 1895". Middle: an English countryside painting with "AMAZING GRACE · ENGLAND · 1773". Right: a Times Square New Year ball photo with "AULD LANG SYNE · ABOUT 1 MILLION HEAR IT AT MIDNIGHT"](/images/20261114-song-stories-shorts/01-세-편-첫-화면.webp)
<small>The opening frames of the three episodes: Waltzing Matilda (Australia), Amazing Grace (made as the US episode), Auld Lang Syne (Scotland)</small>

## Why put songs on a war channel

I run Korea Remembers, a channel that covers the 22 nations that fought in the Korean War, one country at a time. The idea of adding each country's song came first, but tying it to the war felt forced. So I kept the same channel, made a separate playlist, and split the rules.

| Item | War episodes | Song episodes |
|---|---|---|
| Story | That country's units, battles, people | The song and that country's story only. The Korean War is not mentioned |
| Opening / ending | Strip of 22 flags, thank-you message | Neither. Starts with one line of the song and ends with the song |
| Length | 3 minutes, 60 seconds | Under 60 seconds |
| Visuals | Photos of the time, hand-drawn maps | Old photos, paintings, sheet music |

The material is public-domain folk songs or national favorites. The country order follows the channel's audience: the US at 11.4%, the Philippines 6.8%, India 2.5%, Canada 2.1%, Australia 1.6%.

## One wrong note and it's fake

At first I considered laying down an AI-made imitation of each song. I dropped it. Koreans get angry when they see a strangely rearranged Arirang, and people from other countries feel exactly the same. I decided not to change a single melody, beat or instrument, which means using recordings of real people playing.

The catch is that the copyright of the song and the copyright of a recording are separate. Here is what I found researching the first song, Waltzing Matilda.

| Recording | Problem |
|---|---|
| First recording, 1926–27 (tenor John Collinson) | The melody differs from the one people know today. The notes say the 2nd and 4th lines were changed |
| 1938 Peter Dawson version | The recording that made the song a hit. Protection has ended in Australia and the UK, but in the US it lasts until the end of 2038 |
| US Marine 1st Division Band (2021) | Posted as "PUBLIC DOMAIN" on DVIDS, the US military's public media site. A wordless wind-band performance |

The Dawson version is the most "authentic," but 11% of viewers are in the US. I went with the band version. The lyrics appear only as on-screen captions.

![A video page on the DVIDS site. Title "1st Marine Division Band Performs "Waltzing Matilda"", a Marine band member playing a horn, and PUBLIC DOMAIN at the end of the info box below](/images/20261114-song-stories-shorts/02-군악대-음원-페이지.webp)
<small>The page where I got the audio for episode 1. PUBLIC DOMAIN is written at the very bottom of the info box. The 1st Marine Division was stationed in Australia during WWII and adopted this song as its division song</small>

All three episodes were sourced this way.

| Episode | Song | Recording used | Length |
|---|---|---|---|
| 1 | Waltzing Matilda | US Marine 1st Division Band (DVIDS) | 43.2 s |
| 2 | Amazing Grace | Sung version by the US Air Force Reserve band Southern Aire (Wikimedia Commons) | 39.3 s |
| 3 | Auld Lang Syne | US Army Band wind performance (Wikimedia Commons) | 58.9 s |

I don't cut or splice the performance. If it runs 43 seconds, the video is 43 seconds. Only Amazing Grace, whose full version is 130 seconds, was cut at the end of the first verse.

## Choosing by ear isn't automation

When there are several audio candidates, someone has to listen to all of them and judge "yes, that's the song." If that someone is me, it isn't automation. So I took the melody from the most-viewed version as a reference and had code compare the usable candidates, extracting pitch and aligning it even when the tempo differs.

![A horizontal bar chart. Reference versions of the same song score 0.57–0.64, six usable candidates of the same song 0.58–0.72, and two completely different songs 0.52 and 0.64](/images/20261114-song-stories-shorts/03-멜로디-비교-점수.webp)
<small>Lower means more similar melody, yet the unrelated songs scored lower than the real candidates</small>

It failed. A completely different song scored 0.52, looking "more similar" than the real candidates. Stretching to 40-second excerpts didn't help either, and it burned a lot of tokens. I stopped this approach. Now I just listen to the first 30 seconds of the top candidate myself.

## How one episode gets made

After two episodes, the order settled. I reuse the assembly tools I built for the war episodes.

| Step | What happens |
|---|---|
| 1 | Find the audio first: Wikimedia Commons, then DVIDS. Measure its length |
| 2 | Read the Wikipedia article once, build a fact table, write the script. Word count = (song length − 3 s of song-only intro − 5 s of outro) × 2.3 |
| 3 | Download old photos, paintings and scores from public sources |
| 4 | Generate the narration and get word timings by transcription |
| 5 | Write the cut list, assemble the timeline with the Premiere MCP, lay the music, export |
| 6 | Check length, black frames and left/right sound by numbers, then look at one summary sheet |

Working backward from the song's length to the script length is what differs from the war episodes. I can't cut the song, so the words must fit the song.

![Two video frames. Left: a hand-written old score with large caption "PLAYED A MARCH" and a small Korean line. Right: a black-and-white waterhole drawing with "BY A WATERHOLE"](/images/20261114-song-stories-shorts/04-악보와-자막.webp)
<small>Scenes from episode 1: the handwritten score taken down in 1895 and a waterhole drawing. "Said to be" legends and confirmed facts are written separately in the script</small>

## Grab the first 3 seconds with a big number

While uploading episode 2 I realized the opening was weak. The first 3 seconds need the feeling of "have you heard this song?" People want to belong to something big. "That many people know it? Do I know it too?" and they stop scrolling.

I don't invent numbers. I find a source in a search or two and round it.

| Song | Big number on screen | Basis |
|---|---|---|
| Waltzing Matilda | About 1 in 4 Australians picked it as the national song | 28% in the 1977 national vote |
| Amazing Grace | A song sung about once every 3 seconds | A biographer's estimate of roughly 10 million performances a year ÷ 31.5 million seconds in a year |
| Auld Lang Syne | About 1 million people hear it at midnight | Estimated Times Square New Year countdown crowd |

I couldn't find a "what % of people know it" survey for either song. When there isn't one, I substitute another big number, like a vote share or how often it's sung. This opening started from episode 3.

![Two video frames. Left: a Times Square New Year ball photo with "AULD LANG SYNE · ABOUT 1 MILLION HEAR IT AT MIDNIGHT". Right: handwritten lyrics with "SOUTH KOREA'S NATIONAL" and a Korean line](/images/20261114-song-stories-shorts/05-큰-수-도입부.webp)
<small>Episode 3. The left frame is the big-number opening. The right is the line saying South Korea sang its national anthem to this tune from 1945 to 1948</small>

## Where things stand

![YouTube playlist page. Title "Songs and Their Stories", publisher Korea Remembers, below it thumbnails of two shorts with 240 and 497 views](/images/20261114-song-stories-shorts/06-유튜브-재생목록.webp)
<small>The playlist Songs and Their Stories. As of today, episode 1 has 497 views and episode 2 has 240</small>

I uploaded three episodes, but the playlist shows only two today. Episode 3 has turned into an unavailable video, and I'm checking why.

There was also a mistake. Episodes 1–3 have a Korean subtitle line at the bottom. Videos meant for viewers worldwide don't need Korean text. From episode 4, the bottom line switches to Indonesian.

Episode 1 starts from the fact that Australia's best-loved song is really a story about a sheep thief.

{{shorts: UJUn_dsgcus}}
