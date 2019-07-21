#!/usr/bin/python
from reader.collection import RuSentiFramesCollection
from reader.variants.collection import FrameVariantsCollection


frames = RuSentiFramesCollection.from_json("collection.json")
frame_variants = FrameVariantsCollection.from_iterable(
    variants_with_id=frames.iter_frame_id_and_variants())

for frame_id in frames.iter_frames_ids():
    # id
    print("Frame: {}".format(frame_id))
    # variants
    print("Variants: {}".format(",".join(frames.get_frame_variants(frame_id))))
