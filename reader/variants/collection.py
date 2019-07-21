# -*- coding: utf-8 -*-
import collections
from variant import FrameVariant


class FrameVariantsCollection:

    def __init__(self, variants, frames_list):
        """
        frames_list: list
            list of "frame_id" (typeof unicode) items.
        """
        assert(isinstance(variants, dict))
        assert(isinstance(frames_list, list))
        self.__variants = variants
        self.__frames_list = frames_list

    @classmethod
    def from_iterable(cls, variants_with_id):
        assert(isinstance(variants_with_id, collections.Iterable))

        variants = {}
        frames_dict = {}
        frames_list = []
        for frame_id, variant in variants_with_id:
            FrameVariantsCollection.__register_frame(frames_dict, frames_list, frame_id)
            variants[variant] = FrameVariant(variant, frame_id)

        return cls(variants=variants, frames_list=frames_list)

    @staticmethod
    def __register_frame(frames_dict, frames_list, id):
        assert(isinstance(id, unicode))
        if id not in frames_dict:
            frames_dict[id] = len(frames_list)
            frames_list.append(id)
        return frames_dict[id]

    def get_frame_by_index(self, index):
        return self.__frames_list[index]

    def get_variant_by_template(self, template):
        if template in self.__variants:
            return self.__variants[template]
        return None

    def has_variant(self, template):
        return template in self.__variants

    def iter_variants(self):
        for template, variant in self.__variants.iteritems():
            yield template, variant

