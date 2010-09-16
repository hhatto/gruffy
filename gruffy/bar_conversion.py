class BarConversion(object):
    mode = None
    zero = None
    graph_top = None
    graph_height = None
    minimum_value = None
    spread = None

    def getLeftYRightYscaled(self, data_point):
        result = [None, None]
        if self.mode == 1:
            # minimum value >= 0 ( only positiv values )
            result[0] = self.graph_top + \
                            self.graph_height * (1 - data_point) + 1
            result[1] = self.graph_top + self.graph_height - 1
        elif self.mode == 2:
            # only negativ values
            result[0] = self.graph_top + 1
            result[1] = self.graph_top + \
                            self.graph_height * (1 - data_point) - 1
        elif self.mode == 3:
            # positiv and negativ values
            val = data_point - self.minimum_value / self.spread
            if data_point >= self.zero:
                result[0] = self.graph_top + \
                                self.graph_height * (1 - (val - self.zero)) + 1
                result[1] = self.graph_top + \
                                self.graph_height * (1 - self.zero) - 1
            else:
                result[0] = self.graph_top + \
                                self.graph_height * (1 - (val - self.zero)) + 1
                result[1] = self.graph_top + \
                                self.graph_height * (1 - self.zero) - 1
        else:
            result[0] = 0.0
            result[1] = 0.0
        return result
