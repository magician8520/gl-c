# <font color="red">GLaDOS-CheckIn</font>

![stars](https://img.shields.io/github/stars/ChenAi140/GLaDOS-CheckIn?style=social)  
![forks](https://img.shields.io/github/forks/ChenAi140/GLaDOS-CheckIn?style=social)  
![last-commit](https://img.shields.io/github/last-commit/ChenAi140/GLaDOS-CheckIn)  

---

## 一、 说明

GLaDOS代理自动签到  
利用GitHub的Actions功能实现GLaDOS的每天自动签到，具体签到结果可以在Actions中看到  
利用[Server酱](https://sct.ftqq.com/)或者[pushPlus](https://www.pushplus.plus/)将签到结果推送到微信  
新增[Qmsg](https://qmsg.zendee.cn/)可以将消息推送到QQ， 

```bash
# 仓库地址
https://github.com/feixuei/GLaDOS-CheckIn.git
```
每天 `20:05` 开始排队签到， 具体签到时间以GitHub延迟为准，大概延迟`8h+`    
建议大家自行修改一个时间点，防止意外  
如需修改签到时间[点击此处](./.github/workflows/)，打开文档，自行修改cron表达式，不会看这里 [Cron表达式](https://help.aliyun.com/document_detail/64769.html)  

如有疑问，请提交 Issues  

---

## 二、 注册GLaDOS

[GLaDOS注册入口](https://github.com/glados-network/GLaDOS)  

我的邀请码：AZDOF-3654G-EBHR4-O79MD  
填写邀请码双方互利  
工具推荐使用Clash  
[Clash for Windows](https://github.com/Fndroid/clash_for_windows_pkg/tags)  --->  [汉化补丁，可能有广告](https://github.com/BoyceLig/Clash_Chinese_Patch)  
[Clash for Android](https://github.com/Kr328/ClashForAndroid/tags)  

---

## 三、 自动签到教程


1. Fork此仓库  
    <details><summary>点击此处展开</summary><pre>
    点击右上角的 Fork 按钮
        <img src="./GLaDOS/images/fork.png" alt="Fork"><br/>
    点击 Create fork ，然后等待仓库创建成功
        <img src="./GLaDOS/images/create_fork.png" alt="Create fork">
    </pre> </details>

2. 注册GLaDOS，并获取cookie  
    <details><summary>点击此处展开</summary><pre>
    注册GLaDOS：略    
    获取cookie
        <img src="./GLaDOS/images/获取cookie.png" alt="获取cookie">
    </pre> </details>

3. 填写`secrets`  
   将cookie填入`Settings` -> `Secrets and variables` -> `Actions` -> `Repository secrets`中，命名一定要是`GLADOS_COOKIE`
    <details><summary>点击此处展开</summary><pre>
    将cookie填入secrets
        <img src="./GLaDOS/images/配置cookie.png" alt="配置cookie">
    </pre> </details>

4. 激活Actions  
   <details><summary>点击此处展开</summary><pre>
    激活Actions，点击同意
        <img src="./GLaDOS/images/激活Actions.png" alt="激活Actions">
    </pre> </details>

5. 添加定时任务  

    - 打开[./GLaDOS/Schedule.yml](./GLaDOS/Schedule.yml)文件，并复制里面的内容  
    - 打开[.github/workflows/](./.github/workflows/)文件夹，点击`Add file` -> `Create new file`  
    - 将刚才复制的内容粘贴进去，并命名文件，然后提交即可 

   <details><summary>点击此处展开</summary><pre>
    复制./GLaDOS/Schedule.yaml的内容
        <img src="./GLaDOS/images/复制Schedule.png" alt="复制Schedule.yaml内容">
    在.github/workflows/目录下新建Schedule.yml
        <img src="./GLaDOS/images/创建Schedule.png" alt="新建Schedule.yml">
    修改新建的Schedule.yaml的内容
        <img src="./GLaDOS/images/修改新Schedule.png" alt="修改新Schedule">
    修改完成后提交即可
        <img src="./GLaDOS/images/提交Schedule.png" alt="提交新Schedule">
    </pre> </details>

**注意**：Actions中的工作流在仓库闲置60天后就会被停止，所以需要每60天更新一下仓库

---

## 四、 配置微信推送(非必须)  

可以不配置，可以只配置其中一个，也可以都配置  

### 1. Server酱  

和配置cookie一样的方式，将Server酱中的SendKey复制到`Repository secrets`命名为 `SENDKEY`  
然后去你创建的那个`.yml`文件里面修改`is_ServerChan_push`的值为`1`  
[Server酱](https://sct.ftqq.com/)  
暂时只支持`方糖服务号`进行推送(因为懒)  
若此通道被弃用，那到时候再说吧  

### 2. PushPlus  

和配置cookie一样的方式，将pushpuls微信公众号中的token复制到`Repository secrets`命名为 `TOKEN`  
然后去你创建的那个`.yml`文件里面修改`is_PushPlus_push`的值为`1`  
[PushPlus](https://www.pushplus.plus/)  

### 3. Qmsg  

具体配置请查看[私聊消息使用步骤简述](https://qmsg.zendee.cn/api)  
将获取到的key填入`Repository secrets`，命名为`Key`
然后去你创建的那个`.yml`文件里面修改`is_Qmsg_push`的值为`1`  
[Qmsg](https://qmsg.zendee.cn/)  

---


## 五、其它

#### 更新仓库
如果需要更新代码，可以重新Fork此仓库  
或者手动同步更新代码  

   <details><summary>点击此处展开</summary><pre>
    点击 Sync fork，然后点击 Update branch 即可更新代码，这样会保留自己的修改，无需重新配置
        <img src="./GLaDOS/images/手动同步更新.png" alt="手动同步更新">
    </pre> </details>

2023-3-7之前的Fork需要点击`Sync fork` -> `Discard * commits`放弃之前的修改，强制更新，然后重新按教程配置Schedule.yml    

#### 多账号配置  

<details><summary>点击此处展开</summary><pre>
PS: 图片看不清就点开看  
在Repository secrets里面添加多个cookie和推送的key，并分别命名
    <img src="./GLaDOS/images/多账号cookie.png" alt="多账号cookie">
在workflows里面新建yml文件，并修改相应的内容
    <img src="./GLaDOS/images/多账号yml配置.png" alt="多账号yml配置">
</pre> </details>

#### 自动更新仓库  

关于60天更新一次仓库  

看[AutoPush.yml](./GLaDOS/AutoPush.yml)，我测试是能push的，你们可以试试  


---
