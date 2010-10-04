import copy
from gruffy.base import *


class StackedArea(Base, StackedMixin):
    """Stacked Area Graph Object"""

    last_series_goes_on_bottom = None

    def draw(self):
        self.get_maximum_by_stack()
        StackedArea.__base__.draw(self)
        if not self.has_gdata:
            return
        dl = DrawableList()
        self.x_increment = self.graph_width / float(self.column_count - 1)
        dl.append(DrawableStrokeColor('transparent'))

        height = [0 for i in range(self.column_count)]

        data_points = None
        if self.last_series_goes_on_bottom:
            self.norm_data.reverse()
        for data_row in self.norm_data:
            prev_data_points = data_points
            data_points = []
            dl.append(DrawableFillColor(Color(data_row['color'])))
            for index, data_point in enumerate(data_row['values']):
                # Use incremented x and scaled y
                new_x = self.graph_left + (self.x_increment * index)
                new_y = self.graph_top + (self.graph_height - data_point * \
                        self.graph_height - height[index])

                height[index] += (data_point * self.graph_height)
                data_points.append(new_x)
                data_points.append(new_y)
                self.draw_label(new_x, index)

            if prev_data_points:
                poly_points = copy.copy(data_points)
                tmp_max_point = len(prev_data_points) / 2 - 1
                for i in range(tmp_max_point, -1, -1):
                    poly_points.append(prev_data_points[2 * i])
                    poly_points.append(prev_data_points[2 * i + 1])
                poly_points.append(data_points[0])
                poly_points.append(data_points[1])
            else:
                poly_points = copy.copy(data_points)
                poly_points.append(self.graph_right)
                poly_points.append(self.graph_bottom - 1)
                poly_points.append(self.graph_left)
                poly_points.append(self.graph_bottom - 1)
                poly_points.append(data_points[0])
                poly_points.append(data_points[1])
            # generate CoordinateList
            coordinates = [Coordinate(poly_points[i], poly_points[i + 1]) \
                           for i in range(0, len(poly_points), 2)]
            cl = CoordinateList()
            for c in coordinates:
                cl.append(c)
            dl.append(DrawablePolyline(cl))
        dl.append(DrawableScaling(self.scale, self.scale))
        self.base_image.draw(dl)
