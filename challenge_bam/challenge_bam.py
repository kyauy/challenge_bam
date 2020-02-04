#!/usr/bin/env python3

import pysam as ps


def aligned_ratio(bamfile):
    """
    Return aligned ratio in the overall bam
    """
    total = 0
    aligned = 0

    bam = ps.AlignmentFile(bamfile)

    iter = bam.fetch()

    for read in iter:
        total = total + len(read.get_aligned_pairs(matches_only=False))
        aligned = aligned + len(read.get_aligned_pairs(matches_only=True))

    aligned_ratio = aligned / total
    non_aligned_ratio = 1 - aligned_ratio

    return (
        "Aligned ratio is : "
        + str(aligned_ratio)
        + "\nNon-aligned ratio is : "
        + str(non_aligned_ratio)
    )


bamfile = "/home/kevin/dev_seqone/challenge_bam/data/wgs_bam_NA12878_20k_b37_NA12878_20k.b37.bam"

print(aligned_ratio(bamfile))
