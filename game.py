import pygame
pygame.init() 

screen_width = 1000 
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("THE FARMER") 
background = pygame.image.load("배경이미지.png")
background=pygame.transform.scale(background,(1000,300))
clock=pygame.time.Clock()

#이미지 로딩 및 크기 변경
store=pygame.image.load("상점.png")
store=pygame.transform.scale(store,(1000,1000))

player=pygame.image.load("농부.png") 
player=pygame.transform.scale(player,(100,100))

path1=pygame.image.load("표지판1.png")
path1=pygame.transform.scale(path1,(100,100))
path2=pygame.image.load("표지판2.png")
path2=pygame.transform.scale(path2,(100,100))
path3=pygame.image.load("표지판3.png")
path3=pygame.transform.scale(path3,(100,100))

ground1=pygame.image.load("ground.png")   
ground1=pygame.transform.scale(ground1,(100,100))
ground2=pygame.image.load("ground.png")   
ground2=pygame.transform.scale(ground2,(100,100))
ground3=pygame.image.load("ground.png")   
ground3=pygame.transform.scale(ground3,(100,100))

plant1=pygame.image.load("plant1.png")  
plant1=pygame.transform.scale(plant1,(100,100))
plant2=pygame.image.load("plant2.png") 
plant2=pygame.transform.scale(plant2,(100,100))
plant3=pygame.image.load("plant3.png")
plant3=pygame.transform.scale(plant3,(100,100))

splant1=pygame.image.load("splant1.png")
splant1=pygame.transform.scale(splant1,(100,100))
splant2=pygame.image.load("splant2.png")
splant2=pygame.transform.scale(splant2,(100,100))
splant3=pygame.image.load("splant3.png")
splant3=pygame.transform.scale(splant3,(100,100))

gplant1=pygame.image.load("gplant1.png")
gplant1=pygame.transform.scale(gplant1,(100,100))
gplant2=pygame.image.load("gplant2.png")
gplant2=pygame.transform.scale(gplant2,(100,100))
gplant3=pygame.image.load("gplant3.png")
gplant3=pygame.transform.scale(gplant3,(100,100))

ending=pygame.image.load("ending.png")
ending=pygame.transform.scale(ending,(1000,1000))

#이미지의 Rect 정보를 저장
player_Rect=player.get_rect()
store_Rect=store.get_rect()
background_Rect=background.get_rect()
ground1_Rect=ground1.get_rect()
ground2_Rect=ground2.get_rect()
ground3_Rect=ground3.get_rect()

path1_Rect=path1.get_rect()
path2_Rect=path2.get_rect()
path3_Rect=path3.get_rect()

plant1_Rect=plant1.get_rect()
plant2_Rect=plant2.get_rect()
plant3_Rect=plant3.get_rect()

splant1_Rect=splant1.get_rect()
splant2_Rect=splant2.get_rect()
splant3_Rect=splant3.get_rect()

gplant1_Rect=gplant1.get_rect()
gplant2_Rect=gplant2.get_rect()
gplant3_Rect=gplant3.get_rect()

ending_Rect=ending.get_rect()


ground1_Rect.x=100
ground1_Rect.y=500
ground2_Rect.x=400
ground2_Rect.y=500
ground3_Rect.x=800
ground3_Rect.y=500

path1_Rect.x=100
path1_Rect.y=400
path2_Rect.x=400
path2_Rect.y=400
path3_Rect.x=800
path3_Rect.y=400

plant1_Rect.x=1500
plant1_Rect.y=1500
plant2_Rect.x=1500
plant2_Rect.y=1500
plant3_Rect.x=1500
plant3_Rect.y=1500

splant1_Rect.x=1500
splant1_Rect.y=1500
splant2_Rect.x=1500
splant2_Rect.y=1500
splant3_Rect.x=1500
splant3_Rect.y=1500

gplant1_Rect.x=1500
gplant1_Rect.y=1500
gplant2_Rect.x=1500
gplant2_Rect.y=1500
gplant3_Rect.x=1500
gplant3_Rect.y=1500

store_Rect.x=1500
store_Rect.y=1500
background_Rect.x=0
background_Rect.y=0
ending_Rect.x=1500
ending_Rect.y=1500

player_Rect.centerx=round(screen_width/2)  #플레이어 초기위치
player_Rect.centery=round(screen_height/2)


dx=0
dy=0
a=0  #작물생장
b=0
c=0
q=0  #상점열리는거

                
class HUD_coin(pygame.sprite.Sprite):
     def __init__(self, x, y):
         self.stage_0_img = pygame.image.load('coin.png')
         
         pygame.sprite.Sprite.__init__(self)
         self.image = self.stage_0_img    
         self.rect = self.image.get_rect()                               
         self.rect.topleft = x,y
         
