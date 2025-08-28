import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 設定中文字體和圖表大小
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 使用微軟正黑體
plt.rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題
rcParams['figure.figsize'] = 10, 8  # 設定圖表大小

# 讀取資料並預處理（使用您之前的代碼）
df = pd.read_excel('新竹市重要遊憩據點遊客人次統計.xlsx')
df = df.drop(columns=['Countycode', 'YYYMM'])
df = df.round().astype('int32')
df['民國年月'] = df['民國年月'].astype('string')

# 取消樞紐
df_unpivoted = pd.melt(df,
                      id_vars=['民國年月'],
                      value_vars=df.columns.values[1:],
                      var_name='據點',
                      value_name='人數')

# 計算各據點總人數
location_totals = df_unpivoted.groupby('據點')['人數'].sum().sort_values(ascending=False)

# 設定美觀的顏色（根據 據點 數量自動生成）
# colors = plt.cm.hsv.colors[:len(location_totals)]

# 獲取HSV色彩映射
_colormap = plt.cm.twilight_shifted

# 生成n個均勻分布的HSV顏色
n = len(location_totals)  # 據點數量
colors = [_colormap(i/n) for i in range(n)]  # 在0-1之間均勻取值

# 創建圓餅圖
plt.figure(figsize=(12, 10))

# 繪製圓餅圖（增加陰影效果和起始角度）
wedges, texts, autotexts = plt.pie(
    location_totals,
    labels=location_totals.index,
    colors=colors,
    autopct='%5.1f%%',   # 顯示百分比
    startangle=90,       # 起始角度
    shadow=False,        # 陰影效果
    pctdistance=0.8,    # 百分比位置
    textprops={'fontsize': 12}  # 文字大小
)

# 設定標題
plt.title('新竹市重要遊憩據點遊客分布比例', fontsize=16, pad=20)

# 調整百分比文字顏色為白色（在深色區域更清晰）
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')

# 添加圖例（放在圖表右側）
plt.legend(
    wedges,
    location_totals.index,
    title="遊憩據點",
    loc="upper left",
    bbox_to_anchor=(1, 0.6),
    fontsize=10
)

# 確保圖形是正圓形
plt.axis('equal')

# 自動調整版面
plt.tight_layout()

# 顯示圖表
plt.show()

# 可選：儲存圖表
# plt.savefig('新竹市遊憩據點遊客比例.png', dpi=300, bbox_inches='tight')