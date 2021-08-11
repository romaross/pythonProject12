import classess
from random import randint as rnd


def main_func():
    """ Test function """
    obj_list = []
    for _ in range(100):
        magic_num = rnd(1, 3)
        if 1 == magic_num:
            obj_list.append(classess.Circle(
                classess.Point(rnd(-100, 100), rnd(-100, 100)), rnd(1, 10)))
        elif 2 == magic_num:
            obj_list.append(classess.Triangle(
                classess.Point(rnd(-100, 100), rnd(-100, 100)),
                classess.Point(rnd(-100, 100), rnd(-100, 100)),
                classess.Point(rnd(-100, 100), rnd(-100, 100))
            ))
        elif 3 == magic_num:
            obj_list.append(classess.Square(
                            classess.Point(rnd(-100, 100), rnd(-100, 100)),
                            classess.Point(rnd(-100, 100), rnd(-100, 100))))

    for obj_i in obj_list:
        figure_s = ''
        if isinstance(obj_i, classess.Circle):
            figure_s = 'circle '
        elif isinstance(obj_i, classess.Triangle):
            figure_s = 'triangle '
        elif isinstance(obj_i, classess.Square):
            figure_s = 'square '
        print(' {} L= {:.2f} & S= {:.2f}'.format(figure_s, obj_i.length(), obj_i.square()))


if __name__ == '__main__':
    main_func()