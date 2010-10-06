from gruffy.base import *


class Dot(Base):
    """Dot Graph Object"""

    def draw(self):
        self.has_left_labels = True
        Dot.__base__.draw(self)
        if not self.has_gdata:
            return

        spacing_factor = 1.0

        self.items_width = self.graph_height / float(self.column_count)
        self.item_width = self.items_width * \
                          spacing_factor / len(self.norm_data)

        dl = DrawableList()
        dl.append(DrawableStrokeOpacity(0.0))
        padding = (self.items_width * (1 - spacing_factor)) / 2

        for row_index, data_row in enumerate(self.norm_data):
            for point_index, data_point in enumerate(data_row['values']):
                x_pos = self.graph_left + (data_point * self.graph_width) - \
                        round(float(self.item_width) / 6.0)
                y_pos = self.graph_top + (self.items_width * point_index) + \
                        padding + round(float(self.item_width) / 2.0)
                if row_index == 0:
                    dl.append(DrawableStrokeColor(Color(self.marker_color)))
                    dl.append(DrawableStrokeWidth(1.0))
                    dl.append(DrawableStrokeOpacity(0.1))
                    dl.append(DrawableLine(self.graph_left,
                                           y_pos,
                                           self.graph_left + self.graph_width,
                                           y_pos))
                dl.append(DrawableFillColor(Color(data_row['color'])))
                if type(self.transparent) is float:
                    dl.append(DrawableFillOpacity(self.transparent))
                elif self.transparent is True:
                    dl.append(DrawableFillOpacity(DEFAULT_TRANSPARENCY))
                dl.append(DrawableStrokeColor('transparent'))
                dl.append(DrawableCircle(x_pos,
                    y_pos, x_pos + round(float(self.item_width) / 3.0), y_pos))
                # Calculate center based on item_width and current row
                label_center = self.graph_top + (self.items_width * \
                        point_index + self.items_width / 2) + padding
                self.draw_label(label_center, point_index)
        dl.append(DrawableScaling(self.scale, self.scale))
        self.base_image.draw(dl)

    def draw_line_markers(self):
        if self.hide_line_markers:
            return
        dl = DrawableList()
        dl.append(DrawableStrokeAntialias(False))

        # Draw horizontal line markers and annotate with numbers
        dl.append(DrawableStrokeColor(Color(self.marker_color)))
        dl.append(DrawableStrokeWidth(1))
        number_of_lines = 5

        # TODO Round maximum marker value to a round number like
        # 100, 0.1, 0.5, etc.
        increment = self.significant(float(self.maximum_value) / number_of_lines)
        for index in range(number_of_lines + 1):
            line_diff = (self.graph_right - self.graph_left) / number_of_lines
            x = self.graph_right - (line_diff * index) - 1
            dl.append(DrawableLine(x, self.graph_bottom,
                                   x, self.graph_bottom + 0.5 * LABEL_MARGIN))
            diff = index - number_of_lines
            marker_label = abs(diff) * increment

            if not self.hide_line_numbers:
                dl.append(DrawableFillColor(Color(self.font_color)))
                font = self.font if self.font else DEFAULT_FONT
                dl.append(DrawableFont(font, StyleType.NormalStyle, 400,
                                       StretchType.NormalStretch))
                dl.append(DrawableStrokeColor('transparent'))
                dl.append(DrawablePointSize(self.marker_font_size))
                dl.append(DrawableGravity(GravityType.NorthWestGravity))
                font_hight = self.calculate_caps_height(self.marker_font_size)
                text_width = self.calculate_width(self.marker_font_size,
                                                  str(marker_label))
                x -= text_width / 2.0
                y = font_hight / 2.0 + self.graph_bottom + (LABEL_MARGIN * 2.0)
                dl.append(DrawableText(x, y, str(marker_label)))
            dl.append(DrawableStrokeAntialias(True))
        dl.append(DrawableScaling(self.scale, self.scale))
        self.base_image.draw(dl)

    def draw_label(self, y_offset, index):
        if index in self.labels and index not in self.labels_seen:
            dl = DrawableList()
            dl.append(DrawableFillColor(Color(self.font_color)))
            font = self.font if self.font else DEFAULT_FONT
            dl.append(DrawableFont(font, StyleType.NormalStyle, 400,
                                   StretchType.NormalStretch))
            dl.append(DrawableStrokeColor('transparent'))
            dl.append(DrawablePointSize(self.marker_font_size))
            dl.append(DrawableGravity(GravityType.NorthEastGravity))
            font_hight = self.calculate_caps_height(self.marker_font_size)
            text_width = self.calculate_width(self.marker_font_size,
                                              self.labels[index])
            x = self.raw_columns - self.graph_left + LABEL_MARGIN
            y = y_offset + font_hight / 2.0
            dl.append(DrawableText(x, y, self.labels[index]))
            self.labels_seen[index] = 1
            dl.append(DrawableScaling(self.scale, self.scale))
            self.base_image.draw(dl)
