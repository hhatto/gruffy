from gruffy.base import *


class Line(Base):
    """Line Graph Object"""

    line_width = None
    dot_radius = None
    hide_lines = None
    hide_dots = None

    def __init__(self, *args):
        if len(args):
            Base.__init__(self, args[0])
        else:
            Base.__init__(self)
        self.hide_dots = self.hide_lines = False
        self.baseline_color = 'red'
        self.baseline_value = None

    def draw(self):
        Line.__base__.draw(self)
        if not self.has_gdata:
            return
        if self.column_count > 1:
            x_increment = float(self.graph_width / (self.column_count - 1))
        else:
            x_increment = self.graph_width

        dl = DrawableList()
        if hasattr(self, "norm_baseline"):
            level = self.graph_top + (self.graph_height - \
                    self.norm_baseline * self.graph_height)
            dl.append(DrawableStrokeColor(Color(self.baseline_color)))
            dl.append(DrawableFillOpacity(0.0))
            dl.append(DrawableStrokeDasharray(10, 20))
            dl.append(DrawableStrokeWidth(5))
            dl.append(DrawableLine(self.graph_left,
                level, self.graph_left + self.graph_width, level))
            self.base_image.draw(dl)
            del(dl)

        for data_row in self.norm_data:
            prev_x = prev_y = None
            self.one_point = self.is_contains_one_point_only(data_row)
            for index, data_point in enumerate(data_row['values']):
                new_x = self.graph_left + (x_increment * index)
                if data_point is None:
                    continue
                self.draw_label(new_x, index)
                new_y = self.graph_top + (self.graph_height - \
                        data_point * self.graph_height)

                # Reset each time to avoid thin-line errors
                dl.append(DrawableStrokeColor(Color(data_row['color'])))
                dl.append(DrawableFillColor(Color(data_row['color'])))
                if type(self.transparent) is float:
                    dl.append(DrawableFillOpacity(self.transparent))
                elif self.transparent is True:
                    dl.append(DrawableFillOpacity(DEFAULT_TRANSPARENCY))
                dl.append(DrawableStrokeOpacity(1.0))
                dl.append(DrawableStrokeWidth(self.line_width or \
                        self.clip_value_if_greater_than(self.columns / \
                        (len(self.norm_data[0]['values']) * 4), 5.0)))

                circle_radius = self.dot_radius or \
                        self.clip_value_if_greater_than(self.columns / \
                        (len(self.norm_data[0]['values']) * 2.5), 5.0)

                if not self.hide_lines and prev_x and prev_y:
                    dl.append(DrawableLine(prev_x, prev_y, new_x, new_y))
                elif self.one_point:
                    dl.append(DrawableCircle(new_x, new_y,
                                             new_x - circle_radius, new_y))
                if not self.hide_dots:
                    dl.append(DrawableCircle(new_x, new_y,
                                             new_x - circle_radius, new_y))

                prev_x = new_x
                prev_y = new_y
        dl.append(DrawableScaling(self.scale, self.scale))
        self.base_image.draw(dl)

    def normalize(self):
        if self.baseline_value:
            tmp = float(self.baseline_value)
        else:
            tmp = 0
        self.maximum_value = max([float(self.maximum_value), tmp])
        Line.__base__.normalize(self)
        if self.baseline_value:
            self.norm_baseline = (float(self.baseline_value) / \
                                  float(self.maximum_value))

    def is_contains_one_point_only(self, data_row):
        # Spin through data to determine if there is just one_value present.
        one_point = False
        for data_point in data_row['values']:
            if data_point:
                if one_point:
                    # more than one point, bail
                    return False
                else:
                    # there is at least one data point
                    return True
        return one_point
