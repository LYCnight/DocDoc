from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent   # 项目根目录，如：  /DocDoc
curt_path = Path(__file__).parent   # 当前目录，如：  /Hello/current
sys.path.append(str(root_path)) 
sys.path.append(str(curt_path)) 

class PromptTemplate:
    def __init__(self, input_variables, template):
        self.input_variables = input_variables
        self.template = template

    def format(self, **kwargs):
        if set(kwargs.keys()) != set(self.input_variables):
            raise ValueError("Input variables do not match the template's required variables.")
        
        return self.template.format(**kwargs)

if __name__ == "__main__":
    # 没有输入变量的示例 prompt
    no_input_prompt = PromptTemplate(input_variables=[], template="Tell me a joke.")
    print(no_input_prompt.format())
    # -> "Tell me a joke."

    # 有一个输入变量的示例 prompt
    one_input_prompt = PromptTemplate(input_variables=["adjective"], template="Tell me a {adjective} joke.")
    print(one_input_prompt.format(adjective="funny"))
    # -> "Tell me a funny joke."

    # 有多个输入变量的示例 prompt
    multiple_input_prompt = PromptTemplate(
        input_variables=["adjective", "content"], 
        template="Tell me a {adjective} joke about {content}."
    )
    print(multiple_input_prompt.format(adjective="funny", content="chickens"))
    # -> "Tell me a funny joke about chickens."

    from core.prompt import promptlist_template
    title = "武汉大学6号楼绿色工地建设总结报告"
    information = """工地基本信息：
工地名称：武汉大学6号楼
位置：武汉市洪山区武汉大学校园内
施工单位：某某建筑工程公司
工程负责人：张三
施工周期：2022年1月1日至2023年12月31日
绿色工地建设情况：

环保设施：在工地周边设置了固定的垃圾分类回收站，并有专人负责管理和处理
节能措施：采用了节能环保材料，建筑设计符合节能标准，采光、通风等方面考虑充分
水资源利用：合理利用雨水、污水回收等措施，减少对地下水的开采
噪音控制：采用了隔音墙、降噪设备等措施，减少施工噪音对周边环境的影响
绿化覆盖：在工地周边进行了绿化，种植了树木和草坪，美化环境，改善空气质量
安全生产情况：

安全培训：工地所有人员都接受了安全培训，并持证上岗
安全设施：工地设置了安全警示标识，安全通道畅通，消防设施完备
安全监控：工地进行了24小时全天候的安全监控，并配备了专业的安全人员进行巡查和管理
事故处理：对可能发生的安全事故进行了预防性措施，并制定了应急预案，及时处理任何事故发生的情况
社会责任履行情况：

社区关系：与周边社区保持良好关系，定期进行沟通交流，参与社区公益活动
就业贡献：工地吸纳了周边居民就业，提供了稳定的工作岗位和良好的福利待遇
环境保护：积极参与环境保护，定期组织环保宣传教育活动，倡导绿色生活理念"""
    prompt = PromptTemplate(
        input_variables=["title", "information"], 
        template = promptlist_template[0]
    )
    print(prompt.format(title = title, information = information ))
