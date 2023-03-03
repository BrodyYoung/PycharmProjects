# coding=utf-8
import openai
openai.api_key = '输入你的key'

def use(prompt):
	response = openai.ChatCompletion.create(
		  model="gpt-3.5-turbo",
		  messages=[
		        {"role": "user", "content": prompt}
		    ]
		)
	return response['choices'][0]['message']['content']

if __name__ == "__main__":

	r = use('输入你的问题')
	print(r)