class Label:

    @staticmethod
    def from_str(value):
        for l in Label._get_supported_labels():
            if l.to_str() == value:
                return l
        raise Exception("Label by value '{}' doesn't supported".format(value))

    @staticmethod
    def _get_supported_labels():
        supported_labels = [
            PositiveLabel(),
            NegativeLabel()
        ]
        return supported_labels


class PositiveLabel(Label):

    def to_str(self):
        return 'pos'


class NegativeLabel(Label):

    def to_str(self):
        return 'neg'


