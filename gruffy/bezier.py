from gruffy.base import *


class Bezier(Base):
    """Bezier Graph Object"""

    def draw(self):
        Bezier.__base__.draw(self)
        if not self.has_gdata:
            return
        self._draw_bezier()

    def _draw_bezier(self):
        self.x_increment = self.graph_width / float(self.column_count - 1)
        dl = DrawableList()

        for data_row in self.norm_data:
            poly_points = []
            dl.append(DrawableFillColor(data_row[DATA_COLOR_INDEX]))

            for data_point, index in data_row[1]:
                # Use incremented x and scaled y
                new_x = self.graph_left + (self.x_increment * index)
                new_y = self.graph_top + (self.graph_height - data_point * self.graph_height)
                if index == 0:
                    poly_points.append(self.graph_left)
                    poly_points.append(self.graph_bottom - 1)
                poly_points.append(new_x)
                poly_points.append(new_y)
                self.draw_label(new_x, index)
            dl.append(DrawableFillOpacity(0.0))
            dl.append(DrawableStroke(data_row[DATA_COLOR_INDEX]))
            dl.append(DrawableStrokeWidth(self.clip_value_if_greater_than(self.columns / (self.norm_data.first[1].size * 4), 5.0)))
            dl.append(DrawableBezier(poly_points))
        self.base_image.draw(dl)
