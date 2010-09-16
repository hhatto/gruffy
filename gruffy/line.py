import base


class Line(base.Base):

    def __init__(self, *args):
        if len(args) > 2:
            raise ArgumentError, "Wrong number of arguments"
        if args is None:
            base.Base.__init__(self)
        else:
            base.Base.__init__(self, *args)
        self.hide_dots = self.hide_lines = False
        self.baseline_color = 'red'
        self.baseline_value = None

    def draw(self):
        if not self.has_gdata:
            return
        Line.__base__.draw(self)

