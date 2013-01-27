from gruffy.stacked_bar import StackedBar


class AccumulatorBar(StackedBar):
    """Accumulator Bar Graph Object

    A special bar graph that shows a single dataset as a set of
    stacked bars. The bottom bar shows the running total and
    the top bar shows the new value being added to the array.
    """

    def draw(self):
        if not self.has_gdata or len(self.gdata) != 1:
            return
        accumulator_array = []
        memo = []
        for index, value in enumerate(self.gdata[0]['values']):
            if index > 0:
                memo.append(value + max(memo))
            else:
                memo.append(value)
            accumulator_array.append(memo[index] - value)
        #increment_array = memo
        self.data("Accumulator", accumulator_array)
        self.sort = False
        self.gdata.reverse()
        AccumulatorBar.__base__.draw(self)
