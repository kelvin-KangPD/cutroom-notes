---
title: "I made the film for our wedding ceremony with Higgsfield: how to describe a scene to AI"
date: 2026-10-27
series: wedding-ai
part: 1
cover: /images/20261027-higgsfield-wedding-film/01-물병-건네는-컷.webp
summary: "I made the film played in the middle of our wedding ceremony with Higgsfield. What took longest was not generating video but describing each scene to the AI precisely."
---

I made the film played in the middle of our wedding ceremony with Higgsfield. What took longest was not generating video but describing each scene to the AI precisely.

It played at our wedding on September 19, right before the groom's entrance. I didn't hire actors; most of the scenes with my wife and me were made with AI. Every video scene in this post was made with AI.

![A tired man sits on a park bench while a hand holding a water bottle reaches in](/images/20261027-higgsfield-wedding-film/01-물병-건네는-컷.webp)
<small>The low-angle bench shot. The hand offering the water is my wife's (AI-generated)</small>

## The story starts by asking AI about happiness

I wrote the storyboard first. Camera, direction and sound for every cut went on one sheet.

![Storyboard for scene 1, the studio, with columns for cut number, sketch, camera, direction and audio](/images/20261027-higgsfield-wedding-film/02-식중영상-콘티.webp)
<small>Scene 1 of the storyboard. While working on it we called it the pre-ceremony film</small>

| Scene | What happens |
|---|---|
| Studio | Late at night I ask AI for the surest way for a person to be happy. The answer: "Go outside, and someone will appear, and something will flash before your eyes" |
| Search | My face stays in the centre of the frame while only the background changes: café, park, the moon, a snowy mountain, a summer street |
| Bench | Someone hands me a water bottle as I sit exhausted on a bench. When I look up, the backlight clears and there is my wife. Real photos and videos we took pass through the pupil of my eye |
| Venue | From that expression it cuts straight to me in a tuxedo, talking directly to the guests |

The AI chat screen on the monitor was not generated. I built the chat screen separately in HTML, recorded it, and composited it onto the monitor in Premiere. For screens where the text has to be exact, compositing is faster than generating.

![An AI chat window on the monitor with the subtitle "flash"](/images/20261027-higgsfield-wedding-film/03-AI-대화-화면.webp)
<small>The "flash" in the AI's answer comes back later</small>

## I built the places first, then put people in them

In Higgsfield you can save places and characters as elements and call them in a prompt. I made the studio, park, café, moon, snowy mountain and summer street as place elements.

![Higgsfield elements screen showing places bg-snow-5, bg-moon-4, room, bg-summer and bg-park](/images/20261027-higgsfield-wedding-film/04-힉스필드-장소-요소.webp)
<small>Some of the place elements saved in Higgsfield</small>

The order never changed. **Make the place image first, then an image with the person inside that place, then animate that image.** When I threw the place and the person in separately at the video stage, they didn't match. The image I gave as the first frame went into the video as it was.

For the search scene where the background changes, I shot a 15-second selfie clip on a GoPro and converted it with Seedance 2.5 Edit. My own walking movement stayed; only the background and clothes were swapped.

![A man in a spacesuit stands on the moon with the Earth behind him](/images/20261027-higgsfield-wedding-film/05-배경만-바뀌는-컷.webp)
<small>The moon in the search scene. The face stays in place; only the background changes</small>

## For faces, angle matters more than the number of photos

At first I made a character element from a single face photo, but the face came out weak. So instead of the element I fed photos directly as references. But adding more photos didn't make it better.

When I put in front, side and head-down photos together, the angles got averaged and the face blurred out. A single photo taken at an angle close to the shot I wanted worked best, and when I didn't have one, I used one good front photo and one good side photo.

![Three photos of the same person side by side: profile, 45 degrees and front](/images/20261027-higgsfield-wedding-film/06-얼굴-레퍼런스-각도.webp)
<small>My face references. I uploaded each angle separately and picked only the one matching the shot</small>

I also made a Higgsfield Soul character, but it only works in Soul Cinema and couldn't be called from Nano Banana Pro or Cinema Studio. In the end I didn't use it.

## Seven tries for one bench shot

In the high-angle shot of the bench scene, the first watch should look like just a park, and on the second watch you should go "oh, she was there all along" and spot my wife. She had to be hidden behind leaves. I ran this one shot about seven times in Nano Banana Pro, changing the wording each time it got stuck.

| Problem | Wording that changed |
|---|---|
| Distance | "7 metres away" was ignored. Writing it as a screen ratio, like "the figure occupies one eighth of the frame height", pulled the camera back |
| Angle | Giving height, distance and angle all at once made them clash. Give only height and horizontal distance and the angle follows |
| Hiding | Stacking `not visible` and `heavily shaded` smeared the whole person. I described the state instead: "her face is hidden behind the leaves" |
| Leaves | Saying only "close to the lens" turned them into background trees. I concluded you have to pin a distance like 30cm from the lens, but it still never quite worked |
| Path | Asking for a diagonal gave an awkward in-between angle. "Roughly horizontally" looked natural |
| Bench | Hypotheticals like "two people could sit side by side" were ignored or drew two people. I wrote "exactly one bench, with room for one more person to sit beside her" |

When I fed an existing image back as a reference and asked for fixes, the reference often beat the text instructions. In those cases **I first made an image with the problem element removed, then added only what I wanted on top.** It costs twice the credits, but it was cheaper than running the same fix over and over.

Even a single word caused trouble. I had written `soft veil` to describe a faint lens flare and then took it out. In a prompt with a bride, a white dress and a wedding, "veil" can be read as a bridal veil.

The leaves were what never worked. Across seven tries they never covered my wife, so I finished the image with Gemini, uploaded it to Higgsfield and animated that.

![A park path and bench seen from above, with a seated person visible through foreground leaves](/images/20261027-higgsfield-wedding-film/07-벤치-하이앵글.webp)
<small>The finished high-angle shot. My wife is sitting behind the leaves at the lower right (AI-generated)</small>

## Every new chat window left a hole

I worked across my own Claude account and my wife's. When a conversation got long I summarised it and moved to a new one, but the summary kept only the conclusions and dropped why we had decided them. Working from the summary I repeated the same mistakes, and when I finally exported the whole earlier conversation to Word it ran over 230 pages.

I uploaded that file to Google Drive and had Claude read only the parts it needed. Only then did decisions come back, such as the water-bottle shot in the bench scene being one 12-second take rather than two cuts, or that the startled look had to come from turning only the head while the body stayed put. That is what later led me to [build an AI brain on GitHub](/en/posts/github-brain-for-claude/).

Credits were on my mind too. My account is on the Plus plan: 1,000 credits arrive on the 3rd of every month at 11 a.m. Korean time, and leftover credits don't roll over; they disappear. I confirmed this by scrolling through the full transaction history. One image cost 2 credits, and a video cost anywhere from 20 to over 130 credits per run depending on the model and quality. On August 30 alone, mostly generating video, I spent close to 300 credits.

## We played it at the wedding

The finished film played at our ceremony on September 19. The picture ends at about 2 minutes 15 seconds with "Everyone, please turn around," and after that I joined music over a black screen in the same file. The montage inside the pupil uses real photos and videos my wife and I took.
