from gruffy.base import *


class Area(Base):

    def draw(self):
        Area.__base__.draw(self)
        if not self.has_gdata:
            return
        self.x_increment = self.graph_width / float(self.column_count - 1)
        dl = DrawableList()
        dl.append(DrawableStrokeColor(Color('transparent')))
        for data_row in self.norm_data:
            poly_points = CoordinateList()
            prev_x = prev_y = 0.0
            dl.append(DrawableFillColor(Color(data_row[DATA_COLOR_INDEX])))

            for index, data_point in enumerate(data_row[DATA_VALUES_INDEX]):
                # Use incremented x and scaled y
                new_x = self.graph_left + (self.x_increment * index)
                new_y = self.graph_top + \
                        (self.graph_height - data_point * self.graph_height)
                if prev_x > 0 and prev_y > 0:
                    poly_points.append(Coordinate(new_x, new_y))
                else:
                    poly_points.append(Coordinate(self.graph_left,
                                                  self.graph_bottom - 1))
                    poly_points.append(Coordinate(new_x, new_y))
                self.draw_label(new_x, index)
                prev_x = new_x
                prev_y = new_y
            # Add closing points, draw polygon
            poly_points.append(Coordinate(self.graph_right,
                                          self.graph_bottom - 1))
            poly_points.append(Coordinate(self.graph_left,
                                          self.graph_bottom - 1))
            dl.append(DrawablePolyline(poly_points))
        self.base_image.draw(dl)
