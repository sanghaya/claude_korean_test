import anthropic
import asyncio
import json
import time


results = []

async def call_claude(instruction, input_data, max_tokens_to_sample: int = 1000):
    c = anthropic.Client(api_key="")
    resp = await c.acompletion(
        prompt=f"{anthropic.HUMAN_PROMPT} Instruction: {instruction}, Input: {input_data}, Output: {anthropic.AI_PROMPT}",
        stop_sequences=[anthropic.HUMAN_PROMPT],
        model="claude-2",
        max_tokens_to_sample=max_tokens_to_sample,
    )
    print (resp)
    time.sleep(2)
    return resp


def main(): 
    with open('user_oriented_instructions_eval.jsonl', 'r') as file:
        for line in file:
            data = json.loads(line)
            instruction = data.get('instruction')
            input_data = data.get('instances')[0]['input']

            result = asyncio.run(call_claude(instruction, input_data))
            results.append({
                'instruction': instruction,
                'input': input_data,
                'result': result['completion']
            })

    with open('claude_result.jsonl', 'w', encoding='utf-8') as outfile:
        json.dump(results, outfile, ensure_ascii=False)



if __name__ == "__main__":
    main()