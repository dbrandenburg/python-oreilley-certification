#!/usr/local/bin/python3
"""This program takes a table of seperated keys and values and prints a histogram"""
class histogram:
    def __init__(self,table,resolution,y_axis_description_factor,max_value):
        self.resolution = resolution
        self.normalized_table = self.normalize(table,resolution)
        self.max_value = max_value
        self.normalized_max_value = max([y[1] for y in self.normalized_table])
        self.resolution = resolution
        self.y_axis_description_factor = y_axis_description_factor
        
        y_axis = self.generate_y_scale(self.max_value,self.resolution,self.y_axis_description_factor)
        graph = self.generate_graph(self.normalized_table,self.max_value,self.resolution)
        self.print_histogram(y_axis,graph)
        self.x_axis(self.normalized_table, self.max_value)
                
    def normalize(self,table,resolution):
        normalized_table = []
        for index,row in table:
            normalized_table.append((index,int(row/resolution)))
        return normalized_table
        
    def generate_graph(self,normalized_table,max_value,resolution):
        graph = []
        for v in normalized_table:
            column = []
            for i in range(max_value,1,-resolution):
                if v[1] >= int(i/resolution):
                    column.append(3 * '*')
                else:
                    column.append(3 * ' ')
            graph.append(column)
        return graph

    def generate_y_scale(self,max_value,resolution,y_axis_description_factor):
        max_value = max_value - (max_value % resolution)
        y_axis_line = []
        y_axis_description = []
        
        for i in range(max_value,1,-resolution):
            y_axis_line.append('|')
            if (i % (y_axis_description_factor * resolution)) == 0:
                spacing =  len(str(max_value)) - len(str(i))
                y_axis_description.append(' ' * spacing + str(i) + ' -')
            else:
                y_axis_description.append(' ' * (len(str(max_value)) + 2) )
                
        y_axis = []
        y_axis.append(y_axis_description)
        y_axis.append(y_axis_line)
        return y_axis
    
    def x_axis(self, normalized_table, max_value):
        padding_left = len(str(max_value))
        x_axis_values = [x[0] for x in normalized_table]
        zero_prefix = str((padding_left -1) * ' ' + '0 -+')
        x_axis_line = str(len(x_axis_values) * '-+-')
        print(zero_prefix + x_axis_line)
        x_axis_value = "".join(str("{0:^3}".format(x)) for x in x_axis_values)
        x_axis_padding = ((padding_left -1) * ' ' + '    ')
        print(x_axis_padding + x_axis_value)
    
    def print_histogram(self,y_axis,graph):
        zipped = list(zip(*(y_axis + graph)))
        for i in zipped:
            print(''.join(i))
        