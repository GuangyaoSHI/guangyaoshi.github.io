from graphviz import Digraph

def create_research_figure():
    # 创建有向图
    dot = Digraph('ResearchFramework', comment='Multi-Robot Trusted Collaboration')
    
    # 全局属性设置
    dot.attr(rankdir='TB', size='10,14', ratio='fill', dpi='300')
    dot.attr('node', shape='box', style='filled', fontname='Arial', fontsize='10', penwidth='1.5')
    dot.attr('edge', fontname='Arial', fontsize='9', color='#555555', penwidth='1.0')

    # --- 颜色定义 ---
    # 挑战 (红/橙)
    color_challenge = '#FFEBEE' 
    border_challenge = '#D32F2F'
    # 核心框架 (蓝/绿)
    color_forward = '#E3F2FD'
    border_forward = '#1976D2'
    color_inverse = '#E8F5E9'
    border_inverse = '#388E3C'
    color_center = '#FFF3E0'
    border_center = '#F57C00'
    # 成果 (深灰/科技蓝)
    color_pillar = '#FFFFFF'
    border_pillar = '#455A64'
    # 底部 (深蓝)
    color_base = '#263238'
    font_base = '#FFFFFF'

    # =======================
    # 1. 顶部：挑战 (Challenges)
    # =======================
    with dot.subgraph(name='cluster_top') as c:
        c.attr(label='', style='invis') # 隐藏边框
        c.attr(rank='same')
        
        # 物理不确定性
        node_phys = 'phys_unc'
        c.node(node_phys, label='物理不确定性\n(Physical Uncertainty)\n⚡ 节点失效 / 通信阻断 / 性能崩塌', 
               fillcolor=color_challenge, color=border_challenge, fontcolor='#B71C1C')
        
        # 语义不确定性
        node_sem = 'sem_unc'
        c.node(node_sem, label='语义不确定性\n(Semantic Uncertainty)\n❓ 意图模糊 / 动态跳变 / 信任缺失', 
               fillcolor=color_challenge, color=border_challenge, fontcolor='#B71C1C')

    # =======================
    # 2. 中部：核心框架 (Core Framework)
    # =======================
    with dot.subgraph(name='cluster_mid') as c:
        c.attr(label='核心理论框架：双向驱动 (Dual-Drive Framework)', style='rounded', color='#90A4AE', penwidth='2', bgcolor='#FAFAFA')
        c.attr(rank='same')
        
        # 左：正向优化
        node_forward = 'forward_opt'
        c.node(node_forward, label='鲁棒正向优化推演\n(Robust Forward Optimization)\n🛡️ 最坏情形防御 | 近似比保证 | k-连通性', 
               shape='ellipse', fillcolor=color_forward, color=border_forward, fontcolor='#0D47A1', width='2.5', height='1.5')
        
        # 中：数学本质
        node_core = 'core_math'
        c.node(node_core, label='数学本质:\n信息不完备下的\n动态组合优化', 
               shape='doubleoctagon', fillcolor=color_center, color=border_center, fontcolor='#E65100', style='filled,bold')
        
        # 右：逆向优化
        node_inverse = 'inverse_opt'
        c.node(node_inverse, label='逆优化意图反演\n(Inverse Optimization Inference)\n🧠 偏好反演 | 小样本对齐 | 非凸求解', 
               shape='ellipse', fillcolor=color_inverse, color=border_inverse, fontcolor='#1B5E20', width='2.5', height='1.5')

    # =======================
    # 3. 下部：三大创新成果 (Three Pillars)
    # =======================
    with dot.subgraph(name='cluster_bottom') as c:
        c.attr(label='', style='invis')
        c.attr(rank='same')
        
        # 成果一
        node_p1 = 'pillar1'
        c.node(node_p1, label='【创新点一】\n鲁棒容错路径规划 (RMOP)\n✅ 常数因子近似保证\n✅ T-RO (机器人顶刊)\n💡 解决：任务链断裂', 
               fillcolor=color_pillar, color=border_pillar, fontcolor='#37474F')
        
        # 成果二
        node_p2 = 'pillar2'
        c.node(node_p2, label='【创新点二】\n通信韧性维持与自愈\n✅ k-连通性量化 & 毫秒级恢复\n✅ Autonomous Robots\n💡 解决：网络瘫痪', 
               fillcolor=color_pillar, color=border_pillar, fontcolor='#37474F')
        
        # 成果三
        node_p3 = 'pillar3'
        c.node(node_p3, label='【创新点三】\n人机意图自适应反演\n✅ 逆子模最大化 & 自动参数更新\n✅ WAFR/IROS (顶会)\n💡 解决：调参壁垒', 
               fillcolor=color_pillar, color=border_pillar, fontcolor='#37474F')

    # =======================
    # 4. 底部：成效与价值 (Impact)
    # =======================
    node_base = 'impact_base'
    dot.node(node_base, label='可信多机器人智能协同体系\n(The Trusted Collaborative System)\n━━━━━━━━━━━━━━━━━━━━━━\n理论可证 (Proven) | 算法高效 (Efficient) | 实测可信 (Validated)\n━━━━━━━━━━━━━━━━━━━━━━\n🚀 赋能国防现代化与新质战斗力生成', 
             shape='box3d', fillcolor=color_base, fontcolor=font_base, style='filled,bold', fontsize='11')

    # =======================
    # 连接关系 (Edges)
    # =======================
    
    # 挑战 -> 框架
    dot.edge('phys_unc', 'forward_opt', label='驱动', style='dashed', color='#D32F2F')
    dot.edge('sem_unc', 'inverse_opt', label='驱动', style='dashed', color='#D32F2F')
    
    # 框架内部连接
    dot.edge('forward_opt', 'core_math', dir='both', arrowhead='tee', arrowtail='tee', color='#1976D2')
    dot.edge('inverse_opt', 'core_math', dir='both', arrowhead='tee', arrowtail='tee', color='#388E3C')
    
    # 框架 -> 成果 (逻辑映射)
    # 正向优化支撑成果1和2
    dot.edge('forward_opt', 'pillar1', label='事前规划', color='#1976D2')
    dot.edge('forward_opt', 'pillar2', label='事后修复', color='#1976D2')
    # 逆向优化支撑成果3
    dot.edge('inverse_opt', 'pillar3', label='意图对齐', color='#388E3C')
    
    # 成果汇聚到底部
    dot.edge('pillar1', 'impact_base', style='bold', color='#555')
    dot.edge('pillar2', 'impact_base', style='bold', color='#555')
    dot.edge('pillar3', 'impact_base', style='bold', color='#555')

    # 渲染输出
    output_filename = 'research_framework'
    dot.render(output_filename, format='pdf', cleanup=True)
    print(f"图表已生成：{output_filename}.pdf")
    # 如果需要png，取消下面注释
    # dot.render(output_filename, format='png', cleanup=True)

if __name__ == '__main__':
    create_research_figure()