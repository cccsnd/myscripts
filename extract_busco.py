import sys

# 读取命令行参数
input_file = sys.argv[1]
output_file = sys.argv[2]

filename = input_file.split('/')[-1]

# 打开输入文件，提取C:开头的行
with open(input_file, 'r') as file:
    content = file.readlines()
    c_lines = [line.strip() for line in content if line.strip().startswith('C:')]

# 如果有C:开头的行，则写入到输出文件中
if c_lines:
    with open(output_file, 'w') as new_file:
        for line in c_lines:
            new_file.write(f"{filename}\t{line}\n")

