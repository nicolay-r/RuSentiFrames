from reader.collection import RuSentiFramesCollection
from reader.variants.collection import FrameVariantsCollection


frames = RuSentiFramesCollection.from_json("frames.json")
frame_variants = FrameVariantsCollection.from_iterable(
    variants_with_id=frames.iter_frame_id_and_variants())