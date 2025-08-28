# hsinchu-tourism-visitor-stats
新竹市重要遊憩據點遊客人次統計 (Hsinchu Tourism Visitor Stats)

---

##  專案簡介
這是一個以 **Python + Pandas + Matplotlib** 製作的資料視覺化專案，  
將「新竹市重要遊憩據點遊客人次統計」的 Excel 資料，轉換成圓餅圖，呈現各據點的總遊客比例。  

---

##  功能特色
- 讀取 Excel 統計檔案（`新竹市重要遊憩據點遊客人次統計.xlsx`）  
- 資料前處理：刪除無用欄位、轉換格式  
- 資料轉換：取消樞紐 (unpivot)，整理成「月份、據點、人數」格式  
- 計算各據點總遊客人次  
- 使用 **Matplotlib** 繪製圓餅圖（支援中文字體）  
- 自動套用色彩映射，保持圖表美觀  
- 可選擇將圖表輸出為 PNG 檔案  

##  專案結構

```
.
├── main.py                           # 主程式
├── 新竹市重要遊憩據點遊客人次統計.xlsx   # 原始資料
├── README.md                         # 專案說明文件
├── LICENSE                           # MIT 授權
└── .gitignore                        # 忽略檔案
```

---

## 範例圖表

（可在這裡放一張圓餅圖的截圖）

---

## 授權

此專案以 **MIT License** 授權，歡迎自由使用與修改。
