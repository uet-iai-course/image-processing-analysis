# CLAUDE.md

This repo holds the RevealJS lecture decks and exercise banks for **Xử lý và Phân tích Hình ảnh** (image processing and analysis). The published semester is `2526-2/`.

The workspace file `../CLAUDE.md` carries the rules shared by every course: environment, static-site rules, shared CSS, writing style, `no-ai-slop`/`quill`, the sub-agent policy, visual verification and git basics. This file holds only what is specific to this course. The course's own authoring standards live in `prompts/`; `AGENTS.md` only covers the Python environment and is superseded by the workspace venv. Precedence: the user's instructions first; for new or rebuilt decks, `NGUYEN-TAC-TRANG-CHIEU.md` with the parameters in §"Tham số trang chiếu của học phần" below; then `prompts/SLIDE_STYLE_GUIDE.md` and the other standards in `prompts/`, then this file, then `../CLAUDE.md`.

## Repo map

| Path | Contents |
|---|---|
| `2526-2/lecture-N-<topic>.html` | Lecture decks 1–15 (no zero padding) |
| `2526-2/weekN-<topic>.html` | Older per-week decks (weeks 3, 4, 5, 9) |
| `2526-2/lecture-template.html` | Base for new decks |
| `2526-2/lecture-style.css` | Shared stylesheet, identical in every course; synced from `../shared/css/`, never edited here |
| `2526-2/lecture-course.css` | This course's deck styles (when present), loaded after `lecture-style.css` |
| `2526-2/revealjs/`, `plugin/` | Local RevealJS runtime (prebuilt `dist/`; no gulp/npm build) |
| `2526-2/img/` | Figures; only the allow-listed folders in `.gitignore` are tracked |
| `2526-2/index.html`, `index.html` | Semester index and repo landing page |
| `NGUYEN-TAC-TRANG-CHIEU.md` | Shared deck principles NT1–NT28, a byte-identical copy of `../shared/docs/nguyen-tac-trang-chieu.md`; never edited here |
| `prompts/SLIDE_STYLE_GUIDE.md` | The deck standard: pedagogy, audience, non-negotiables, 120-minute structure, recurring patterns, section and slide rules. **Read before any deck work.** |
| `prompts/prompt_create_slides_from_book_chapter.md`, `prompt_revise_*.md`, `prompt_draw_diagram.md` | Task prompts for creating decks from a chapter, revising text and drawing diagrams |
| `prompts/question-authoring-standards.md`, `essay-question-authoring-standards.md` | Standards for MCQ and essay questions (model answer, rubric, grading notes) |
| `exercises/` | Weekly question sets (`weekX-weekY-{mcq,essay-short-answer}[-set-N].md`) and source PDFs (untracked) |
| `skills/slide-text-style-editor/` | Project skill for editing slide wording to the style guide |
| `pptx/` | Source PPTX decks (untracked) |
| `../tools/courses/image-processing-analysis/` | Figure generators (workspace tooling, not in this repo) |

## Commands

```bash
../.venv/bin/python -m reloadserver 8765          # from repo root
# deck: http://localhost:8765/2526-2/lecture-N-<topic>.html
git diff --check
```

## Tham số trang chiếu của học phần

New or rebuilt decks of this course follow principles NT1–NT28 in `NGUYEN-TAC-TRANG-CHIEU.md` at the repo root. That file is a byte-identical copy of `shared/docs/nguyen-tac-trang-chieu.md` in the workspace and is never edited in this repo; where it conflicts with the deck rules in this file or in `prompts/`, it wins, except for the parameters below. The parameters live here because `AGENTS.md` only covers the Python environment. Existing decks keep the old rules until a logged revision requested by the user.

