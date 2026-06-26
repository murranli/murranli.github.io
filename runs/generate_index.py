#!/usr/bin/env python3
"""Regenerate ../index.html (repo root) from runs/manifest.json.

Usage: python3 generate_index.py
Run this from inside the runs/ directory after appending a new entry to manifest.json.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)

with open(os.path.join(HERE, "manifest.json"), encoding="utf-8") as f:
    runs = json.load(f)

runs_sorted = sorted(runs, key=lambda r: r["date"], reverse=True)

rows = []
for r in runs_sorted:
    rows.append(f"""
      <li class="run">
        <div class="run-date">{r['date']}</div>
        <div class="run-body">
          <a class="run-title" href="runs/{r['run_id']}/index.html">{r['title']}</a>
          <div class="run-request">{r['original_request']}</div>
          <div class="run-links">
            <a href="runs/{r['run_id']}/index.html">查看报告</a>
            ·
            <a href="runs/{r['run_id']}/review.md">查看复盘 (review.md)</a>
          </div>
        </div>
      </li>""")

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>调研报告归档</title>
<style>
  body {{ font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif;
         max-width: 760px; margin: 40px auto; padding: 0 20px; color: #1f2428; background: #f7f5ef; }}
  h1 {{ font-size: 1.5rem; margin-bottom: .2rem; }}
  .subtitle {{ color: #687077; margin-bottom: 2rem; }}
  ul.runs {{ list-style: none; padding: 0; }}
  li.run {{ display: flex; gap: 16px; padding: 16px 0; border-bottom: 1px solid #ded8cb; }}
  .run-date {{ flex: 0 0 90px; color: #687077; font-size: .85rem; padding-top: 2px; }}
  .run-title {{ font-size: 1.05rem; font-weight: 600; color: #245f73; text-decoration: none; }}
  .run-title:hover {{ text-decoration: underline; }}
  .run-request {{ color: #444; font-size: .9rem; margin: 4px 0 6px; }}
  .run-links {{ font-size: .85rem; }}
  .run-links a {{ color: #b2563b; }}
</style>
</head>
<body>
  <h1>调研报告归档</h1>
  <div class="subtitle">由 research 调研流水线产出，按时间倒序排列</div>
  <ul class="runs">{''.join(rows)}
  </ul>
</body>
</html>
"""

out_path = os.path.join(REPO_ROOT, "index.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)
print("written", out_path)
