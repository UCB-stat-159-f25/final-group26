__version__ = "0.1.0"

# Re-export common functions/classes at the package top-level:
from .readligo import (
    loaddata, read_hdf5, read_frame,
    getsegs, getstrain, dq2segs, dq_channel_to_seglist,
    FileList, SegmentList,
)

# Also expose the submodule object as ligotools.readligo
from . import readligo

__all__ = [
    "readligo",
    "loaddata", "read_hdf5", "read_frame",
    "getsegs", "getstrain", "dq2segs", "dq_channel_to_seglist",
    "FileList", "SegmentList",
    "__version__",
]
