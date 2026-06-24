#!/usr/bin/env python3
"""
生成完全自包含的HTML文件，所有图片都内嵌为base64
这样客户不需要在同一网络下也能查看
"""

import base64
import os
import glob
import json

base_dir = r"C:\Users\a3177\Desktop\Reasonix产出\PPT模板集合"
output_file = os.path.join(base_dir, "小林PPT模板展示.html")

def file_to_base64(filepath):
    """将文件转换为base64"""
    with open(filepath, 'rb') as f:
        data = f.read()
    ext = os.path.splitext(filepath)[1].lower()
    mime_map = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.svg': 'image/svg+xml',
    }
    mime = mime_map.get(ext, 'image/png')
    return f"data:{mime};base64,{base64.b64encode(data).decode('utf-8')}"

# 模板配置
templates = [
    {"name": "AI时代的学习革命", "desc": "教育科技 · AI", "color": "#667eea", "folder": "00_成品_AI学习革命/slides", "ext": "png"},
    {"name": "远程办公的未来", "desc": "企业管理 · 远程协作", "color": "#C9A96E", "folder": "00_成品_远程办公/slides", "ext": "png"},
    {"name": "学术技术蓝图风", "desc": "技术研究 · 学术会议", "color": "#3182CE", "folder": "01_学术技术蓝图风/svg_output", "ext": "svg"},
    {"name": "野兽派报纸风", "desc": "高冲击力设计", "color": "#FF0000", "folder": "02_野兽派报纸风/svg_output", "ext": "svg"},
    {"name": "瑞士字体排版风", "desc": "极简设计 · 字体排版", "color": "#E53E3E", "folder": "03_瑞士字体排版风/svg_output", "ext": "svg"},
    {"name": "毛玻璃SaaS风", "desc": "SaaS产品 · 科技公司", "color": "#667eea", "folder": "04_毛玻璃SaaS风/svg_output", "ext": "svg"},
    {"name": "中国水墨美学风", "desc": "文化传承 · 东方美学", "color": "#C41E3A", "folder": "05_中国水墨美学风/svg_output", "ext": "svg"},
    {"name": "顶级咨询风", "desc": "商业咨询 · 战略报告", "color": "#C9A96E", "folder": "06_顶级咨询风/svg_output", "ext": "svg"},
    {"name": "奢华杂志风", "desc": "高端品牌 · 奢侈品", "color": "#D4AF37", "folder": "07_奢华杂志风/svg_output", "ext": "svg"},
    {"name": "工程蓝图风", "desc": "技术文档 · 系统架构", "color": "#4A90D9", "folder": "08_工程蓝图风/svg_output", "ext": "svg"},
    {"name": "AI时代人的价值在哪里", "desc": "人文思考 · AI时代", "color": "#C9A96E", "folder": "09_AI时代人的价值/slides", "ext": "jpg"},
]

# 收集所有图片的base64
print("正在转换图片...")
templates_data = []
for tmpl in templates:
    folder = os.path.join(base_dir, tmpl["folder"])
    files = sorted(glob.glob(os.path.join(folder, f"*.{tmpl['ext']}")))
    
    slides_b64 = []
    for f in files:
        print(f"  转换: {os.path.basename(f)}")
        slides_b64.append(file_to_base64(f))
    
    templates_data.append({
        "name": tmpl["name"],
        "desc": tmpl["desc"],
        "color": tmpl["color"],
        "slides": slides_b64
    })

print(f"\n共转换 {len(templates_data)} 个模板")

