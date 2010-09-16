import base
import pgmagick as pg


class SideBar(base.Base):

    bar_spacing = None

    def __init__(self, *args):
        base.Base.__init__(self)

    def draw(self):
        self.has_left_labels = True
        if not self.has_gdata:
            return
        SideBar.__base__.draw(self)
        self._draw_bars()

    def _draw_bars(self):
        dl = pg.DrawableList()
        self.bar_spacing = self.bar_spacing or 0.9
        self.bars_width = self.graph_height / float(self.column_count)
        self.bar_width = self.bars_width / len(self.norm_data)
        dl.append(pg.DrawableStrokeOpacity(0.0))
        height = [0 for i in range(self.column_count)]
        length = [self.graph_left for i in range(self.column_count)]
        padding = (self.bar_width * (1 - self.bar_spacing)) / 2

        for row_index, data_row in enumerate(self.norm_data):
            dl.append(pg.DrawableFillColor(pg.Color(data_row[base.DATA_COLOR_INDEX])))
            for point_index, data_point in enumerate(data_row[base.DATA_VALUES_INDEX]):
                # Using the original calcs from the stacked bar chart
                # to get the difference between
                # part of the bart chart we wish to stack.
                temp1 = self.graph_left + \
                        (self.graph_width - data_point * self.graph_width - height[point_index])
                temp2 = self.graph_left + self.graph_width - height[point_index]
                difference = temp2 - temp1

                left_x = length[point_index] - 1
                left_y = self.graph_top + (self.bars_width * point_index) + \
                         (self.bar_width * row_index) + padding
                right_x = left_x + difference
                right_y = left_y + self.bar_width * self.bar_spacing
                height[point_index] += (data_point * self.graph_width)
                dl.append(pg.DrawableRectangle(left_x, left_y, right_x, right_y))

                # Calculate center based on bar_width and current row
                label_center = self.graph_top + (self.bars_width * point_index + self.bars_width / 2)
                self.draw_label(label_center, point_index)
        self.base_image.draw(dl)

    # Instead of base class version, draws vertical background lines and label
    def draw_line_markers(self):
        if self.hide_line_markers:
            return

        dl = pg.DrawableList()
        dl.append(pg.DrawableStrokeAntialias(False))

        # Draw horizontal line markers and annotate with numbers
        dl.append(pg.DrawableFillColor(pg.Color(self.marker_color)))
        dl.append(pg.DrawableStrokeWidth(1))
        number_of_lines = 5

        # TODO Round maximum marker value to a round number like 100, 0.1, 0.5, etc.
        increment = self.significant(float(self.spread) / number_of_lines)
        for index in range(number_of_lines + 1):
            line_diff = (self.graph_right - self.graph_left) / number_of_lines
            x = self.graph_right - (line_diff * index) - 1
            dl.append(pg.DrawableLine(x, self.graph_bottom, x, self.graph_top))
            diff = index - number_of_lines
            marker_label = abs(diff) * increment + self.minimum_value

            if not self.hide_line_numbers:
                dl.append(pg.DrawableFillColor(pg.Color(self.font_color)))
                font = self.font if self.font else ""
                dl.append(pg.DrawableFont(font, pg.StyleType.NormalStyle, 400,
                                          pg.StretchType.NormalStretch))
                dl.append(pg.DrawableStrokeColor(pg.Color('transparent')))
                dl.append(pg.DrawablePointSize(self.scale_fontsize(self.marker_font_size)))
                dl.append(pg.DrawableGravity(pg.GravityType.CenterGravity))
                # TODO Center text over line
                dl.append(pg.DrawableText(x, self.graph_bottom + (base.LABEL_MARGIN * 2.0),
                                          str(marker_label)))
            dl.append(pg.DrawableStrokeAntialias(True))
            self.base_image.draw(dl)

    def draw_label(self, y_offset, index):
        if self.labels.has_key(index) and not self.labels_seen.has_key(index):
            dl = pg.DrawableList()
            dl.append(pg.DrawableFillColor(self.font_color))
            font = self.font if self.font else ""
            dl.append(pg.DrawableFont(font, pg.StyleType.NormalStyle, 400,
                                      pg.StretchType.NormalStretch))
            dl.append(pg.DrawableStrokeColor(pg.Color('transparent')))
            dl.append(pg.DrawablePointSize(self.scale_fontsize(self.marker_font_size)))
            dl.append(pg.DrawableGravity(pg.GravityType.WestGravity))
            dl.append(pg.DrawableText(-self.graph_left + base.LABEL_MARGIN * 2.0, y_offset,
                                   self.labels[index]))
            self.labels_seen[index] = 1
            self.base_image.draw(dl)
