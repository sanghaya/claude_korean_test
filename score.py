
import json
import re

total_score = {
    "이해가능성": 0,
    "자연스러움": 0,
    "맥락 유지": 0,
    "흥미롭기": 0,
    "Instruction 사용": 0,
    "전반적인 품질": 0,
}

def main(): 
    with open('eval_result.jsonl', 'r') as file:
         idx = 0
         for line in file:
            data = json.loads(line)
            scores = data.get('result')
            numbers = re.findall(r': ([\d.]+)', scores)
            numbers = [float(num) for num in numbers]
            assert len(numbers) == 6
            total_score['이해가능성'] += numbers[0]
            total_score['자연스러움'] += numbers[1] 
            total_score['맥락 유지'] += numbers[2]
            total_score['흥미롭기'] += numbers[3] 
            total_score['Instruction 사용'] += numbers[4]
            total_score['전반적인 품질'] += numbers[5] 
            idx += 1
    
    for key in total_score:
        total_score[key] /= idx

    print (total_score)

    with open('score.jsonl', 'w', encoding='utf-8') as outfile:
        json.dump(total_score, outfile, ensure_ascii=False)


if __name__ == "__main__":
    main()
  

