from gruffy.base import *

TEXT_OFFSET_PERCENTAGE = 0.15


def _deg2rad(angle):
    return angle * (math.pi / 180.0)


class Pie(Base):
    """Pie Graph Object"""

    def _initialize_ivars(self):
        Pie.__base__._initialize_ivars(self)
        self.zero_degree = 0.0
        self.hide_labels_less_than = 0.0

    def draw(self):
        self.hide_line_markers = True
        Pie.__base__.draw(self)
        if not self.has_gdata:
            return
        radius = (min([self.graph_width, self.graph_height]) / 2.0) * 0.8
        #diameter = self.graph_height
        #top_x = self.graph_left + (self.graph_width - diameter) / 2.0
        center_x = self.graph_left + (self.graph_width / 2.0)
        center_y = self.graph_top + (self.graph_height / 2.0) - 10
        total_sum = self.sums_for_pie()
        prev_degrees = self.zero_degree

        def percentages_compare(comp_a, comp_b):
            """Use full data since we can easily calculate percentages"""
            if comp_a['values'][0] > comp_b['values'][0]:
                return 1
            elif comp_a['values'][0] < comp_b['values'][0]:
                return -1
            return 0
        self.gdata.sort(percentages_compare)

        dl = DrawableList()
        for data_row in self.gdata:
            if data_row['values'][0] > 0:
                dl.append(DrawableStrokeColor(data_row['color']))
                dl.append(DrawableFillColor('transparent'))
                # stroke width should be equal to radius.
                # we'll draw centered on (radius / 2)
                dl.append(DrawableStrokeWidth(radius))

                current_degrees = (float(data_row['values'][0]) \
                                    / total_sum) * 360.0

                # ellipse will draw the the stroke centered on
                # the first two parameters offset by the second two.
                # therefore, in order to draw a circle of the proper diameter
                # we must center the stroke at
                # half the radius for both x and y
                dl.append(DrawableEllipse(center_x, center_y,
                          radius / 2.0, radius / 2.0,
                          prev_degrees, prev_degrees + current_degrees + 0.5))
                          # <= +0.5 'fudge factor' gets rid of the ugly gaps

                half_angle = prev_degrees + \
                        ((prev_degrees + current_degrees) - prev_degrees) / 2

                label_val = round(float(data_row['values'][0]) / \
                                  total_sum * 100.0)
                if not (label_val < self.hide_labels_less_than):
                    label_string = str(label_val) + '%%'
                    self.draw_label(center_x, center_y, half_angle,
                                    radius + (radius * TEXT_OFFSET_PERCENTAGE),
                                    label_string)
                prev_degrees += current_degrees
        # TODO debug a circle where the text is drawn...
        self.base_image.draw(dl)

    def draw_label(self, center_x, center_y, angle, radius, amount):
        """
        Labels are drawn around a slightly wider ellipse to give room for
        labels on the left and right.
        """
        dl = DrawableList()
        # TODO Don't use so many hard-coded numbers
        # The distance out from the center of the pie to get point
        r_offset = 20.0
        # + 15.0 # The label points need to be tweaked slightly
        x_offset = center_x
        y_offset = center_y  # This one doesn't though
        radius_offset = (radius + r_offset)
        ellipse_factor = radius_offset * 0.15
        x = x_offset + ((radius_offset + ellipse_factor) * \
                        math.cos(_deg2rad(angle)))
        y = y_offset + (radius_offset * math.sin(_deg2rad(angle)))

        # Draw label
        dl.append(DrawableFillColor(Color(self.font_color)))
        font = self.font if self.font else DEFAULT_FONT
        dl.append(DrawableFont(font, StyleType.NormalStyle, 900,
                               StretchType.NormalStretch))
        dl.append(DrawablePointSize(self.scale_fontsize(
                                        self.marker_font_size)))
        dl.append(DrawableStrokeColor('transparent'))
        dl.append(DrawableGravity(GravityType.NorthWestGravity))
        dl.append(DrawableText(x, y, amount))
        # FIXME: unable scaling
        dl.append(DrawableScaling(self.scale, self.scale))
        self.base_image.draw(dl)

    def sums_for_pie(self):
        """collect data values"""
        return sum([data_row['values'][0] for data_row in self.gdata])
