# -*- coding: utf-8 -*-
import collections
from .variant import FrameVariant


class FrameVariantsCollection:

    def __init__(self, variants):
        assert(isinstance(variants, dict))
        self.__variants = variants

    @classmethod
    def from_iterable(cls, variants_with_id):
        assert(isinstance(variants_with_id, collections.Iterable))

        variants = {}
        frames_dict = {}
        frames_list = []
        for frame_id, variant in variants_with_id:
            FrameVariantsCollection.__register_frame(frames_dict, frames_list, frame_id)
            variants[variant] = FrameVariant(variant, frame_id)

        return cls(variants=variants)

    @staticmethod
    def __register_frame(frames_dict, frames_list, frame_id):
        assert(isinstance(frame_id, str))
        if frame_id not in frames_dict:
            frames_dict[frame_id] = len(frames_list)
            frames_list.append(frame_id)
        return frames_dict[frame_id]

    def get_variant_by_value(self, value):
        return self.__variants[value] if value in self.__variants else None

    def has_variant(self, template):
        return template in self.__variants

    def iter_variants(self):
        for template, variant in self.__variants.items():
            yield template, variant