class HUD_water(pygame.sprite.Sprite):
     def __init__(self, x, y):
         self.stage_1_img = pygame.image.load('water.png')
         
         pygame.sprite.Sprite.__init__(self)
         self.image = self.stage_1_img    
         self.rect = self.image.get_rect()                                           
         self.rect.topleft = x,y
         
class HUD_seed1(pygame.sprite.Sprite):
     def __init__(self, x, y):
         self.stage_2_img = pygame.image.load('seed1.png')
         
         pygame.sprite.Sprite.__init__(self)
         self.image = self.stage_2_img     
         self.rect = self.image.get_rect()                                           
         self.rect.topleft = x,y
         
class HUD_seed2(pygame.sprite.Sprite):
     def __init__(self, x, y):
         self.stage_3_img = pygame.image.load('seed2.png')
         
         pygame.sprite.Sprite.__init__(self)
         self.image = self.stage_3_img    
         self.rect = self.image.get_rect()                                          
         self.rect.topleft = x,y
         
class HUD_seed3(pygame.sprite.Sprite):
     def __init__(self, x, y):
         self.stage_4_img = pygame.image.load('seed3.png')
         
         pygame.sprite.Sprite.__init__(self)
         self.image = self.stage_4_img   
         self.rect = self.image.get_rect()                                            
         self.rect.topleft = x,y   

       
object_list =pygame.sprite.Group()  
coin_png =HUD_coin(500,880)
object_list.add(coin_png)
water_png = HUD_water(600,880)
object_list.add(water_png)
seed1_png =HUD_seed1(700,880)
object_list.add(seed1_png)
seed2_png = HUD_seed2(800,880)
object_list.add(seed2_png)
seed3_png =HUD_seed3(900,880)
object_list.add(seed3_png)

font_test= pygame.font.SysFont(None,30)

