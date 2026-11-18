# Verification — news-image-20261117

Verified 2026-11-18 (UTC+8) against the competition requirements. All checks PASS.

- [x] **PASS — entry.png format/size:** PNG, 1024 × 1024 px, 720,893 bytes (≤ 1 MiB / 1,048,576 bytes). Measured with `file` and `stat`.
- [x] **PASS — main.py reproducibility:** two runs with `MAKEFUN_OUTPUT_DIR` set to `/tmp/vrf_a` and `/tmp/vrf_b` both produced `entry.png` with sha256 `0b65b3d44bacb1789d52766ace42f985be40dbd2ceb25a4bd08a0eeebd470759` — identical to each other and to the committed `entry.png`. Imports are stdlib only (`os`, `shutil`). Note: this machine has Python 3.12.3 only (no 3.13 interpreter installed); the script uses nothing version-specific, so it is expected to run identically under 3.13.
- [x] **PASS — LICENSE:** first line declares `SPDX-License-Identifier: MIT` (full MIT license text follows).
- [x] **PASS — README.md badges:** contains all three make.fun badges for `news-image-20261117` (make.fun badge, rank badge, reward badge) and links to make.fun (`make.fun/bounty/news-image-20261117`, leaderboard, and `make.fun/?ref=...`).
- [x] **PASS — .makefun/owner.json:** wallet is `65vVJeFVjuysZ2rMthJyiUeaMcxyCQCz7M4DLemZNVbC`, as required.
- [x] **PASS — entry.png visual read:** masthead date reads "TUESDAY · 17 NOVEMBER 2026" (17 November 2026 is a Tuesday). All four stories present with legible, ungarbled, uncut headlines: "BRIDGE TO CRIMEA COLLAPSES" (Kerch Bridge span down after a Ukrainian strike); "Tankers mined in the Strait of Hormuz"; "Xi, Trump and Putin to meet Thursday" (three-way talks in Shenzhen); "Vulcan fails; 40 Amazon satellites lost". No headline text is garbled or cut off.

## Notes

- `main.py` copies the committed `entry.png` byte-for-byte into the output dir rather than generating the image at run time; reproducibility holds by construction, and both runs matched the committed file's hash.
- No files other than this VERIFY.md were created or modified in the repo.
