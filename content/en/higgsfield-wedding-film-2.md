---
title: "Our wedding film, part 2: the workroom and the wandering scenes (the monitor is an HTML composite, the selfie cam is Seedance Edit)"
date: 2026-10-27
series: wedding-ai
part: 2
cover: /images/20261027-wedding-film-2/01-달-우주복-컷.webp
summary: "AI couldn't get the text right on the workroom monitor, so I composited it in HTML. For the wandering scene, I shot the selfie cam myself to keep my face fixed and used Seedance 2.5 Edit only for clothes and backgrounds. I also added a scene that deliberately says 'this is AI.'"
---

I didn't force AI to do what it couldn't. **I composited the monitor screen where the text had to be exact, and I shot the scene myself where my face had to stay in place.** The AI's only job was to put clothes and backgrounds on top.

In [part 1](/en/posts/higgsfield-wedding-film/) I covered the opening and the prep. Part 2 runs from after the opening to about 47 seconds in: the workroom where I ask AI about happiness, and the scene where I wander looking for the "flash."

![A man in a spacesuit on the moon's surface, with Earth and a green alien behind him](/images/20261027-wedding-film-2/01-달-우주복-컷.webp)
<small>0:41 in the final cut. The moon, from the wandering scene (AI-generated). The walk and the expression are straight from the footage I shot on a GoPro</small>

## AI can't write on the monitor

I made the workroom scene with Higgsfield's Cinema Studio, a video model where you pick camera, lens, aperture and genre to shoot like a film. One shot has me typing from the side and asking, "AI, what's the surest way for a person to be happy?" The other has me asking back, "Love? How do you find someone like that?"

![Higgsfield video history: three clips of a man typing in front of a monitor in a dark workroom](/images/20261027-wedding-film-2/04-시네마스튜디오-작업실.webp)
<small>Workroom shots made with Cinema Studio</small>

But the real star of this scene is the monitor. The screen where AI answers how to be happy has to be readable for the story to move. At first I tried to make that screen with AI too. As video, as images, switching models, I asked it to "close up on the part of this monitor with the AI's answer."

![Higgsfield image history: 8 close-ups of a monitor screen, with blurry English sentences or a blank screen](/images/20261027-wedding-film-2/05-모니터-생성-시도.webp)
<small>Monitor close-up attempts. The text comes out in English or smeared, and the last one is a blank screen</small>

Switching models didn't change where it got stuck. The text on screen was English, not Korean, and even that was nonsense like "What are your question stuff?" The closer the shot, the more the letters smeared. Every line had to match the subtitles, so look-alike text wouldn't do.

So I changed approach. **I made the monitor a blank screen, built the chat screen separately in HTML, recorded it, and composited it onto the monitor in Premiere.**

![Left, a monitor blank in light blue; right, the same monitor with the AI chat screen composited on](/images/20261027-wedding-film-2/06-빈-모니터-합성.webp)
<small>Left is the blank monitor made for compositing (AI-generated), right is the result with the HTML chat screen on it</small>

Switching to compositing came with a bonus. The storyboard line was "Go outside. When you meet your true match, something will flash! before your eyes," but in the final cut it turned into chat-style speech: "First go outside, and someone will appear where something goes flash! Go meet people." HTML is just typing the text yourself, so edits like this cost no credits.

![Chat screen with orange speech bubbles: "First go outside, and someone will appear where something goes flash," with a "*flash*" subtitle below](/images/20261027-wedding-film-2/07-대화-화면-번쩍.webp)
<small>0:31 in the final cut. The "flash" comes back later in the bench and wedding hall scenes</small>

## A scene that says "this is AI"

Next is S#2, the scene the storyboard called "the odd search." Kang PD goes outside as the AI said and wanders through a cafe, a park, the moon, a snowy mountain and a summer street looking for the flash.

![S#2 storyboard: cafe, park, space, winter mountain, summer street, and flopping down on a bench](/images/20261027-wedding-film-2/03-콘티-헤매기.webp)
<small>S#2 storyboard. The face stays locked in the center while outfit and background switch every 2–3 seconds</small>

I put this scene in for two reasons.

| Reason | What it does |
|---|---|
| The feel of searching for the flash | It gives the sense of roaming around looking for the "flash" the AI talked about |
| Reminding people it's AI video | Hiking a snowy mountain, a spacesuit on the moon, an alien walking by: anyone can see these couldn't be filmed for real. This stretch says on screen, "This is AI, don't be fooled" |

The second reason mattered more than I expected. After the film, quite a few older guests asked when we'd gone around filming all of that. Many of them thought we'd actually shot it. That's how hard it has become to tell AI video from reality. **A film made with AI needs a stretch where it's clearly recognizable as AI.** This scene played that role.

## I shot my face, AI did only clothes and backgrounds

The storyboard camera note for this scene was "C.U (Center-Locked), Body-Mount / Head-Lock." The face is pinned in the center as if the camera were strapped to the body, and only the world changes.

If AI makes that from scratch, the face position and size shift with every location. So I didn't hand this part to AI. **I shot 15 seconds of selfie cam myself, walking with a GoPro.** Then I put that clip into Seedance 2.5 Edit. Edit keeps the source video's motion and redraws only what the prompt specifies, so the walk, the expression and the camera shake stay as shot while backgrounds and clothes get swapped. The source clip shows the inside of my home, so it's not included here.

The first prompt was a shot list: just what location and what clothes at which second. Watching test runs, I added sentences one at a time. Here's why.

| Sentence added | Why |
|---|---|
| "The camera is handheld and walks with him; background and person share the same camera motion" | A selfie cam shakes with every step. The background has to shake the same way to read as one frame |
| For the first 2 seconds he sits in the workroom (@room), then stands up | A bridge from S#1 in the workroom into S#2 |
| "Reference images are for environment, lighting and clothing only; do not copy the person" | Narrowed what to take from the location references to environment, lighting and clothes |
| The full 15 seconds as a timed schedule | The shot list left blank what happens at each second and how the camera moves |

The most fun part of the results was the passersby. For each location the prompt only said "a woman walks past, seen from behind." In the cafe a woman walks past, in the park a woman in running gear jogs by, and on the moon a green alien walks past. As I said above, the alien is a device that makes it unmistakable this is AI, so I kept it.

![Four results from the wandering scene: the man in the cafe with a woman walking by, in the park with a woman jogging, a spacesuit and an alien on the moon, a white T-shirt on a summer street](/images/20261027-wedding-film-2/10-헤매기-결과-4장.webp)
<small>From top left: cafe, park, moon, summer street (AI-generated). The face position is straight from the source selfie footage</small>

In the final cut the wandering scene starts in the cafe at 0:36 and ends around 0:47. The storyboard's 25 seconds shrank to just over 10. The last shot, flopping down on a bench, hands over to the bench scene I made separately in part 3.

If I made the same scenes again, I'd do this.

| What to do | Why |
|---|---|
| Composite any screen with visible text from the start | A screen whose lines must match the subtitles couldn't be generated right, whatever model I used |
| Shoot what must stay fixed, then use Edit | Walk, expression and face position come from the source; AI only draws clothes and backgrounds |
| Timed schedule from the start | A shot list alone leaves timing and camera motion blank |
| Write the role of each reference in the prompt | I should have said from the start what to take from the location images |

Part 3 is the bench scene: why my face drifted further from me with every run, and why one photo matched to the angle beat a character built from many photos.

## Trial-and-error log

Workroom Cinema Studio: all 8 seconds, camera Modern, lens Halation Vintage, aperture f/1.4, genre Drama 2020s. Straight to 1080p with no 480p test. For 8 seconds, 720p was 20 credits and 1080p was 45–72.

| Time | Resolution | Content |
|---|---|---|
| Aug 31, 01:03 | 1080p | Typing from the side and saying, "AI, what's the surest way for a person to be happy?" |
| Sep 2, 01:27 | 1080p | Regenerated with the same line |
| Sep 2, 01:29 | 1080p | "Love? How do you find someone like that?" |

S#1 was 15 seconds in the storyboard, 0:00 to 0:15, but with the Beat motorcycle opening in front and a longer conversation it ran to 0:35 in the final cut.

Monitor generation attempts: on September 2 at 01:37 I made one 480p clip with Seedance 2.5, asking for "a conversation with AI on the screen like the example photo," "in light mode." On September 6 I went at it again with images. At 1:31 p.m., and between 4:17 and 4:26 p.m., I made several close-ups with Nano Banana Pro and Seedream 5.0 Pro, and at 4:28 I also tried Angles, which changes the viewing angle.

S#2 storyboard shots:

| Shot | Location | Outfit | Sound |
|---|---|---|---|
| #05-1 | Cafe → park | Light spring clothes, plain white tee | Silent-film-style rhythmic beat, cafe sounds |
| #05-2 | Park → space | Running gear, Oakley sunglasses | Shutter sound, space sound, wind |
| #05-3 | Space → winter mountain | Spacesuit | Same |
| #05-4 | Winter mountain → summer street | Winter hiking gear | Same |
| #05-4 | Summer street | Beads of sweat | Same |
| #06 | Low-angle bench from the ground | Flops down, exhausted, on the bench on the left | A sigh |

Seedance 2.5 Edit runs (August 30): locations called the location elements from part 1 (@bg-cafe, @bg-park, @bg-moon, @bg-snow, @bg-summer).

![Higgsfield video history for August 30: six thumbnails starting in a cafe or a dark workroom](/images/20261027-wedding-film-2/08-시댄스에디트-기록.webp)
<small>Seedance 2.5 Edit history for August 30. Thumbnails are first frames, so the early ones start in the cafe and the later ones, after I added the workroom bridge, start in the workroom</small>

| Version | Time | Resolution | What changed |
|---|---|---|---|
| v1 | 18:10 | 480p | Called five location elements and wrote only a timed shot list like "0.0s cafe white tee → 1.6s park running gear → 3.2s moon spacesuit…" |
| v2 | 19:30 | 480p | Shared camera motion sentence |
| v3 | 21:17 | 480p | 2 seconds in the workroom, "do not copy the person" |
| v3 again | 21:22 | 480p | Regenerated with the same prompt |
| v4 | 22:15 | 480p | Rewrote the full 15 seconds as a timed schedule |
| v4 final | 22:41 | 1080p | Swapped the snow and moon elements to @bg-snow-5 and @bg-moon-4 for the final |

The start of the v4 prompt:

```
@bg-snow-3 @bg-moon-3 @room @bg-park @bg-cafe @bg-summer
Keep the man's face, body, pose, expression and framing exactly
as in the source video throughout. He stays centred and sharp
the whole time. His face is clean-shaven with smooth, even skin.
OPENING: For the first two seconds he is ...
```

![Higgsfield video detail page: a man in a spacesuit on the moon, with the prompt and Seedance 2.5 Edit, 480p, 854x480, August 30, 2026, 10:15 p.m. in the right panel](/images/20261027-wedding-film-2/09-프롬프트-상세.webp)
<small>v4 480p detail page. Model, resolution, size and time stay on the right. I blurred the source video thumbnail in the panel</small>

| Item | Instruction |
|---|---|
| Face | Face, body, pose, expression and framing exactly as in the source. Centered and sharp to the end. Clean-shaven, smooth skin |
| Opening | Sitting in the monitor's glow, stands up at 2 seconds. Camera stays at eye level, no low angle |
| Location changes | Five locations as hard cuts after 4 seconds, each with a set time |
| Clothes and light | Clothes and lighting written separately per location |
| Gaze | "Searching for the flash." Looks around left to right only twice |
| Passersby | At each location a woman walks past, seen from behind. A different person each time, no men |
| Walk | The walk gets more tired with each location |

Credits: the final 1080p run alone was 132.73 credits. A 480p test started at 19.26, so this one run ate most of it. By the transaction history, close to 300 credits went out on August 30.
