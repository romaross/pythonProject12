import classess
from random import randint as rnd


def main_func():
    """ Test function """
    obj_list = []
    for _ in range(100):
        magic_num = rnd(1, 3)
        if 1 == magic_num:
            obj_list.append(classess.Circle(
                classess.Point(rnd(10, 300), rnd(10, 300)), rnd(10, 90)))
        elif 2 == magic_num:
            obj_list.append(classess.Triangle(
                classess.Point(rnd(10, 400), rnd(10, 400)),
                classess.Point(rnd(10, 400), rnd(10, 400)),
                classess.Point(rnd(10, 400), rnd(10, 400))
            ))
        elif 3 == magic_num:
            obj_list.append(classess.Square(
                classess.Point(rnd(10, 400), rnd(10, 400)),
                classess.Point(rnd(10, 400), rnd(10, 400))))

    values_len = []
    values_square = []
    for obj_i in obj_list:
        values_len.append(obj_i.length())
        values_square.append(obj_i.square())
        figure_s = ''
        if isinstance(obj_i, classess.Circle):
            figure_s = 'circle  '
        elif isinstance(obj_i, classess.Triangle):
            figure_s = 'triangle'
        elif isinstance(obj_i, classess.Square):
            figure_s = 'square  '
        print(' {} L= {:8.2f} & S= {:8.2f}'.format(figure_s, obj_i.length(), obj_i.square()))

    # Test begin
    for obj_i in obj_list:
        my_vec = classess.Point(rnd(10, 30), rnd(15, 35))
        obj_i.add_vec(my_vec)

    for index, obj_i in enumerate(obj_list):
        if obj_i.length() != values_len[index]:
            print('No pass length')
        if obj_i.square() != values_square[index]:
            print('No pass square')
    # Test end

    # app = QApplication([])
    # _ = Window(obj_list)
    # app.exec()


if __name__ == '__main__':
    main_func()