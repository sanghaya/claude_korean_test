# Note: you need to be using OpenAI Python v0.27.0 for the code below to work

import openai
import json
import time


tic = time.time()
openai.api_key = ''
results = []

def call_gpt(instruction, input_data, response):
    eval_result = openai.ChatCompletion.create(
        model="gpt-4",
        messages = [
            {
                "role": "system", "content": 
             f"두 사람 간의 대화가 주어집니다. 다음의 지시문(Instruction), 입력(Input)을 받게 될 것입니다. 그리고 지시문과 입력에 대한 응답(Response)이 제시됩니다. \
            당신의 작업은 응답을 평가 단계에 따라 응답을 평가하는 것입니다. \
            이 평가 기준을 꼼꼼히 읽고 이해하는 것이 중요합니다. 평가하는 동안 이 문서를 계속 열어두고 필요할 때 참조해 주세요. \
            평가 기준: \
            - 이해 가능성 (0 - 1): Input에 기반하여 Response를 이해 할 수 있나요? \
            - 자연스러움 (1 - 3): 사람이 자연스럽게 말할 법한 Instruction 인가요? \
            - 맥락 유지 (1 - 3): Input을 고려했을 때 Response가 맥락을 유지하나요? \
            - 흥미롭기 (1 - 3): Response가 지루한가요, 아니면 흥미로운가요? \
            - Instruction 사용 (0 - 1): Instruction에 기반하여 Response를 생성 했나요? \
            - 전반적인 품질 (1 - 5): 위의 답변을 바탕으로 이 발언의 전반적인 품질에 대한 인상은 어떤가요? \
            평가 단계: \
            1. Instruction, Input, 그리고 Response을 주의깊게 읽습니다. \
            2. 위의 평가 기준에 따라 Response을 평가합니다. \
            예시 1: \
            Instruction: 주어진 문장이 너무 장황하거나 복잡하거나 불분명할 수 있습니다. 문장을 다시 작성하고 간결하게 유지하여 글을 더 명확하게 만드세요. 가능하면 복잡한 문장은 여러 문장으로 나누고 불필요한 단어는 제거하세요. \
            Input: 제 요금에 대해 궁금한 점이 있거나 이 프로젝트의 범위를 늘리거나 줄여야 할 필요가 있는 경우 알려주세요. \
            Response: If you have any questions about my rate or find it necessary to increase or decrease this project's scope, please let me know. \
            Result \
            - 이해 가능성 (0 - 1): 0.9 \
            - 자연스러움 (1 - 3): 3 \
            - 맥락 유지 (1 - 3): 1.5 \
            - 흥미롭기 (1 - 3): 1.5 \
            - Instruction 사용 (0 - 1): 0 \
            - 전반적인 품질 (1 - 5): 2.3 \
            예시 2: \
            Instruction: 제품 또는 비즈니스 YouTube 채널의 이름을 선택하는 것은 프로세스의 중요한 부분입니다. 제품 또는 비즈니스에 대한 설명을 바탕으로 흥미로운 이름을 생각해 내야 합니다. 시간을 내어 아이디어를 브레인스토밍하세요. \
            Input: 대학원 지원 방법과 대학원 지원 절차를 준비하는 데 도움이 되는 동영상과 콘텐츠를 찾을 수 있습니다. \
            Response: GradSchoolPrep, GoGradSchool, GradSchoolVidz, Apply2Gradschool \
            Result \
            - 이해 가능성 (0 - 1): 1 \
            - 자연스러움 (1 - 3): 3 \
            - 맥락 유지 (1 - 3): 2.8 \
            - 흥미롭기 (1 - 3): 2.25 \
            - Instruction 사용 (0 - 1): 0.89  \
            - 전반적인 품질 (1 - 5): 3.4" 

            },
            {"role": "user", "content":  
            f"Instruction: {instruction} \
            Input: {input_data} \
            Response: {response} \
            Result \
            - 이해 가능성 (0 - 1): \
            - 자연스러움 (1 - 3): \
            - 맥락 유지 (1 - 3): \
            - 흥미롭기 (1 - 3): \
            - Instruction 사용 (0 - 1): \
            - 전반적인 품질 (1 - 5):" 
            }
        ],
        temperature = 0,
        top_p = 1    
    )
    result = eval_result['choices'][0]['message']['content']
    time.sleep(2)
    return result

def main(): 
    with open('claude_result.jsonl', 'r') as file:
         for line in file:
            data = json.loads(line)
            instruction = data.get('instruction')
            input_data = data.get('input')
            output_data = data.get('output')

            result = call_gpt(instruction, input_data, output_data)
            results.append({
                'instruction': instruction,
                'input': input_data,
                'output': output_data, 
                'result': result
            })


    with open('eval_result.jsonl', 'w', encoding='utf-8') as outfile:
        json.dump(results, outfile, ensure_ascii=False)


if __name__ == "__main__":
    main()
  

