from challenge_bam import __version__
from challenge_bam.challenge_bam import aligned_ratio


def test_version():
    assert __version__ == "0.1.0"


def test_aligned_ratio():
    bamfile = "/home/kevin/dev_seqone/challenge_bam/data/wgs_bam_NA12878_20k_b37_NA12878_20k.b37_toy.bam"
    assert (
        aligned_ratio(bamfile)
        == "Aligned ratio is : 0.704\nNon-aligned ratio is : 0.29600000000000004"
    )
