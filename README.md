# LD-USB
It's a usb to pixel controller. This controller is designed for Jinx and standalone playback.

LD-USB是一個簡單易用的LED Pixel控制器, 為小型商演/Maker/DIY提供另一種選擇.

功能如下:
1. 支援JINX即時輸出顯示
2. 多種撥放模式, 在Standalone模式, 無須PC, 即插即播.
3. 最多768點輸出
4. 隔離電路設計, 分離USB和驅動訊號
5. 16 MBytes Flash容量
6. DIP switch 多種功能切換
7. 目前支援ws2812/sk6812/ws2815(800k)
8. mass storage 韌體更新

QA:

1. Switch pin的定義(switch pin上為1, 下為0)
   
   [8:7]<---表示Pin8 Pin7的組合
   00:Standalone
   01:保留
   10:USB Mode
   11:隨身碟模式

   Pin6: 26/37Hz 切換
        1: 38Hz
        0: 26Hz
   
   Pin5:保留
   Pin4:保留
   
   [3:1]: 當設定在Standalone下, 一開機要撥放的.out檔
   ex. 011: 撥放LDSHOW3.out
       010: 撥放LDSHOW2.out
       000: 撥放LDSHOW0.out
       111: 撥放LDSHOW7.out

3. 如何進入隨身碟模式
   斷電後, 把Pin[8:7]全都切成1, 再插上USB即可進入隨身碟模式.

4. 如何進入Standalone模式
   斷電後, 把Pin[8:7]切換成0, 再插上USB即可進入Standalone模式.
   在這個模式下, 當板子一送電,就會開始撥放節目.
   
5. 如何把Jinx的.out檔放入flash

6. 如何一送電就要播放某一個節目

7. 如何使用LD-USB控制器搭配Jinx即時顯示

8. 如何更新韌體

持續編輯中...

LEDDot Studio

email:StudioLedDot@gmail.com
