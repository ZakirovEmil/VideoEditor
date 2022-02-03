import moviepy
from moviepy.editor import *


class Editor:
    @staticmethod
    def subclip(start, end, clip):
        return clip.subclip(start, end)

    @staticmethod
    def speed_up(coef, clip):
        return clip.fx(vfx.speedx, float(coef))

    @staticmethod
    def rotate(angle, clip):
        return clip.rotate(int(angle))

    @staticmethod
    def concatenate(args):
        return concatenate_videoclips(args)

    @staticmethod
    def crop(x1, y1, x2, y2, clip):
        return moviepy.video.fx.all.crop(clip, x1=int(x1), y1=int(y1), x2=int(x2), y2=int(y2))

