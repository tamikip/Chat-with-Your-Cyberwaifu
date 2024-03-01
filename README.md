# README

This Python script is a chatbot that interacts with users and generates anime-style characters (waifus) based on user input. It uses the OpenAI API for generating text and can also generate images of the characters.（Support for third-party APIs）

## Features

- **Chat with the bot**: The bot can carry on a conversation with the user. It uses the OpenAI API to generate responses.

- **Generate characters**: The bot can generate descriptions of anime-style characters, including their name, appearance, age, height, weight, hobbies, background, favorite foods, zodiac sign, dislikes, and other details.

- **Generate images**: The bot can generate images of the characters it creates. It uses the OpenAI API to generate a description of the character, which is then used as input to an image generation API.

- **Save and load data**: The bot can save and load data, including the user's current amount of money, whether the bot is in local or cloud drawing mode, the user's current waifus, and the conversation history with each waifu.

- **Switch between local and cloud drawing modes**: The bot can switch between generating images locally or in the cloud.

- **Redraw images**: The bot can redraw images, either by upscaling an image, generating variations of an image, or generating a completely new image.

## How to Use

1. Run the script. If you have not yet configured the OpenAI API key, you will be prompted to enter it.

2. Enter a command. The available commands are:
   - "抽卡" (draw a card): Generates a new character. Costs 2000 money.
   - "waifu对话" (waifu dialogue): Starts a conversation with one of your waifus.
   - "查看waifu" (view waifu): Shows a list of your current waifus.
   - "查看金币" (view money): Shows your current amount of money.
   - "本地/云端绘画模式" (local/cloud drawing mode): Switches between local and cloud drawing modes.
   - "图片重绘" (redraw image): Redraws an image.

3. If you choose to start a conversation with a waifu, you will be prompted to enter the name of the waifu you want to talk to. Then, you can enter what you want to say to the waifu. The bot will generate a response and play it as audio.

4. If you choose to generate a new character, the bot will generate a description of the character and an image of the character. The image will be saved as a .jpg file.

5. If you choose to redraw an image, you will be prompted to enter the ID of the image you want to redraw, the index of the image (if there are multiple images), and the action you want to perform (either "放大" to upscale the image, "变换" to generate variations of the image, or "重新生成" to generate a new image).


======================================================================================================================================================================

# README

这个Python脚本是一个聊天机器人，可以与用户进行交互，并根据用户的输入生成动漫风格的角色（waifu）。它使用OpenAI API来生成文本(支持中转api)，并且还可以生成角色的图像。

## 功能

- **与机器人聊天**：机器人可以与用户进行对话。它使用OpenAI API来生成回应。

- **生成角色**：机器人可以生成动漫风格角色的描述，包括他们的名字、外貌、年龄、身高、体重、爱好、背景、喜欢的食物、星座、讨厌的东西以及其他细节。

- **生成图像**：机器人可以生成它创建的角色的图像。它使用OpenAI API生成角色的描述，然后将描述作为输入传递给图像生成API。

- **保存和加载数据**：机器人可以保存和加载数据，包括用户当前的金币数量、机器人是否处于本地或云端绘图模式、用户当前的waifu以及与每个waifu的对话历史。

- **切换本地和云端绘图模式**：机器人可以在本地生成图像和云端生成图像之间切换。

- **重绘图像**：机器人可以重绘图像，可以通过放大图像、生成图像的变体或生成全新的图像。

## 如何使用

1. 运行脚本。如果你还没有配置OpenAI API密钥，你将被提示输入。

2. 输入一个命令。可用的命令有：
   - "抽卡"：生成一个新的角色。需要2000金币。
   - "waifu对话"：开始与你的一个waifu进行对话。
   - "查看waifu"：显示你当前的waifu列表。
   - "查看金币"：显示你当前的金币数量。
   - "本地/云端绘画模式"：切换本地和云端绘图模式。
   - "图片重绘"：重绘一张图像。

3. 如果你选择与waifu开始对话，你将被提示输入你想要对话的waifu的名字。然后，你可以输入你想对waifu说的话。机器人将生成一个回应并将其播放为音频。

4. 如果你选择生成一个新的角色，机器人将生成角色的描述和角色的图像。图像将被保存为.jpg文件。

5. 如果你选择重绘一张图像，你将被提示输入你想重绘的图像的ID、图像的索引（如果有多张图像）以及你想执行的操作（"放大"以放大图像，"变换"以生成图像的变体，或者"重新生成"以生成新的图像）。


