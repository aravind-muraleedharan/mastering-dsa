# Contains Duplicate (NeetCode #1 · Arrays & Hashing)

**Problem:** Given a list of integers, return True if any value appears more than once.
**Link:** https://neetcode.io/problems/duplicate-integer
**Difficulty:** Easy


What I learned:
- `x in list` scans every item, so the loop becomes O(n²).
- Return as soon as the answer is known; no flag variable needed.

## List vs set

| | List | Set |
|---|---|---|
| Structure | Ordered sequence | Hash table |
| `x in ...` | Scan one by one, O(n) | Jump to slot, O(1) average |
| Order / indexing | Yes | No |
| Duplicates | Kept | Removed |
| Items | Anything | Must be hashable (no lists) |
| Memory | Less | More |

## How a set lookup works

1. Compute `hash(x)` (for most ints, `hash(42) == 42`).
2. Map the hash to a slot directly (roughly `hash % table_size`); no search.
3. Compare only at that slot: stored hash, then value.
4. Collision (two values, same slot): probe the next candidate slot.
5. The table resizes at about two-thirds full, so probes stay short.

Result: O(1) **on average**; worst case O(n) if many values collide (rare, but can be forced).
