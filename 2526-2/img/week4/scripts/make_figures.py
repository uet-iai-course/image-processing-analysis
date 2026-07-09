from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy import ndimage, signal


ROOT = Path(__file__).resolve().parents[1]
COURSE_ROOT = Path(__file__).resolve().parents[5]
SOURCE = COURSE_ROOT / "slides" / "phần 1" / "week4" / "code"


def load_rgb(name, max_side=None):
    img = Image.open(SOURCE / name).convert("RGB")
    if max_side:
        img.thumbnail((max_side, max_side), Image.Resampling.LANCZOS)
    return np.asarray(img).astype(np.float32)


def save_grid(filename, images, titles, cols=None, figsize=None):
    if cols is None:
        cols = len(images)
    rows = int(np.ceil(len(images) / cols))
    if figsize is None:
        figsize = (3.2 * cols, 3.0 * rows)
    fig, axes = plt.subplots(rows, cols, figsize=figsize)
    axes = np.atleast_1d(axes).ravel()
    for ax, img, title in zip(axes, images, titles):
        ax.imshow(np.clip(img, 0, 255).astype(np.uint8))
        ax.set_title(title, fontsize=12, pad=8)
        ax.axis("off")
    for ax in axes[len(images):]:
        ax.axis("off")
    fig.tight_layout(pad=0.6)
    fig.savefig(ROOT / filename, dpi=180, bbox_inches="tight")
    plt.close(fig)


def per_channel(img, fn):
    return np.dstack([fn(img[..., c]) for c in range(img.shape[-1])])


def gaussian(img, sigma):
    return per_channel(img, lambda ch: ndimage.gaussian_filter(ch, sigma=sigma))


def uniform(img, size):
    return per_channel(img, lambda ch: ndimage.uniform_filter(ch, size=size))


def median(img, size):
    return per_channel(img, lambda ch: ndimage.median_filter(ch, size=size))


def make_filtering_results():
    img = load_rgb("pepper.jpg", max_side=360)
    box = uniform(img, 9)
    gauss = gaussian(img, 2)
    med = median(img, 7)
    blur = gaussian(img, 2.5)
    sharp = np.clip(1.7 * img - 0.5 * blur, 0, 255)
    save_grid(
        "filtering-results.png",
        [img, box, gauss, med, sharp],
        ["Gốc", "Box 9x9", "Gaussian", "Median 7x7", "Unsharp"],
        cols=5,
        figsize=(11, 3),
    )


def correlate_rgb(img, kernel, boundary):
    mode = "same"
    return per_channel(
        img,
        lambda ch: signal.correlate2d(ch, kernel, mode=mode, boundary=boundary, fillvalue=0),
    )


def make_boundary_modes():
    img = load_rgb("pepper.jpg", max_side=300)
    kernel = np.zeros((81, 81), dtype=np.float32)
    kernel[10, 64] = 1.0
    fill = correlate_rgb(img, kernel, "fill")
    wrap = correlate_rgb(img, kernel, "wrap")
    symm = correlate_rgb(img, kernel, "symm")
    save_grid(
        "boundary-modes.png",
        [img, fill, wrap, symm],
        ["Gốc", "fill = 0", "wrap", "symm"],
        cols=4,
        figsize=(9, 3),
    )


def make_box_vs_gaussian():
    img = load_rgb("wheatfield.jpg", max_side=520)
    crop = img[140:460, 170:490]
    box = uniform(crop, 21)
    gauss = gaussian(crop, 4.0)
    save_grid(
        "box-vs-gaussian.png",
        [crop, box, gauss],
        ["Gốc", "Box 21x21", "Gaussian 21x21"],
        cols=3,
        figsize=(8.4, 3),
    )


def make_median_noise():
    rng = np.random.default_rng(7)
    img = load_rgb("pepper.jpg", max_side=360)
    noisy = img.copy()
    mask = rng.random(img.shape[:2])
    noisy[mask < 0.035] = 0
    noisy[(mask >= 0.035) & (mask < 0.07)] = 255
    med = median(noisy, 5)
    gauss = gaussian(noisy, 1.2)
    save_grid(
        "median-noise.png",
        [img, noisy, gauss, med],
        ["Gốc", "Salt-pepper", "Gaussian", "Median 5x5"],
        cols=4,
        figsize=(9, 3),
    )


def make_unsharp():
    img = load_rgb("wheatfield_ori.jpg", max_side=700)
    crop = img[80:390, 170:760]
    blur = gaussian(crop, 4.0)
    mask = np.clip((crop - blur) * 2 + 128, 0, 255)
    sharp = np.clip(crop + 1.4 * (crop - blur), 0, 255)
    save_grid(
        "unsharp-masking.png",
        [crop, blur, mask, sharp],
        ["Gốc", "Làm mờ", "Mặt nạ", "Sắc nét hơn"],
        cols=4,
        figsize=(10, 3),
    )


def make_shading_correction():
    n = 360
    yy, xx = np.mgrid[0:n, 0:n]
    checker = (((xx // 36) + (yy // 36)) % 2).astype(np.float32)
    base = 70 + 145 * checker
    shade = 0.55 + 0.45 * (xx / n) + 0.15 * np.sin(2 * np.pi * yy / n)
    observed = np.clip(base * shade, 0, 255)
    estimate = ndimage.gaussian_filter(observed, sigma=28)
    corrected = observed / np.maximum(estimate, 1) * np.mean(estimate)
    observed_rgb = np.dstack([observed] * 3)
    estimate_rgb = np.dstack([estimate] * 3)
    corrected_rgb = np.dstack([corrected] * 3)
    save_grid(
        "shading-correction.png",
        [observed_rgb, estimate_rgb, corrected_rgb],
        ["Ảnh có shading", "Nền mờ ước lượng", "Chia để sửa shading"],
        cols=3,
        figsize=(8.4, 3),
    )


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    make_filtering_results()
    make_boundary_modes()
    make_box_vs_gaussian()
    make_median_noise()
    make_unsharp()
    make_shading_correction()


if __name__ == "__main__":
    main()
