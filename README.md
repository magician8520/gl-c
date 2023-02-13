# <font color="red">GLaDOS-CheckIn</font>

## 说明  
GLaDOS代理自动签到  
利用GitHub的Actions功能实现GLaDOS的每天自动签到，具体签到结果可以在Actions中看到  
利用[Server酱](https://sct.ftqq.com/)将签到结果推送到微信  

```bash
# 项目地址
https://github.com/ChenAi140/GLaDOS-CheckIn
```
每天 <font color="red">20:05</font> 开始排队签到，具体签到时间以GitHub延迟为准  
经过本人测试，大概签到时间为早上 04:20 左右，建议大家适当修改时间，防止意外  
如需修改签到时间[点击此处](./.github/workflows/GLaDOS_CheckIn.yml)，打开文档，自行修改cron表达式，不会自行百度  

## 注册GLaDOS

[GLaDOS注册入口](https://github.com/glados-network/GLaDOS)  

我的邀请码：AZDOF-3654G-EBHR4-O79MD  
填写邀请码双方互利  
工具推荐使用Clash  


## Github-Actions每天自动签到教程  

1. Fork此仓库  

2. 获取GLaDOS的cookie  
   
    有些浏览器可能显示的英文，但都大差不差，若图片未显示，则需要使用魔法或者解决DNS污染  
    
    ![获取cookie.png](./GLaDOS/images/获取cookie.png)  

3. 将cookie填入`Settings` -> `Secrets and variables` -> `Actions` -> `Repository secrets`中，命名一定要是`GLADOS_COOKIE`  
   
    ![配置cookie.png](./GLaDOS/images/配置cookie.png)  


## 配置微信推送(Server酱)(非必须)  

和配置cookie一样的方式，将Server酱中的SendKey复制到`Repository secrets`命名为 `SendKey`  
[Server酱](https://sct.ftqq.com/)  
暂时只支持`方糖服务号`进行推送(因为懒)  
若此通道被弃用，那到时候再说吧  