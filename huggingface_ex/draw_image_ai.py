from huggingface_hub import login
from dotenv import load_dotenv
import os
from diffusers import DiffusionPipeline

# 1️⃣ .env 파일의 내용을 로드
load_dotenv(".env", override=True)

# 2️⃣ 환경 변수 가져오기
HF_READ_TOKEN = os.getenv("HF_READ_TOKEN")
# print(HF_READ_TOKEN)

login(HF_READ_TOKEN) # 로그인 실행
# --------------
model ="runwayml/stable-diffusion-v1-5"
pipe = DiffusionPipeline.from_pretrained(model)

result = pipe("Draw a woman looking at the sea")
image = result.images[0]  # 첫 번째 이미지 선택
# 이미지 보여주기
image.show()  # 기본 이미지 뷰어에서 확인
# 이미지 저장 (선택)
image.save("output.png")