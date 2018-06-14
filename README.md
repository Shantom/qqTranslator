# 简介

本脚本意为方便学生毕设进行外文文献的翻译，用户需自行申请API使用，用户可校正机翻后的文本，脚本最后将用户校正后的翻译件输出。

# 使用步骤

1. 使用了腾讯翻译官的API，用户请进入https://cloud.tencent.com/product/tmt，自行申请API，目前是免费的，申请得到secretID和secretKey请保存在同目录的keys.txt文件（没有请自行创建）。
2. 将语句通顺的英文放入同目录的source.txt中，使用Python3 运行preprocess.py和process.py得到tobechecked.md文件。

~~~shell
python3 preprocess.py
python3 process.py
~~~

3. 用户在tobechecked.md文件中进行译文的校正，不要删除段尾标记^p。
4. 校正完毕后使用Python3运行postprocess.py，即可得到完整的翻译件target.md。

```shell
python3 postprocess.py
```

