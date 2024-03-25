'''
# AIdoc.py
使用 core 里面的核心组件，搭建了大量用于 文本生成 的方法。
'''

from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent   # 项目根目录，如：  /DocDoc
curt_path = Path(__file__).parent   # 当前目录，如：  /Hello/current
sys.path.append(str(root_path)) 
sys.path.append(str(curt_path)) 

from typing import List
from PromptUtil import PromptTemplate

def AIgen_chapter(title:str, prompt:str, llm, information:str = None)  -> str:
    '''
    - 功能：
        输入 prompt，生成一个章节的内容
    '''
    promptObj = PromptTemplate(input_variables=["title", "information"], template=prompt)
    print(promptObj.format(title = title, information = information))   # 打印提示词
    chapter = llm(promptObj.format(title = title, information = information))
    return chapter

def AIgen_doc(title:str, llm, information:str=None) -> str:
    '''
    - 功能：
        输入文章标题和辅助信息，返回整篇文章（长文本）
    '''
    # content = AIgen_content(title)
    # prompt_list = AIgen_promptlist(content, information)
    # doc = f"{title}\n\n"
    # for prompt in prompt_list:
    #     doc += AIgen_chapter(prompt, llm) + "\n\n"

    content = AIgen_content(title)
    prompt_list = AIgen_promptlist(content)
    doc = f"{title}\n\n"
    for prompt in prompt_list:
        doc += AIgen_chapter(title, prompt, llm, information)
    return doc

def AIgen_content(title:str, content:str = None) -> str:
    '''
    - 功能：
        输入标题，让AI生成 文章目录 content
        用户也可以自己传目录进来，不让AI生成目录
    - 参数
        - title：文章标题
        - content：用户自定义的目录，默认为空
    '''
    if content == None:
        pass
        '''
            code: AI生成目录
        '''
    else:
        pass
        '''
            code: 使用用户传入的目录
        '''
        # ----用于测试的默认目录模板----
        from core.prompt import content_template
        content = content_template
        # ----用于测试的默认目录模板----

    return content

def AIgen_promptlist(content:str) -> List[str]:
    '''
        传入 文章目录 content，AI生成 promptlist 并将其返回
        用户也可以自己传入 promptlist 进来，不让AI生成 promptlist
    '''
    # ----用于测试的默认模板----
    from core.prompt import promptlist_template
    promptlist = promptlist_template
    # ----用于测试的默认模板----
    
    return promptlist 

def AIContinue(text, llm) -> str:
    '''
    - 功能
        AI续写，传入一段文本，续写内容
    - 参数
        - text：传入的文本
        - llm：AI模型
    '''
    # 导入上下文 text
    from core.prompt import AIContinue_template 
    prompt = AIContinue_template + text
    # print(prompt)
    # 生成续写 response
    response = llm(prompt) # 基于上下文的续写

    return response

def AIImprove(text, llm) -> str:
    '''
    - 功能
        AI续写，传入一段文本，优化内容
    - 参数
        - text：传入的文本
        - llm：AI模型
    '''
    # 导入上下文 text
    from core.prompt import AIImprove_template 
    prompt = AIImprove_template + text
    # print(prompt)
    # 生成续写 response
    response = llm(prompt) # 基于上下文的续写

    return response


if __name__ == "__main__":
    pass
    ProjectPath = "/remote-home/yy/lzd/DocDoc" 
    MODEL_PATH = "/remote-home/share/LLM_model/chatglm3-6b"
    TOKENIZER_PATH = "/remote-home/share/LLM_model/chatglm3-6b"
    EMBEDDING_PATH = "/remote-home/share/LLM_model//bge-large-zh"

    # 模型加载
    from LLMs import ChatGLM
    llm= ChatGLM()
    llm.load_model(MODEL_PATH, TOKENIZER_PATH)
    # from langchain.embeddings.huggingface import HuggingFaceEmbeddings
    # embeddings = HuggingFaceEmbeddings(model_name = EMBEDDING_PATH,
    #                                     model_kwargs = {'device': "cuda"})


    # --- test: AIgen_chapter()
    # from core.prompt import promptlist_template_short
    # title = "张靖皋长江大桥ZJG-A5标段绿色工地建设阶段性工作总结"
    # print(AIgen_chapter(title, promptlist_template_short, llm, information="张靖皋长江大桥ZJG-A5标段，于2021年12月1日开始施工，2023年3月2日竣工"))
   
    # --- test: AIContinue()
    # text = "我是一只小狗"
    # response = AIContinue(text, llm)
    # print(response)

    # --- test: AIImprove()
    # text = "工程绿色审核人工智能支持系统的存储系统使用了 mysql和 redis，后端选用了python进行构建，前端使用了 webpack 和 React"
    # response = AIImprove(text, llm)
    # print(response)

    # --- test: AIgen_doc()
    # import time
    # # 记录开始时间
    # start_time = time.time()
    # from core.prompt import promptlist_template_short
    from core.prompt import promptlist_template
    title = "武汉大学6号楼绿色工地建设总结报告"
    information = """"""
    doc = AIgen_doc(title=title, llm=llm, information=information)
    print(doc)

    # from core.outputer import PdfOutputer
    # pdfOutputer = PdfOutputer()
    # pdfOutputer.output(doc, outputfile="绿色工地报告.pdf")

    # # 记录结束时间
    # end_time = time.time()
    # # 计算运行时间
    # elapsed_time = end_time - start_time
    # print(f"程序运行时间：{elapsed_time} 秒")
    # print(f"程序运行时间：{elapsed_time/60} 分钟")



    
    