import json

from .state import FrameState
from .common.labels import Label, PositiveLabel, NegativeLabel
from .polarity import FramePolarity
from .role import FrameRole


class RuSentiFramesCollection:

    __frames_key = "frames"
    __polarity_key = "polarity"
    __state_key = "state"

    def __init__(self, data):
        assert(isinstance(data, dict))
        self.__data = data

    @classmethod
    def from_json(cls, filepath):
        assert(isinstance(filepath, str))
        with open(filepath, 'r') as f:
            data = json.load(f)
        return cls(data)

    def get_frame_roles(self, frame_id):
        assert(isinstance(frame_id, str))
        return [FrameRole(source=key, description=value)
                for key, value in self.__data[frame_id]["roles"].items()]

    def get_frame_polarities(self, frame_id):
        assert(isinstance(frame_id, str))

        if not self.__check_has_frame_polarity_key(frame_id):
            return []

        return [self.__frame_polarity_from_args(args)
                for args in self.__data[frame_id][self.__frames_key][self.__polarity_key]]

    def try_get_frame_polarity(self, frame_id, role_src, role_dest):
        assert(isinstance(role_src, str))
        assert(isinstance(role_dest, str))

        if not self.__check_has_frame_polarity_key(frame_id):
            return None

        for args in self.__data[frame_id][self.__frames_key][self.__polarity_key]:
            if args[0] == role_src and args[1] == role_dest:
                return self.__frame_polarity_from_args(args)
        return None

    def get_frame_states(self, frame_id):
        assert(isinstance(frame_id, str))

        if self.__state_key not in self.__data[frame_id][self.__frames_key]:
            return []

        return [FrameState(role=args[0], label=Label.from_str(args[1]), prob=args[2])
                for args in self.__data[frame_id][self.__frames_key][self.__state_key]]

    def get_frame_titles(self, frame_id):
        assert(isinstance(frame_id, str))
        return self.__data[frame_id]["title"]

    def get_frame_variants(self, frame_id):
        return self.__data[frame_id]["variants"]

    def get_frame_values(self, frame_id):
        assert(isinstance(frame_id, str))
        # TODO. Not implemented yet.
        pass

    def get_frame_effects(self, frame_id):
        assert(isinstance(frame_id, str))
        # TODO. Not implemented yet.
        pass

    def iter_frames_ids(self):
        for frame_id in self.__data.keys():
            yield frame_id

    def __check_has_frame_polarity_key(self, frame_id):
        return self.__polarity_key in self.__data[frame_id][self.__frames_key]

    @staticmethod
    def __frame_polarity_from_args(args):
        return FramePolarity(src=args[0], dest=args[1], label=Label.from_str(args[2]), prob=args[3])

    def iter_frame_id_and_variants(self):
        for id, frame in self.__data.items():
            for variant in frame["variants"]:
                yield id, variant
