money = 10000
import openai
import requests
import base64
import json
import time
import threading
import re
import soundfile as sf
import sounddevice as sd
import os

openai.api_key = None
openai.api_base = 'https://one-api.bltcy.top/v1'

waifu = []
waifu2 = {}
lists_dict = {}
if_local_draw = False


def remove_affinity_suffix(text):
    # 正则表达式匹配模式：（好感度：后跟一个或多个数字，然后是一个闭合括号）
    pattern = r'（好感度：\d+）$'
    # 使用正则表达式的sub函数替换匹配的文本为空字符串
    new_text = re.sub(pattern, '', text)
    return new_text


def waifu_chat(name1, prompt):
    # 将用户的新消息添加到会话历史中
    lists_dict[f"{name1}_conversation_history"].append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=lists_dict[f"{name1}_conversation_history"],
        temperature=0.7
    )

    ai_message = response['choices'][0]['message']['content']
    lists_dict[f"{name1}_conversation_history"].append({"role": "assistant", "content": ai_message})
    return ai_message


def my_function(response):
    response = remove_affinity_suffix(response)

    try:
        url2 = f'https://api.lolimi.cn/API/yyhc/y.php?msg={response}&speaker=宵宫&Length=1&noisew=0.8&sdp=0.3&noise=0.6&type=&yy=中'
    except:
        url2 = f'https://api.lolimi.cn/API/yyhc/y.php?msg=对不起我没听清，可以再说一次吗&speaker=宵宫&Length=1&noisew=0.8&sdp=0.3&noise=0.6&type=&yy=中'
    finally:
        response = requests.post(url2)
        data = json.loads(response.text)
        audio_url = data.get('music', None)
        # 指定您希望保存音频文件的本地路径和文件名
        local_filename = "output.mp3"
        response = requests.get(audio_url, stream=True)

    if response.status_code == 200:
        with open(local_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)


