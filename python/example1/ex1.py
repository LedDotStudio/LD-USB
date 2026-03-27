# -*- coding: utf-8 -*-

import serial
import time
import math
import colorsys

# ===== 使用者設定 =====
COM_PORT = "COM61"   # ← 改這裡
BAUDRATE = 921600  # Jinx 常用速度（可拉高到 1M）
WIDTH = 48
HEIGHT = 16

FRAME_DELAY = 0.03  # 30ms

# ===== TPM2.Net 封包 =====
def build_tpm2_packet(rgb_data):
    length = len(rgb_data)
    packet = bytearray()

    packet.append(0xC9)
    packet.append(0xDA)
    packet.append((length >> 8) & 0xFF)
    packet.append(length & 0xFF)

    packet.extend(rgb_data)
    packet.append(0x36)

    return packet

# ===== 彩虹產生 =====
def generate_rainbow_frame(t):
    frame = []

    for y in range(HEIGHT):
        for x in range(WIDTH):
            # 產生彩虹（x + t 讓它流動）
            hue = (x / WIDTH + t) % 1.0
            r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)

            frame.append(int(r * 255))
            frame.append(int(g * 255))
            frame.append(int(b * 255))

    return bytearray(frame)

# ===== 主程式 =====
def main():
    print(f"Opening {COM_PORT}...")
    ser = serial.Serial(COM_PORT, BAUDRATE)

    t = 0.0
    
    #do clear 
    rgb_frame = generate_rainbow_frame(t)
    packet = build_tpm2_packet(rgb_frame)
    packet[0] = 0
    
    ser.write(packet)

    try:
        while True:
            rgb_frame = generate_rainbow_frame(t)
            packet = build_tpm2_packet(rgb_frame)

            #for debug use
            #DOTNUM = 1
            #packet[4+3*DOTNUM] = 0x00; #G
            #packet[5+3*DOTNUM] = 0xF8; #R
            #packet[6+3*DOTNUM] = 0xF1; #B
            
            ser.write(packet)

            t += 0.03  # 控制動畫速度
            time.sleep(FRAME_DELAY)

    except KeyboardInterrupt:
        print("Stopped by user")

    finally:
        ser.close()


if __name__ == "__main__":
    main()
