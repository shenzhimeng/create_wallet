## 功能

批量生成 ETH 钱包地址

## 环境

电脑需要安装 python 

## 使用说明

1、安装 eth-account

```python
pip install eth-account
```

2、命令行输入，需要生成多少个就在命令后面填多少，比如生成20个钱包地址的命令如下

```
python create_wallet.py 20
```

输完命令后，会在当前目录下生成一个 `wallet_accounts.json` 的文件，里面有钱包地址，私钥和助记词

再次使用命令时，会把 `wallet_accounts.json` 文件内容覆盖，所以如果已经生成的钱包地址记得保存到其他地方

