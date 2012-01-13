import math
import os
from pgmagick import *

# Space around text elements. Mostly used for vertical spacing
LEGEND_MARGIN = TITLE_MARGIN = 20.0
LABEL_MARGIN = 10.0
DEFAULT_MARGIN = 20.0

DEFAULT_TRANSPARENCY = 0.7
DEFAULT_TARGET_WIDTH = 800
DEFAULT_FONT = "Vera.ttf"

THOUSAND_SEPARATOR = ','


class Base(object):
    """This object is based on all Graph Object.
    When you create new graph object, override this object::

        from gruffy.base import Base

        class NewGraph(Base):
            pass
    """

    #: Title of Graph.
    title = None

    #: Transparent flag (or value).
    #: *False* is non-transparent rendering, *True* is default value
    #: transparent, *float* value is value's transparent.
    transparent = False

    #: setting labels
    x_axis_label = y_axis_label = None
    additional_line_values = False

    def __init__(self, target_width=DEFAULT_TARGET_WIDTH):
        if type(target_width) is not int:
            geometric_width, geometric_height = target_width.split('x')
            self.columns = float(geometric_width)
            self.rows = float(geometric_height)
        else:
            self.columns = float(target_width)
            self.rows = target_width * 0.75

        self._initialize_ivars()
        self._reset_themes()
        self.theme_keynote()

    def _initialize_ivars(self):
        """Internal for calculations"""
        self.raw_columns = 800.0
        self.raw_rows = 800.0 * (self.rows / self.columns)
        self.column_count = 0
        self.marker_count = None
        self.maximum_value = self.minimum_value = None
        self.has_gdata = False
        self.gdata = []
        self.labels = {}
        self.labels_seen = {}
        self.sort = True

        self.scale = self.columns / self.raw_columns

        if 'MAGICK_FONT_PATH' in os.environ:
            vera_font_path = os.path.join(os.environ['MAGICK_FONT_PATH'],
                                          DEFAULT_FONT)
        else:
            vera_font_path = 'Vera.ttf'
        self.font = vera_font_path if os.path.exists(vera_font_path) else None

        self.marker_font_size = 21.0
        self.legend_font_size = 20.0
        self.title_font_size = 36.0

        self.top_margin = DEFAULT_MARGIN
        self.bottom_margin = DEFAULT_MARGIN
        self.left_margin = DEFAULT_MARGIN
        self.right_margin = DEFAULT_MARGIN
        self.legend_margin = LEGEND_MARGIN
        self.title_margin = TITLE_MARGIN

        self.legend_box_size = 20.0

        self.no_data_message = "No Data"

        self.hide_line_markers = False
        self.hide_legend = False
        self.hide_title = False
        self.hide_line_numbers = False
        self.center_labels_over_point = True
        self.has_left_labels = False

        self.additional_line_colors = []
        self.theme_options = {}

        self.y_axis_increment = None
        self.stacked = None
        self.norm_data = None

    def _reset_themes(self):
        self.color_index = 0
        self.labels_seen = {}
        self.theme_options = {}

    def theme_keynote(self):
        """Setting up Keynote like gradient theme.
        """
        self.blue = '#6886B4'
        self.yellow = '#FDD84E'
        self.green = '#72AE6E'
        self.red = '#D1695E'
        self.purple = '#8A6EAF'
        self.orange = '#EFAA43'
        self.white = 'white'
        self.colors = [self.yellow, self.blue, self.green, self.red,
                       self.purple, self.orange, self.white]

        self.set_theme({'colors': self.colors,
                        'marker_color': 'white',
                        'font_color': 'white',
                        'background_colors': ['black', '#4a465a']})

    def theme_37signals(self):
        """Setting up 37 signals like gradient theme.
        """
        self.green = '#339933'
        self.purple = '#cc99cc'
        self.blue = '#336699'
        self.yellow = '#FFF804'
        self.red = '#ff0000'
        self.orange = '#cf5910'
        self.black = 'black'
        self.colors = [self.yellow, self.blue, self.green, self.red,
                       self.purple, self.orange, self.black]
        self.set_theme({'colors': self.colors,
                        'marker_color': 'black',
                        'font_color': 'black',
                        'background_colors': ['#d1edf5', 'white']})

    def theme_rails_keynote(self):
        """A color scheme from the colors used on the 2005 Rails keynote
        presentation at RubyConf.
        """
        self.green = '#00ff00'
        self.grey = '#333333'
        self.orange = '#ff5d00'
        self.red = '#f61100'
        self.white = 'white'
        self.light_grey = '#999999'
        self.black = 'black'
        self.colors = [self.green, self.grey, self.orange, self.red,
                       self.white, self.light_grey, self.black]
        self.set_theme({'colors': self.colors,
                        'marker_color': 'white',
                        'font_color': 'white',
                        'background_colors': ['#0083a3', '#0083a3']})

    def theme_odeo(self):
        """A color scheme similar to that used on the popular podcast site.
        """
        self.grey = '#202020'
        self.white = 'white'
        self.dark_pink = '#a21764'
        self.green = '#8ab438'
        self.light_grey = '#999999'
        self.dark_blue = '#3a5b87'
        self.black = 'black'
        self.colors = [self.grey, self.white, self.dark_blue,
                       self.dark_pink, self.green, self.light_grey, self.black]
        self.set_theme({'colors': self.colors,
                        'marker_color': 'white',
                        'font_color': 'white',
                        'background_colors': ['#ff47a4', '#ff1f81']})

    def theme_pastel(self):
        """Setting up pastel color theme."""
        self.colors = ['#a9dada',   # blue
                       '#aedaa9',   # green
                       '#daaea9',   # peach
                       '#dadaa9',   # yellow
                       '#a9a9da',   # dk purple
                       '#daaeda',   # purple
                       '#dadada',   # grey
                      ]
        self.set_theme({'colors': self.colors,
                        'marker_color': '#aea9a9',
                        'font_color': 'black',
                        'background_colors': 'white'})

    def theme_django(self):
        """Setting up Django like theme"""
        self.colors = ['#a9dada', '#aedaa9', '#94da3a',
                       '#487854', '#a9a9da', '#dadada']
        self.set_theme({'colors': self.colors,
                        'marker_color': '#ab5603',
                        'font_color': 'white',
                        'background_colors': ['#092e20', '#234f32']})

    def theme_greyscale(self):
        """Setting up black and white theme"""
        self.colors = ['#282828', '#383838', '#686868',
                       '#989898', '#c8c8c8', '#e8e8e8']
        self.set_theme({'colors': self.colors,
                        'marker_color': '#aea9a9',
                        'font_color': 'black',
                        'background_colors': 'white'})

    def render_background(self):
        if type(self.theme_options['background_colors']) is list:
            colors = self.theme_options['background_colors']
            self.base_image = self.render_gradiated_background(*colors)
        elif type(self.theme_options['background_colors']) is str:
            colors = self.theme_options['background_colors']
            self.base_image = self.render_solid_background(colors)
        else:
            image = self.theme_options['background_image']
            self.base_image = self.render_image_background(image)

    def render_solid_background(self, color):
        return Image(Geometry(int(self.columns), int(self.rows)), color)

    def render_gradiated_background(self, top_color, bottom_color):
        im = Image(Geometry(int(self.columns), int(self.rows)),
                   Color('transparent'))
        im.read("gradient:%s-%s" % (top_color, bottom_color))
        return im

    def render_image_background(self, image_path, opacity=True):
        image = Image(image_path)
        if type(opacity) is int:
            image.opacity(opacity)
        elif opacity is True:
            image.opacity(50)
        return image

    def set_theme(self, options):
        self._reset_themes()

        defaults = {
                'colors': ['black', 'white'],
                'additional_line_colors': [],
                'marker_color': 'white',
                'font_color': 'black',
                'background_colors': None,
                'background_image': None}
        defaults.update(options)
        self.theme_options = defaults
        self.colors = self.theme_options['colors']
        self.marker_color = self.theme_options['marker_color']
        self.font_color = self.theme_options['font_color'] or self.marker_color
        self.additional_line_colors = self.theme_options['additional_line_colors']

        self.render_background()

    def increment_color(self):
        self.color_index = (self.color_index + 1) % len(self.colors)
        return self.colors[self.color_index - 1]

    def data(self, name, data_points=[], color=None):
        """Set up graph dataset

        :param name: data name
        :param data_points: list of data point
        :param color: *force* settig color of graph data
        """
        data_points = list(data_points)
        self.gdata.append({'label': name,
                           'values': data_points,
                           'color': color or self.increment_color()})
        if len(data_points) > self.column_count:
            self.column_count = len(data_points)
        for cnt, data_point in enumerate(data_points):
            if data_points is None:
                continue
            if self.maximum_value is None and self.minimum_value is None:
                self.maximum_value = self.minimum_value = data_point
                if self.minimum_value >= 0:
                    self.minimum_value = 0
            # TODO Doesn't work with stacked bar graphs
            if self.larger_than_max(data_point):
                self.maximum_value = data_point
            if self.maximum_value >= 0:
                self.has_gdata = True
            if self.less_than_min(data_point):
                self.minimum_value = data_point
            if self.minimum_value < 0:
                self.has_gdata = True

    def draw_line_markers(self):
        if self.hide_line_markers:
            return
        self.base_image.draw(DrawableStrokeAntialias(False))

        if self.y_axis_increment is None:
            # Try to use a number of horizontal lines that will come out even.
            #
            # TODO Do the same for larger numbers...100, 75, 50, 25
            if self.marker_count is None:
                for lines in range(3, 7):
                    if self.spread % lines == 0.0:
                        self.marker_count = lines
                        break
                self.marker_count = self.marker_count or 4
            if self.spread > 0:
                self.increment = self.significant(self.spread / self.marker_count)
            else:
                self.increment = 1
        else:
            # TODO Make this work for negative values
            self.maximum_value = max([self.maximum_value.ceil,
                                      self.y_axis_increment])
            self.minimum_value = math.floor(self.minimum_value)
            self.calculate_spread()
            self.normalize(true)

            self.marker_count = int(self.spread / self.y_axis_increment)
            self.increment = self.y_axis_increment
        self.increment_scaled = float(self.graph_height) / (self.spread / self.increment)

        # Draw horizontal line markers and annotate with numbers
        dl = DrawableList()
        for index in range(self.marker_count + 1):
            y = self.graph_top + self.graph_height - float(index) * self.increment_scaled

            dl.append(DrawableFillColor(Color(self.marker_color)))
            dl.append(DrawableLine(self.graph_left, y, self.graph_right, y))

            marker_label = index * self.increment + float(self.minimum_value)

            if not self.hide_line_numbers:
                dl.append(DrawableFillColor(Color(self.font_color)))
                font = self.font if self.font else DEFAULT_FONT
                dl.append(DrawableFont(font, StyleType.NormalStyle, 400,
                                       StretchType.NormalStretch))
                dl.append(DrawableStrokeColor('transparent'))
                marker_font_size = self.scale_fontsize(self.marker_font_size)
                dl.append(DrawablePointSize(marker_font_size))

                # Vertically center with 1.0 for the height
                dl.append(DrawableGravity(GravityType.NorthWestGravity))
                x = self.calculate_width(self.marker_font_size, marker_label) / 2
                y = y + self.calculate_caps_height(marker_font_size) / 3
                dl.append(DrawableText(self.graph_left - LABEL_MARGIN - x,
                                       y, self.label(marker_label)))
        dl.append(DrawableScaling(self.scale, self.scale))
        dl.append(DrawableStrokeAntialias(True))
        self.base_image.draw(dl)

    def draw_label(self, x_offset, index):
        if self.hide_line_markers:
            return
        if index in self.labels and index not in self.labels_seen:
            y_offset = self.graph_bottom + LABEL_MARGIN

            dl = DrawableList()
            dl.append(DrawableFillColor(Color(self.font_color)))
            dl.append(DrawableGravity(GravityType.NorthWestGravity))
            font = self.font if self.font else DEFAULT_FONT
            dl.append(DrawableFont(font, StyleType.NormalStyle, 400,
                                   StretchType.NormalStretch))
            dl.append(DrawableStrokeColor(Color('transparent')))
            dl.append(DrawablePointSize(self.marker_font_size))
            label_font_height = self.calculate_caps_height(self.marker_font_size) / 2
            label_text_width = self.calculate_width(self.marker_font_size,
                                                    self.labels[index])
            dl.append(DrawableText(x_offset - label_text_width / 2.0,
                                   y_offset + label_font_height,
                                   self.labels[index]))
            dl.append(DrawableScaling(self.scale, self.scale))
            self.base_image.draw(dl)
            self.labels_seen[index] = 1

    def draw_no_data(self):
        dl = DrawableList()
        dl.append(DrawableFillColor(Color(self.font_color)))
        font = self.font if self.font else DEFAULT_FONT
        dl.append(DrawableGravity(GravityType.CenterGravity))
        dl.append(DrawableFillColor(Color(self.font_color)))
        dl.append(DrawableFont(font, StyleType.NormalStyle, 800,
                               StretchType.NormalStretch))
        dl.append(DrawablePointSize(self.scale_fontsize(80)))
        dl.append(DrawableText(0, 0, self.no_data_message))
        dl.append(DrawableScaling(self.scale, self.scale))
        self.base_image.draw(dl)

    def scale_fontsize(self, value):
        return value * self.scale

    def clip_value_if_greater_than(self, value, max_value):
        return max_value if value > max_value else value

    def larger_than_max(self, data_point):
        return True if data_point > self.maximum_value else False

    def less_than_min(self, data_point):
        return True if data_point < self.minimum_value else False

    def significant(self, inc):
        if inc == 0:
            return 1.0
        factor = 1.0
        while (inc < 10):
            inc = inc * 10
            factor = factor / 10
        while (inc > 100):
            inc = inc / 10
            factor = factor * 10
        res = math.floor(inc) * factor
        if float(int(res)) == res:
            return int(res)
        else:
            return res

    def sort_norm_data(self):
        def normcompare(a, b):
            a_sum = sum(a['values'])
            b_sum = sum(b['values'])
            if a_sum > b_sum:
                return 1
            elif a_sum < b_sum:
                return -1
            return 0
        self.norm_data.sort(normcompare)
        self.norm_data.reverse()

    def center(self, size):
        return (self.raw_columns - size) / 2

    def draw_axis_labels(self):
        if self.x_axis_label:
            dl = DrawableList()
            # X Axis
            # Centered vertically and horizontally by setting the
            # height to 1.0 and the width to the width of the graph.
            x_axis_label_y_coordinate = self.graph_bottom + \
                    LABEL_MARGIN * 2 + self.marker_caps_height

            dl.append(DrawableFillColor(Color(self.font_color)))
            font = self.font if self.font else DEFAULT_FONT
            dl.append(DrawableFont(font, StyleType.NormalStyle, 400,
                                   StretchType.NormalStretch))
            dl.append(DrawableStrokeColor('transparent'))
            dl.append(DrawablePointSize(self.marker_font_size))
            dl.append(DrawableGravity(GravityType.NorthGravity))
            # graph center
            #dl.append(DrawableText(self.graph_left / 2.0,
            #                       x_axis_label_y_coordinate,
            #                       self.x_axis_label))
            dl.append(DrawableText(0.0, x_axis_label_y_coordinate,
                                   self.x_axis_label))
            dl.append(DrawableScaling(self.scale, self.scale))
            self.base_image.draw(dl)
        if self.y_axis_label:
            # Y Axis, rotated vertically
            dl = DrawableList()
            dl.append(DrawableFillColor(Color(self.font_color)))
            font = self.font if self.font else DEFAULT_FONT
            dl.append(DrawableFont(font, StyleType.NormalStyle, 400,
                                   StretchType.NormalStretch))
            dl.append(DrawableStrokeColor('transparent'))
            fontsize = self.marker_font_size
            dl.append(DrawablePointSize(fontsize))
            dl.append(DrawableRotation(90))
            dl.append(DrawableGravity(GravityType.WestGravity))
            x = -(self.calculate_width(fontsize, self.y_axis_label) / 2.0)
            y = -(self.left_margin + self.marker_caps_height / 2.0)
            dl.append(DrawableText(x, y, self.y_axis_label))
            dl.append(DrawableScaling(self.scale, self.scale))
            dl.append(DrawableRotation(-90))
            self.base_image.draw(dl)

    def draw_legend(self):
        if self.hide_legend:
            return
        self.legend_labels = [gdata['label'] for gdata in self.gdata]
        legend_square_width = self.legend_box_size

        dl = DrawableList()

        font = self.font if self.font else DEFAULT_FONT
        dl.append(DrawablePointSize(self.legend_font_size))

        label_widths = [[]]     # Used to calculate line wrap
        for label in self.legend_labels:
            metrics = TypeMetric()
            self.base_image.fontTypeMetrics(str(label), metrics)
            label_width = metrics.textWidth() + legend_square_width * 2.7
            label_widths[-1].append(label_width)
            if sum(label_widths[-1]) > (self.raw_columns * 0.9):
                label_widths.append([label_widths[-1].pop()])

        current_x_offset = self.center(sum(label_widths[0]))
        if self.hide_title:
            current_y_offset = self.top_margin + self.title_margin
        else:
            current_y_offset = self.top_margin + self.title_margin + self.title_caps_height

        dl.append(DrawableStrokeColor('transparent'))
        for index, legend_label in enumerate(self.legend_labels):
            # Now draw box with color of this dataset
            dl.append(DrawableFillColor(Color(self.gdata[index]['color'])))
            dl.append(DrawableRectangle(current_x_offset,
                                        current_y_offset - legend_square_width / 2.0,
                                        current_x_offset + legend_square_width,
                                        current_y_offset + legend_square_width / 2.0))

            # Draw label
            dl.append(DrawableFillColor(Color(self.font_color)))
            font = self.font if self.font else DEFAULT_FONT
            dl.append(DrawableFont(font, StyleType.NormalStyle, 400,
                                   StretchType.NormalStretch))
            dl.append(DrawablePointSize(self.legend_font_size))
            dl.append(DrawableGravity(GravityType.NorthWestGravity))
            x = current_x_offset + legend_square_width * 1.7
            y = current_y_offset + self.legend_caps_height / 3
            dl.append(DrawableText(x, y, str(legend_label)))

            dl.append(DrawablePointSize(self.legend_font_size))
            metrics = TypeMetric()
            self.base_image.fontTypeMetrics(str(legend_label), metrics)
            current_string_offset = metrics.textWidth() + legend_square_width * 2.7

            # Handle wrapping
            del(label_widths[0][0])
            if len(label_widths[0]) == 0:
                del(label_widths[0])
                if len(label_widths) != 0:
                    current_x_offset = self.center(sum(label_widths[0]))
                line_height = max([self.legend_caps_height, legend_square_width]) + self.legend_margin
                if len(label_widths) > 0:
                    # Wrap to next line and shrink available graph dimensions
                    current_y_offset += line_height
                    self.graph_top += line_height
                    self.graph_height = self.graph_bottom - self.graph_top
            else:
                current_x_offset += current_string_offset
        if len(dl):
            dl.append(DrawableScaling(self.scale, self.scale))
            self.base_image.draw(dl)
        self.color_index = 0

    def draw_title(self):
        if self.hide_title or self.title is None:
            return
        dl = DrawableList()
        dl.append(DrawableFillColor(Color(self.font_color)))
        font = self.font if self.font else DEFAULT_FONT
        dl.append(DrawableGravity(GravityType.NorthGravity))
        dl.append(DrawableFont(font, StyleType.NormalStyle, 800,
                               StretchType.NormalStretch))
        dl.append(DrawablePointSize(self.title_font_size))
        y = self.top_margin + self.title_caps_height / 2.0
        dl.append(DrawableText(0, y, self.title))
        dl.append(DrawableScaling(self.scale, self.scale))
        self.base_image.draw(dl)

    def setup_drawing(self):
        if not self.has_gdata:
            self.draw_no_data()
            return
        self.normalize()
        self.setup_graph_measurements()
        if self.sort:
            self.sort_norm_data()
        self.draw_legend()
        self.draw_line_markers()
        self.draw_axis_labels()
        self.draw_title()

    # Make copy of data with values scaled between 0-100
    def normalize(self, force=False):
        if (self.norm_data is None) or force:
            self.norm_data = []
            if not self.has_gdata:
                return

            self.calculate_spread()

            for data_row in self.gdata:
                norm_data_points = []
                for data_point in data_row['values']:
                    if data_point is None:
                        norm_data_points.append(None)
                    else:
                        norm_data_points.append(((float(data_point) - \
                                float(self.minimum_value)) / self.spread))
                self.norm_data.append({'label': data_row['label'],
                                       'values': norm_data_points,
                                       'color': data_row['color']})

    def calculate_spread(self):
        self.spread = float(self.maximum_value) - float(self.minimum_value)
        if self.spread <= 0:
            self.spread = 1

    def calculate_caps_height(self, font_size):
        self.base_image.fontPointsize(font_size)
        tm = TypeMetric()
        self.base_image.fontTypeMetrics('X', tm)
        return tm.textHeight()

    def calculate_width(self, font_size, text):
        self.base_image.fontPointsize(font_size)
        tm = TypeMetric()
        self.base_image.fontTypeMetrics(str(text), tm)
        return tm.textWidth()

    def label(self, value):
        #if not self.marker_count:
        #    self.marker_count = 0
        if not self.spread:
            self.spread = 0
        # TODO: fixme
        if True:#(float(self.spread) % float(self.marker_count) == 0) or self.y_axis_increment is not None:
            glabel = str(int(value))
        elif self.spread > 10.0:
            glabel = "%0i" % value
        elif self.spread >= 3.0:
            glabel = "%0.2f" % value
        else:
            glabel = str(value)
        parts = glabel.split('.')
        #import re
        #parts[0] = re.subn("(\d)(?=(\d\d\d)+(?!\d))", "\\1%s" % THOUSAND_SEPARATOR, parts[0])
        return '.'.join(parts)

    def setup_graph_measurements(self):
        if self.hide_line_markers:
            self.marker_caps_height = 0
        else:
            self.marker_caps_height = self.calculate_caps_height(self.marker_font_size)
        if self.hide_title:
            self.title_caps_height = 0
        else:
            self.title_caps_height = self.calculate_caps_height(self.title_font_size)
        if self.hide_legend:
            self.legend_caps_height = 0
        else:
            self.legend_caps_height = self.calculate_caps_height(self.legend_font_size)

        if self.hide_line_markers:
            (self.graph_left, self.graph_right_margin, self.graph_bottom_margin) = \
                    [self.left_margin, self.right_margin, self.bottom_margin]
        else:
            longest_left_label_width = 0
            if self.has_left_labels:
                value = ""
                longest_value = None
                for memo in self.labels.values():
                    if len(str(value)) > len(str(memo)):
                        longest_value = value
                    else:
                        longest_value = memo
                        value = memo
                longest_left_label_width = self.calculate_width(
                        self.marker_font_size, longest_value) * 1.25
            else:
                longest_left_label_width = self.calculate_width(
                                             self.marker_font_size,
                                             self.label(float(self.maximum_value)))

            # Shift graph if left line numbers are hidden
            if self.hide_line_numbers and not self.has_left_labels:
                line_number_width = 0.0
            else:
                line_number_width = longest_left_label_width + LABEL_MARGIN * 2

            if self.y_axis_label is None:
                tmp = 0.0
            else:
                tmp = self.marker_caps_height + LABEL_MARGIN * 2
            self.graph_left = self.left_margin + line_number_width + tmp

            # Make space for half the width of the rightmost column label.
            # Might be greater than the number of columns if between-style bar
            # markers are used.
            tmp = self.labels.keys()
            tmp.sort()
            if len(tmp):
                last_label = int(tmp[-1])
            else:
                last_label = 0
            if last_label >= (self.column_count - 1) and \
               self.center_labels_over_point:
                extra_room_for_long_label = \
                        self.calculate_width(self.marker_font_size,
                                             self.labels[last_label]) / 2.0
            else:
                extra_room_for_long_label = 0
            self.graph_right_margin = self.right_margin + extra_room_for_long_label

            self.graph_bottom_margin = self.bottom_margin + self.marker_caps_height + LABEL_MARGIN

        self.graph_right = self.raw_columns - self.graph_right_margin
        self.graph_width = self.raw_columns - self.graph_left - self.graph_right_margin

        # When self.hide title, leave a title_margin space for aesthetics.
        # Same with self.hide_legend
        if self.hide_title:
            tmp = self.title_margin
        else:
            tmp = self.title_caps_height + self.title_margin
        if self.hide_legend:
            tmp += self.legend_margin
        else:
            tmp += self.legend_caps_height + self.legend_margin
        self.graph_top = self.top_margin + tmp

        if self.x_axis_label is None:
            x_axis_label_height = 0.0
        else:
            x_axis_label_height = self.marker_caps_height + LABEL_MARGIN
        self.graph_bottom = self.raw_rows - self.graph_bottom_margin - x_axis_label_height
        self.graph_height = self.graph_bottom - self.graph_top

    def draw(self):
        # TODO: not implement
        #if self.stacked:
        #    self.make_stacked()
        self.setup_drawing()

    def write(self, filename="graph.png"):
        """draw graph and save the graph image.
        """
        self.draw()
        self.base_image.write(filename)

    def display(self):
        """wrapper for :func:`pgmagick.Image.display`

        draw graph, and render graph.
        """
        self.draw()
        self.base_image.display()


class StackedMixin(object):
    """Stacked Graph Mix-in

    When you create new stacked graph object, mixed in this object::

        from gruffy.base import Base, StackedMixin

        class NewStackedGraph(Base, StackedMixin):
            pass
    """

    def get_maximum_by_stack(self):
        """get sum of each stack"""
        max_hash = {}
        for data_set in self.gdata:
            for i, data_point in enumerate(data_set['values']):
                if i not in max_hash:
                    max_hash[i] = 0.0
                max_hash[i] += float(data_point)
        for key in max_hash.keys():
            if max_hash[key] > self.maximum_value:
                self.maximum_value = max_hash[key]
            self.minimum_value = 0
