
import sys
import json
from eth_account import Account


# 创建钱包的方法
def create_wallet(number):

	if number < 1:
		return

	accounts = []
	Account.enable_unaudited_hdwallet_features()

	for x in range(number):
		acct, mnemonic = Account.create_with_mnemonic()
		print()
		print(acct.address)
		print(acct.key.hex())
		print(mnemonic)

		accounts.append({
	        "count": x+1, # 计数
	        "address": acct.address, # 钱包地址
	        "private": acct.key.hex(), # 私钥
	        "mnemonic": mnemonic # 助记词
	    })

	print()
	
	# 将生成的账号写入当前文件夹的 wallet_accounts.json 文件，覆盖写入，所以如果之前生成过，要记得将之前的数据保存到其他地方
	with open('wallet_accounts.json', 'w') as f:
		json.dump(accounts, f, indent=4, ensure_ascii=False)

	f.close()


def main():
	if len(sys.argv) < 2:
		print('请在命令后输入要生成的地址数量')
		return

	number = sys.argv[1]

	if number.isdigit() == 0:
		print('请在命令后输入要生成的地址数量，不要输入非数字内容')
		return	

	create_wallet(int(number))


main()

