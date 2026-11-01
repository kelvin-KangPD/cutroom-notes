---
title: "Face references for AI video: many photos from every angle vs one matching photo (wedding film part 3, the bench scene)"
date: 2026-10-27
series: wedding-ai
part: 3
cover: /images/20261027-wedding-film-3/00-캐릭터-강준구-대표.webp
summary: "When putting my face into AI video, one photo matched to the shot's angle looked far more like me than a character packed with front, side, up and down photos. And composition only worked when written as screen proportions, not meters."
---

When putting my face into AI video, **one photo matched to the shot's angle looked far more like me than a character packed with front, side, up and down photos.** A face that's small and far away didn't come out well either way.

I learned this on the bench scene of our wedding film. In the end there were two reasons I kept regenerating the same shot. The low-angle composition was hard to describe in words, and the more I reran it, the less my face looked like me. Getting the composition right also taught me to write in screen proportions instead of meters.

![A park path seen from up in a tree. A man in a white T-shirt sits on a bench, and next to him a woman in a white dress sits half hidden by leaves](/images/20261027-wedding-film-3/01-하이앵글-벤치.webp)
<small>0:50 in the final cut. The bench seen from a high angle (AI-generated). The leaves hiding my wife were laid over in the edit</small>

[Part 1](/en/posts/higgsfield-wedding-film/) was the opening and prep, [part 2](/en/posts/higgsfield-wedding-film-2/) the workroom and wandering scene. Part 3 runs from about 0:47 to 1:04: worn out from wandering, I sit on a bench and my wife offers me water. I split this scene across three cameras.

![A high-angle park image with a black stick figure and red arrows: the path from the walkway to the bench](/images/20261027-wedding-film-3/02-씬3-동선-설계.webp)
<small>Scene 3 blocking. I drew the walk from the path to the bench directly on top of an AI image</small>

| Camera | Position | What it does |
|---|---|---|
| A high angle | Looking down from up in a tree | Me walking up and sitting down, and my wife, her face hidden by leaves |
| B low angle | Bench seat height | I sit worn out, and a hand holding a water bottle comes in from off screen |
| C POV | My eye level | I look at the offered bottle, then raise my eyes to my wife's face (#07) |

