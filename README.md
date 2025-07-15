# eckert_agent


# 创建虚拟环境（例如命名为myenv）
python3 -m venv myenv

# 激活虚拟环境
source myenv/bin/activate  # Linux/Mac
# 或
.\myenv\Scripts\activate   # Windows

# 在激活的虚拟环境中安装包（无需sudo）
(myenv) $ pip install modelscope

# 使用完后，退出虚拟环境
(myenv) $ deactivate

 

cd ollama-linux
sudo chmod 777 ./ollama-modelscope-install.sh
./ollama-modelscope-install.sh

ollama run deepseek-r1:1.5b


dQCJCjCqaP1drj7KsmA9TvW6adpkaE1OpxRx1J4AZNLeGHY1B7HU4CubXcJfa489fHfPrFCXDkhjE3voPy7M9g