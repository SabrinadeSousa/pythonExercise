from graphics import *


class Formas:

    def triangulo(self, pse, pid, corLinha, corFundo, win):
        ret = Rectangle(pse, pid)
        ret.setOutline('red')
        ret.draw(win)

        p1 = Point(pse.getX() + (pid.getX() - pse.getX()) / 2, pse.getY())
        p2 = pid
        p3 = Point(pse.getX(), pid.getY())

        tri = Polygon(p1, p2, p3)
        tri.setOutline(corLinha)
        tri.setFill(corFundo)
        tri.draw(win)

    def losango(self, pse, pid, corLinha, corFundo, win):
        ret = Rectangle(pse, pid)
        ret.setOutline('red')
        ret.draw(win)

        p1 = Point(pse.getX() + (pid.getX() - pse.getX()) / 2, pse.getY())
        p2 = Point(pid.getX(), pse.getY() + (pid.getY() - pse.getY()) / 2)
        p3 = Point(pse.getX() + (pid.getX() - pse.getX()) / 2, pid.getY())
        p4 = Point(pse.getX(), pse.getY() + (pid.getY() - pse.getY()) / 2)

        los = Polygon(p1, p2, p3, p4)
        los.setOutline(corLinha)
        los.setFill(corFundo)
        los.draw(win)


        return
