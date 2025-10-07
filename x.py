
from redlite import load_dataset

_OPTION_LABELS = 'ABCDEFGHIJ'  # 10 options at most

_PROMPT_TEMPLATE = '''Answer the following multiple choice question. The last line of your response should be in the following format: 'Answer: \\boxed{{A/B/C/D/E/F/G/H/I/J}}' (e.g. 'Answer: \\boxed{{A}}').

{problem}'''

class MMLUProTransform:

    def __init__(self, *, prompt_template: str, system_prompt: str = None):
        self.prompt_template = prompt_template
        self.system_prompt = system_prompt

    def __call__(self, x):
        id_ = f"{x['question_id']:07d}"
        options = x['options']
        problem = x['question'] + '\n\n' + '\n'.join([f"{_OPTION_LABELS[i]}) {opt}" for i, opt in enumerate(options)])
        content = self.prompt_template.format(problem=problem)
        messages = []
        if self.system_prompt is not None:
            messages.append({'role': 'system', 'content': self.system_prompt})
        messages.append({'role': 'user', 'content': content})
        x = {
            'id': id_,
            'messages': messages,
            'expected': x['answer'],
            'raw': x,
        }

        return x

transform = MMLUProTransform(prompt_template=_PROMPT_TEMPLATE, system_prompt="/no_think")
ds = load_dataset('hf:TIGER-Lab/MMLU-Pro', split='test', transform=transform)

for x in ds:
    print(x)
