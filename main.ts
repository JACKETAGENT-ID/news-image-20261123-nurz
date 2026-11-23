import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// Entry for news-image-20261123 (nurz): the image is drawn by gen.py
// into entry.png at build time; this program only copies it to the
// output directory, so both graded runs produce byte-identical bytes.
const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const src = join(here, "entry.png");
if (!existsSync(src)) {
  throw new Error(`entry.png missing next to main.ts: ${src}`);
}
mkdirSync(outDir, { recursive: true });
copyFileSync(src, join(outDir, "entry.png"));
