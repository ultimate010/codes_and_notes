# coding:utf-8
'''
@Copyright:LintCode
@Author:   ultimate010
@Problem:  http://www.lintcode.com/problem/shape-factory
@Language: Python
@Datetime: 16-06-18 11:08
'''

"""
Your object will be instantiated and called as such:
sf = ShapeFactory()
shape = sf.getShape(shapeType)
shape.draw()
"""
class Shape:
    def draw(self):
        raise NotImplementedError('This method should have implemented.')

class Triangle(Shape):
    # Write your code here
    def draw(self):
        sh = '  /\ \n /  \ \n/____\ \n'
        print sh


class Rectangle(Shape):
    # Write your code here
    def draw(self):
        sh = ''' ---- 
|    |
 ----
        '''

        print sh


class Square(Shape):
    # Write your code here
    def draw(self):
        sh = ''' ----
|    |
|    |
 ----
        '''
        print sh

class ShapeFactory:
    # @param {string} shapeType a string
    # @return {Shape} Get object of type Shape
    def getShape(self, shapeType):
        # Write your code here
        if shapeType == 'Square':
            return Square()
        elif shapeType == 'Triangle':
            return Triangle()
        else:
            return Rectangle()