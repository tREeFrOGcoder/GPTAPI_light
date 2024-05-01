from GPT_light import GPT

gpt = GPT(model_name='gpt-3.5-turbo', p_key="<api_key>")
flag, response = gpt.call("龙猫今天怎么样了？")
print(response)


