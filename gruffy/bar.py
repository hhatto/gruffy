from gruffy.base import *
from gruffy.bar_conversion import BarConversion


class Bar(Base):
    """Bar Graph Object"""

    bar_spacing = 0

    def draw(self):
        if len(self.labels.keys()) > self.column_count:
            self.center_labels_over_point = True
        else:
            self.center_labels_over_point = False
        Bar.__base__.draw(self)
        if not self.has_gdata:
            return
        self._draw_bars()

    def _draw_bars(self):
        self.bar_spacing = self.bar_spacing or 0.9
        self.bar_width = self.graph_width / \
                            float(self.column_count * len(self.gdata))
        padding = (self.bar_width * (1 - self.bar_spacing)) / 2
        dl = DrawableList()
        dl.append(DrawableStrokeOpacity(0.0))
        conversion = BarConversion()
        conversion.graph_height = self.graph_height
        conversion.graph_top = self.graph_top
        if self.minimum_value >= 0:
            conversion.mode = 1
        else:
            if self.maximum_value <= 0:
                conversion.mode = 2
            else:
                conversion.mode = 3
                conversion.spread = self.spread
                conversion.minimum_value = self.minimum_value
                conversion.zero = -self.minimum_value / self.spread
        for row_index, data_row in enumerate(self.norm_data):
            for point_index, data_point in enumerate(data_row['values']):
                left_x = self.graph_left + (self.bar_width * \
                             (row_index + point_index + \
                             ((len(self.gdata) - 1) * point_index))) + padding
                right_x = left_x + self.bar_width * self.bar_spacing
                conv = conversion.getLeftYRightYscaled(data_point)
                dl.append(DrawableFillColor(Color(data_row['color'])))
                if type(self.transparent) is float:
                    dl.append(DrawableFillOpacity(self.transparent))
                elif self.transparent is True:
                    dl.append(DrawableFillOpacity(DEFAULT_TRANSPARENCY))
                dl.append(DrawableRectangle(left_x, conv[0], right_x, conv[1]))

                label_center = self.graph_left + \
                                (len(self.gdata) * self.bar_width * point_index) + \
                                (len(self.gdata) * self.bar_width / 2.0)
                if self.center_labels_over_point:
                    tmp = self.bar_width / 2.0
                else:
                    tmp = 0.0
                self.draw_label(label_center - tmp, point_index)
        if self.center_labels_over_point:
            self.draw_label(self.graph_right, self.column_count)
        dl.append(DrawableScaling(self.scale, self.scale))
        self.base_image.draw(dl)
