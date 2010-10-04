from gruffy.base import *
from gruffy.sidebar import SideBar


class StackedSideBar(SideBar, StackedMixin):
    """Stacked Side Bar Graph Object"""

    bar_spacing = None

    def draw(self):
        self.has_left_labels = True
        self.get_maximum_by_stack()
        SideBar.draw(self)

    def draw_bars(self):
        # Setup spacing.
        #
        # Columns sit stacked.
        self.bar_spacing = self.bar_spacing or 0.9

        self.bar_width = self.graph_height / float(self.column_count)
        dl = DrawableList()
        dl.append(DrawableStrokeOpacity(0.0))
        height = [0 for i in range(self.column_count)]
        length = [self.graph_left for i in range(self.column_count)]
        padding = (self.bar_width * (1 - self.bar_spacing)) / 2

        for row_index, data_row in enumerate(self.norm_data):
            for point_index, data_point in enumerate(data_row['values']):
                # using the original calcs from the stacked bar chart to
                # get the difference between part of the bart chart
                # we wish to stack.
                tmp1 = self.graph_left + (self.graph_width - \
                       data_point * self.graph_width - height[point_index]) + 1
                tmp2 = self.graph_left + \
                       self.graph_width - height[point_index] - 1
                difference = tmp2 - tmp1
                dl.append(DrawableFillColor(Color(data_row['color'])))
                if type(self.transparent) is float:
                    dl.append(DrawableFillOpacity(self.transparent))
                elif self.transparent is True:
                    dl.append(DrawableFillOpacity(DEFAULT_TRANSPARENCY))
                left_x = length[point_index]
                left_y = self.graph_top + \
                         (self.bar_width * point_index) + padding
                right_x = left_x + difference
                right_y = left_y + self.bar_width * self.bar_spacing
                length[point_index] += difference
                height[point_index] += (data_point * self.graph_width - 2)

                dl.append(DrawableRectangle(left_x, left_y, right_x, right_y))

                # Calculate center based on bar_width and current row
                label_center = self.graph_top + \
                               (self.bar_width * point_index) + \
                               (self.bar_width * self.bar_spacing / 2.0)
                self.draw_label(label_center, point_index)
        dl.append(DrawableScaling(self.scale, self.scale))
        self.base_image.draw(dl)

    def larger_than_max(self, data_point, index=0):
        if self.lmax(data_point, index) > self.maximum_value:
            return True
        return False

    def lmax(self, data_point, index):
        #self.gdata.inject(0) {|sum, item| sum + item['values'][index]}
        total = 0
        for data in self.gdata:
            total += data['values'][index]
        return total
