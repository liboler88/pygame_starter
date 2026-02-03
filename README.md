# Pygame 貪吃蛇基礎教學專案 (Snake Game Starter)

這是一個專為 Python 初學者設計的 Pygame 專案。本專案展示了如何使用 Python 和 `pygame-ce` 函式庫，從零開始構建一個即時互動的遊戲視窗。

目前的版本實作了貪吃蛇最核心的移動機制：**方向控制**與**空間穿梭（螢幕邊界循環）**。

---

## 📋 目錄
1. [專案簡介](#專案簡介)
2. [系統需求與安裝](#系統需求與安裝)
3. [如何執行](#如何執行)
4. [操作說明](#操作說明)
5. [程式碼架構詳解](#程式碼架構詳解)
6. [技術原理](#技術原理)

---

## 專案簡介

本專案並非只是一個遊戲，更是一份教學範本。它演示了遊戲開發中最基本的「**遊戲迴圈 (Game Loop)**」架構。

### 目前已實作功能：
- **視窗系統**：建立 640x480 解析度的遊戲視窗。
- **角色控制**：使用鍵盤方向鍵控制綠色方塊（蛇頭）的移動方向。
- **持續移動**：角色會根據當前向量自動前進，模擬真實蛇的移動感。
- **邊界處理**：實作「穿牆」機制，當蛇超出螢幕右側會從左側出現（上下亦同）。
- **畫面渲染**：使用雙緩衝技術與 60 FPS 幀率鎖定，確保畫面流暢不閃爍。

---

## 系統需求與安裝

### 1. 環境需求
- Python 3.12 或更高版本
- `pygame-ce` (Community Edition) - 這是 Pygame 的現代化社群維護版本，效能與相容性較佳。

### 2. 安裝依賴
請在終端機 (Terminal) 執行以下指令安裝所需套件：

```bash
pip install -r requirements.txt
```

若您沒有 `requirements.txt`，可直接安裝：
```bash
pip install pygame-ce
# 若遇到 SSL 錯誤，請參考以下指令：
# pip install pygame-ce --trusted-host pypi.org --trusted-host files.pythonhosted.org
```

---

## 如何執行

在專案根目錄下執行：

```bash
python main.py
```

---

## 操作說明

| 按鍵 | 功能 |
| :--- | :--- |
| **↑ (Up Arrow)** | 往上移動 |
| **↓ (Down Arrow)** | 往下移動 |
| **← (Left Arrow)** | 往左移動 |
| **→ (Right Arrow)** | 往右移動 |
| **ESC / 點擊 X** | 關閉遊戲 |

---

## 程式碼架構詳解

整支程式 (`main.py`) 的運作流程如下：

### 1. 初始化 (Initialization)
```python
pygame.init()
screen = pygame.display.set_mode((640, 480))
```
- 啟動 Pygame 內部的模組（聲音、輸入、繪圖引擎）。
- 請求作業系統給我們一個 640x480 的繪圖平面。

### 2. 變數設定 (State Management)
我們使用變數來記錄遊戲的「狀態」：
- `snake_pos = [320, 240]`: 蛇目前的座標 `[x, y]`。
- `direction = [snake_speed, 0]`: 蛇目前的**速度向量**。
    - `[5, 0]` 代表向右，每偵 X+5。
    - `[0, -5]` 代表向上，每偵 Y-5 (注意：Y軸向上是減少)。

### 3. 多媒體操作 (Input Handling)
使用 `pygame.event.get()` 捕捉鍵盤事件。
- 這裡的邏輯是：**按鍵只改變「方向 (direction)」，不直接改變「位置 (pos)」**。
- 這保證了蛇在你不按鍵時，依然會依照最後的方向繼續滑行。

### 4. 邏輯更新 (Game Logic)
這是每一幀 (Frame) 電腦在後台做的運算：
```python
# 位置 = 舊位置 + 方向向量
snake_pos[0] += direction[0]
snake_pos[1] += direction[1]
```
**穿牆邏輯**：
當 `snake_pos[0] > 640` (超出右邊) 時，將 `snake_pos[0]` 設為 `0` (回到左邊)。

### 5. 畫面渲染 (Rendering)
```python
screen.fill("black")  # 1. 清除上一幀的畫面 (刷黑)
pygame.draw.rect(...) # 2. 在新位置畫上蛇
pygame.display.flip() # 3. 翻頁 (將後台畫好的圖推上前台)
```

---

## 技術原理

### 座標系統 (Coordinate System)
Pygame 的座標系與數學直角座標系略有不同：
- **原點 (0, 0)**：位於螢幕的 **左上角**。
- **X 軸**：向右增加。
- **Y 軸**：**向下增加** (這是新手最容易搞混的地方)。

### 雙緩衝 (Double Buffering)
為什麼要 `display.flip()`？
- 為了防止使用者看到「繪製中的半成品」（導致畫面閃爍），電腦通常有兩個畫布。
- 我們一直在「後台畫布」作畫，畫好後瞬間與「前台畫布」交換。這個交換的動作就是 `flip`。

---

## 未來擴充路線
目前的版本僅包含移動機制，您可以嘗試實作以下功能來完成完整的貪吃蛇遊戲：
1. **食物系統**：隨機產生紅色方塊。
2. **碰撞偵測**：當蛇頭座標重疊食物座標時，分數+1。
3. **身體增長**：使用 `List` 來儲存蛇身的每一段座標，而不僅僅是蛇頭。
4. **自殺判定**：當蛇頭撞到自己的身體時，遊戲結束。

---
**GitHub Repository**: [liboler88/pygame_starter](https://github.com/liboler88/pygame_starter) (待上傳)
**Author**: liboler88
