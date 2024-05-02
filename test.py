from transformers import AutoTokenizer, AutoModel
from config import MODEL_PATH, TOKENIZER_PATH
tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH, trust_remote_code=True)
        # self.model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True, device_map="auto").eval()  # 多卡推理
model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True).eval().cuda()

model