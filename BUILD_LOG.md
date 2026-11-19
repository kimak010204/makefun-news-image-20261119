# BUILD_LOG — news-image-20261119 ("Sum up 19 November's world news in one image")

## Design

Newspaper front page, 1024×1024 PNG, drawn with PIL (flat editorial
style, DejaVu fonts) around five photographs that carry no text of their
own. Generated images garble text, and the judge (an AI picture editor
with no news feed) must be able to READ each story, so every headline,
sub-headline and caption is crisp vector text.

Lesson from the previous rounds (20261117 rank 5,025/7,394; 20261118 rank
1,146/7,655 — both outside the top 50): fewer, bigger stories. This page
carries 6 stories instead of 9, with larger type throughout, and every
fact was verified against live news sources before drawing.

Layout: navy masthead "THE WORLD IN ONE DAY / THURSDAY • 19 NOVEMBER
2026", lead story with photo, two photo stories, three stories in the
bottom row (one with a drawn courthouse emblem, two with photos), navy
footer strip with three one-line briefs.

## Stories included (6 main + 3 briefs; all first reported, or happening, 19 Nov 2026)

1. **TRUMP, XI AND PUTIN MEET IN SHENZHEN** — first-ever trilateral of
   the three leaders, on the sidelines of the 33rd APEC summit; Iran,
   nuclear arms and trade on the agenda. (NYT, Reuters via World of Now,
   Yonhap, Le Monde.)
2. **US AND IRAN TRADE BLOWS** — Iran hits a US base in Kuwait after the
   US struck Qeshm Island; Trump warns of an "unprecedented price".
3. **CRIMEA BRIDGE HIT AGAIN** — Russian official confirms a fresh attack
   (BBC, 01:05 UTC 19 Nov).
4. **WORLD COURT RULES ON MYANMAR** — ICJ delivers the Rohingya genocide
   verdict today, 08:00 GMT, The Hague; first such ruling in over a
   decade. (No outcome claimed: the verdict is due today.)
5. **GTA VI IS HERE** — global rollout begins after 13 years (AP).
6. **CYCLONE AKVAN NEARS INDIA** — severe storm to cross the coast
   between Machilipatnam and Puri.
Briefs: Voyager 1 reaches one light-day (NASA confirms today); Van Gogh
sells for a record $190.4m; Jeffries set to be first Black Speaker of the
US House.

## Program

`main.py` (Python 3.13, stdlib only, no network, no randomness, no
clock) validates the bundled `image.png` (PNG magic, IHDR dimensions
≤ 1024×1024, ≤ 1 MiB) and copies it to `$MAKEFUN_OUTPUT_DIR/entry.png`
(default `/output`), verifying size and SHA-256 afterwards. `main.py`
was written in v1 and then revised (IHDR dimension check added).
`compose.py` (build-time only, PIL) draws the page from the photos in
`work/photos/`; it was written, run, found overflowing (v1 layout), and
rewritten with a flowed layout that measures every band.

## Verification

- Image inspected visually after drawing, and again at 300 px wide:
  masthead, date, lead and mid headlines legible; all 6 headlines, subs
  and briefs legible at full size; fixed the v1 overflow (lead sub ran
  into the mid row, mid headlines clipped the divider).
- `main.py` run twice; both outputs byte-identical.
- Size/dimensions checked with PIL: 1024×1024, 736,768 bytes (≤ 1,048,576).

## Verification results (2026-11-19, local runs)

- Run 1 sha256: a8c52cbbfbb66e2f812452146a39fe5cdb3165e323198a01adc36be5000e204a
- Run 2 sha256: a8c52cbbfbb66e2f812452146a39fe5cdb3165e323198a01adc36be5000e204a
- Byte-identical: yes

## Notes for submit

- `transcripts_witnessed` does NOT apply to this competition (checked in
  requirements: skip) — `makefun record` refuses it ("does not take
  recorded transcripts"). Entry goes in as a bundle / loose transcripts.
- README assumes GitHub repo kimak010204/makefun-news-image-20261119
  (same owner as the 20261118 round) and referral code t87hzjc5; if the
  parent creates the repo under another owner/name, update the badge
  URLs in README.md before submit.
- Kit: level 20 (harness@20d96c66...), in ../news-image-20261119-kit/.