In A my wife's face is hidden by leaves, so it's first revealed in C, after the bottle. After C come my face turned blankly toward her (#08), the zoom into the eye (#09), the montage inside the eye (#10), and the zoom back out to a smiling face (#11). The #10 montage is our real photos, so it's not included here.

## My face stopped looking like me

The face problem blew up most in B, the low angle where the water is offered. The camera looks at me from bench seat height, I'm slumped at the end of the bench, and a hand with a water bottle comes in from off screen right. Its owner is my wife, sitting off screen at the camera's end of the bench.

![Two low-angle results: a man at the end of a bench fanning his shirt, then a hand holding a water bottle coming in from the right beside him](/images/20261027-wedding-film-3/07-로우앵글-물병.webp)
<small>0:52 and 0:54 in the final cut (AI-generated). A hand with a water bottle comes in beside me as I fan my shirt</small>

Three things kept me regenerating this shot.

| Where it got stuck | Why | What I changed |
|---|---|---|
| The composition wouldn't land in words | Camera at seat height, backrest running long from the right of the frame, me at its end, the hand coming from off screen on the camera side. That space was hard to write out | Added "strictly follow the camera composition of the reference image," handing the composition I couldn't write to an image |
| The timing of the hand and my reaction | In this shot I'm just a tired guy. The startled look belongs to #08 later | Switched from an English prompt to a Korean one I wrote myself, toned the shirt fanning down to "light and slow," and finally added a timed schedule: 0–2s sigh, 2–6s fanning shirt, 6–8s hand with bottle |
| The face | Every rerun to fix the timing drifted my face a little further from me | Below |

"Does not look surprised" was in from first run to last. Only once I added the timed schedule did the hand's timing land, the same conclusion as the wandering scene in part 2.

![Higgsfield video history for September 6: several clips with the same composition of a man in a white tee from bench seat height; the top row has eye and tuxedo clips](/images/20261027-wedding-film-3/06-로우앵글-여덟-번-기록.webp)
<small>September 6 history. The middle two rows are the bench low angle. Same composition, but the face differs a little each run. The eye and tuxedo clips on top are part 4 scenes</small>

Here's what happened with the face. In Higgsfield I had character elements bundling many photos of my face: @강준구 with 7 photos, and the Soul character @강준구-cinema with 17 photos from different angles and places, like a cafe, a restaurant and our wedding shoot. You just call the name in the prompt and it draws that face. The high-angle video called @강준구-cinema, and the low-angle prompt also started by calling a character, "@char_jungu white short-sleeve T-shirt, jeans…." Convenient, but on the bench scene it didn't work well.

![Higgsfield Soul character 강준구-cinema detail page with 17 thumbnails from different angles and places below](/images/20261027-wedding-film-1/11-소울캐릭터-17장.webp)
<small>The Soul character @강준구-cinema with 17 photos. More photos didn't make the face look more like me</small>

First, distant faces were a problem. In a shot like the high angle, where the person is about 1/8 of the frame height, the face didn't come out well. In the low angle too I'm sitting deep in the frame, so my face isn't big. On top of that, run after run, my face drifted a little each time.

So here's what I learned. Rather than calling a character that mixes many angles, putting in just one photo of my face shot at an angle close to the shot I'm making produced a much better face. Mixing angles seems to average each angle into a face that's no one.

| Method | Result |
|---|---|
| Character element (bundles like @강준구 with 7 photos, @강준구-cinema with 17) | Easy to call. When the face is small or you rerun a lot, it gradually stops being me |
| One face photo matched to the shot's angle | The face comes out better. It takes the effort of picking the right photo for each shot |
| Small, distant face | Doesn't come out well either way. Frame closer for shots where the face must show |

## Composition in screen proportions, not meters

I started A, the high angle, as an image: lock the image, then use it as the first frame for the video. The composition of this one image kept going wrong. Grouped by the way it went wrong:

| What went wrong | Why it was a problem | What I changed |
|---|---|---|
| The camera crept closer with every run | Writing meters and angles like 4 m high, 8 m away, 25 degrees didn't work | Dropped the angle and gave only height and horizontal distance. Wrote **in screen proportions**: the person 1/8 of frame height, the bench 1/4 of frame width, the empty path the lower 2/3 |
| The bench shrank to one, or two benches faced each other front to back, or it went back to two | To hand over water from the side, we had to sit side by side, left and right on one bench, with an empty seat for me | `Exactly one bench`, the empty seat `wide enough for another person to sit down`. Dropped conditionals like "two people could sit" |
| Given a reference and four fixes at once, only the hair color changed | The sentence telling it to keep the reference as is overrode every other instruction | Two-step method. First make the location with the problem element (the person) removed, then use that as a reference and add only what's wanted |
| The path came out diagonal and looked awkward | Writing `diagonally` gave a halfway angle | `roughly horizontally`, one paving pattern |
| The sun was behind my wife | Backlight was only needed in C, when she appears blocking the sun | A and B switched to front light with the sun behind the camera |
| The leaves didn't cover my wife | She had to be passed over as background at first and noticed on a second look | Changed "the leaves cover her" to a state, like "her face is hidden behind these leaves." It never worked |

The core of the final prompt:

```
The camera is 3.5 metres above the ground. The horizontal distance
from the camera to the bench is 12 metres.
A paved walking path runs roughly horizontally across the frame ...
The empty path fills the lower two thirds of the frame.
Exactly one wooden park bench ... occupies about one quarter of the frame width.
... her figure occupies about one eighth of the frame height.
The left half of the bench seat is clearly empty and unoccupied,
wide enough for another person to sit down beside her.
Everything above her chest is hidden behind these leaves.
```

To the end, the leaves didn't cover my wife by a single pixel. They sat neatly in the top right corner every time. The model seemed to draw them as part of a background tree, not as foreground.

In the end I pulled up the history list and picked one myself. It was a blue dress, but it had the best distance, bench and path. I handled the leaves in Premiere by laying real leaf footage over it. **Handing what AI can't do over to the edit is a decision too.** I should have done it sooner.

![High-angle park image: a woman in a blue dress alone on one horizontal bench, with leaves only in the top right](/images/20261027-wedding-film-3/03-벤치A-일곱번째.webp)
<small>The run I picked from the list myself (AI-generated). A blue dress, and the leaves don't cover my wife</small>

I finished the picked image with Gemini and uploaded it back to Higgsfield, and it became the first frame of the A video. The video prompt for Seedance 2 was just "@강준구-cinema walks up the path and flops down on the bench, camera locked."

![Four high-angle results: a man walks up the path, sits on the bench and lowers his head. Beyond the leaves in front, a woman in a white dress](/images/20261027-wedding-film-3/04-하이앵글-결과-4장.webp)
<small>0:48–0:51 in the final cut (AI-generated). In the final cut the dress is white and the leaves in front cover my wife</small>

## "Water bottle POV": whose point of view?

Shot C (#07) is the tilt-up from the offered bottle to my wife's face. In our conversation I called this shot "water bottle POV," and that went wrong once.

Claude understood it as the bottle's point of view and wrote the prompt that way. What I meant was **my point of view looking at the bottle being offered.** The hand is my wife's, and the camera moving up from the bottle to her face is my gaze moving up. Only after fixing that did the bottle and hand land in the right place. When one word in a shot name is off, the whole prompt goes off.

I also dropped the phrase `soft veil`. I meant light spreading softly, but in a wedding film it risked being read as a bridal veil. For the glow I wrote `lens flare` and `bloom`.

![Three first-frame candidates for the bottle POV: a woman in a white dress offering a water bottle from the bench; in the last she smiles](/images/20261027-wedding-film-3/09-물병-첫-프레임.webp)
<small>The image stage of the bottle POV shot (AI-generated). The face is AI-made</small>

The motion was written as a timed schedule: 0–1s the bottle, 1–2.2s tilt up following the arm, 2.2–3.3s backlit sun flare, 3.3–4.2s she leans in and blocks the sun, 4.2–6s smile and line.

![Two tilt-up results: a woman in a white sleeveless top in strong backlit flare, then the flare clears and her smiling face is sharp](/images/20261027-wedding-film-3/10-역광-플레어.webp)
<small>0:58 and 0:59 in the final cut (AI-generated). My wife's face emerges from the flare</small>

#08 is a blank face, only the head turned, that we slowly move toward before being sucked into the eye. Here posture was everything. Torso and shoulders stay facing the front of the bench; only the head turns toward the camera. If the body turns too, he's already someone mid-conversation. Only the head turning keeps the moment of having just looked up in surprise. Mouth slightly open, and I wrote `not smiling`.

![A man in a white tee leaning on the backrest with only his head turned toward the camera; in the next frame light spreads](/images/20261027-wedding-film-3/11-고개만-돌린-얼굴.webp)
<small>1:00 and 1:01 in the final cut (AI-generated). Body facing the bench front, only the head turned</small>

#11 is the reverse, zooming out from the eye. The line is "Yes, I'd like that." The gaze isn't into the lens but past it, up behind the camera, looking up at my wife standing there. This smiling face becomes the front half of the match cut into the wedding hall scene in part 4.

## Prompt principles that set on the bench scene

These are the principles I put together through the bench scene. If I made the same scene again, I'd write this way from the start.

| Principle | Detail |
|---|---|
| One photo matched to the angle for the face | Better than a character bundling many angles. Frame close for shots where the face must show |
| Screen proportions instead of meters | Writing fractions, like the person at 1/8 of frame height and the bench at 1/4 of frame width, is what worked |
| Only height and horizontal distance | Writing height, angle and distance all together makes them clash. Give height and horizontal distance and the angle follows |
| Don't tell it to hide | Stacking `not visible`, `heavily shaded`, `face is not readable` smears the whole person. Write a state, like `Her face is hidden behind these leaves` |
| Foreground by lens distance | To keep leaves in the foreground, pin the distance from the lens, like `just 30cm from the lens, heavily blurred`. Otherwise they become a background tree (I only noted this; in practice I moved to the edit) |
| No conditionals | `Two people could sit side by side` gets ignored or draws two people. State things as they are |
| Fix one thing at a time | Change four things at once and one sticks, and you can't tell where the rest got stuck |
| Two-step method | For when the reference beats the text. Make a result with the problem element removed first, then use it as a reference to add only what you want. Double the credits, but more reliable than fixing over and over |
| Combine location and person in the image | Don't throw location and person in separately at the video stage. Combine them into one image, then animate |
| Say whose view in the shot name | Not "water bottle POV" but "my POV looking at the bottle" |
| Motion as a timed schedule | Timing lands only when you write what happens at each second |
| Hand off early to the edit what won't work | For the leaf cover I kept rewriting sentences and finally moved it to Premiere |

Part 4 is the wedding hall scene: why the AI-made selfie cam talked so cheesily I couldn't use it, how I put a tuxedo and the wedding hall on a video I acted myself instead, and what I thought after finishing all four parts.

## Trial-and-error log

High-angle image (early August 31, Nano Banana Pro), checked in the Claude conversation history:

| Run | What changed | Result |
|---|---|---|
| 1 | Gave the previous day's result as reference and asked for four things at once: "open up the path, cover the bride with leaves at top right, black hair, white dress" | Only the hair color changed. The sentence telling it to keep the reference as is overrode every other instruction |
| 2 | Step one of the two-step method: remove the people, path and leaves only | Two benches became one, the camera came closer, and the leaves didn't cover the bench. The bench had to be long enough at least for me to have a seat |
| 3 | Fresh run: 4 m high, 8 m away, 25 degrees, 35 mm, two benches | The two benches faced each other front to back. Then she can't hand me water from the side |
| 4 | One bench horizontal, the bride at the far right of the frame, 3.5 m, 7 m, 27 degrees. Rewrote the leaf sentence as a state and dropped `clearly visible` | The leaves missed again. The word `cover` was weak |
| 5 | Moved the sun from behind the bride to behind the camera (front light), deleted lines like "she is small" and conditionals | Front light, horizontal bench, 27 degrees were right. But it crept closer every run. Meters didn't work |
| 6 | Dropped the angle, height and horizontal distance only. 12 m, person 1/8 of frame height, bench 1/4 of frame width, path the lower 2/3, leaves the top-right 1/4, "everything above the chest behind leaves" | Distance, position and tree were spot on. The path came out diagonal and looked awkward |
| 7 | Path `roughly horizontally`, one paving pattern | Two benches again. Fixed to `Exactly one bench`, the empty seat `wide enough for another person to sit down` |

I also asked whether I could set the generation order (draw the leaves last), but there was no such option.

High-angle video: September 6 at 4:59 a.m., Seedance 2, 1080p. Only this one run is in the history. In the final cut it runs about 4 seconds, 0:48 to 0:51.

Low-angle prep: right after settling A, the question of matching the space came up. In A my wife sits at the far right of the frame and I sit on the left. In B the camera goes to her seat and looks at me along the length of the bench. Logically right, but viewers could get left and right confused.

![Three images from August 30: an empty bench at low angle with the sun flaring, a hand offering a water bottle to someone on a bench, a man on a bench looking ahead in surprise](/images/20261027-wedding-film-3/05-8월30일-벤치-이미지.webp)
<small>Bench scene images made first, on August 30 (AI-generated). Empty bench at low angle, the hand with the bottle, a surprised look</small>

Low-angle video (September 6, all Seedance 2.5):

| Time | Resolution | What changed |
|---|---|---|
| 05:08 | 480p | English prompt. 3.8–4.5s hand with bottle from the right, 4.5–5.5s looks at the bottle, does not look surprised |
| 05:45 | 480p | Regenerated |
| 05:53 | 1080p | Regenerated |
| 06:12 | 480p | Switched to a Korean prompt I wrote myself: "white short-sleeve T-shirt, jeans… fanning his shirt as if hot… a hand offering water from the right of the frame… does not look surprised" |
| 06:20 | 1080p | Fanning changed to "light and slow" |
| 07:26 | 1080p | Added "strictly follow the camera composition of the reference image" |
| 07:48 | 480p | Added a timed schedule: 0–2s sigh, 2–6s fanning shirt, 6–8s hand with bottle |
| 08:20 | 1080p | Final with that schedule |

Bottle POV shot (early September 2): in order, four days before B. For my wife's face reference I put in all three photos, as described in part 1.

![Higgsfield video history for September 2: an eye close-up, two clips of a man leaning on a bench with his head turned, four of a woman in a white dress offering a water bottle, a workroom clip](/images/20261027-wedding-film-3/08-9월2일-기록.webp)
<small>September 2 history. The middle row and top right are the bottle POV shot; the middle two of the top row are my turned face (#08)</small>

| Time | Model | Resolution | What changed |
|---|---|---|---|
| 03:06 | Cinema Studio Video | 480p | First try |
| 03:13 | Seedance 2.5 | 480p | As a timed schedule |
| 03:19 | Seedance 2.5 | 480p | Added "he is taller than she" |
| 03:25 | Seedance 2.5 | 1080p | Final |

The structure settled on September 1 was one continuous 12-second shot: not split into two shots, with the rack focus from the bottle to my wife inside one take, and the end frame with the flare gone and her face sharp. The actual Seedance prompt was cut down to a 6-second schedule.

#08 and #11: #08 was made at 03:47 and 03:54 on September 2, Seedance 2.5 1080p. #11 was first made at 03:55 on September 2 at 1080p, then again on September 3 at 00:17 (480p), 00:28 and 00:41 (1080p).

Writing up the principles: on September 1, opening a new chat, I wrote up the trial and error so far as principles and handed them over. Most came from the high angle; the low angle came after, on September 6.
