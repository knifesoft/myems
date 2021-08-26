# MyEMS

 [中文](./README.md) | [EN](./README_EN.md) | [DE](./README_DE.md)

 [![Documentation Status](https://readthedocs.org/projects/myems/badge/?version=latest)](https://myems.readthedocs.io/en/latest/?badge=latest)
 [![Maintainability](https://api.codeclimate.com/v1/badges/e01a2ca1e833d66040d0/maintainability)](https://codeclimate.com/github/MyEMS/myems/maintainability)
 [![Test Coverage](https://api.codeclimate.com/v1/badges/e01a2ca1e833d66040d0/test_coverage)](https://codeclimate.com/github/MyEMS/myems/test_coverage)
 [![Total alerts](https://img.shields.io/lgtm/alerts/g/MyEMS/myems.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MyEMS/myems/alerts/)
 [![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/MyEMS/myems.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MyEMS/myems/context:python)
 [![Language grade: JavaScript](https://img.shields.io/lgtm/grade/javascript/g/MyEMS/myems.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MyEMS/myems/context:javascript)
 [![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/MyEMS/myems/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/MyEMS/myems/?branch=master)
 [![Build Status](https://scrutinizer-ci.com/g/MyEMS/myems/badges/build.png?b=master)](https://scrutinizer-ci.com/g/MyEMS/myems/build-status/master)
 [![Codacy Badge](https://app.codacy.com/project/badge/Grade/b2cd6049727240e2aaeb8fc7b4086166)](https://www.codacy.com/gh/MyEMS/myems/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=MyEMS/myems&amp;utm_campaign=Badge_Grade)

## MyEMS 介绍

MyEMS是行业领先的开源能源管理系统，利用云计算、物联网、大数据、人工智能等信息化技术构建而成。MyEMS可用于构建统一规范、功能强大的综合能源管理服务平台。MyEMS由资深专业团队开发维护，系统代码基于MIT开源软件许可协议发布。用开源助力实现碳达峰碳中和。

## MyEMS架构

![MyEMS Architecture Function View](/docs/images/architecture-function-view.png)

![MyEMS Architecture Site View](/docs/images/architecture-site-view.png)


## MyEMS组件(社区版)

MyEMS项目由下列组件构成:
### MyEMS 数据库 (SQL)

[安装 数据库](./database/README.md)

### MyEMS API 应用程序接口 (Python)

[安装 myems-api](./myems-api/README.md)

### MyEMS 管理 UI (AngularJS version 1.x)

[安装 admin UI](./admin/README.md)

### MyEMS Modbus TCP 数据采集服务 (Python)

[安装 myems-modbus-tcp](./myems-modbus-tcp/README.md)

### MyEMS 数据清洗服务 (Python)

[安装 myems-cleaning](./myems-cleaning/README.md)

### MyEMS 数据规范化服务 (Python)

[安装 myems-normalization](./myems-normalization/README.md)

### MyEMS 数据汇总服务 (Python)

[安装 myems-aggregation](./myems-aggregation/README.md)

### MyEMS Web UI (ReactJS)

[安装 web UI](./web/README.md)

### 默认端口号

MyEMS API: 8000

MyEMS Web UI: 80

MyEMS Admin UI: 8001

### 默认密码
<details>
  <summary>Admin UI</summary>

```
administrator

!MyEMS1
```
</details>

<details>
  <summary>Web UI</summary>

```
administrator@myems.io

!MyEMS1
```
</details>

### Docker Docker-compose 安装

```
git clone https://gitee.com/myems/myems.git 
```

修改以下文件中的数据库IP
假定数据库IP为: 192.168.2.2
```
sudo nano myems-api/config.py 
sudo nano myems-aggregation/config.py 
sudo nano myems-cleaning/config.py 
sudo nano myems-modbus-tcp/config.py 
sudo nano myems-normalization/config.py 

# host: '127.0.0.1' => 'host': '192.168.2.2'
```

修改web和admin文件夹下nginx.conf中的location '/api'
假定本机IP为: 192.168.2.3
```
sudo nano admin/nginx.conf
sudo nano web/nginx.conf
# proxy_pass http://127.0.0.1:8000/;  => proxy_pass http://192.168.2.3:8000/; 
```

将Web打包生成产品文件
```
cd myems/web
npm install
npm run build
```
使用docker-compose安装
```
cd myems
docker-compose up -d 
```

## 功能版本对比

| 功能                              |社区版         |企业版    |       说明              |
| :---                              |      :----:   |  :----:  |  :----:               |
| 开源                              | ✔️             | ❌      |                      |                   
| 价格                              | 免费           | 收费      | 标准组件授权费；定制组件开发费； |
| 更换品牌名称与标志LOGO              | ❌             | ✔️       |                     |
| Modbus TCP 协议                   | ✔️             | ✔️        | 采集数据 https://modbus.org/ |
| 数据点数量                         | 无限制         |无限制      | 实际数量受限于服务器资源上限|
| 计量表数量                         | 无限制         |无限制      | 实际数量受限于服务器资源上限|
| 空间数量                           | 无限制         |无限制      | 实际数量受限于服务器资源上限|
| 设备数量                           | 无限制         |无限制      | 实际数量受限于服务器资源上限|
| 租户数量                           | 无限制         |无限制      | 实际数量受限于服务器资源上限|
| 门店数量                           | 无限制         |无限制      | 实际数量受限于服务器资源上限|
| 车间数量                           | 无限制         |无限制      | 实际数量受限于服务器资源上限|
| 组合设备数量                       | 无限制         |无限制      | 实际数量受限于服务器资源上限|
| Docker容器化部署                   | ✔️            | ✔️        | https://www.docker.com/ |
| Kubernetes部署                    | ❌             | ✔️        | https://kubernetes.io/ |
| MySQL                             | ✔️             | ✔️        | http://mysql.com/    |
| MariaDB                           | ✔️             | ✔️        | https://mariadb.org/ |
| SingleStore                       | ❌️            | ✔️        | https://www.singlestore.com/ |
| AWS 云部署                         | ✔️             | ✔️        | https://aws.amazon.com/ |
| AZure 云部署                       | ✔️             | ✔️        | https://azure.microsoft.com/ |
| 阿里云部署                         | ✔️             | ✔️        | https://aliyun.com/ |
| 私有云部署                         | ✔️             | ✔️        |                      |
| 总览页                             | ✔️             | ✔️        | 本月总能耗、本月总成本、本月消耗吨标准煤、本月吨二氧化碳排放、分时消耗电量、成本占比、吨标准煤占比、吨二氧化碳排放占比、本月能耗趋势、本月成本趋势、相关参数、本月子空间数据 |
| 数据比较分析                        | ✔️             | ✔️        | 同比、环比、自由比、不比 |
| Excel 导出                         | ✔️             | ✔️        | 表格、曲线图、柱状图、饼状图 |
| 计量表数据/能耗分析                 | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期总能耗、基准期总能耗、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期能耗趋势、相关参数、详细数据、导出Excel |
| 计量表数据/成本分析                 | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期总成本、基准期总成本、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期成本趋势、相关参数、详细数据、导出Excel |
| 计量表数据/趋势分析                 | ✔️             | ✔️        | 按空间层级筛选、趋势值、相关参数、详细数据、导出Excel |
| 计量表数据/实时分析                 | ✔️             | ✔️        | 按空间层级筛选、能耗值点最新值、能耗值点最近一小时趋势、 相关参数最新值、实时刷新 |
| 计量表数据/总分表平衡分析            | ✔️             | ✔️        | 按空间层级筛选、多种时间尺度、报告期总表消耗、报告期分表消耗、报告期差值、报告期差值百分比、导出Excel  |
| 计量表数据/离线表能耗分析            | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期总能耗、基准期总能耗、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期能耗趋势、相关参数、详细数据、导出Excel |
| 计量表数据/离线表成本分析            | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期总成本、基准期总成本、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期成本趋势、相关参数、详细数据、导出Excel |
| 计量表数据/虚拟表能耗分析            | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期总能耗、基准期总能耗、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期能耗趋势、相关参数、详细数据、导出Excel |
| 计量表数据/虚拟表成本分析            | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期总成本、基准期总成本、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期成本趋势、相关参数、详细数据、导出Excel |
| 计量表数据/计量表台账                | ✔️             | ✔️        | 按空间层级筛选、包含名称、空间、成本中心、能耗分类、描述等属性、导出Excel |
| 空间数据/能耗分类分析               | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类总能耗、基准期分类总能耗、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分类能耗趋势、单位面积值、相关参数、详细数据、子空间数据、导出Excel |
| 空间数据/能耗分项分析               | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分项总能耗、基准期分项总能耗、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分项能耗趋势、单位面积值、相关参数、详细数据、子空间数据、导出Excel |
| 空间数据/成本分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期总成本、报告期分类总成本、基准期分类总成本、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分类成本趋势、单位面积值、相关参数、详细数据、子空间数据、导出Excel |
| 空间数据/产出分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类总产出、基准期分类总产出、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分类产出趋势、单位面积值、相关参数、详细数据、子空间数据、导出Excel |
| 空间数据/收入分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期总收入、报告期分类总收入、基准期分类总收入、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分类收入趋势、单位面积值、相关参数、详细数据、子空间数据、导出Excel |
| 空间数据/效率分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期累积效率、报告期累积效率趋势、单位面积值、相关参数、详细数据、子空间数据、导出Excel |
| 空间数据/负荷分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类平均负荷、报告期分类最大负荷、报告期分类负荷系数、报告期分类平均负荷趋势、报告期分类最大负荷趋势、报告期分类负荷系数趋势、单位面积值、相关参数、详细数据、子空间数据、导出Excel |
| 空间数据/统计分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类消耗算术平均数、报告期分类消耗中位数、报告期分类消耗最小值、报告期分类消耗最大值、报告期分类消耗样本标准差、报告期分类消耗样本方差、单位面积值、相关参数、详细数据、子空间数据、导出Excel |
| 空间数据/节能分析                   | ❌             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类总节约(基线-实际)、报告期吨标准煤总节约(基线-实际)、报告期减少吨二氧化碳排放(基线-实际)、节约吨标准煤占比、减少吨二氧化碳排放占比、报告期分类节约趋势、单位面积值、相关参数、详细数据、子空间数据、导出Excel、需要能耗预测组件 |
| 设备数据/能耗分类分析               | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类总能耗、基准期分类总能耗、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分类能耗趋势、相关参数、详细数据、导出Excel |
| 设备数据/能耗分项分析               | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分项总能耗、基准期分项总能耗、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分项能耗趋势、相关参数、详细数据、导出Excel |
| 设备数据/成本分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期总成本、报告期分类总成本、基准期分类总成本、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分类成本趋势、相关参数、详细数据、导出Excel |
| 设备数据/产出分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类总产出、基准期分类总产出、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分类产出趋势、相关参数、详细数据、导出Excel |
| 设备数据/收入分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期总收入、报告期分类总收入、基准期分类总收入、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分类收入趋势、相关参数、详细数据、导出Excel |
| 设备数据/效率分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期累积效率、报告期累积效率趋势、相关参数、详细数据、导出Excel |
| 设备数据/负荷分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类平均负荷、报告期分类最大负荷、报告期分类负荷系数、报告期分类平均负荷趋势、报告期分类最大负荷趋势、报告期分类负荷系数趋势、单位面积值、相关参数、详细数据、导出Excel |
| 设备数据/统计分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类消耗算术平均数、报告期分类消耗中位数、报告期分类消耗最小值、报告期分类消耗最大值、报告期分类消耗样本标准差、报告期分类消耗样本方差、相关参数、详细数据、导出Excel |
| 设备数据/节能分析                   | ❌             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类总节约(基线-实际)、报告期吨标准煤总节约(基线-实际)、报告期减少吨二氧化碳排放(基线-实际)、节约吨标准煤占比、减少吨二氧化碳排放占比、报告期分类节约趋势、相关参数、详细数据、导出Excel、需要能耗预测组件 |
| 设备数据/批量分析                   | ✔️             | ✔️        | 按空间层级筛选、空间向下递归查询、按报告期查询全部能耗分类数据、导出Excel |
| 设备数据/设备台账                   | ✔️             | ✔️        | 按空间层级筛选、设备列表包括名称、空间、成本中心、描述等、导出Excel |
| 租户数据/能耗分类分析                | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类总能耗、基准期分类总能耗、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分类能耗趋势、单位面积值、相关参数、详细数据、导出Excel |
| 租户数据/能耗分项分析                | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分项总能耗、基准期分项总能耗、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分项能耗趋势、单位面积值、相关参数、详细数据、导出Excel |
| 租户数据/成本分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期总成本、报告期分类总成本、基准期分类总成本、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分类成本趋势、单位面积值、相关参数、详细数据、导出Excel |
| 租户数据/负荷分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类平均负荷、报告期分类最大负荷、报告期分类负荷系数、报告期分类平均负荷趋势、报告期分类最大负荷趋势、报告期分类负荷系数趋势、单位面积值、相关参数、详细数据、导出Excel |
| 租户数据/统计分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类消耗算术平均数、报告期分类消耗中位数、报告期分类消耗最小值、报告期分类消耗最大值、报告期分类消耗样本标准差、报告期分类消耗样本方差、单位面积值、相关参数、详细数据、导出Excel |
| 租户数据/节能分析                   | ❌             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类总节约(基线-实际)、报告期吨标准煤总节约(基线-实际)、报告期减少吨二氧化碳排放(基线-实际)、节约吨标准煤占比、减少吨二氧化碳排放占比、报告期分类节约趋势、单位面积值、相关参数、详细数据、导出Excel、需要能耗预测组件 |
| 租户数据/租户账单                   | ✔️             | ✔️        | 按空间层级筛选、付款通知书包含租赁合同号码、租户地址、账单号码、账单日期、付款到期日、应付款金额、结算时间范围、数量、单位、金额、小计、增值税销项税金、应付金额合计等、导出Excel |
| 租户数据/批量分析                   | ✔️             | ✔️        | 按空间层级筛选、空间向下递归查询、按报告期查询全部能耗分类数据、导出Excel |
| 门店数据/能耗分类分析                | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类总能耗、基准期分类总能耗、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分类能耗趋势、单位面积值、相关参数、详细数据、导出Excel |
| 门店数据/能耗分项分析                | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分项总能耗、基准期分项总能耗、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分项能耗趋势、单位面积值、相关参数、详细数据、导出Excel |
| 门店数据/成本分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期总成本、报告期分类总成本、基准期分类总成本、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分类成本趋势、单位面积值、相关参数、详细数据、导出Excel |
| 门店数据/负荷分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类平均负荷、报告期分类最大负荷、报告期分类负荷系数、报告期分类平均负荷趋势、报告期分类最大负荷趋势、报告期分类负荷系数趋势、单位面积值、相关参数、详细数据、导出Excel |
| 门店数据/统计分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类消耗算术平均数、报告期分类消耗中位数、报告期分类消耗最小值、报告期分类消耗最大值、报告期分类消耗样本标准差、报告期分类消耗样本方差、单位面积值、相关参数、详细数据、导出Excel |
| 门店数据/节能分析                   | ❌             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类总节约(基线-实际)、报告期吨标准煤总节约(基线-实际)、报告期减少吨二氧化碳排放(基线-实际)、节约吨标准煤占比、减少吨二氧化碳排放占比、报告期分类节约趋势、单位面积值、相关参数、详细数据、导出Excel、需要能耗预测组件 |
| 门店数据/批量分析                   | ✔️             | ✔️        | 按空间层级筛选、空间向下递归查询、按报告期查询全部能耗分类数据、导出Excel |
| 车间数据/能耗分类分析                | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类总能耗、基准期分类总能耗、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分类能耗趋势、单位面积值、单位产品值、相关参数、详细数据、导出Excel |
| 车间数据/能耗分项分析                | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分项总能耗、基准期分项总能耗、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分项能耗趋势、单位面积值、单位产品值、相关参数、详细数据、导出Excel |
| 车间数据/成本分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期总成本、报告期分类总成本、基准期分类总成本、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分类成本趋势、单位面积值、单位产品值、相关参数、详细数据、导出Excel |
| 车间数据/负荷分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类平均负荷、报告期分类最大负荷、报告期分类负荷系数、报告期分类平均负荷趋势、报告期分类最大负荷趋势、报告期分类负荷系数趋势、单位面积值、单位产品值、相关参数、详细数据、导出Excel |
| 车间数据/统计分析                   | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类消耗算术平均数、报告期分类消耗中位数、报告期分类消耗最小值、报告期分类消耗最大值、报告期分类消耗样本标准差、报告期分类消耗样本方差、单位面积值、单位产品值、相关参数、详细数据、子空间数据、导出Excel |
| 车间数据/节能分析                   | ❌             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类总节约(基线-实际)、报告期吨标准煤总节约(基线-实际)、报告期减少吨二氧化碳排放(基线-实际)、节约吨标准煤占比、减少吨二氧化碳排放占比、报告期分类节约趋势、单位面积值、单位产品值、相关参数、详细数据、导出Excel、需要能耗预测组件 |
| 车间数据/批量分析                   | ✔️             | ✔️        | 按空间层级筛选、空间向下递归查询、报告期查询全部能耗分类数据、导出Excel |
| 组合设备数据/能耗分类分析             | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类总能耗、基准期分类总能耗、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分类能耗趋势、单位面积值、相关参数、详细数据、相关设备数据、导出Excel |
| 组合设备数据/能耗分项分析             | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分项总能耗、基准期分项总能耗、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分项能耗趋势、单位面积值、相关参数、详细数据、相关设备数据、导出Excel |
| 组合设备数据/成本分析                | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期总成本、报告期分类总成本、基准期分类总成本、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分类成本趋势、相关参数、详细数据、相关设备数据、导出Excel |
| 组合设备数据/产出分析                | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类总产出、基准期分类总产出、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分类产出趋势、相关参数、详细数据、相关设备数据、导出Excel |
| 组合设备数据/收入分析                | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期总收入、报告期分类总收入、基准期分类总收入、报告期消耗吨标准煤、报告期吨二氧化碳排放、报告期分类收入趋势、相关参数、详细数据、相关设备数据、导出Excel |
| 组合设备数据/效率分析                | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期累积效率、报告期累积效率趋势、相关参数、详细数据、导出Excel  |
| 组合设备数据/负荷分析                | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类平均负荷、报告期分类最大负荷、报告期分类负荷系数、报告期分类平均负荷趋势、报告期分类最大负荷趋势、报告期分类负荷系数趋势、相关参数、详细数据、相关设备数据、导出Excel |
| 组合设备数据/统计分析                | ✔️             | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类消耗算术平均数、报告期分类消耗中位数、报告期分类消耗最小值、报告期分类消耗最大值、报告期分类消耗样本标准差、报告期分类消耗样本方差、相关参数、详细数据、相关设备数据、导出Excel |
| 组合设备数据/节能分析                | ❌            | ✔️        | 按空间层级筛选、多种比较类型、多种时间尺度、报告期分类总节约(基线-实际)、报告期吨标准煤总节约(基线-实际)、报告期减少吨二氧化碳排放(基线-实际)、节约吨标准煤占比、减少吨二氧化碳排放占比、报告期分类节约趋势、相关参数、详细数据、相关设备数据、导出Excel、需要能耗预测组件 |
| 组合设备数据/批量分析                | ✔️             | ✔️        | 按空间层级筛选、空间向下递归查询、按报告期查询全部能耗分类数据、导出Excel |
| 能流图分析                         | ✔️             | ✔️        | 表示能源流动状况、节点显示用能单位、链接显示本月能源总量 |
| 配电系统分析                       | ✔️             | ✔️        | 高中低压配电系统、实时数据、配电系统图 |
| REST API                          | ✔️             | ✔️        | 基于Python开发，提供系统配置、能源报告、Excel导出接口 |
| Web UI                            | ✔️             | ✔️        | 基于React开发，用于能源数据分析 |
| Admin UI                          | ✔️             | ✔️        | 基于Angular开发，用于系统配置管理 |
| BACnet/IP 协议                    | ❌             | ✔️        | 采集数据 http://www.bacnet.org/ |
| MQTT 订阅                         | ❌            | ✔️        | 采集数据 https://mqtt.org/ |
| Modbus RTU 协议                   | ❌            | ✔️        | 采集数据 https://modbus.org/ |
| OPC UA 协议                       | ❌            | ✔️        | 采集数据 https://opcfoundation.org/ |
| OPC DA 协议                       | ❌            | ✔️        | 采集数据 https://opcfoundation.org/ |
| Siemens S7 协议                   | ❌            | ✔️        | 采集数据 https://siemens.com/ |
| IEC 104 协议                      | ❌            | ✔️        | 采集数据 IEC 60870-5-104 https://en.wikipedia.org/wiki/IEC_60870-5 |
| Johnson Controls Metasys API     | ❌             | ✔️        | 采集数据 https://www.johnsoncontrols.com/ |
| Honeywell EBI                    | ❌             | ✔️        | 采集数据 https://www.honeywell.com/ |
| SIEMENS Desigo CC                | ❌            | ✔️        |  采集数据 https://siemens.com/ |
| QWeather API                     | ❌            | ✔️        | 采集数据 https://www.qweather.com/ |
| FDD 能效故障诊断系统              | ❌            | ✔️        | 需要企业版组件许可或定制开发 |
| 高级报表系统                      | ❌            | ✔️        | 需要企业版组件许可或定制开发 |
| 能耗预测                         | ❌            | ✔️        | 需要企业版组件许可或定制开发 |
| 组态图形绘制工具                  | ❌            | ✔️        | 需要企业版组件许可或定制开发 |
| 设备远程控制                      | ❌            | ✔️        | 需要企业版组件许可或定制开发 |
| BACnet Server                    | ❌            | ✔️        | 发布数据 http://www.bacnet.org/ |
| Modbus TCP Server                | ❌            | ✔️        | 发布数据 https://modbus.org/ |
| OPC UA Server                    | ❌            | ✔️        | 发布数据 https://opcfoundation.org/ |
| MQTT 发布                         | ❌             | ✔️        | 发布数据 https://mqtt.org/ |
| iOS APP                          | ❌            | ✔️        | 需要企业版组件许可或定制开发 |
| Android APP                      | ❌            | ✔️        | 需要企业版组件许可或定制开发 |
| 微信小程序                         | ❌           | ✔️        | 需要企业版组件许可或定制开发 |
| 支付宝小程序                       | ❌           | ✔️        | 需要企业版组件许可或定制开发 |
| 工控机硬件网关(数据采集和远程控制）    | ❌         | ✔️        | MyEMS认证工控机硬件 |
| LoRa无线数传电台模块(数据采集和远程控制）| ❌        | ✔️        | MyEMS认证LoRa硬件设备  |
| 重点用能单位能耗在线监测系统上传省级平台通信协议| ❌  | ✔️        | 需要企业版组件许可或定制开发 |
| 第三方系统集成服务                  | ❌           | ✔️        | 需要企业版组件许可或定制开发 |
| 线上软件使用培训                    | ❌           | ✔️        |                      |
| 线下软件使用培训                    | ❌           | ✔️        |                      |
| 在线社区技术支持                    | ✔️           | ✔️        |                      |
| 邮件技术支持                       | ❌️           | ✔️         |                     |
| 电话技术支持服务                   | ❌            | ✔️        |                      |
| 微信技术支持服务                   | ❌            | ✔️        |                      |
| 远程桌面技术支持服务               | ❌            | ✔️        |                      |
| 投标技术支持服务                   | ❌            | ✔️        |                      |
| 二次开发技术支持服务               | ❌            | ✔️        |                      |
| 现场技术支持服务                   | ❌            | ✔️        |                      |

## MyEMS截图
![MyEMS Space EnergyCategory1](/docs/images/myems-space-energycategory1.gif)
![MyEMS Space EnergyCategory2](/docs/images/myems-space-energycategory2.gif)
![MyEMS Space EnergyCategory3](/docs/images/myems-space-energycategory3.gif)
![MyEMS Large Screen Dashboard](/docs/images/myems-large-screen-dashboard.gif)


## MyEMS路线图

[社区版路线图](https://github.com/orgs/MyEMS/projects)

## MyEMS镜像

[1]. [Github](https://github.com/MyEMS/myems) https://github.com/MyEMS/myems
  
[2]. [Gitee](https://gitee.com/myems/myems) https://gitee.com/myems/myems

[3]. [Bitbucket](https://bitbucket.org/myems/myems) https://bitbucket.org/myems/myems

[4]. [Gitlab](https://gitlab.com/myems/myems) https://gitlab.com/myems/myems