| Code | Parameter | Course value | Basis |
|---|---|---|---|
| P1 | Content source | `deck nguồn + ghi chú`; the course has no lecture notes yet (no `lecture-note.md`). Keep the order, storyline and main points of the source: the previous semester's PPTX/PDF deck in `pptx/13 tuần slides/weekN/` or the assigned book-chapter PDF; until notes exist, that source is the reference for notation, statements and numbers | `prompts/prompt_create_slides_from_book_chapter.md` §C ("The PDF is the single source of truth", "Keep the chapter's narrative order"); repo map row `pptx/`; `2526-2/week3-histogram.html` follows the order of `week3 - histogram.pptx` (slides 8–21) |
| P2 | Terminology, spelling | Vietnamese term first, English in parentheses at first use; keep standard abbreviations and model names (`IoU`, `FPN`, `RoI`, `CNN`, `ViT`); one name per concept throughout a deck; "Ký hiệu:". The `glossaries.yaml` the guide cites is not in the repo; otherwise default | `SLIDE_STYLE_GUIDE.md` §"Nguyên tắc không thương lượng" 3, 8 and §"Quy tắc về wording" 0, 2; `tools/deck/courses.json` |
| P3 | Conclusion label, extra labels | "Kết luận:"; extra labels "Đầu vào:", "Đầu ra:" | `SLIDE_STYLE_GUIDE.md` §"Tiêu chuẩn ở mức slide" 3 (input, output); `tools/deck/courses.json` |
| P4 | Third column of the summary table | default | none in the course |
| P5 | Extra opening slides | 1–2 hook-story slides with a concrete case taken from the source (P1), closed again in "Tổng kết" | `SLIDE_STYLE_GUIDE.md` §"Cấu trúc chuẩn của một deck 120 phút" 1, §"Pattern thường dùng" 1 |
| P6 | Duration, slide count | 120-minute theory session; one deck 45–55 slides; a week split into 1–3 decks has 30–55 slides per deck (25–35 for 60 minutes); above 60 slides requires the `📚 Nâng cao` strategy | `SLIDE_STYLE_GUIDE.md` §"Cấu trúc chuẩn của một deck 120 phút", §"Số lượng slide gợi ý" |
| P7 | Technical frame | `2526-2/lecture-template.html`; footer "Xử lý và Phân tích Hình ảnh (Học kỳ 2, 2025-2026) §N: <tên bài>" as in decks 1–15; `data-slide-id` default; `lecture-style.css` then `lecture-course.css`, no per-lecture CSS; no `<style>`; `style=""` only for a one-slide adjustment or a genuinely special layout, a repeated pattern goes to `lecture-course.css`; no `\(...\)` in `h1`–`h3` | §"Course-specific rules" (CSS) below; `SLIDE_STYLE_GUIDE.md` §"Tiêu chuẩn kỹ thuật cho Reveal.js / HTML" 2, §"Quy tắc về công thức" 5 |
| P8 | External sources | the source deck and book chapter of P1; for decks 10–15, CS231n and the original papers listed on each deck's "Tài liệu tham khảo" slide | P1; `2526-2/lecture-10-…html` to `lecture-15-…html` |
| P9 | Agents | Opus 5.5 at `high` for every role; minimum pipeline in §"Sub-agents (course settings)" | §"Sub-agents (course settings)" below |
| P10 | Course checks | `deck_lint.py --course image-processing-analysis`; rubric §F of the guide: no `class="fragment"`, no `<p class="inline-code">`, every code block has `data-trim` and the right `language-*` class | `tools/deck/courses.json`; `SLIDE_STYLE_GUIDE.md` §"Rubric rà soát một lecture" F |
| P11 | Extra principles | NT-IPA-1: no `class="fragment"`; an on-slide "Lời giải:" (NT24) goes on the next slide with the same title (§"Những điều bị cấm" 6). NT-IPA-2: every technical slide has one visual centre (pipeline, architecture, input/output images, feature map or mask, comparison chart) showing input, output and the main transformation (§"Nguyên tắc không thương lượng" 7; §"Tiêu chuẩn ở mức slide" 3–4). NT-IPA-3: each important model, algorithm or architecture becomes a slide sequence: problem, overview, each main component, the shift from the previous model, training, inference or loss when it drives the behaviour, comparison (§"Nguyên tắc không thương lượng" 6; §"Tiêu chuẩn ở mức section"). NT-IPA-4: slides not needed in class carry the `📚 Nâng cao` badge (`.advanced-badge` after `h2`), never a hinge slide or a core concept (§"Quy tắc về badge"). NT-IPA-5: code blocks use `data-trim` and the correct `language-*` class; `.inline-code` only on `<span>` (§"Quy tắc về code blocks" 1; §"Những điều bị cấm" 7) | `SLIDE_STYLE_GUIDE.md`, sections cited |

## Course-specific rules

- Follow `prompts/SLIDE_STYLE_GUIDE.md` §"Nguyên tắc không thương lượng" and §"Những điều bị cấm hoặc nên tránh mạnh"; use its patterns (card stacks, two-column comparisons, code-heavy slides, SVG diagrams) rather than inventing new layouts. Existing decks may keep its running question, "Nhìn lại và đi tiếp" bridge slides and closing extension exercises; new or rebuilt decks replace them with the single "Vấn đề trung tâm" box at the opening and the "Vấn đề trung tâm" slide in "Tổng kết" (NT11, NT15), strand title slides with an on-slide linking sentence (NT10, NT12, NT13) and "Bài tập về nhà" from the lecture's exercises (NT15, NT24); the hook story is P5.
- In new or rebuilt decks, `prompts/` yields to `NGUYEN-TAC-TRANG-CHIEU.md` where they conflict (see `NGUYEN-TAC-TRANG-CHIEU.md`): part-title slides are `section.strand-title`, not `<h1><span class="text-light">K.</span>…` (NT12); "Mục tiêu học tập", not "Mục tiêu buổi học" (NT11); no font reduction to make a slide fit (NT17); SVG text at least 16 px, SVG files in `2526-2/img/lec-NN/`, rasters only with the user's approval in `review-log.md` (NT25); 2–4 "Câu hỏi tự kiểm tra", not 4–6 (NT15); a softener such as "thường" only with its condition or number (NT20).
- Slide wording edits use the `slide-text-style-editor` skill together with `no-ai-slop`; keep formulas, code, abbreviations, model names and technical content intact.
- Questions in `exercises/` follow the two question-authoring standards: every essay item has a `model_answer`, a `rubric` and `grading_notes`, and gives enough context to be answered independently.
- **CSS:** decks link `lecture-style.css` then `lecture-course.css` (if present); no per-lecture CSS files.
- Figures generated by script are regenerated from `../tools/courses/image-processing-analysis/…` with the shared venv; the generator's original data path outside the repo may be stale, so check before running.

## Sub-agents (course settings)

The policy in `../CLAUDE.md` applies at effort `high`. This course has no fixed multi-stage pipeline; for a new deck use at least plan → draft → independent review (content accuracy, student view, wording with `no-ai-slop` Detect) → revise → browser check, scaled down for small edits.

## Git (course settings)

Ask before committing or pushing.
