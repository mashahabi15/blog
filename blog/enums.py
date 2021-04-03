from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((x.value, x.name) for x in cls)


class ScoreType(ChoiceEnum):
    like = 1
    dislike = 2
