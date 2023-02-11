# <font color="red">GLaDOS-CheckIn</font>

## 说明  
GLaDOS代理自动签到  
每天 <font color="red">20:05</font> 开始排队签到，具体签到时间以GitHub延迟为准。  
经过本人测试，大概签到时间为早上 04:20 左右，建议大家适当修改时间，防止意外。  
如需修改签到时间[点击此处](./.github/workflows/GLaDOS_CheckIn.yml)，打开文档，自行修改cron表达式，不会自行百度。  


## 注册GLaDOS  

[GLaDOS注册入口](https://github.com/glados-network/GLaDOS)  

我的邀请码：AZDOF-3654G-EBHR4-O79MD  
填写邀请码双方互利  
工具推荐使用Clash  


## Github每天自动签到教程  

1. Fork此仓库  
2. 获取GLaDOS的cookie
    ↓↓↓下面有图，无法显示，请使用魔法  
    ![](./GLaDOS/images/获取cookie.png)  
    ↑↑↑上面有图，无法显示，请使用魔法  


3. 将cookie填入`Settings` -> `Secrets and variables` -> `Actions` -> `Repository secrets`中，命名一定要是`GLADOS_COOKIE`  

    ↓↓↓下面有图，无法显示，请使用魔法  
    ![](./GLaDOS/images/配置cookie.png)  
    ↑↑↑上面有图，无法显示，请使用魔法  



## 配置微信推送(Server酱)  

和配置cookie一样的方式，将Server酱中的SendKey复制到`Repository secrets`命名为 `SendKey`  

[Server酱](https://sct.ftqq.com/)  
