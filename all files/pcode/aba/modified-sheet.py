import pandas as pd
import os

# 源文件夹和目标文件夹路径
source_folder = 'C:/all files/aba/portuglal/sheets'
target_folder = 'C:/all files/aba/portugal/modified_sheets'

# 确保目标文件夹存在
os.makedirs(target_folder, exist_ok=True)

# 定义修改DataFrame的函数
def set_pdDistrict(row):
    lat = row['latitude']
    lon = row['longitude']
    if 41 <= lat <= 42 and -8.5 <= lon <= -6.5:
        return 'Norte'
    elif 39.5 <= lat < 41 and -8.5 <= lon <= -6.5:
        return 'Centro'
    elif 38.5 <= lat <= 39.5 and -9 <= lon <= -8:
        return 'Lisboa VT'
    elif 37.5 <= lat <= 39.5 and -8.5 <= lon <= -6.5:
        return 'Alentejo'
    elif 37 <= lat <= 37.5 and -8.5 <= lon <= -7.5:
        return 'Algarve'
    else:
        return 'Other'

# 遍历源文件夹中的所有文件
for filename in os.listdir(source_folder):
    # 构建完整的文件路径
    file_path = os.path.join(source_folder, filename)
    
    # 确保是CSV文件
    if os.path.isfile(file_path) and filename.endswith('.csv'):
        # 加载CSV文件
        df = pd.read_csv(file_path)
        
        # 应用函数并创建新列
        df['pdDistrict'] = df.apply(set_pdDistrict, axis=1)
        
        # 构建新的文件路径并保存修改后的文件
        new_file_path = os.path.join(target_folder, filename)
        df.to_csv(new_file_path, index=False)
