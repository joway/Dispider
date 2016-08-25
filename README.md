# Dispider

Based on elastic search

## 架构


### Scheduler ( Django Server )

- 支持 Nginx 负载均衡
- Redis 存储 links base
- Mysql 存储 Project 信息
- 支持 HTTP CALLBACK

### Spider

#### Fetcher

- 下载 (&&渲染) html

#### Processor

- 处理 html
- 将新链 CALLBACK 回 Scheduler

#### Pipeline

- 持久化到数据库(elastic search)