# 生成HTML
html = f'''<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>小林 PPT 模板展示</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        :root {{
            --bg-primary: #050510; --bg-secondary: #0a0a2e;
            --bg-card: rgba(10, 10, 30, 0.6); --text-primary: #f5f5f5;
            --text-secondary: rgba(255,255,255,0.5); --accent-blue: #4A7AFF;
            --accent-dark: #002FA7; --accent-gold: #c9a96e;
            --border: rgba(74, 122, 255, 0.15);
        }}
        [data-theme="light"] {{
            --bg-primary: #f5f7fa; --bg-secondary: #e8ecf1;
            --bg-card: rgba(255, 255, 255, 0.8); --text-primary: #1a1a2e;
            --text-secondary: rgba(0,0,0,0.5); --accent-blue: #2563eb;
            --accent-dark: #1d4ed8; --accent-gold: #b8860b;
            --border: rgba(0, 0, 0, 0.1);
        }}
        body {{ font-family: 'Inter', 'Segoe UI', sans-serif; color: var(--text-primary); min-height: 100vh; background: var(--bg-primary); transition: background 0.3s; }}
        .container {{ max-width: 1600px; margin: 0 auto; padding: 40px 30px; }}
        .theme-toggle {{ position: fixed; top: 20px; right: 20px; z-index: 100; background: var(--bg-card); border: 1px solid var(--border); width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; font-size: 1.2rem; backdrop-filter: blur(10px); transition: all 0.3s; }}
        .theme-toggle:hover {{ border-color: var(--accent-blue); transform: scale(1.1); }}
        header {{ text-align: center; margin-bottom: 50px; }}
        .logo {{ display: inline-flex; align-items: center; gap: 12px; margin-bottom: 20px; }}
        .logo-icon {{ width: 44px; height: 44px; background: linear-gradient(135deg, var(--accent-dark), var(--accent-blue)); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 22px; font-weight: 700; color: #fff; }}
        .logo-text {{ font-size: 1.6rem; font-weight: 300; letter-spacing: 6px; font-family: 'Space Grotesk', sans-serif; }}
        header h1 {{ font-size: 2.8rem; font-weight: 200; letter-spacing: 2px; margin-bottom: 12px; font-family: 'Space Grotesk', sans-serif; }}
        header h1 span {{ background: linear-gradient(135deg, var(--accent-blue), var(--accent-dark)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 400; }}
        header p {{ color: var(--text-secondary); font-size: 1rem; }}
        .stats {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 50px; }}
        .stat {{ background: var(--bg-card); border: 1px solid var(--border); border-radius: 12px; padding: 20px; text-align: center; transition: all 0.3s; backdrop-filter: blur(10px); }}
        .stat:hover {{ border-color: var(--accent-blue); transform: translateY(-5px); box-shadow: 0 15px 35px rgba(0, 47, 167, 0.3); }}
        .stat-num {{ font-size: 2.2rem; font-weight: 200; color: var(--accent-blue); margin-bottom: 6px; font-family: 'Space Grotesk', sans-serif; }}
        .stat-label {{ color: var(--text-secondary); font-size: 0.8rem; }}
        .templates-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-bottom: 60px; }}
        .template-block {{ background: var(--bg-card); border: 1px solid var(--border); border-radius: 14px; overflow: hidden; backdrop-filter: blur(10px); transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); cursor: pointer; }}
        .template-block:hover {{ border-color: var(--accent-blue); transform: translateY(-5px); box-shadow: 0 20px 40px rgba(0, 47, 167, 0.2); }}
        .template-block:active {{ transform: scale(0.97); transition: transform 0.1s; }}
        .template-block.clicking {{ animation: clickPulse 0.3s ease; }}
        @keyframes clickPulse {{ 0% {{ transform: scale(1); }} 50% {{ transform: scale(0.97); }} 100% {{ transform: scale(1); }} }}
        .template-header {{ padding: 16px 20px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid var(--border); }}
        .template-info {{ display: flex; align-items: center; gap: 12px; }}
        .template-num {{ width: 36px; height: 36px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.9rem; color: #fff; font-family: 'Space Grotesk', sans-serif; }}
        .template-name {{ font-size: 1rem; font-weight: 600; }}
        .template-tag {{ font-size: 0.65rem; padding: 3px 10px; border-radius: 100px; border: 1px solid var(--border); }}
        .slides-row {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; padding: 12px; }}
        .slide-thumb {{ border-radius: 6px; overflow: hidden; cursor: pointer; transition: all 0.3s; border: 2px solid transparent; position: relative; }}
        .slide-thumb:hover {{ border-color: var(--accent-blue); transform: scale(1.05); z-index: 5; box-shadow: 0 8px 20px rgba(0,0,0,0.3); }}
        .slide-thumb img {{ width: 100%; height: auto; display: block; transition: transform 0.3s; }}
        .slide-thumb:hover img {{ transform: scale(1.1); }}
        .slide-thumb .slide-num {{ position: absolute; bottom: 4px; right: 4px; background: rgba(0,0,0,0.8); color: #fff; font-size: 0.6rem; padding: 2px 6px; border-radius: 4px; }}
        .viewer {{ display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(5,5,16,0.95); z-index: 1000; flex-direction: column; }}
        .viewer.active {{ display: flex; animation: zoomIn 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards; }}
        @keyframes zoomIn {{ from {{ opacity: 0; transform: scale(0.3); }} to {{ opacity: 1; transform: scale(1); }} }}
        .viewer.closing {{ animation: zoomOut 0.35s cubic-bezier(0.4, 0, 0.2, 1) forwards; }}
        @keyframes zoomOut {{ from {{ opacity: 1; transform: scale(1); }} to {{ opacity: 0; transform: scale(0.3); }} }}
        .viewer-bar {{ display: flex; align-items: center; justify-content: space-between; padding: 14px 24px; background: var(--bg-card); border-bottom: 1px solid var(--border); backdrop-filter: blur(10px); animation: slideDown 0.4s ease 0.1s both; }}
        @keyframes slideDown {{ from {{ transform: translateY(-100%); opacity: 0; }} to {{ transform: translateY(0); opacity: 1; }} }}
        .viewer-info {{ display: flex; align-items: center; gap: 12px; }}
        .viewer-title {{ font-size: 1rem; font-weight: 500; }}
        .viewer-actions {{ display: flex; gap: 10px; }}
        .viewer-btn {{ background: rgba(0, 47, 167, 0.3); color: var(--text-primary); border: 1px solid var(--border); padding: 7px 14px; border-radius: 6px; cursor: pointer; font-size: 0.8rem; transition: all 0.2s; }}
        .viewer-btn:hover {{ background: var(--accent-dark); border-color: var(--accent-blue); }}
        .viewer-stage {{ flex: 1; display: flex; align-items: center; justify-content: center; padding: 30px; position: relative; }}
        .slide-frame {{ position: relative; width: 100%; max-width: 1100px; aspect-ratio: 16/9; background: #fff; border-radius: 10px; box-shadow: 0 30px 60px rgba(0,0,0,0.5); overflow: hidden; animation: frameSlideUp 0.5s ease 0.2s both; }}
        @keyframes frameSlideUp {{ from {{ transform: translateY(30px) scale(0.95); opacity: 0; }} to {{ transform: translateY(0) scale(1); opacity: 1; }} }}
        .slide {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0; transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1); }}
        .slide.active {{ opacity: 1; animation: slideIn 0.5s ease forwards; }}
        @keyframes slideIn {{ from {{ transform: scale(0.95) translateX(30px); opacity: 0; }} to {{ transform: scale(1) translateX(0); opacity: 1; }} }}
        .slide img, .slide svg {{ width: 100%; height: 100%; object-fit: contain; }}
        .nav-arrow {{ position: absolute; top: 50%; transform: translateY(-50%); width: 50px; height: 50px; border-radius: 50%; background: var(--bg-card); color: var(--text-primary); border: 1px solid var(--border); font-size: 1.4rem; cursor: pointer; transition: all 0.3s; display: flex; align-items: center; justify-content: center; z-index: 10; animation: fadeIn 0.4s ease 0.4s both; }}
        @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
        .nav-arrow:hover {{ background: var(--accent-dark); border-color: var(--accent-blue); transform: translateY(-50%) scale(1.1); }}
        .nav-arrow.prev {{ left: 16px; }}
        .nav-arrow.next {{ right: 16px; }}
        .slide-info {{ position: absolute; bottom: 16px; left: 50%; transform: translateX(-50%); background: var(--bg-card); color: var(--text-secondary); padding: 7px 18px; border-radius: 100px; font-size: 0.8rem; border: 1px solid var(--border); backdrop-filter: blur(10px); }}
        footer {{ text-align: center; padding: 40px 0; border-top: 1px solid var(--border); margin-top: 40px; }}
        footer p {{ color: var(--text-secondary); font-size: 0.8rem; line-height: 2; }}
        @media (max-width: 1200px) {{ .templates-grid {{ grid-template-columns: 1fr; }} }}
        @media (max-width: 768px) {{
            .container {{ padding: 20px 15px; }}
            header h1 {{ font-size: 1.8rem; }}
            .stats {{ grid-template-columns: repeat(2, 1fr); }}
            .slides-row {{ grid-template-columns: repeat(2, 1fr); }}
            .viewer-stage {{ padding: 15px; }}
            .nav-arrow {{ width: 40px; height: 40px; font-size: 1.2rem; }}
        }}
    </style>
</head>
<body>
    <!-- 启动动画 -->
    <div id="splash" style="position:fixed;top:0;left:0;width:100%;height:100%;background:#ffffff;z-index:9999;display:flex;flex-direction:column;align-items:center;justify-content:center;overflow:hidden;">
        <!-- Logo -->
        <div style="margin-bottom:32px;opacity:0;animation:logoIn 0.6s cubic-bezier(0.16,1,0.3,1) 0.1s forwards;">
            <div style="width:80px;height:80px;background:linear-gradient(135deg,#002FA7,#4A7AFF);border-radius:18px;display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:700;color:#fff;font-family:'Space Grotesk',sans-serif;box-shadow:0 12px 40px rgba(0,47,167,0.3);">林</div>
        </div>
        <!-- 品牌名 -->
        <div style="font-family:'Space Grotesk',sans-serif;font-size:1.4rem;font-weight:300;letter-spacing:12px;color:#1a1a2e;margin-bottom:12px;opacity:0;animation:fadeInUp 0.4s ease 0.3s forwards;">XIAOLIN</div>
        <!-- 分隔线 -->
        <div style="width:48px;height:2px;background:linear-gradient(90deg,#4A7AFF,#c9a96e);margin:20px 0;opacity:0;animation:fadeInUp 0.4s ease 0.4s forwards;"></div>
        <!-- 主标题 -->
        <div style="font-family:'Space Grotesk',sans-serif;font-size:2.4rem;font-weight:200;letter-spacing:6px;color:#1a1a2e;margin-bottom:10px;opacity:0;animation:fadeInUp 0.4s ease 0.5s forwards;">PPT 模板展示</div>
        <!-- 副标题 -->
        <div style="font-family:'Inter',sans-serif;font-size:0.9rem;color:rgba(0,0,0,0.4);letter-spacing:2px;margin-bottom:48px;opacity:0;animation:fadeInUp 0.4s ease 0.6s forwards;">专业级演示文稿模板 · 10 种风格</div>
        <!-- 进度条 -->
        <div style="width:240px;height:3px;background:rgba(0,0,0,0.08);border-radius:2px;overflow:hidden;opacity:0;animation:fadeInUp 0.4s ease 0.7s forwards;">
            <div id="progress" style="width:0%;height:100%;background:linear-gradient(90deg,#4A7AFF,#c9a96e);border-radius:2px;transition:width 0.15s ease;"></div>
        </div>
        <!-- 加载文字 -->
        <div id="loadingText" style="font-family:'Inter',sans-serif;font-size:0.75rem;color:rgba(0,0,0,0.3);margin-top:14px;letter-spacing:1px;opacity:0;animation:fadeInUp 0.4s ease 0.8s forwards;">加载中...</div>
    </div>
    <style>
        @keyframes fadeInUp {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        @keyframes logoIn {{ from {{ opacity: 0; transform: scale(0.7); }} to {{ opacity: 1; transform: scale(1); }} }}
    </style>
    <button class="theme-toggle" onclick="toggleTheme()" id="themeBtn">☀️</button>
    <div class="container" id="homePage" style="display:none;">
        <header>
            <div class="logo">
                <div class="logo-icon">林</div>
                <div class="logo-text">XIAOLIN</div>
            </div>
            <h1>PPT <span>模板展示</span></h1>
            <p>专业级演示文稿模板 · 10 种风格 · 点击缩略图查看完整演示</p>
        </header>
        <div class="stats">
            <div class="stat"><div class="stat-num" data-target="2">0</div><div class="stat-label">成品案例</div></div>
            <div class="stat"><div class="stat-num" data-target="8">0</div><div class="stat-label">模板风格</div></div>
            <div class="stat"><div class="stat-num" data-target="80">0</div><div class="stat-label">总页面数</div></div>
            <div class="stat"><div class="stat-num" data-target="10">0</div><div class="stat-label">PPTX 文件</div></div>
        </div>
        <div class="templates-grid" id="templatesGrid"></div>
        <footer>
            <p>小林 PPT Studio · 专业级 PPT 动效模板</p>
            <p>每套模板均含自动入场动画 · 兼容 WPS / PowerPoint</p>
        </footer>
    </div>
    <div class="viewer" id="viewer">
        <div class="viewer-bar">
            <div class="viewer-info"><div class="viewer-title" id="viewerTitle"></div></div>
            <div class="viewer-actions">
                <button class="viewer-btn" onclick="closeViewer()">✕ 关闭</button>
            </div>
        </div>
        <div class="viewer-stage">
            <div class="slide-frame" id="slideFrame"></div>
            <button class="nav-arrow prev" onclick="prevSlide()">‹</button>
            <button class="nav-arrow next" onclick="nextSlide()">›</button>
            <div class="slide-info" id="slideInfo">1 / 8</div>
        </div>
    </div>
    <script>
        const templates = {json.dumps(templates_data, ensure_ascii=False)};
        
        // 启动动画
        const splash = document.getElementById('splash');
        const progress = document.getElementById('progress');
        const loadingText = document.getElementById('loadingText');
        const homePage = document.getElementById('homePage');
        let loadProgress = 0;
        
        const loadingMessages = [
            '加载模板资源...',
            '渲染预览图...',
            '准备就绪'
        ];
        
        function updateSplash() {{
            loadProgress += Math.random() * 30 + 20;
            if (loadProgress > 100) loadProgress = 100;
            progress.style.width = loadProgress + '%';
            
            const msgIndex = Math.min(Math.floor(loadProgress / 35), loadingMessages.length - 1);
            loadingText.textContent = loadingMessages[msgIndex];
            
            if (loadProgress < 100) {{
                setTimeout(updateSplash, 80);
            }} else {{
                setTimeout(() => {{
                    // 平滑过渡：淡出 + 淡入
                    splash.style.transition = 'opacity 0.3s ease';
                    splash.style.opacity = '0';
                    setTimeout(() => {{
                        splash.style.display = 'none';
                        homePage.style.opacity = '0';
                        homePage.style.display = 'block';
                        setTimeout(() => {{
                            homePage.style.transition = 'opacity 0.3s ease';
                            homePage.style.opacity = '1';
                            setTimeout(animateNumbers, 200);
                        }}, 50);
                    }}, 300);
                }}, 200);
            }}
        }}
        
        setTimeout(updateSplash, 500);
        
        let currentSlide = 0, currentTemplate = null, savedScrollY = 0;
        
        // 数字滚动动画
        function animateNumbers() {{
            const nums = document.querySelectorAll('.stat-num[data-target]');
            nums.forEach(num => {{
                const target = parseInt(num.getAttribute('data-target'));
                const duration = 1500;
                const step = target / (duration / 16);
                let current = 0;
                const timer = setInterval(() => {{
                    current += step;
                    if (current >= target) {{
                        current = target;
                        clearInterval(timer);
                    }}
                    num.textContent = Math.floor(current);
                }}, 16);
            }});
        }}
        
        function toggleTheme() {{
            const html = document.documentElement;
            const current = html.getAttribute('data-theme');
            const next = current === 'light' ? '' : 'light';
            html.setAttribute('data-theme', next);
            document.getElementById('themeBtn').textContent = next === 'light' ? '☀️' : '🌙';
        }}
        
        function renderTemplateBlocks() {{
            const grid = document.getElementById('templatesGrid');
            templates.forEach((t, i) => {{
                const block = document.createElement('div');
                block.className = 'template-block';
                block.onclick = (e) => {{
                    block.classList.add('clicking');
                    setTimeout(() => {{
                        block.classList.remove('clicking');
                        openViewer(i, 0);
                    }}, 200);
                }};
                const num = i < 2 ? `成品${{i+1}}` : `模板${{String(i-1).padStart(2,'0')}}`;
                let thumbsHtml = '';
                t.slides.forEach((s, j) => {{
                    thumbsHtml += `<div class="slide-thumb" onclick="event.stopPropagation(); openViewer(${{i}}, ${{j}})"><img src="${{s}}" alt="Slide ${{j+1}}"><div class="slide-num">${{j+1}}</div></div>`;
                }});
                block.innerHTML = `<div class="template-header"><div class="template-info"><div class="template-num" style="background:${{t.color}}">${{num}}</div><div><div class="template-name">${{t.name}}</div><div style="font-size:0.75rem;color:var(--text-secondary)">${{t.desc}}</div></div></div><div class="template-tag" style="color:${{t.color}};border-color:${{t.color}}40">${{t.desc}}</div></div><div class="slides-row">${{thumbsHtml}}</div>`;
                grid.appendChild(block);
            }});
        }}
        
        function openViewer(templateIndex, slideIndex = 0) {{
            savedScrollY = window.scrollY;
            currentTemplate = templateIndex;
            currentSlide = slideIndex;
            const t = templates[templateIndex];
            document.getElementById('viewerTitle').textContent = t.name;
            
            // 获取点击的卡片位置用于iOS风格动画
            const blocks = document.querySelectorAll('.template-block');
            if (blocks[templateIndex]) {{
                const rect = blocks[templateIndex].getBoundingClientRect();
                const centerX = rect.left + rect.width / 2;
                const centerY = rect.top + rect.height / 2;
                document.getElementById('viewer').style.transformOrigin = centerX + 'px ' + centerY + 'px';
            }}
            
            renderSlides(t.slides);
            updateCounter(t.slides.length);
            document.getElementById('viewer').classList.add('active');
            document.getElementById('homePage').style.display = 'none';
            document.body.style.overflow = 'hidden';
        }}
        
        function closeViewer() {{
            const viewer = document.getElementById('viewer');
            viewer.classList.add('closing');
            setTimeout(() => {{
                viewer.classList.remove('active', 'closing');
                document.getElementById('homePage').style.display = 'block';
                document.body.style.overflow = '';
                window.scrollTo(0, savedScrollY);
            }}, 300);
        }}
        
        function renderSlides(slides) {{
            const frame = document.getElementById('slideFrame');
            frame.innerHTML = '';
            slides.forEach((s, i) => {{
                const div = document.createElement('div');
                div.className = 'slide' + (i === currentSlide ? ' active' : '');
                div.innerHTML = `<img src="${{s}}">`;
                frame.appendChild(div);
            }});
        }}
        
        function goToSlide(index) {{
            const slides = templates[currentTemplate].slides;
            if (index < 0 || index >= slides.length) return;
            document.querySelectorAll('.slide').forEach((s, i) => {{
                s.classList.remove('active', 'prev');
                if (i < index) s.classList.add('prev');
                if (i === index) s.classList.add('active');
            }});
            currentSlide = index;
            updateCounter(slides.length);
        }}
        
        function nextSlide() {{ if (currentSlide < templates[currentTemplate].slides.length - 1) goToSlide(currentSlide + 1); }}
        function prevSlide() {{ if (currentSlide > 0) goToSlide(currentSlide - 1); }}
        function updateCounter(total) {{ document.getElementById('slideInfo').textContent = `${{currentSlide+1}} / ${{total}}`; }}
        
        document.addEventListener('keydown', e => {{
            if (!document.getElementById('viewer').classList.contains('active')) return;
            switch(e.key) {{
                case 'ArrowRight': case ' ': e.preventDefault(); nextSlide(); break;
                case 'ArrowLeft': prevSlide(); break;
                case 'Escape': closeViewer(); break;
            }}
        }});
        
        renderTemplateBlocks();
    </script>
</body>
</html>'''

# 写入文件
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html)

file_size = os.path.getsize(output_file)
print(f"\n生成完成: {output_file}")
print(f"文件大小: {file_size / 1024 / 1024:.1f} MB")
print(f"\n这个文件是完全自包含的，可以直接发给客户，不需要任何服务器！")
