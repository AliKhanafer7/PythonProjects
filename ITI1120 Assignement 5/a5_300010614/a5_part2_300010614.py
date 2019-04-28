class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle:

    def __init__(self,bottom_left_corner,top_right_corner,color):
        '''(Rectangle,Point,Point,str)->None'''
        self.left=bottom_left_corner
        self.right=top_right_corner
        self.col=color

    def __repr__(self):
        '''(Rectangle)->str'''
        return 'Rectangle(' + str(self.left) + ', ' + str(self.right) + ', \'' + str(self.col) + "\')"

    def __eq__(self,rectangle2):
        '''(Rectangle,Rectangle)->bool '''
        return self.left==rectangle2.left and self.right==rectangle2.right and self.col==rectangle2.col
    def __str__(self):
        '''(Rectangle)->string '''
        return 'I am a ' + self.col + ' rectangle with bottom left corner at ' + str(self.left.get()) + ' and top right corner at ' + str(self.right.get()) + '.'
    
    def get_color(self):
        '''(Rectangle)->str ''' 
        return self.col
    
    def get_bottom_left(self):
        '''(Rectangle)->Point '''
        return self.left
    
    def get_top_right(self):
        '''(Rectangle)->Point'''
        return self.right

    def get_perimeter(self):
        '''(Rectangle)->Number'''
        return ((self.right.x-self.left.x)*2)+((self.right.y-self.left.y)*2)

    def get_area(self):
        '''(Rectangle)->Number'''
        return (self.right.x-self.left.x)*(self.right.y-self.left.y)
    def reset_color(self,new_color):
        '''(Rectangle,str)->None'''
        self.col=new_color
        
    def move(self,dx,dy):
        '''(Rectangle,Number,Number)->None'''
        self.left.move(dx,dy)
        self.right.move(dx,dy)
        
    def intersects(self,rectangle2):
        '''(Rectangle,Rectangle)->bool'''
        if self.right.x<rectangle2.left.x or self.right.y<rectangle2.left.y:
            return False
        elif rectangle2.right.x<self.left.x or rectangle2.right.y<self.left.y:
            return False
        else:
            return True
    
    def contains(self,x,y):
        '''(Rectangle,Number,Number)->bool'''
        if self.left.x<=x<=self.right.x and self.left.y<=y<=self.right.y:
            return True
        else:
            return False

        
        
class Canvas:

    def __init__(self):
        '''(Canvas)->None'''
        self.lst=[]

    def __len__(self):
        '''(Canvas)->int'''
        return len(self.lst)

    def __repr__(self):
        '''(Canvas)->str'''
        return 'Canvas(' + str(self.lst) + ')'

    def add_one_rectangle(self,rectangle):
        '''(Canvas,Rectangle)->None'''
        self.lst.append(rectangle)

    def count_same_color(self,color):
        '''(Canvas,str)->int'''
        accumilator=0
        for rectangle in self.lst:
            if rectangle.col==color:
                accumilator +=1
        return accumilator
    
    def total_perimeter(self):
        '''(Canvas)->Number'''
        perimeter=0
        for rectangle in self.lst:
            perimeter += rectangle.get_perimeter()
        return perimeter

    def min_enclosing_rectangle(self):
        '''(Canvas)->Rectangle'''
        all_x=[]
        all_y=[]
        for rectangle in self.lst:
            all_x.append(rectangle.left.x)
            all_x.append(rectangle.right.x)
            all_y.append(rectangle.left.y)
            all_y.append(rectangle.right.y)
        return Rectangle(Point(min(all_x),min(all_y)),Point(max(all_x),max(all_y)),'red')

    def common_point(self):
        '''(Canvas)->bool'''
        for i in self.lst:
            for j in self.lst:
                if not i.intersects(j):
                    return False
        return True
