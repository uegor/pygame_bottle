from pygame import *
from settings import *

class Bottle:

    bottles = []

    def __init__(self,pos,win,colors):
        Bottle.bottles.append(self)
        self.colors = colors
        self.win = win

        self.rect = Rect(pos[0],pos[1],100,500)

        self.picked = False
        self.recalc_colors()
    
    def pick(self):
        self.picked = True

    def unpick(self):
        self.picked = False

    def recalc_colors(self):
        l = len(self.colors)
        for i in range(1,l):
            
            color_name = list(self.colors[i].keys())[0]
            if i+1 in self.colors:
                next_color_name = list(self.colors[i+1].keys())[0]
            else: return 0
            
            if color_name == next_color_name:
                self.colors[i][color_name] += self.colors[i+1][color_name]
            
                for j in range(i+1,len(self.colors)):
                    self.colors[j] = self.colors[j+1]

                del self.colors[len(self.colors)]
                l -= 1
                
    def move_top_to(self,aim):
        if len(self.colors) > 0:
            top_number_from = max(list(self.colors.keys()))
        else: 
            self.unpick()
            return 0

        if len(aim.colors) > 0:
            top_number_to = max(list(aim.colors.keys()))
            
        else: top_number_to = 0

        aim.colors[top_number_to+1] = self.colors[top_number_from]
        del self.colors[top_number_from]

        aim.recalc_colors()

        self.unpick()
        aim.unpick()

        return aim.check_result()

    def check_result(self):
        total_h = 0
        for num in self.colors:
            for color_name in self.colors[num]:
                total_h += self.colors[num][color_name]
        
        if total_h > self.rect.height: return "loose"
        else: return "ok"


    def draw(self):
        draw.rect(self.win, (0,0,0) ,self.rect, 5)
        if self.picked:
            draw.rect(self.win, (255,255,255) ,self.rect, 10)

        x = self.rect.x + 5
        y = self.rect.bottom - 5
        w = self.rect.w - 10

        for num in self.colors:
            for color_name in self.colors[num]:
                h = self.colors[num][color_name]
                y -= h
                color_rect = (x,y,w,h)
                
                draw.rect(self.win, colors_codes[color_name] ,color_rect)
                draw.rect(self.win, (0,0,0) ,color_rect, 1)