def cyberwaifu():
    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": """现在请你扮演人设生成器，你要生成一个美好的二次元女生人设，包括名字（那一栏就叫名字，名字可以独特一点，写中文名），外貌（那一栏就叫外貌，包括平时的衣着风格，全部内容放在同一行），年龄（应该在15 - 25
    岁之间），身高，体重，兴趣爱好（只写一项，可以多元化一些），背景，喜欢吃的东西，星座，讨厌的东西，甚至可以自行补充点备注。现在就开始生成，要按照格式生成"""}],
        temperature=0.8
    )
    ai_message = response['choices'][0]['message']['content']
    print(ai_message)
    return ai_message


def take_feature(feature):
    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system",
             "content": f"现在请你总结人物的特征，用英文的短词或短语来概括我所描述的特征，不能用英文句子概括！单词或短语之间用英文的逗号隔开，举个例子，你的输出格式应该如下：'a girl,red,eyes,lolita dress,white shoes,beautiful,long hair,',名字不用打印，一般打印外貌特征，衣着特征即可，不需要风格。以下是内容：{feature}"}],
        temperature=0.2
    )
    prompt = response['choices'][0]['message']['content']
    return prompt


def mj_draw(prompt, image_name):
    url1 = "https://one-api.bltcy.top/mj-relax/mj/submit/imagine"

    payload = json.dumps({
        "notifyHook": "string",
        "prompt": f"a girl ,ACGN,lovely,full_body,background， {prompt} --niji 5 --ar 9:16",
        "state": "string"
    })
    headers = {
        'Authorization': 'Bearer sk-Lf7dN6r59Dv9KvHM4b353a777a6247F7Bd4729C6B0E87a28',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url1, headers=headers, data=payload)

    print("图片生成中...大约4分钟")
    data = json.loads(response.text)
    id = data.get('result', None)
    time.sleep(240)
    url2 = f"https://one-api.bltcy.top/mj/task/{id}/fetch"

    payload = {}
    headers = {
        'Authorization': 'Bearer xxxxx',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
    }

    response = requests.request("GET", url2, headers=headers, data=payload)

    json_data = response.text

    data = json.loads(json_data)


    image_url = data.get('imageUrl', '')


    if image_url:

        response = requests.get(image_url)
        if response.status_code == 200:
            image_content = response.content
            image_path = f'{image_name}.jpg'
            with open(image_path, 'wb') as image_file:
                image_file.write(image_content)
            print(f"你的图片id是{id}，请你记住你的图片id")

            print(f'图片已经保存至 {image_path}')
        else:
            print(f'下载图片失败！. 状态码: {response.status_code}')
    else:
        print('没有找到图片URL！')


def mj_draw_new(id1, action, index):
    url = "https://one-api.bltcy.top/mj/submit/change"

    payload = json.dumps({
        "action": action,
        "index": int(index),
        "notifyHook": "string",
        "state": "string",
        "taskId": id1
    })
    headers = {
        'Authorization': 'Bearer xxxxxx',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    data = json.loads(response.text)
    id = data.get('result', None)
    time.sleep(240)
    url2 = f"https://one-api.bltcy.top/mj/task/{id}/fetch"

    payload = {}
    headers = {
        'Authorization': 'Bearer xxxxxxxxx',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
    }

    response = requests.request("GET", url2, headers=headers, data=payload)

    json_data = response.text

    data = json.loads(json_data)

    image_url = data.get('imageUrl', '')

    if image_url:
        response = requests.get(image_url)

        if response.status_code == 200:
            image_content = response.content

            image_path = f'{id}.jpg'
            with open(image_path, 'wb') as image_file:
                image_file.write(image_content)
            print(f"你的图片id是{id}，请你记住你的图片id")

            print(f'图片已经保存至 {image_path}')
        else:
            print(f'下载图片失败！. 状态码: {response.status_code}')
    else:
        print('没有找到图片URL！')


def generate_image(prompt, image_name):
    url = "http://127.0.0.1:7860"
    payload = {
        "prompt": f"masterpiece,a girl,solo,wallpaper,background,{prompt}",
        "negative_prompt": "Easynagative,bad,worse,nsfw",
        "steps": 20,
        "sampler_name": "DPM++ 2M SDE Karras",
        "width": 540,
        "height": 960,
        "restore_faces": False,
        "sd_model_checkpoint": "天空之境.safetensors [c1d961233a]",
    }
    try:
        response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
        if response.status_code == 200:
            r = response.json()
            for i, img_data in enumerate(r['images']):
                if ',' in img_data:
                    base64_data = img_data.split(",", 1)[1]
                else:
                    base64_data = img_data

                image_data = base64.b64decode(base64_data)
                final_image_name = f'{image_name}.png'
                with open(final_image_name, 'wb') as f:
                    f.write(image_data)
                i += 1
                print(f'图片已保存为 {final_image_name}')
        else:
            print("Failed to generate image:", response.text)
    except:
        print("绘图失败！建议切换为云端绘图模式！")


file_path = 'data.txt'
if os.path.exists(file_path):
    print(f" '{file_path}' 存在，加载配置中...")
    with open('data.txt', 'r') as file:
        lines = file.readlines()

    # 分别执行前三行
    for line in lines[:3]:
        # 执行单行Python代码
        exec(line)
else:
    print(f"'{file_path}' 不存在，为你重新生成...")
    lines = ["money = 10000\n", "if_local_draw = False\n", "waifu = []\n", "lists_dict = {}\n"]
    with open(file_path, 'w') as file:
        file.writelines(lines)

# 打开文件


remaining_code = "".join(lines[3:])
# 执行合并后的代码
exec(remaining_code)
while True:
    b = input("您还未配置gpt，请先输入GPT-KEY:\n")
    if b == "admin":
        openai.api_key = 'xxxxxxxx'
        print("已经启用管理员模式！")
        break
    else:
        if not b.startswith("sk-"):
            print("你的密钥似乎有误!请重新检查输入！")
            continue
        else:
            openai.api_key = b
            break
while True:
    print("目前的指令有“抽卡”，“waifu对话”，“查看waifu”，“查看金币”，“本地/云端绘画模式（默认是云端）”，“图片重绘”")
    a = input("请输入你的指令：")
    if a == "抽卡":
        if money >= 2000:
            money -= 2000
            with open('data.txt', 'r') as file:
                lines = file.readlines()  # 读取所有行到一个列表中
                lines[0] = f"money = {money}\n"
            with open('data.txt', 'w') as file:
                file.writelines(lines)
            print("人设生成中，请稍等...（大约两分钟）")
            renshe = cyberwaifu()
            print("抽卡成功！")
            lines = renshe.splitlines()
            for line in lines:
                if '名字' in line:
                    name = line.lstrip("名字：")
                    break
                if '名称' in line:
                    name = line.lstrip("名称：")
                    break
            waifu.append(name)
            with open('data.txt', 'r') as file:
                lines = file.readlines()  
                lines[2] = f"waifu = {waifu}\n"
            with open('data.txt', 'w') as file:
                file.writelines(lines)
            # 查找外貌这一行的内容
            lines = renshe.splitlines()
            for line in lines:
                if '外貌' in line:
                    feature_line = line
                    break
            waifu2[name] = renshe
            lists_dict[f"{name}_conversation_history"] = []
            lists_dict[f"{name}_conversation_history"].append(
                {"role": "system",
                 "content": f"下面，你要模仿一名少女角色。，以下是你的人设{renshe}，你要以你的人设与我进行聊天，但是不必刻意地提起你的人设，你和我之前的对话应该简短精炼，像是一位普通女生说出来的话，现在我和你是初次见面，请不要再对话中经常向我提问，记住。在你的对话结束后显示你对我的好感度，范围是1-100，格式:（好感度：xx）"}
            )
            with open('data.txt', 'r') as file:
                lines = file.readlines()  # 读取所有行到一个列表中
                lines[3] = f"lists_dict = {lists_dict}\n"
            with open('data.txt', 'w') as file:
                file.writelines(lines)
            feature_en = take_feature(feature_line)  # 转为绘画tag
            if if_local_draw:
                print("当前是本地绘画模式，开始绘图中...")
                generate_image(feature_en, name)  # 生成图像
            else:
                print("当前是云端绘画模式，开始绘图中...")
                thread_mj = threading.Thread(target=mj_draw, args=(feature_en, name))
                thread_mj.start()
            continue
        else:
            print("余额不足！")
            continue
    if a == "查看waifu":
        if waifu == []:
            print("你现在没有waifu呢，快去抽卡吧！")
            continue
        else:
            print(waifu)
            continue
    if a == "查看金币":
        print(f"你的金币数为{money}")
        continue
    if a == f"waifu对话":
        choose_waifu = input("请选择你的对话waifu：\n")
        if choose_waifu in waifu:
            print(f"加载waifu{choose_waifu}中...")
            while True:
                say = input("请输入你要说的话:\n")
                if say == "退出":
                    break
                else:
                    answer = waifu_chat(choose_waifu, say)
                    print(answer)
                    my_function(answer)
                    data, fs = sf.read("output.mp3")
                    sd.play(data, samplerate=fs)
                    sd.wait()
            continue
        else:
            print("该waifu不存在！")

            continue
    if a == "本地绘画模式":
        if_local_draw = True
        with open('data.txt', 'r') as file:
            lines = file.readlines()  # 读取所有行到一个列表中
            lines[1] = f"if_local_draw = {if_local_draw}\n"
        with open('data.txt', 'w') as file:
            file.writelines(lines)
        print("已切换为本地绘画模式")
    if a == "云端绘画模式":
        if_local_draw = False
        with open('data.txt', 'r') as file:
            lines = file.readlines()  # 读取所有行到一个列表中
            lines[1] = f"if_local_draw = {if_local_draw}\n"
        with open('data.txt', 'w') as file:
            file.writelines(lines)
        print("已切换为云端绘画模式")
    if a == "图片重绘":
        id2 = input("请输入重绘图片的id：")
        index = input("请输入重绘第几张图片：")
        action = input(
            "请输入重绘图片操作（放大(放大四张中的一张，)，变换(放大四张中的一张,仍然生成四张)，重新生成（再生成四张）：")
        if action == "放大":
            action = "UPSCALE"
        if action == "变换":
            action = "VARIATION"
        if action == "重新生成":
            action = "REROLL"
        id2 = f"{id2}"
        mj_draw_new(id2, action, index)
    else:
        print("指令有误，重新输入！")
