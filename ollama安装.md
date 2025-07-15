https://github.com/ollama/ollama/releases

sudo tar -C /usr -zxvf ollama-linux-amd64.tgz
sudo useradd -r -s /bin/false -U -m -d /usr/share/ollama ollama
# 修改用户信息
sudo usermod -a -G ollama $(whoami)

# 编辑文件
sudo vi /etc/systemd/system/ollama.service

# 文件内容
[Unit]
Description=Ollama Service
After=network-online.target

[Service]
ExecStart=/usr/bin/ollama serve
User=ollama
Group=ollama
Restart=always
RestartSec=3
Environment="PATH=$PATH"
Environment="OLLAMA_HOST=0.0.0.0:11434"
Environment="OLLAMA_ORIGINS=*"

[Install]
WantedBy=default.target

# 重载配置
sudo systemctl daemon-reload
# 启动服务
sudo systemctl start ollama.service
# 查看服务状态
sudo systemctl status ollama.service
# 设置服务开机自启动
sudo systemctl enable ollama.service

ollama pull deepseek-r1:1.5b


