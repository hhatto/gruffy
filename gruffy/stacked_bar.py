from gruffy.base import *


class StackedBar(Base, StackedMixin):
    """Stacked Bar Graph Object"""

    bar_spacing = None

    def draw(self):
        self.get_maximum_by_stack()
        StackedBar.__base__.draw(self)
        if not self.has_gdata:
            return

        # Setup spacing.
        #
        # Columns sit stacked.
        self.bar_spacing = self.bar_spacing or 0.9
        self.bar_width = self.graph_width / float(self.column_count)
        padding = (self.bar_width * (1 - self.bar_spacing)) / 2

        dl = DrawableList()
        dl.append(DrawableStrokeOpacity(0.0))
        height = [0 for i in range(self.column_count)]
        for raw_index, data_row in enumerate(self.norm_data):
            for point_index, data_point in enumerate(data_row['values']):
                dl.append(DrawableFillColor(Color(data_row['color'])))
                # Calculate center based on bar_width and current row
                label_center = self.graph_left + \
                               (self.bar_width * point_index) + \
                               (self.bar_width * self.bar_spacing / 2.0)
                self.draw_label(label_center, point_index)

                if data_point == 0:
                    continue
                # Use incremented x and scaled y
                left_x = self.graph_left + \
                         (self.bar_width * point_index) + padding
                left_y = self.graph_top + (self.graph_height - \
                         data_point * self.graph_height - \
                         height[point_index]) + 1
                right_x = left_x + self.bar_width * self.bar_spacing
                right_y = self.graph_top + \
                          self.graph_height - height[point_index] - 1
                # update the total height of the current stacked bar
                height[point_index] += (data_point * self.graph_height)
                dl.append(DrawableRectangle(left_x, left_y, right_x, right_y))
        dl.append(DrawableScaling(self.scale, self.scale))
        self.base_image.draw(dl)
