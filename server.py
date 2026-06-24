#!/usr/bin/env python3
"""
简单的HTTP服务器，用于在局域网内分享PPT模板展示页面
使用方法：python server.py
然后在手机浏览器中访问 http://你的IP:8080
"""

import http.server
import socketserver
import socket
import os
import webbrowser

# 设置端口
PORT = 8080

# 设置工作目录
os.chdir(r"C:\Users\a3177\Desktop\Reasonix产出\PPT模板集合")

# 获取本机IP地址
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

# 创建HTTP服务器
Handler = http.server.SimpleHTTPRequestHandler

# 设置MIME类型
Handler.extensions_map.update({
    '.svg': 'image/svg+xml',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.html': 'text/html',
    '.css': 'text/css',
    '.js': 'application/javascript',
})

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    local_ip = get_local_ip()
    print("=" * 60)
    print("PPT 模板展示服务器已启动")
    print("=" * 60)
    print(f"\n本机访问: http://localhost:{PORT}")
    print(f"手机访问: http://{local_ip}:{PORT}")
    print("\n请确保手机和电脑在同一WiFi网络下")
    print("=" * 60)
    
    # 自动打开浏览器
    webbrowser.open(f"http://localhost:{PORT}")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
        httpd.shutdown()
