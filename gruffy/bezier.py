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
            poly_points = CoordinateList()
            dl.append(DrawableFillColor(data_row['color']))

            for index, data_point in enumerate(data_row['values']):
                # Use incremented x and scaled y
                new_x = self.graph_left + (self.x_increment * index)
                new_y = self.graph_top + (
                    self.graph_height - data_point * self.graph_height)
                if index == 0:
                    poly_points.append(Coordinate(self.graph_left, self.graph_bottom - 1))
                poly_points.append(Coordinate(new_x, new_y))
                self.draw_label(new_x, index)
            dl.append(DrawableFillOpacity(0.0))
            dl.append(DrawableStrokeColor(data_row['color']))
            dl.append(DrawableStrokeWidth(self.clip_value_if_greater_than(self.columns / (len(self.norm_data[0]['values']) * 4), 5.0)))
            dl.append(DrawableBezier(poly_points))
        self.base_image.draw(dl)
