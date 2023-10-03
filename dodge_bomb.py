import random
import sys
import pygame as pg

WIDTH, HEIGHT = 1600, 900
delta = {  # 練習３：移動量辞書
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
}

#kakudo=[[225,270,0],[180,0,315],[135,90,45]]
def check_bount(obj_rct):
    """
    引数：こうかとんorばくだんrect
    """
    yoko,tate=True,True
    if obj_rct.left < 0 or WIDTH < obj_rct.right: #横方向判定
        yoko=False
    if obj_rct.top <0 or HEIGHT < obj_rct.bottom:
        tate=False
    return yoko,tate
    
def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    """こうかとん"""
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img_tr=pg.transform.flip(kk_img,False,True)
    kk_img1 = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_img2 = pg.transform.rotozoom(kk_img,315, 2.0)
    kk_img3 = pg.transform.rotozoom(kk_img_tr,-90 , 2.0)
    kk_img4 = pg.transform.rotozoom(kk_img_tr,225 , 2.0)
    kk_img5 = pg.transform.rotozoom(kk_img_tr,180 , 2.0)
    kk_img6 = pg.transform.rotozoom(kk_img_tr,135, 2.0)
    kk_img7 = pg.transform.rotozoom(kk_img_tr,-270, 2.0)
    kk_img8 = pg.transform.rotozoom(kk_img,45, 2.0)
    kk_dct = {(-5,0):kk_img1,(-5,-5) :kk_img2,(0,-5): kk_img3, (5,-5):kk_img4,(5,0): kk_img5, (5,5):kk_img6, (0,5):kk_img7,(-5,5): kk_img8 }
    kk_rct = kk_img.get_rect()
    kk_rct.center = (900, 400)  # 練習３：こうかとんの初期座標を設定する
    """ばくだん"""
    bd_img = pg.Surface((20, 20))  # 練習１：爆弾Surfaceを作成する
    bd_img.set_colorkey((0, 0, 0))  # 練習１：黒い部分を透明にする
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)
    bd_rct = bd_img.get_rect()  # 練習１：SurfaceからRectを抽出する
    x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    bd_rct.center = (x, y)  # 練習１：Rectにランダムな座標を設定する
    vx, vy = +5, +5  # 練習２：爆弾の速度
    clock = pg.time.Clock()
    tmr = 0
    n=kk_img1
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        if kk_rct.colliderect(bd_rct):
            print("ゲームーバー")
            return

        screen.blit(bg_img, [0, 0])
        bd_rct.move_ip(vx, vy)  # 練習２：爆弾を移動させる
        screen.blit(bd_img, bd_rct)  # 練習１：Rectを使って試しにblit
        """こうかとん"""
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for key, mv in delta.items():
            if key_lst[key]:
                sum_mv[0] += mv[0]  # 練習３：横方向の合計移動量
                sum_mv[1] += mv[1]  # 練習３：縦方向の合計移動量
        
        kk_rct.move_ip(sum_mv[0], sum_mv[1])  # 練習３：移動させる
        if (sum_mv[0],sum_mv[1])!=(0,0):
            n=kk_dct[(sum_mv[0],sum_mv[1])]
        screen.blit(n, kk_rct)  # 練習３：移動後の座標に表示させる
        
        if check_bount(kk_rct)!=(True,True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        
        """"ばくだん"""
        bd_rct.move_ip(vx+0.00001*tmr, vy+0.00001*tmr)  # 練習２：爆弾を移動させる
        yoko,tate=check_bount(bd_rct)
        if not yoko:
            vx*= -1
        if not tate:
            vy*= -1
        

        screen.blit(bd_img, bd_rct)  # 練習１：Rectを使って試しにblit
        pg.display.update()
        tmr += 1
        clock.tick(25)
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()