coin=100
water =100
seed1=1
seed2=0
seed3=0

    
running = True
while running:
    for event in pygame.event.get(): # running 중 키보드나,마우스 입력값(이벤트)을 체크해주는것
        
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는지
            running = False # 게임이 진행중이 아님
        
        if event.type ==pygame.KEYDOWN:
            
            if event.key==pygame.K_LEFT:
               dx =-5
            if event.key==pygame.K_RIGHT:
                dx =5
            if event.key==pygame.K_UP:
               dy =-5
            if event.key==pygame.K_DOWN:
               dy=5
            if  event.key==pygame.K_p:  #상점열리는
                q = 1
                store_Rect.x=0
                store_Rect.y=0
            if  event.key==pygame.K_z:   #상점닫히는
                q=0
                store_Rect.x=1500
                store_Rect.y=1500
                
            if q==1:  #상점구매  엔딩여기에
                if event.key==pygame.K_1: #눌린 키가 0일때=(소)씨앗
                     if coin>= 10:
                          seed1+=1
                          coin-=10
                        
                if event.key==pygame.K_2:#눌린 키가 0일때=(소)씨앗
                    if coin>= 10:
                        seed2+=1
                        coin-=100
                        
                if event.key==pygame.K_3: #눌린 키가 0일때=(소)씨앗
                    if coin>= 10:
                        seed3+=1
                        coin-=1000
                        
                if event.key==pygame.K_e:  #엔딩구매
                    if coin>= 10000:
                       ending_Rect.x=0
                       ending_Rect.y=0
                if event.key==pygame.K_r:      
                        if coin>= 100:
                            water =100
                            coin-=100
                            
            if player_Rect.x<150 and player_Rect.x>50 and player_Rect.y<550 and player_Rect.y>450:   #1번씨앗심는땅
                if event.type ==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        if seed1 !=-1   :
                            if water!=0:
                                a+=1
                                water-=1
                            
            if player_Rect.x<450 and player_Rect.x>350 and player_Rect.y<550 and player_Rect.y>450:
                 if event.type ==pygame.KEYDOWN:
                     if event.key==pygame.K_SPACE:
                         if seed2 !=-1:
                             if water!=0:
                                 b+=1
                                 water-=1
            if player_Rect.x<850 and player_Rect.x>750 and player_Rect.y<550 and player_Rect.y>450:
                 if event.type ==pygame.KEYDOWN:
                     if event.key==pygame.K_SPACE:
                         if seed3 !=-1:
                             if water!=0:
                                 c+=1
                                 water-=1
                             
        if event.type ==pygame.KEYUP:
            
            if event.key==pygame.K_LEFT:
                dx =0
            if event.key==pygame.K_RIGHT:
                 dx =0
            if event.key==pygame.K_UP:
                dy =0
            if event.key==pygame.K_DOWN:
                 dy=0  
                 
            

              
    player_Rect.x+=dx
    player_Rect.y+=dy
    
    if player_Rect.left<0:
        player_Rect.left=0
    if player_Rect.right>screen_width:
        player_Rect.right=screen_height
    if player_Rect.top<0:
        player_Rect.top=0
    if player_Rect.bottom>screen_width:
        player_Rect.bottom=screen_height
    
    if a==1:   # 식물1 생장함수
        seed1-=1
        a=2
        ground1_Rect.x=1500
        ground1_Rect.y=1500
        plant1_Rect.x=100
        plant1_Rect.y=500
        
        
    elif a==3:
        plant1_Rect.x=1500
        plant1_Rect.y=1500
        plant2_Rect.x=100
        plant2_Rect.y=500
        
    
    elif a==5:
        plant2_Rect.x=1500
        plant2_Rect.y=1500
        plant3_Rect.x=100
        plant3_Rect.y=500
    
    elif a==7:
        a=0
        coin+=20
        plant3_Rect.x=1500
        plant3_Rect.y=1500
        ground1_Rect.x=100
        ground1_Rect.y=500
        
    if b==1:   # 식물2 생장함수
         seed2-=1
         b=2
         ground2_Rect.x=1500
         ground2_Rect.y=1500
         splant1_Rect.x=400
         splant1_Rect.y=500
         
         
    elif b==4:
         splant1_Rect.x=1500
         splant1_Rect.y=1500
         splant2_Rect.x=400
         splant2_Rect.y=500
         
     
    elif b==8:
         splant2_Rect.x=1500
         splant2_Rect.y=1500
         splant3_Rect.x=400
         splant3_Rect.y=500
     
    elif b==10:
         b=0
         coin+=200
         splant3_Rect.x=1500
         splant3_Rect.y=1500
         ground2_Rect.x=400
         ground2_Rect.y=500
         
    if c==1:   # 식물3 생장함수
         seed3-=1
         c=2
         ground1_Rect.x=1500
         ground1_Rect.y=1500
         gplant1_Rect.x=800
         gplant1_Rect.y=500
         
         
    elif c==5:
         gplant1_Rect.x=1500
         gplant1_Rect.y=1500
         gplant2_Rect.x=800
         gplant2_Rect.y=500
         
     
    elif c==10:
         gplant2_Rect.x=1500
         gplant2_Rect.y=1500
         gplant3_Rect.x=800
         gplant3_Rect.y=500
     
    elif c==15:
         c=0
         coin+=2000
         gplant3_Rect.x=1500
         gplant3_Rect.y=1500
         ground1_Rect.x=800
         ground1_Rect.y=500
        
    screen.fill((139, 0, 255)) #RGB형식으로 이미지 로드
#스크린의 원하는 좌표에 이미지 복사하기
    screen.blit(background, background_Rect)

    screen.blit(ground1, ground1_Rect)
    screen.blit(ground2, ground2_Rect)
    screen.blit(ground3, ground3_Rect)
    
    screen.blit(plant1, plant1_Rect)
    screen.blit(plant2, plant2_Rect)
    screen.blit(plant3, plant3_Rect)
    
    screen.blit(path1, path1_Rect)
    screen.blit(path2, path2_Rect)
    screen.blit(path3, path3_Rect)
    
    screen.blit(splant1, splant1_Rect)
    screen.blit(splant2, splant2_Rect)
    screen.blit(splant3, splant3_Rect)
    
    screen.blit(gplant1, gplant1_Rect)
    screen.blit(gplant2, gplant2_Rect)
    screen.blit(gplant3, gplant3_Rect)
    
    screen.blit(player, player_Rect)
    screen.blit(store, store_Rect)
    
    text_coin =font_test.render(str(coin), True,(0,0,0))     
    screen.blit(text_coin,(520,980))
    text_water =font_test.render(str(water), True,(0,0,0))     
    screen.blit(text_water,(630,980))
    text_maxwater =font_test.render("/100", True,(0,0,0))     
    screen.blit(text_maxwater,(660,980))
    text_seed1 =font_test.render(str(seed1), True,(0,0,0))     
    screen.blit(text_seed1,(750,980))
    text_seed2 =font_test.render(str(seed2), True,(0,0,0))     
    screen.blit(text_seed2,(850,980))
    text_seed3 =font_test.render(str(seed3), True,(0,0,0))     
    screen.blit(text_seed3,(950,980))
    
    for obj in object_list:
               screen.blit(obj.image,(obj.rect.x, obj.rect.y))
    screen.blit(ending, ending_Rect)
    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()


pygame.quit()