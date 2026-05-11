# LD-USB
It's a usb to pixel controller. This controller is designed for Jinx and standalone playback.

LD-USB是一個簡單易用的LED Pixel控制器, 為小型商演/Maker/DIY提供另一種選擇.

## 功能如下:
1. 支援JINX即時輸出顯示
2. 多種撥放模式, 在Standalone模式, 無須PC, 即插即播.
3. 最多768點輸出
4. 隔離電路設計, 分離USB和驅動訊號
5. 16 MBytes Flash容量
6. DIP switch 多種功能切換
7. 目前支援ws2812/sk6812/ws2815(800k)
8. mass storage 韌體更新

## QA:

1. Switch pin的定義為何 (switch pin上為1, 下為0)  
   [8:7] <--- 表示Pin8 Pin7的組合  
   00 Standalone  
   01:保留  
   10:USB Mode  
   11:隨身碟模式  

   Pin6: 26/37Hz 切換  
        1: 38Hz  
        0: 26Hz  
   
   Pin5:保留  
   Pin4:保留  
   
   [3:1]: 當設定在Standalone下, 一開機要撥放的.out檔  
   ex.  
   011: 撥放LDSHOW3.out  
   010: 撥放LDSHOW2.out  
   000: 撥放LDSHOW0.out  
   111: 撥放LDSHOW7.out

2. 如何進入隨身碟模式    
   斷電後, 把Pin[8:7]全都切成1, 再插上USB即可進入隨身碟模式.

3. 如何進入Standalone模式  
   斷電後, 把Pin[8:7]切換成0, 再插上USB即可進入Standalone模式.
   在這個模式下, 當板子一送電,就會開始撥放節目.
   
4. 如何更新韌體  
   進入隨身碟模式後, 把LDUSB_FW.bin拷貝至隨身槽後, 重新插拔USB, 即可更新.
   若有更新成功, LDUSB_FW.bin的檔名會被改成LDUSB_F@.bin
     
5. 如何把Jinx的.out檔放入flash  
   進入隨身碟模式後, 在電腦上把 .out拷貝至LD-USB即可, 若要一送電就撥放節目, 
   記得要切換至Standalone模式
   
6. 如何一送電就要播放某一個節目  
   步驟1. 斷電後, 切換至Standalone模式, 並切換要撥放的節目代號  
   步驟2. 送電

7. 如何使用LD-USB控制器搭配Jinx即時顯示  
   步驟1. 切換至USB模式   
   步驟2. 執行Jinx  
   步驟3. 確定com port的號碼  

8. 如何26Hz/38Hz播放速度切換  
   切換pin 6來選擇, 這功能只有在standalone模式才會有作用.  
   之所以有26Hz/38Hz切換的功能, 是因為Jinx的即時輸出是26Hz左右,   
   但在standalone模式下LD-USB可選擇用更快的速度來播放(38Hz).

9. 節目命名方式  
   LDSHOWX.out, X從0 ~ 7  
   例如 LDSHOW0.out LDSHOW5.out...等  

11. 開源 protocol 說明  
    封包協定是走TPM2的協定, 若使用者想自行控制LED, 可用TPM2協定來跟LD-USB通訊並點亮LED.  
    有python範例可參考

12. 出廠switch pin的預設值  
    出廠的LD-USB DIP switch都是0,   
    意思是: standalone模式, 撥放節目0, 撥放速度是26Hz.  

持續編輯中...

LEDDot Studio

email:StudioLedDot@gmail.com
