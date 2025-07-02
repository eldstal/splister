# splister
Split a sorted wordlist into chunks for incremental use. Top1000 without top100 in it, etc.

## Why?

I find myself often wanting to try a small shortlist of passwords/domains/... and then changing my mind.

If you've already run top1000 and then run top10000, aren't you running 11000 tests for 10000 results? Yes!

Splister takes a long wordlist and splits it into parts of increasing size with no overlap.

This mostly makes sense for wordlists which are sorted by prevalence, e.g. passwords in order of how common they are believed to be.

## Example

If you set `--base 10`, each new file will be 10x the size of the previous one. With `--start 100`, this means the first file will be top 100, the next will be top 1000, etc.

**However**, the output files have no overlap. The contents of the files are actually like this:

```
top100: 1-100
top1000: 101-1000
top10000: 1001-10000
```

and so on. That means you can try your crack with the top 100 first, and then run with top1000 later without redoing a bunch of work. Neat.



