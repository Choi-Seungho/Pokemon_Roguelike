import random
import time
from ursina import *
from Player import Player
from Tile import Tile

class Map:
    Map_makingTime=0
    Map_size=0
    Map_map=None
    Map_mapList=None
    Map_exitWay=None
    startPoint_x=1
    startPoint_y=0
    endPoint_x=0
    endPoint_y=0

    def __init__(self,input_size, p):
        list_Map=list()
        self.player = p
        for i in range(input_size):
            list_Map.append(list())
            for j in range(input_size):
                list_Map[i].append(1)
        self.Map_map=list_Map
        self.Map_size=int(input_size)
        self.entity = [[0 for col in range(self.Map_size)] for row in range(self.Map_size)]

        self.creat_map()
        self.duplicate_MapToList()

    def creat_map(self):
        temp_way=list()
        self.Map_map[self.startPoint_y][self.startPoint_x]=0
        temp_x,temp_y=self.startPoint_x,self.startPoint_y+1
        temp_prevDir=4
        temp_way.append(temp_prevDir)
        self.Map_map[temp_y][temp_x]=0

        while True:
            int_exit_select=random.randint(1,4)
            if temp_x==0 or temp_y==0 or temp_x==self.Map_size-1 or temp_y==self.Map_size-1:
                break
            elif temp_prevDir==3:
                if int_exit_select<3:
                    temp_x+=1
                    temp_prevDir=3
                    temp_way.append(temp_prevDir)
                    self.Map_map[temp_y][temp_x]=0
                else:
                    temp_y+=1
                    temp_prevDir=4
                    temp_way.append(temp_prevDir)
                    self.Map_map[temp_y][temp_x]=0

            elif temp_prevDir==4:
                if int_exit_select<3:
                    temp_y+=1
                    temp_prevDir=4
                    temp_way.append(temp_prevDir)
                    self.Map_map[temp_y][temp_x]=0
                else:
                    temp_x+=1
                    temp_prevDir=3
                    temp_way.append(temp_prevDir)
                    self.Map_map[temp_y][temp_x]=0

        self.Map_exitWay=temp_way
        self.endPoint_x,self.endPoint_y=temp_x,temp_y
        temp_x,temp_y=self.startPoint_x,self.startPoint_y

        for temp_prev in temp_way:
            if temp_prev==4:
                self.randomspace(temp_x-1,temp_y,1)
                self.randomspace(temp_x+1,temp_y,3)
                temp_y+=1
            else:
                self.randomspace(temp_x,temp_y-1,2)
                self.randomspace(temp_x,temp_y+1,4)
                temp_x+=1

    def duplicate_MapToList(self):
        self.Map_mapList=list()
        for i,line in enumerate(self.Map_map):
            self.Map_mapList.append(list())
            for line_ele in line:
                self.Map_mapList[i].append(line_ele)

    def randomspace(self,point_x,point_y,prev):
        if  point_x==0 or point_y==0 or point_x==self.Map_size-1 or point_y==self.Map_size-1:
            return

        int_select=random.randint(1,10)

        if prev==1:
            if self.Map_map[point_y-1][point_x]==1 and self.Map_map[point_y+1][point_x]==1 and self.Map_map[point_y][point_x-1]==1:
                if int_select<8:
                    self.Map_map[point_y][point_x]=0
                    self.randomspace(point_x-1,point_y,1)
                    self.randomspace(point_x,point_y-1,2)
                    self.randomspace(point_x,point_y+1,4)
        elif prev==2:
            if self.Map_map[point_y-1][point_x]==1 and self.Map_map[point_y][point_x-1]==1 and self.Map_map[point_y][point_x+1]==1:
                if int_select<8:
                    self.Map_map[point_y][point_x]=0
                    self.randomspace(point_x-1,point_y,1)
                    self.randomspace(point_x,point_y-1,2)
                    self.randomspace(point_x+1,point_y,3)
        elif prev==3:
            if self.Map_map[point_y-1][point_x]==1 and self.Map_map[point_y+1][point_x]==1 and self.Map_map[point_y][point_x+1]==1:
                if int_select<8:
                    self.Map_map[point_y][point_x]=0
                    self.randomspace(point_x+1,point_y,3)
                    self.randomspace(point_x,point_y-1,2)
                    self.randomspace(point_x,point_y+1,4)
        else:
            if self.Map_map[point_y+1][point_x]==1 and self.Map_map[point_y][point_x-1]==1 and self.Map_map[point_y][point_x+1]==1:
                if int_select<8:
                    self.Map_map[point_y][point_x]=0
                    self.randomspace(point_x-1,point_y,1)
                    self.randomspace(point_x+1,point_y,3)
                    self.randomspace(point_x,point_y+1,4)

    def set_MapLine(self):
        check_road = [[0 for col in range(self.Map_size)] for row in range(self.Map_size)]
        Entity_SCALE = (0.32, 0.32)
        for temp_x in range(self.Map_size):
            for temp_y in range(self.Map_size):
                Entity_POSITION = (1 + (temp_x * 0.32), 0 - (temp_y * 0.32))
                check_road[temp_y][temp_x] = [0] * 8
                if self.Map_mapList[temp_y][temp_x]==0:
                    if temp_y-1>=0:
                        if self.Map_mapList[temp_y-1][temp_x]==0:
                            check_road[temp_y][temp_x][1] = 1
                    if temp_x-1>=0:
                        if self.Map_mapList[temp_y][temp_x-1]==0: 
                            check_road[temp_y][temp_x][2] = 1
                    if temp_y+1<=self.Map_size-1:
                        if self.Map_mapList[temp_y+1][temp_x]==0:
                            check_road[temp_y][temp_x][4] = 1
                    if temp_x+1<=self.Map_size-1:
                        if self.Map_mapList[temp_y][temp_x+1]==0:
                            check_road[temp_y][temp_x][5] = 1

                        # [0,1,0,0,0,0,0,0] = 1
                        # [0,1,0,0,1,0,0,0] = 2
                        # [0,0,0,0,1,0,0,0] = 3
                        # [0,0,0,0,1,1,0,0] = 4
                        # [0,0,1,0,1,0,0,0] = 5
                        # [0,1,0,0,0,1,0,0] = 6
                        # [0,1,1,0,0,0,0,0] = 7
                        # [0,0,1,0,0,1,0,0] = 8
                        # [0,0,1,0,1,1,0,0] = 9
                        # [0,1,1,0,0,1,0,0] = 10
                        # [0,1,1,0,1,1,0,0] = 11
                        # [0,0,0,0,0,1,0,0] = 12
                        # [0,0,1,0,0,0,0,0] = 13
                        # [0,1,1,0,1,0,0,0] = 14
                        # [0,1,0,0,1,1,0,0] = 15
                if self.Map_mapList[temp_y][temp_x] == 1:
                    self.Map_map[temp_y][temp_x]="0"
                    self.entity[temp_y][temp_x] = Tile(model = 'quad', texture = './resources/sprites/water_tile_5.png', p=self.player,
                                                            scale = Entity_SCALE, position = Entity_POSITION, highlight_color=color.red)
                if check_road[temp_y][temp_x] == [0,1,0,0,0,0,0,0]:
                    self.Map_map[temp_y][temp_x]="1"
                    self.entity[temp_y][temp_x] = Tile(model = 'quad', texture = './resources/sprites/road_tile_1.png', p=self.player,
                                                            scale = Entity_SCALE, position = Entity_POSITION)
                elif check_road[temp_y][temp_x] == [0,1,0,0,1,0,0,0]:
                    self.Map_map[temp_y][temp_x]="1"
                    self.entity[temp_y][temp_x] = Tile(model = 'quad', texture = './resources/sprites/road_tile_2.png', p=self.player,
                                                            scale = Entity_SCALE, position = Entity_POSITION)
                elif check_road[temp_y][temp_x] == [0,0,0,0,1,0,0,0]:
                    self.Map_map[temp_y][temp_x]="1"
                    self.entity[temp_y][temp_x] = Tile(model = 'quad', texture = './resources/sprites/road_tile_3.png', p=self.player,
                                                            scale = Entity_SCALE, position = Entity_POSITION)
                elif check_road[temp_y][temp_x] == [0,0,0,0,1,1,0,0]:
                    self.Map_map[temp_y][temp_x]="1"
                    self.entity[temp_y][temp_x] = Tile(model = 'quad', texture = './resources/sprites/road_tile_4.png', p=self.player,
                                                            scale = Entity_SCALE, position = Entity_POSITION)
                elif check_road[temp_y][temp_x] == [0,0,1,0,1,0,0,0]:
                    self.Map_map[temp_y][temp_x]="1"
                    self.entity[temp_y][temp_x] = Tile(model = 'quad', texture = './resources/sprites/road_tile_5.png', p=self.player,
                                                            scale = Entity_SCALE, position = Entity_POSITION)
                elif check_road[temp_y][temp_x] == [0,1,0,0,0,1,0,0]:
                    self.Map_map[temp_y][temp_x]="1"
                    self.entity[temp_y][temp_x] = Tile(model = 'quad', texture = './resources/sprites/road_tile_6.png', p=self.player,
                                                            scale = Entity_SCALE, position = Entity_POSITION)
                elif check_road[temp_y][temp_x] == [0,1,1,0,0,0,0,0]:
                    self.Map_map[temp_y][temp_x]="1"
                    self.entity[temp_y][temp_x] = Tile(model = 'quad', texture = './resources/sprites/road_tile_7.png', p=self.player,
                                                            scale = Entity_SCALE, position = Entity_POSITION)
                elif check_road[temp_y][temp_x] == [0,0,1,0,0,1,0,0]:
                    self.Map_map[temp_y][temp_x]="1"
                    self.entity[temp_y][temp_x] = Tile(model = 'quad', texture = './resources/sprites/road_tile_8.png', p=self.player,
                                                            scale = Entity_SCALE, position = Entity_POSITION)
                elif check_road[temp_y][temp_x] == [0,0,1,0,1,1,0,0]:
                    self.Map_map[temp_y][temp_x]="1"
                    self.entity[temp_y][temp_x] = Tile(model = 'quad', texture = './resources/sprites/road_tile_9.png', p=self.player,
                                                            scale = Entity_SCALE, position = Entity_POSITION)
                elif check_road[temp_y][temp_x] == [0,1,1,0,0,1,0,0]:
                    self.Map_map[temp_y][temp_x]="1"
                    self.entity[temp_y][temp_x] = Tile(model = 'quad', texture = './resources/sprites/road_tile_10.png', p=self.player,
                                                            scale = Entity_SCALE, position = Entity_POSITION)
                elif check_road[temp_y][temp_x] == [0,1,1,0,1,1,0,0]:
                    self.Map_map[temp_y][temp_x]="1"
                    self.entity[temp_y][temp_x] = Tile(model = 'quad', texture = './resources/sprites/road_tile_11.png', p=self.player,
                                                            scale = Entity_SCALE, position = Entity_POSITION)
                elif check_road[temp_y][temp_x] == [0,0,0,0,0,1,0,0]:
                    self.Map_map[temp_y][temp_x]="1"
                    self.entity[temp_y][temp_x] = Tile(model = 'quad', texture = './resources/sprites/road_tile_12.png', p=self.player,
                                                            scale = Entity_SCALE, position = Entity_POSITION)
                elif check_road[temp_y][temp_x] == [0,0,1,0,0,0,0,0]:
                    self.Map_map[temp_y][temp_x]="1"
                    self.entity[temp_y][temp_x] = Tile(model = 'quad', texture = './resources/sprites/road_tile_13.png', p=self.player,
                                                            scale = Entity_SCALE, position = Entity_POSITION)
                elif check_road[temp_y][temp_x] == [0,1,1,0,1,0,0,0]:
                    self.Map_map[temp_y][temp_x]="1"
                    self.entity[temp_y][temp_x] = Tile(model = 'quad', texture = './resources/sprites/road_tile_14.png', p=self.player,
                                                            scale = Entity_SCALE, position = Entity_POSITION)
                elif check_road[temp_y][temp_x] == [0,1,0,0,1,1,0,0]:
                    self.Map_map[temp_y][temp_x]="1"
                    self.entity[temp_y][temp_x] = Tile(model = 'quad', texture = './resources/sprites/road_tile_15.png', p=self.player,
                                                            scale = Entity_SCALE, position = Entity_POSITION)


    def set_MapSquare(self):
        for temp_x in range(self.Map_size):
            for temp_y in range(self.Map_size):
                if self.Map_mapList[temp_y][temp_x]==0:
                    self.Map_map[temp_y][temp_x]=" "
                else:
                    self.Map_map[temp_y][temp_x]="◼︎"
        self.Map_map[self.startPoint_y][self.startPoint_x]="#︎"

    def print_Map(self,mode=0):
        t_start=time.time()
        if mode==0:
            self.set_MapLine()
        elif mode==1:
            print()
        else:
            self.set_MapSquare()
        t_end=time.time()
        for line in self.Map_map:
            for temp_char in line:
                print(temp_char,end="")
            print("")
        return t_end-t_start

    def save_txtMap(self,mode=0):
        if mode==0:
            self.set_MapLine()
        else:
            self.set_MapSquare()
        f_Map=open("Map.txt","w")
        for line in self.Map_map:
            for temp_char in line:
                f_Map.write(temp_char)
            f_Map.write("\n")
if __name__ == '__main__':
    import sys
    window.borderless = False
    app = Ursina()
    sys.setrecursionlimit(2000)
    Map_size=10
    p = Player()
    
    m_test=Map(input_size=Map_size, p=p)
    m_test.set_MapLine()
    p.x = m_test.entity[0][1].x
    p.y = m_test.entity[0][1].y

    app.run()