# GPTAPI_light
## How to use?
1. Keep file strcture as:
```text
AnyFolder/
└── GPT_light/
    ├── __init__.py
    └── GPTAPI.py
└── request.py
```
2. Open `request.py`:
	- `gpt = GPT(model_name='<model_name>', p_key=<api_key>)` ---> Instantiation of the gpt class. 
		- Change `<model_name>` to actual model name such as `gpt-3.5-turbo`. Support any model that OpenAI supports. Check https://platform.openai.com/docs/models/overview for available models.
		- Change `<api_key>` to actual api key which is typically `sk-*` where `*` is a 48-digit code.
	- `flag, response = gpt.call(<prompt>)` ---> Receive API feedback.
		- Change `<prompt>` to actual prompt. `Response` will be the text response from the model.

## Anything else?
1. No restrictions on network connection. No need of campus network or VPN.
2. Default transmitting url is *api.ai-gaochao.cn*.
3. As far as we know, this provider can handle very high number of parallel requesting. 4. Multi-processing package will be updated later.
