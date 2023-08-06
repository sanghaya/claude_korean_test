# Overview
많은 분들이 Claude / Claude 2가 한국어를 잘한다는 걸 아시지만, 정성적으로 측정된 사례가 없는 것 같아서, 미력하지만 직접 테스트를 해보았습니다 🤖
https://github.com/nlpai-lab/KULLM에서 정리해주신 [Evaluation Metric](https://github.com/nlpai-lab/KULLM#evaluation)을 기반으로 진행되었습니다.

[Test set](https://github.com/nlpai-lab/KULLM/blob/master/data/user_oriented_instructions_eval.jsonl)
[Claude2 result](https://github.com/sanghaya/claude_korean_test/blob/main/claude_result.jsonl)
[Evaluation result, scored by GPT4](https://github.com/sanghaya/claude_korean_test/blob/main/eval_result.jsonl)

- 각각 시스템 메세지는 `generate.py`, `eval.py`에서 확인하실 수 있습니다
- Claude는 Claude 2 (Token window: 1,000를 제외한 Default 세팅)
- GPT는 GPT4 (temperature = 0, top_p = 1)으로 진행되었습니다

https://github.com/nlpai-lab/KULLM 와 https://github.com/yizhongw/self-instruct를 쓰윽 보고 비전문가가 진행한 테스트이기에, **결과가 정확하지 않을 수 있으며, 프로덕션에 사용하실 경우, 테스트를 직접 돌려보시기 바랍니다**.

추가로 코드 상에는 없는 JSON 데이터 정리 (ex: "" Escape 처리), JSONL로 바꾸는 작업들이 있었습니다

## Result
| Type | Base-model |	Model |	이해 가능성 (0 - 1) | 자연스러움 (1 - 3) |	맥락 유지 (1 - 3) |	흥미롭기 (1 - 3) |	지시어 사용 (0-1) |	전반적인 품질 (1-5) |
| :--: | :--------: | :----: |:--------------: | :---------------: |:---------------: |:---------------: |:----------: |:---------------: |
| **Closed** | **?** |	**Claude 2** |	**0.982** |	**2.948** |	**2.920** |	**2.200** |	**0.963** |	**4.331** |
| Closed | GPT3.5-turbo |	GPT-3.5 |	0.980 |	2.806 |	2.849 |	2.056 |	0.917 |	3.905 |
| Closed |	GPT-4 |	GPT-4 |	0.984 |	2.897 |	2.944 |	2.143 |	0.968 |	4.083 |
| Open |	Polyglot-ko-12.8b |	KoAlpaca v1.1 |	0.651 |	1.909 |	1.901 |	1.583 |	0.385 |	2.575 |
| Open |	LLaMA-7b |	koVicuna |	0.460 |	1.583 |	1.726 |	1.528 |	0.409 |	2.440 |
| Open |	Polyglot-ko-12.8b |	KULLM v2 |	0.742 |	2.083 |	2.107 |	1.794 |	0.548 |	3.036 |

위 결과에 의하면, Claude 2는 `자연스러움`과 `흥미롭기`에서 GPT4보다 근소한 우위를 점하고 있지만, 신기하게 전반적인 품질에서 눈에 띄게 더 나은 점수를 보여주고 있습니다. 
